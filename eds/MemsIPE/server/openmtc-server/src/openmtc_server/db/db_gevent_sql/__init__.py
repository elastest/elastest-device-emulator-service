# openmtc imports
from openmtc_scl.methoddomain.db import DBAdapter, BasicSession, Shelve
from openmtc_scl.methoddomain.db.exc import DBError, DBNotFound
from openmtc_scl.methoddomain.db.util import (get_paths, get_parent_paths,
                                              get_etsi_path, get_onem2m_path)
from openmtc_unified.model import (UnifiedResource, get_unified_type,
                                   get_unified_types)

from openmtc.model import FlexibleAttributesMixin, Entity
from openmtc.model.exc import ModelTypeError
from openmtc.util import UTC
from openmtc_etsi.exc import SCLConflict
from openmtc_etsi.model import (ETSIResource, SclBase, ContentInstance,
                                ContentInstances, get_etsi_type, get_etsi_types)
from openmtc_onem2m.model import (CSEBase, OneM2MResource, get_onem2m_type,
                                  get_onem2m_types)
from openmtc_scl.methoddomain.filtercriteria import filter_resources
from openmtc_server.exc import ConfigurationError

# imports from submodules
from .exception import SQLDBAdapterException
from .util import create_table_name
from .gevent_db import DBPool
from .sql_creator import SQLCreator, SQLiteSQLCreator
from .sql_model import Column, ForeignKey, Table
from .serializer import loads, dumps, pickle, unpickle, b64_unpickle

# external libs
from itertools import izip
from futile import NOT_SET
from enum import Enum
from datetime import datetime
import traceback

DEFAULT_CONCURRENCY = 20

"""
.. module:: sql db adapter
   :platform: Unix, Windows
   :synopsis: Maps Unified, M2M, ONEM2M Models to a SQL Database. Further it
   uses the db structures to access the data a remap the other direction.

.. moduleauthor:: kca, bro


"""


class GEventSQLSession(BasicSession):

    def __init__(self, connection, sql_creator, db_adapter, *args, **kwargs):
        super(GEventSQLSession, self).__init__(*args, **kwargs)

        self.__adapter = db_adapter
        self.__connection = connection
        self.__cursor = connection.cursor()
        self.__sql_creator = sql_creator
        self.__mapped_column_names = {}
        self.__cache = {}

    def _get_table(self, resource_type):
        """ Gets a sql model table from the resource tables dictionary based on
        a model resource_type.

        :param resource_type: the model's type.
        :type resource_type: Table.
        :returns: the resource sql table.
        """
        try:
            return self.__adapter._tables[resource_type]
        except KeyError:
            traceback.print_stack()

    def get_etsi(self, request, path, types_hint=None):
        etsi_resource = self.get("etsi", path)
        return etsi_resource

    def get_onem2m(self, request, path, types_hint=None):
        onem2m_resource = self.get("onem2m", path)
        return onem2m_resource

    def get(self, get_type, path):
        # first of all get the resource type from the database entry in table
        # tbl_resource
        sql = self.__sql_creator.create_select_fields_sql(
            self.__adapter._resource_table, ("type", ), path=path,
            etsi_path=None, onem2m_path=None, parent_path=None, limited=True)
        self.__cursor.execute(sql)
        result = self.__cursor.fetchone()
        if result is None:
            raise DBNotFound(path)

        typename = result[0]
        resource_type = self.__get_resource_type(typename)

        return self._get(resource_type, path, get_type)

    def _get(self, resource_type, path, get_type="etsi"):
        """
        try:
            return self.__cache[path]
        except KeyError:
            pass
        """
        resource_table = self._get_table(resource_type)
        fields = resource_type.attribute_names
        # do we have an etsi model - add the parent path
        if (resource_type.__model_name__ == "etsi" or
                resource_type.__model_name__ == "onem2m"):
            if resource_type is not SclBase or resource_type is not CSEBase:
                fields = ["parent_path"] + fields
                if issubclass(resource_type, FlexibleAttributesMixin):
                    fields.append("flex_values")
            sql = self.__sql_creator.create_select_fields_sql(
                resource_table, fields, path=path, etsi_path=None,
                onem2m_path=None, parent_path=None, limited=True)
        elif resource_type.__model_name__ == "unified":
            fields = ["etsi_path"] + ["onem2m_path"] + fields
            # decide based on the caller (get_etsi | get_onem2m) what element
            # to get
            if get_type == "etsi":
                sql = self.__sql_creator.create_select_fields_sql(
                    resource_table, fields, path=None, etsi_path=path,
                    onem2m_path=None, parent_path=None, limited=True)
            if get_type == "onem2m":
                sql = self.__sql_creator.create_select_fields_sql(
                    resource_table, fields, path=None, etsi_path=None,
                    onem2m_path=path, parent_path=None, limited=True)
        self.__cursor.execute(sql)
        result = self.__cursor.fetchone()
        assert result is not None, "DB returned nothing"
        db_result_dict = dict(izip(fields, result))
        return self._map_result(db_result_dict, resource_type, path)

    def _map_result(self, db_result, resource_type, path):
        # set the path explicitly

        converted_results = {}
        # set the parent_path for all tables who have it
        # parent_path = db_result.get("parent_path")
        # if parent_path:
        # TODO: is this the right attr?
        #    converted_results["parent"] = parent_path

        if resource_type is ContentInstances:
            # both are serialized due to a special condition in sql_creators
            # update() method as the controller needs this behaviour
            latest_content_instance = db_result["latest"]
            if latest_content_instance is not None:
                oldest_content_instance = db_result["oldest"]
                db_result["oldest"] = self.__deserialize(
                    oldest_content_instance)
                if oldest_content_instance == latest_content_instance:
                    db_result["latest"] = db_result["oldest"]
                else:
                    db_result["latest"] = self.__deserialize(
                        latest_content_instance)

        # set all other attributes
        for attr in resource_type.attributes:
            a_name = attr.name
            a_type = attr.type
            val = db_result[a_name]

            # don't add NoneType results from the db
            if val is None:
                continue

            if a_type is datetime:
                if not isinstance(val, datetime):
                    # format the received db dates
                    val = datetime.strptime(val, "%Y-%m-%d %X") \
                        .replace(tzinfo=UTC)
                elif val.tzinfo is None:
                    val = val.replace(tzinfo=UTC)

            # TODO: Replace the next section with something more generic. E.g.
            # look at the models type -> if different format
            elif issubclass(a_type, (dict, list, tuple, set, frozenset)):
                val = self.__deserialize(val)
            elif issubclass(a_type, (Enum,)):
                # look into enum library api
                val = getattr(a_type, val)
            elif issubclass(a_type, (Entity,)):
                val = self.__deserialize(val)

            converted_results[a_name] = val

        try:
            flex_values = db_result["flex_values"]
        except KeyError:
            pass
        else:
            flex_values = loads(flex_values)
            converted_results.update(flex_values)

        if (resource_type.__model_name__ == "etsi" or
                resource_type.__model_name__ == "onem2m"):
            converted_results["path"] = path
            resource = resource_type(**converted_results)
        elif resource_type.__model_name__ == "unified":
            resource = resource_type(
                db_result["onem2m_path"], db_result["etsi_path"],
                **converted_results)
        else:
            raise DBError("Model name unknown")
        # self.__cache[path] = resource
        return resource

    def get_collection(self, request, resource_type, parent,
                       filter_criteria=None, limited=False):
        """Gets a collection of resource type(s) or the parent's collection of
        children.
        If request type is None, the method does the same as get(parent).

        :param request: the original request
        :param resource_type:
        :type resource_type: list, tuple, set or resource type
        :param parent: the parent of the resource to get the collection from
        :type parent: resource
        :param filter_criteria: some filter criteria
        :param limited: limits the number of database entries
        """
        self.logger.debug("Getting %s children of %s (%s)", resource_type,
                          parent, parent.__model_name__)

        results = []
        sql_statements = []
        fields_list = []
        resource_types = []

        # prepare the sql with the resource type or parent path
        if resource_type:
            # check the resource type instance.
            if isinstance(resource_type, (list, tuple, set)):
                for res_type in resource_type:
                    fields = self._get_fields(res_type)
                    r_type = res_type
                    sql_statement = self._get_collection_resource_sql(
                        r_type, parent, fields, filter_criteria, limited)
                    sql_statements.append(sql_statement)
                    fields_list.append(fields)
                    resource_types.append(r_type)
            else:
                # not something iterable, resource type can directly be used
                fields = self._get_fields(resource_type)
                r_type = resource_type
                sql_statement = self._get_collection_resource_sql(
                    r_type, parent, fields, filter_criteria, limited)
                sql_statements.append(sql_statement)
                fields_list.append(fields)
                resource_types.append(r_type)
        else:
            # no resource type was given - get the parent path and all resource
            # stored that have this parent path
            # first of all get all the resources (->tables names) that reference
            # the parent path
            etsi_parent_path, onem2m_parent_path = get_paths(parent)
            if etsi_parent_path:
                sql = self.__sql_creator.create_select_fields_sql(
                    self.__adapter._resource_table, ("path", "type", ),
                    path=None, etsi_path=None, onem2m_path=None,
                    parent_path=etsi_parent_path, limited=False)
            elif onem2m_parent_path:
                sql = self.__sql_creator.create_select_fields_sql(
                    self.__adapter._resource_table, ("path", "type", ),
                    path=None, etsi_path=None, onem2m_path=None,
                    parent_path=onem2m_parent_path, limited=False)
            self.__cursor.execute(sql)

            # append every resource to the result list
            row = self.__cursor.fetchone()
            while row is not None:
                path = row[0]
                resource_type = self.__get_resource_type(row[1])
                results.append(self._get(resource_type, path,
                                         parent.__model_name__))
                row = self.__cursor.fetchone()

            return results

        # execute the sql and map the resources
        for sql_statement in sql_statements:
            self.__cursor.execute(sql_statement)
            row = self.__cursor.fetchone()
            while (row is not None):
                # as the lists are filled together, use this instead of an own
                # datatype
                fields = fields_list[sql_statements.index(sql_statement)]
                map_resource_type = resource_types[
                    sql_statements.index(sql_statement)]

                # izip consumes less memory than zip
                result_dict = dict(izip(fields, row))
                model = parent.__model_name__
                if model == "etsi" or model == "onem2m":
                    # try for etsi, if fails, try for onem2m
                    try:
                        path = get_etsi_path(result_dict)
                    except:
                        path = get_onem2m_path(result_dict)
                    results.append(
                        self._map_result(result_dict, map_resource_type, path))
                elif model == "unified":
                    results.append(
                        self._map_result(result_dict, map_resource_type,
                                         parent.etsi_path))
                row = self.__cursor.fetchone()
        results = filter_resources(results, filter_criteria)
        return results

    def _get_fields(self, resource_type):
        """Get a full field name (column_name) list of any resource type stored
        in the db.

        :param resource_type:
        :returns: a full list of field names (column_names) for the resource
                  type db table
        """
        if (resource_type.__model_name__ == "etsi" or
                resource_type.__model_name__ == "onem2m"):
            return ["path", "parent_path"] + [attribute.name for attribute
                                              in resource_type.attributes]
        elif resource_type.__model_name__ == "unified":
            return ["etsi_path", "onem2m_path"] + [attribute.name for attribute
                                                   in resource_type.attributes]

    def _get_collection_resource_sql(self, resource_type, parent, fields,
                                     filter_criteria=None, limited=False):
        """Creates the sql for for the resource_type based on the parent's
        (paths).

        :param resource_type: a type of etsi, onem2m or unified resource
        :param parent: an instance of an etsi, onem2m or unified resource
        :param fields: the columns the database shall deliver
                       (SELECT fields FROM ...)
        :type fields: a list of column names
        :param filter_criteria:
        :param limited: limit the db result to <limited> entries
        :returns: the sql for the resource_type based on the parent's (paths)
        """
        table = self._get_table(resource_type)
        etsi_parent_path, onem2m_parent_path = get_paths(parent)
        if resource_type.__model_name__ == "etsi":
            if resource_type is SclBase:
                return self.__sql_creator.create_select_fields_sql(
                    table, fields, path=etsi_parent_path, limited=limited,
                    filter_criteria=filter_criteria)
            else:
                return self.__sql_creator.create_select_fields_sql(
                    table, fields, parent_path=etsi_parent_path,
                    limited=limited, filter_criteria=filter_criteria)
        elif resource_type.__model_name__ == "onem2m":
            if resource_type is CSEBase:
                return self.__sql_creator.create_select_fields_sql(
                    table, fields, path=onem2m_parent_path, limited=limited,
                    filter_criteria=filter_criteria)
            else:
                return self.__sql_creator.create_select_fields_sql(
                    table, fields, parent_path=onem2m_parent_path,
                    limited=limited, filter_criteria=filter_criteria)
        elif resource_type.__model_name__ == "unified":
            if (etsi_parent_path):
                return self.__sql_creator.create_select_fields_sql(
                    table, fields, etsi_parent_path=etsi_parent_path,
                    limited=limited, filter_criteria=filter_criteria)
            elif onem2m_parent_path:
                return self.__sql_creator.create_select_fields_sql(
                    table, fields, onem2m_parent_path=onem2m_parent_path,
                    limited=limited, filter_criteria=filter_criteria)
            else:
                raise DBError("Cannot get the resource without a path")
        else:
            raise DBError(
                "Resource Model type does not fit the {etsi, onem2m, unified}")

    def get_etsi_path(self, request, onem2m_path):
        """ Gets the etsi path of a onem2m resource.

        :param request: the request, not really needed for the db adapter but
        specified as the interface.
        :param onem2m_path: the path of the onem2m resource
        :returns: the etsi path as str
        """
        self.logger.debug("Calling get ETSI path", request, onem2m_path)
        onem2m_resource = self.get_onem2m(request, onem2m_path)
        return onem2m_resource.etsi_path

    def _exists(self, resource_type, fields):

        if resource_type:
            # safety condition
            if (issubclass(resource_type, ETSIResource) or
                    issubclass(resource_type, OneM2MResource) or
                    issubclass(resource_type, UnifiedResource)):
                resource_type = resource_type
            else:
                raise DBError("Cannot use the resources type as it is not "
                              "stored in the db")
        else:
            # try to get the resources type. First of all get a path from the
            # fields list
            try:
                path = fields["path"]
            except KeyError:
                try:
                    path = fields["etsi_path"]
                except KeyError:
                    try:
                        path = fields["etsi_path"]
                    except KeyError:
                        raise DBError("Cannot infer type without path")

            # generate sql to get the type of a path from the resource table
            sql = self.__sql_creator.create_select_fields_sql(
                self.__adapter._resource_table, ("type", ), path=path,
                etsi_path=None, onem2m_path=None, parent_path=None,
                limited=True)

            self.__cursor.execute(sql)
            result = self.__cursor.fetchone()
            if result is None:
                return False
            if len(fields) == 1:
                return True

            resource_type = result[0]

        # check on the sub table if the resource exists
        table = self._get_table(resource_type)
        # this is old and in somehow static
        # sql = self.__sql_creator.create_exist_fields_sql(table, fields)

        # create a new dict only with the paths. OneM2m and etsi resource have
        # a path, unified resources have etsi_- and onem2m_paths
        column_value_dict = {}

        try:
            column_value_dict["path"] = fields["path"]
        except KeyError:
            try:
                column_value_dict["etsi_path"] = fields["etsi_path"]
            except KeyError:
                try:
                    column_value_dict["onem2m_path"] = fields["onem2m_path"]
                except KeyError:
                    raise DBError("Cannot create column values dict without "
                                  "at least a path")

        sql = self.__sql_creator.create_generic_exist_sql(
            table, column_value_dict)
        self.__cursor.execute(sql)
        return self.__cursor.fetchone()[0] > 0

    def exists(self, request, resource_type, fields):
        return self._exists(resource_type, fields)

    def store(self, request, resource):
        """Handles generic stores. Means that this method is able to handle
        unified, etsi and onem2m stores to the db

        :param request: the request
        :param resource: the resource to store
        :raises: SCLConflict
        """

        etsi_path, onem2m_path = get_paths(resource)
        etsi_parent_path, onem2m_parent_path = get_parent_paths(resource)

        # get the sql tables to be inserted to
        resource_table = self.__adapter._resource_table
        subtype_table = self._get_table(type(resource))
        sql_statements = []

        # prepare sql statements
        # Handle unified stores
        if isinstance(resource, UnifiedResource):
            resource_values = {"type": resource.typename}
            sql_etsi_resource_supertype_insert = self.__sql_creator.create_insert_sql(
                resource_table, path=etsi_path, parent_path=etsi_parent_path,
                values=resource_values)
            sql_onem2m_resource_supertype_insert = self.__sql_creator.create_insert_sql(
                resource_table, path=onem2m_path,
                parent_path=onem2m_parent_path, values=resource_values)
            # create subtype (that references the resources path) sql
            values = resource.attribute_values
            sql_resource_subtype_insert = self.__sql_creator.create_insert_sql(
                subtype_table, etsi_path=etsi_path, onem2m_path=onem2m_path,
                etsi_parent_path=etsi_parent_path,
                onem2m_parent_path=onem2m_parent_path, values=values)

            # append statements to the sql chain
            sql_statements.append(sql_etsi_resource_supertype_insert)
            sql_statements.append(sql_onem2m_resource_supertype_insert)
            sql_statements.append(sql_resource_subtype_insert)
        else:
            # Handle etsi stores
            if (etsi_path):
                # to not use the data model in the sql creator itself split the
                # resource object here and to not add the path to the values
                # create resource sql
                resource_values = {"type": resource.typename}
                sql_resource_supertype_insert = self.__sql_creator.create_insert_sql(
                    resource_table, path=etsi_path,
                    parent_path=etsi_parent_path, values=resource_values)
                # create subtype (that references the resources path) sql
                values = resource.attribute_values
                try:
                    flex_values = resource.flex_values
                except AttributeError:
                    pass
                else:
                    values["flex_values"] = dumps(flex_values)
                sql_resource_subtype_insert = self.__sql_creator.create_insert_sql(
                    subtype_table, path=etsi_path, parent_path=etsi_parent_path,
                    values=values)

                # send the sql inserts via the event bus to the db module, one
                # by another
            # Handle onem2m stores
            elif (onem2m_path):
                resource_values = {"type": resource.typename}
                sql_resource_supertype_insert = self.__sql_creator.create_insert_sql(
                    resource_table, path=onem2m_path,
                    parent_path=onem2m_parent_path, values=resource_values)
                # create subtype (that references the resources path) sql
                values = resource.attribute_values
                sql_resource_subtype_insert = self.__sql_creator.create_insert_sql(
                    subtype_table, path=onem2m_path,
                    parent_path=onem2m_parent_path, values=values)

            sql_statements.append(sql_resource_supertype_insert)
            sql_statements.append(sql_resource_subtype_insert)

        # execute statements
        try:
            for sql_statement in sql_statements:
                self.__cursor.execute(sql_statement)
        except self.__adapter._pool.exc.IntegrityError as e:
            # TODO: kca: flimsy. at least test properly
            errorstr = str(e).lower()
            if "unique" in errorstr or "duplicate" in errorstr:
                raise SCLConflict(etsi_path, onem2m_path)
            raise

    def update(self, request, resource, fields=None):
        table = self._get_table(type(resource))

        if fields:
            values = {name: getattr(resource, name) for name in fields}
        else:
            values = resource.attribute_values

        if (resource.__model_name__ == "etsi" or
                resource.__model_name__ == "onem2m"):
            try:
                flex_values = resource.flex_values
            except AttributeError:
                pass
            else:
                values["flex_values"] = dumps(flex_values)
            sql = self.__sql_creator.create_update_sql(
                table, values, path=resource.path)
        elif resource.__model_name__ == "unified":
            etsi_path, onem2m_path = get_paths(resource)
            sql = self.__sql_creator.create_update_sql(
                table, values, etsi_path=etsi_path, onem2m_path=onem2m_path)
        self.__cursor.execute(sql)

    def delete(self, request, resource):

        etsi_path, onem2m_path = get_paths(resource)
        resource_type = type(resource)
        table = self._get_table(resource_type)
        sql_statements = []

        if (resource.__model_name__ == "etsi" or
                resource.__model_name__ == "onem2m"):
            # delete the etsi_path from the subtype and the super resource
            # table
            path = resource.path
            sql_statements.append(
                self.__sql_creator.create_delete_sql(table, path=path))
            sql_statements.append(self.__sql_creator.create_delete_sql(
                self.__adapter._resource_table, path=path))
        elif resource.__model_name__ == "unified":
            # delete the etsi_path and onem2m_path entries from the subtype and
            # the super resource table
            # as foreign keying is not enabled by default in sqlite, delete
            # all the instances manually
            sql_statements.append(self.__sql_creator.create_delete_sql(
                table, etsi_path=etsi_path, onem2m_path=onem2m_path))
            sql_statements.append(self.__sql_creator.create_delete_sql(
                self.__adapter._resource_table, path=etsi_path))
            sql_statements.append(self.__sql_creator.create_delete_sql(
                self.__adapter._resource_table, path=onem2m_path))

        self.__execute_sql_statements(sql_statements)

    def commit(self):
        # "Executing a transaction commit"
        self.__connection.commit()
        self.__connection.release()
        self.__cache.clear()

    def rollback(self):
        # "Executing a transaction rollback"
        self.__connection.rollback()
        self.__connection.release()
        self.__cache.clear()

    def __deserialize(self, value):
        try:
            # try json
            return loads(value)
        except:
            try:
                # try b64pickle
                return b64_unpickle(value)
            except:
                # if both fail - there is nothing to deserialize
                return value

    def __execute_sql_statements(self, sql_statements):
        try:
            for sql_statement in sql_statements:
                self.__cursor.execute(sql_statement)
        except:
            # raise WHAT?
            raise

    def __get_resource_type(self, typename):
        try:
            return get_etsi_type(typename)
        except ModelTypeError:
            try:
                return get_onem2m_type(typename)
            except ModelTypeError:
                try:
                    return get_unified_type(typename)
                except ModelTypeError:
                    raise SQLDBAdapterException("Could not find appropriate "
                                                "Model Type for DBResource "
                                                "type in get()")


class GEventSQLDBAdapter(DBAdapter):
    LONG_STRING_SIZE = 512  # needed for mysql; TODO: add VERY_LONG_STRING_TYPE
    SHORT_STRING_SIZE = 30

    _type_map = {
        int: "INTEGER",
        long: "INTEGER",
        unicode: "VARCHAR(%s)" % LONG_STRING_SIZE,
        str: "VARCHAR(%s)" % LONG_STRING_SIZE,
        float: "DOUBLE",
        bool: "BOOLEAN",
        datetime: "DATETIME",
        dict: "VARCHAR(%s)" % LONG_STRING_SIZE,
        list: "VARCHAR(%s)" % LONG_STRING_SIZE,
        Entity: "VARCHAR(%s)" % LONG_STRING_SIZE,
    }

    _custom_type_map = {
        'longstring': "VARCHAR(1023)",
        'string': "VARCHAR(%s)" % LONG_STRING_SIZE,
        'shortstring': "VARCHAR(%s)" % SHORT_STRING_SIZE
    }

    def __init__(self, *args, **kw):
        super(GEventSQLDBAdapter, self).__init__(*args, **kw)

        self._shelves = set()
        self._mapped_column_names = {}

        try:
            driver = self.config["backend"]
            connectionstring = self.config["connectionstring"]
        except KeyError as e:
            raise ConfigurationError("DB configuration key missing: %s" % (e,))

        poolsize = self.config.get("concurrency", DEFAULT_CONCURRENCY)
        if driver == "sqlite3" and poolsize != 1:
            self.logger.warn(
                "Limiting DB Connection pool size to 1 for sqlite DB")
            poolsize = 1

        try:
            self._pool = DBPool(connectionstring=connectionstring,
                                poolsize=poolsize,
                                modulename=driver)
        except Exception as e:
            self.logger.debug("DB module loading failed", exc_info=True)
            raise DBError("Failed to load database backend driver '%s': %s" %
                          (driver, e))

        if driver == "sqlite3":
            self.__sql_creator = SQLiteSQLCreator()
        else:
            self.__sql_creator = SQLCreator()

        # this is necessary for generating inserts with mapped column names
        # (that contain e.g. "-")
        self.__sql_creator.mapped_column_names = self._mapped_column_names

        self._map_types()

        if self._pool.paramstyle not in ("qmark", "format", "quote"):
            raise NotImplementedError("paramstyle", self._pool.paramstyle)

    def start_session(self):
        # TODO: kca: do this lazily
        return GEventSQLSession(self._pool.get(), self.__sql_creator, self)

    def get_shelve(self, name):
        tablename = "shelve_%s" % (name, )

        if tablename not in self._shelves:

            with self._pool.get() as connection:
                cursor = connection.cursor()
                try:
                    cursor.execute(
                        "SELECT COUNT(_key) FROM %s LIMIT 1" % (tablename, ))
                except (self._pool.exc.OperationalError,
                        self._pool.exc.ProgrammingError) as e:
                    errorstr = str(e).lower()
                    if "no such table" not in errorstr and \
                            "doesn't exist" not in errorstr:
                        raise

                    table = Table(
                        tablename,
                        Column(
                            '_key', self._ca_type('string'), primary_key=True,
                            nullable=False),
                        Column(
                            'value', self._ca_type('longstring'), nullable=True)
                    )

                    sql = self.__sql_creator.create_sql_string(table)
                    cursor.execute(sql)
                    sql = "INSERT INTO %s (name) VALUES ('%s')" % (
                        create_table_name("shelves"), tablename, )
                    cursor.execute(sql)

            self._shelves.add(tablename)
        shelve = GEventSQLShelve(
            self._pool.get(), tablename, self._pool.paramstyle)
        return shelve

    def is_initialized(self):
        return self._is_initialized()

    def _is_initialized(self):
        try:
            return self.__is_initialized
        except AttributeError:
            with self._pool.get() as connection:
                cursor = connection.cursor()
                try:
                    # check for an etsi base
                    check_etsi_base_sql = self.__sql_creator.create_exist_fields_sql(
                        self._resource_table, {"path": "/m2m"})
                    cursor.execute(check_etsi_base_sql)
                except (self._pool.exc.OperationalError,
                        self._pool.exc.ProgrammingError) as e:
                    errorstr = str(e).lower()
                    if ("no such table" not in errorstr and
                            "doesn't exist" not in errorstr):
                        raise
                    initialized = False
                else:
                    result = cursor.fetchone()
                    initialized = result[0] > 0

            self.__is_initialized = initialized

            return initialized

    def initialize(self, force=False):
        # send generated tables starting from the resource table (all others
        # reference its columns) to the db
        if self._is_initialized():
            if not force:
                raise Exception("DB is already initialized")
            self._drop_db()
        else:
            self._send_tables()

    def _get_shelve_names(self, cursor):
        cursor.execute("SELECT name FROM %s" % (create_table_name("shelves"),))
        return [r[0] for r in cursor.fetchall()]

    def _drop_db(self):
        with self._pool.get() as connection:
            cursor = connection.cursor()
            tables = self._tables.values()
            for table in tables:
                cursor.execute(self.__sql_creator.create_drop_table_sql(table))
            cursor.execute(self.__sql_creator.create_drop_table_sql(
                self._resource_table))
            # if there is an sclbase initialized in the db,
            # delete the shelves, too
            if self._is_initialized():
                for name in self._get_shelve_names(cursor):
                    cursor.execute("DROP TABLE IF EXISTS %s" % (name, ))
            cursor.execute(self.__sql_creator.create_drop_table_sql(
                self._shelves_table))

            self._do_send_tables(tables, cursor)

    def _send_tables(self):
        with self._pool.get() as connection:
            self._do_send_tables(self._tables.values(), connection.cursor())

    def _do_send_tables(self, tables, cursor):
        cursor.execute(self.__sql_creator.create_sql_string(
            self._shelves_table))
        cursor.execute(self.__sql_creator.create_sql_string(
            self._resource_table))
        for table in tables:
            sql = self.__sql_creator.create_sql_string(table)
            cursor.execute(sql)

        self.__is_initialized = True

    def _ca_type(self, resource_type):
        try:
            return self._custom_type_map[resource_type]
        except KeyError:
            raise TypeError(resource_type)

    def _sa_type(self, resource_type):
        try:
            return self._type_map[resource_type]
        except KeyError:
            raise TypeError(resource_type)

    def _map_types(self):

        #         hold all the mapped tables with this dict
        #         get the types to map
        etsi_types = get_etsi_types()
        unified_types = get_unified_types()
        onem2m_types = get_onem2m_types()

#         create an initial ressource table for etsi and onem2m resources
        self._resource_table = Table(
            create_table_name("resource"),
            Column("path", self._ca_type('string'), primary_key=True,
                   nullable=False),
            Column("parent_path", self._ca_type('string'), nullable=True),
            Column('type', self._ca_type('shortstring'), nullable=False)
        )

        self._shelves_table = Table(
            create_table_name("shelves"),
            Column('shelve_id', self._sa_type(int), nullable=False,
                   autoincrement=True),
            Column('name', self._ca_type('string'), nullable=False,
                   unique=True)
        )

        tables = self._tables = {}

        # dots = 70

        # iterate over unified types from the model and create tables
        for unified_type in unified_types:
            self._map_unified_type(unified_type, tables)

        # iterate over etsi_types from the etsi model and create tables
        for etsi_type in etsi_types:
            if not etsi_type.virtual:
                self._map_etsi_type(etsi_type, tables)

        # iterate over onem2m_types from the onem2m model and create tables
        for onem2m_type in onem2m_types:
            self._map_onem2m_type(onem2m_type, tables)

    def _map_unified_type(self, resource_type, tables, level=1):
        # if the table exists..skip it.
        try:
            return tables[resource_type]
        except KeyError:
            pass

        foreign_key_to = create_table_name("resource" + " (path)")

#         all mapped models MUST reference the resource
        # create the etsi path column
        etsi_path_column = Column("etsi_path",
                                  self._ca_type('string'),
                                  foreign_key=ForeignKey(foreign_key_to,
                                                         onupdate="CASCADE",
                                                         ondelete="CASCADE"),
                                  primary_key=True, nullable=False)
        # create the etsi path column
        onem2m_path_column = Column("onem2m_path",
                                    self._ca_type('string'),
                                    foreign_key=ForeignKey(foreign_key_to,
                                                           onupdate="CASCADE",
                                                           ondelete="CASCADE"),
                                    primary_key=False, nullable=False)

        etsi_parent_path_column = Column("etsi_parent_path",
                                  self._ca_type('string'),
                                  foreign_key=ForeignKey(foreign_key_to,
                                                         onupdate="CASCADE",
                                                         ondelete="CASCADE"),
                                  primary_key=False, nullable=True)
        # create the etsi path column
        onem2m_parent_path_column = Column("onem2m_parent_path",
                                    self._ca_type('string'),
                                    foreign_key=ForeignKey(foreign_key_to,
                                                           onupdate="CASCADE",
                                                           ondelete="CASCADE"),
                                    primary_key=False, nullable=True)

        columns = [etsi_path_column, onem2m_path_column,
                   etsi_parent_path_column, onem2m_parent_path_column]

        for a in resource_type.attributes:
            if a.type == ContentInstance:
                columns.append(Column(a.name, self._ca_type('string'),
                                      foreign_key=ForeignKey(
                                          foreign_key_to, onupdate="CASCADE",
                                          ondelete="SET NULL"), nullable=True))
            elif issubclass(a.type, Entity):
                columns.append(Column(a.name, self._ca_type('string')))
            elif issubclass(a.type, Enum):
                columns.append(Column(a.name, self._ca_type('string')))
            else:
                # special characters treatment in model that produce non sql
                # executable code. In map_types() they get re-mapped
                name = self._map_typename(a.name)
                columns.append(Column(name, self._sa_type(a.type)))

        for a in resource_type.subresources:
            if not a.type.virtual:
                self._map_unified_type(a.type, tables, level=level + 1)

        for a in resource_type.collections:
            # as it might produces infinite creation recursion", a.name
            continue

        if issubclass(resource_type, FlexibleAttributesMixin):
            columns.append(Column("flex_values", self._ca_type("longstring"),
                                  nullable=False))

        table = Table(
            create_table_name(resource_type.typename, "unified"), *columns)
        tables[resource_type] = table
        return table

    def _map_etsi_type(self, resource_type, tables, level=1):
        # if the table exists..skip it.
        try:
            return tables[resource_type]
        except KeyError:
            pass

        foreign_key_to = create_table_name("resource" + " (path)")

#         all mapped models MUST reference the resource
        path_column = Column("path",
                             self._ca_type('string'),
                             foreign_key=ForeignKey(foreign_key_to,
                                                    onupdate="CASCADE",
                                                    ondelete="CASCADE"),
                             primary_key=True, nullable=False)

        columns = [path_column]

        if resource_type is not SclBase:
            # all types except SclBase a column for the path of their parent
            # as well as the appropriate property reference to the original
            # resource table
            columns.append(Column("parent_path",
                                  self._ca_type('string'),
                                  foreign_key=ForeignKey(foreign_key_to),
                                  nullable=False))

        for a in resource_type.attributes:
            if a.type == ContentInstance:
                columns.append(Column(a.name, self._ca_type('string'),
                                      foreign_key=ForeignKey(
                                          foreign_key_to, onupdate="CASCADE",
                                          ondelete="SET NULL"), nullable=True))
            elif issubclass(a.type, Entity):
                columns.append(Column(a.name, self._ca_type('string')))
            elif issubclass(a.type, Enum):
                columns.append(Column(a.name, self._ca_type('string')))
            else:
                name = self._map_typename(a.name)
                columns.append(Column(name, self._sa_type(a.type)))

        for a in resource_type.subresources:
            if not a.type.virtual:
                self._map_etsi_type(a.type, tables, level=level + 1)

        for a in resource_type.collections:
            # as it might produces infinite creation recursion", a.name
            continue

        if issubclass(resource_type, FlexibleAttributesMixin):
            columns.append(Column("flex_values", self._ca_type("longstring"),
                                  nullable=False))

        table = Table(
            create_table_name(resource_type.typename, "etsi"), *columns)
        tables[resource_type] = table
        return table

    def _map_onem2m_type(self, resource_type, tables, level=1):
        # if the table exists..skip it.
        try:
            return tables[resource_type]
        except KeyError:
            pass

        foreign_key_to = create_table_name("resource" + " (path)")

        # all mapped models MUST reference the resource
        path_column = Column("path",
                             self._ca_type('string'),
                             foreign_key=ForeignKey(foreign_key_to,
                                                    onupdate="CASCADE",
                                                    ondelete="CASCADE"),
                             primary_key=True, nullable=False)

        columns = [path_column]

        if resource_type is not CSEBase:
            # all types except SclBase a column for the path of their parent
            # as well as the appropriate property reference to the original
            # resource table
            columns.append(Column("parent_path",
                                  self._ca_type('string'),
                                  foreign_key=ForeignKey(foreign_key_to),
                                  nullable=False))

        for a in resource_type.attributes:
            if a.type == ContentInstance:
                columns.append(Column(a.name, self._ca_type('string'),
                                      foreign_key=ForeignKey(
                                          foreign_key_to, onupdate="CASCADE",
                                          ondelete="SET NULL"), nullable=True))
            elif issubclass(a.type, Entity):
                columns.append(Column(a.name, self._ca_type('string')))
            elif issubclass(a.type, Enum):
                columns.append(Column(a.name, self._ca_type('string')))
            else:
                name = self._map_typename(a.name)
                columns.append(Column(name, self._sa_type(a.type)))

        for a in resource_type.subresources:
            if not a.type.virtual:
                self._map_onem2m_type(a.type, tables, level=level + 1)

        for a in resource_type.collections:
            # as it might produces infinite creation recursion", a.name
            continue

        if issubclass(resource_type, FlexibleAttributesMixin):
            columns.append(Column("flex_values", self._ca_type("longstring"),
                                  nullable=False))

        table = Table(
            create_table_name(resource_type.typename, "onem2m"), *columns)
        tables[resource_type] = table
        return table

    # maps a column name to a new name. This is used for sql compliance of
    # character as "-" in some parameters name e.g. CSE-ID -> CSE
    def _map_typename(self, name):
        MAPPED_CHARS = {"-"}
        REPLACE_CHAR = "_mapped_"
        for mapped_char in MAPPED_CHARS:
            if name.find(mapped_char) > -1:
                # map it
                mapped_name = name.replace(mapped_char, REPLACE_CHAR)
                self._mapped_column_names[mapped_name] = name
                return mapped_name
        # if it was not mapped return the original name
        return name


class GEventSQLShelve(Shelve):

    def __init__(self, connection, tablename, paramstyle, *args, **kw):
        super(GEventSQLShelve, self).__init__(*args, **kw)
        self.__tablename = tablename
        self.__connection = connection
        self.__cursor = connection.cursor()
        self.__paramstyle = paramstyle

    def commit(self):
        self.__connection.commit()
        self.__connection.release()

    def rollback(self):
        self.__connection.rollback()
        self.__connection.release()

    def __getitem__(self, k):
        return self._getitem(k)

    def _get_placeholder(self, name):
        if self.__paramstyle == "qmark":
            return "?"
        if self.__paramstyle == "quote":
            return "%s"
        if self.__paramstyle == "format":
            return '%%(%s)s' % (name, )
        raise NotImplementedError("paramstyle", self._pool.paramstyle)

    def _create_getitem_sql(self, key):
        if self.__paramstyle == "format":
            data = {"_key": key}
        else:
            data = (key, )
        ph = self._get_placeholder("_key")
        sql = "SELECT value FROM %s WHERE _key=%s LIMIT 1" % (self.__tablename,
                                                              ph)
        return sql, data

    def _create_setitem_sql(self, key, value):
        if self.__paramstyle == "format":
            data = {"_key": key, "value": value}
        else:
            data = (key, value)
        ph1 = self._get_placeholder("_key")
        ph2 = self._get_placeholder("value")
        sql = "INSERT INTO %s (_key, value) VALUES(%s, %s)" % (self.__tablename,
                                                               ph1, ph2)
        return sql, data

    def _create_delitem_sql(self, key):
        if self.__paramstyle == "format":
            data = {"_key": key}
        else:
            data = (key, )
        ph = self._get_placeholder("_key")
        sql = "DELETE FROM %s WHERE _key=%s" % (self.__tablename, ph)
        return sql, data

    def _getitem(self, k):
        sql, data = self._create_getitem_sql(k)
        self.__cursor.execute(sql, data)
        row = self.__cursor.fetchone()
        if row is None:
            raise KeyError(k)
        return unpickle(str(row[0]))

    def __setitem__(self, k, v):
        self._delitem(k)
        v = pickle(v, 0)
        sql, data = self._create_setitem_sql(k, v)
        self.__cursor.execute(sql, data)

    def pop(self, k, default=NOT_SET):
        try:
            v = self._getitem(k)
        except KeyError:
            if default is NOT_SET:
                raise
            v = default
        else:
            self._delitem(k)
        return v

    def __delitem__(self, k):
        sql, data = self._create_delitem_sql(k)
        self.__cursor.execute(sql, data)

    def get(self, k, default=None):
        try:
            return self._getitem(k)
        except KeyError:
            return default

    def __len__(self):
        self.__cursor.execute(
            "SELECT COUNT(_key) FROM %s" % (self.__tablename, ))
        return self.__cursor.fetchone()[0]

    def __iter__(self):
        return iter(self.values())

    def items(self):
        self.__cursor.execute(
            "SELECT _key, value FROM %s" % (self.__tablename, ))
        return [(k, unpickle(str(v)))
                for k, v in self.__cursor.fetchall()]
