from flask import request

from openmtc_ngsi.requests import (
    DiscoverContextAvailabilityRequest, EntityId,
    UnsubscribeContextAvailabilityRequest, SubscribeContextAvailabilityRequest)
from openmtc_ngsi.resources_base import NGSIResource


class NGSI9ContextEntityResource(NGSIResource):
    def get(self, entity_id=None, entity_type=None, attribute=None):
        ngsi_request = DiscoverContextAvailabilityRequest(
            entityIdList=[EntityId(
                isPattern=False,
                id=entity_id,
                type=entity_type
            )]
        )

        if attribute:
            ngsi_request.attributeList = [attribute]

        return self.ngsi9.discoverContextAvailability(ngsi_request)

    def post(self):
        ngsi_request = self.parser.parse_request(
            request.data, DiscoverContextAvailabilityRequest)
        return self.ngsi9.registerContext(ngsi_request)


class NGSI9SubscriptionsResource(NGSIResource):
    def post(self):
        ngsi_request = self.parser.parse_request(
            request.data, SubscribeContextAvailabilityRequest)
        return self.ngsi9.subscribeContextAvailability(ngsi_request)


class NGSI9SubscriptionResource(NGSIResource):
    def delete(self, subscription_id):
        return self.ngsi9.unsubscribeContextAvailability(
            UnsubscribeContextAvailabilityRequest(
                subscriptionId=subscription_id)
        )

    def put(self, subscription_id):
        ngsi_request = self.parser.parse_request(
            request.data, SubscribeContextAvailabilityRequest)
        return self.ngsi9.subscribeContextAvailability(ngsi_request)
