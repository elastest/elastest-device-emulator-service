from futile.logging import LoggerMixin
from futile.net.http import quote
from openmtc.exc import SCLNotFound
from openmtc.model import Application, Container
from openmtc_ngsi.db.exc import DBEntityNotFound


class SCLDb(LoggerMixin):
    def __init__(self, scl, id_prefix, helper, prefix, *args, **kw):
        super(SCLDb, self).__init__(*args, **kw)
        self.scl = scl
        self.internal_app_id = id_prefix + "openmtc-ngsi"
        self._helper = self.helper = helper
        self.prefix = prefix + "-"
        self._get_subscriptions_db()

    @property
    def _content_instances_path(self):
        return ("/applications/" + quote(self.internal_app_id) +
                "/containers/" + self.prefix +
                "subscription_db/contentInstances")

    def _get_subscriptions_db(self):
        content_instances_path = self._content_instances_path

        try:
            content_instances = self.scl.retrieve(
                content_instances_path).resource.values  # [1]
        except SCLNotFound:
            self._create_subscriptions_db_container()
            return self._get_subscriptions_db()

    def _create_subscriptions_db_container(self):
        containers_path = "/applications/" + quote(
            self.internal_app_id) + "/containers"

        try:
            self.scl.create(containers_path,
                            Container(id=self.prefix + "subscription_db"))
        except SCLNotFound:
            self.scl.create("/applications",
                            Application(appId=self.internal_app_id))
            self._create_subscriptions_db_container()

    def _get_subscription_id(self, path):
        try:
            path = path.rpartition("/")[-1][15:]
        except:
            self.logger.exception("Failed to split path %s", path)

        return path

    def add_subscription(self, subscription):
        path = self.helper.create_content_instance(self._content_instances_path,
                                                   subscription).resourceURI
        return self._get_subscription_id(path)

    def delete_subscription(self, subscription_id):
        path = (self._content_instances_path +
                ("/contentInstance%s" % subscription_id))
        try:
            self.scl.delete(path)
        except SCLNotFound:
            raise DBEntityNotFound(subscription_id)

    def find_app_subscriptions(self, app_type, app_id):
        found = []
        subscriptions = self._helper.get_content_instances(
            self._content_instances_path)
        for content_instance, subscription in subscriptions:
            if not subscription["attributeList"]:
                matched = []
                for subscription_type, is_pattern, subscription_entity_id in \
                        subscription["entityIdList"]:
                    if self._helper.id_matches(entity_type=subscription_type,
                                               is_pattern=is_pattern,
                                               entity_id=subscription_entity_id,
                                               app_type=app_type, app_id=app_id
                                               ):
                        matched.append((subscription_type, is_pattern,
                                        subscription_entity_id))
                if matched:
                    subscription["subscriptionId"] = self._get_subscription_id(
                        content_instance["href"])
                    subscription["entityIdList"] = matched
                    found.append(subscription)
        return found

    def find_container_subscriptions(self, app_type, app_id, attribute):
        found = []
        subscriptions = self._helper.get_content_instances(
            self._content_instances_path)
        for content_instance, subscription in subscriptions:

            matched = []
            for subscription_type, is_pattern, subscription_entity_id in \
            subscription["entityIdList"]:
                if ((not subscription["attributeList"] or attribute in
                    subscription["attributeList"]) and
                        self._helper.id_matches(entity_type=subscription_type,
                                                is_pattern=is_pattern,
                                                entity_id=subscription_entity_id,
                                                app_type=app_type, app_id=app_id
                                                )):
                    matched.append(
                        (subscription_type, is_pattern, subscription_entity_id))

            if matched:
                subscription["subscriptionId"] = self._get_subscription_id(
                    content_instance.href)
                subscription["entityIdList"] = matched
                found.append(subscription)
        return found
