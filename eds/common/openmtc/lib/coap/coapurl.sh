#!/bin/sh
cd $(dirname $(readlink -f ${0}))
PYTHONPATH=../:../../src:../../../../futile/src exec python coapurl.py "$@"


#Test Commands !
#./coapurl.sh -X POST -H '{"content_type": "application/json"}' -d '{"subscription": {"id":"A_S", "contact": "coap://localhost:12345"}}' coap://localhost:5682/m2m/applications/subscriptions

#./coapurl.sh -X POST -H '{"content-type": "application/json"}' -d '{"application": {"appId":"DA"}}' coap://localhost:5682/m2m/applications
