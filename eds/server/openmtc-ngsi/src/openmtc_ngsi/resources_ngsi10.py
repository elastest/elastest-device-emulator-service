from flask import request

from openmtc_ngsi.requests import (SubscribeContextRequest,
                                   UnsubscribeContextRequest,
                                   QueryContextResponse, EntityId,
                                   RegisterContextRequest)
from openmtc_ngsi.resources_base import NGSIResource


class NGSI10ContextEntityResource(NGSIResource):
    def get(self, entity_id=None, entity_type=None, attribute=None):
        ngsi_request = QueryContextResponse(
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
        ngsi_request = self.parser.parse_request(request.data,
                                                 RegisterContextRequest)
        return self.ngsi9.registerContext(ngsi_request)


class NGSI10SubscriptionsResource(NGSIResource):
    def post(self):
        ngsi_request = self.parser.parse_request(request.data,
                                                 SubscribeContextRequest)
        return self.ngsi9.subscribeContextAvailability(ngsi_request)


class NGSI10SubscriptionResource(NGSIResource):
    def delete(self, subscription_id):
        return self.ngsi10.unsubscribeContext(
            UnsubscribeContextRequest(subscriptionId=subscription_id)
        )

    def put(self, subscription_id):
        ngsi_request = self.parser.parse_request(request.data,
                                                 SubscribeContextRequest)
        return self.ngsi9.subscribeContextAvailability(ngsi_request)
