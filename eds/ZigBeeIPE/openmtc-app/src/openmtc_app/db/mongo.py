from futile.logging import LoggerMixin
from pymongo import MongoClient


class MongoWrapper(LoggerMixin):
    """ Wraps a MongoDB connection.

        @note: Specifically created for MongoNA and MongoUI (Chile).
        @requires: pymongo
    """
    __sensors = []

    def __init__(self, host=None, port=None, db="mtc_store", *args, **kw):
        """ init

            @param host: mongoDB server address
            @param port: mongoDB server port
            @param db: mongo database name
        """
        self.db = db
        if host and port:
            self.client = MongoClient(host, port)
        else:
            self.client = MongoClient()

        self.db = self.client[db]

    def trace(self, msg):
        """ Convenience method for low priority logging.

            @param msg: log message
        """
        # DEBUG == 10
        self.logger.log(0, msg)

    def store_data(self, scl, sensor, data):
        """ Stores data in the collection of the sensor.
            Updates the scls collection with info about the scl and sensor.

            @param scl: scl ID
            @param sensor: sensor ID
            @param data: document data
        """
        self.trace("storing data: %s %s" % (sensor, data))
        if not sensor:
            return  # ignore data without sensor ID

        if sensor.startswith(scl):
            sensor_id = sensor.replace(scl, scl.replace("-", "_") + "_")
        else:
            sensor_id = scl.replace("-", "_") + "__" + sensor
        if sensor_id not in self.__sensors:
            self.__sensors.append(sensor_id)
            # self.db["sensors"].insert({ "_id": sensor})
            self.db["scls"].update({"_id": scl},
                                   {"$addToSet": {"sensors": sensor_id}},
                                   upsert=True, )

        sensor = self.db[sensor_id]
        sensor.insert(data)

    def get_sensors(self, scl):
        """ Retrieves the sensors field of a document with _id == scl.

            @param scl: scl ID
            @return: list of sensors for the specified scl
        """
        sensors = sorted(self.db["scls"].find_one({"_id": scl})["sensors"],
                         cmp=lambda x, y: cmp(str(x), str(y)))
        # sensors = self.db.collection_names(include_system_collections=False)
        self.trace("found sensors: %s" % (sensors))
        return sensors

    def get_sensor_data(self, sensor, limit=1000, skip=0):
        """ Retrieves all documents from the sensor's collection.

            @param sensor: unique sensor ID
            @param limit: (optional) result size limit
            @param skip: amount of documents to skip
            @return: list of documents found
        """
        sensor = self.db[sensor]
        sensor.ensure_index("DescriptionDate", background=True)
        cursor = sensor.find(fields={"_id": 0},
                             limit=limit,
                             sort=[("DescriptionDate", 0)],
                             skip=skip)
        self.trace("found %s documents." % (cursor.count()))
        return list(cursor)

    def get_scls(self):
        """ Retrieves all documents from the scls collection.

            @return: list of documents found
        """
        cursor = self.db["scls"].find(sort=[("_id", 1)])
        return list(cursor)
