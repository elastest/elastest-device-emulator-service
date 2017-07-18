#!/usr/bin/env bash

CONFIG_FILE="/etc/openmtc/gevent/config-nscl.json"

# defaults global
REQUIRE_AUTH=${REQUIRE_AUTH-false}

# defaults logging
LOGGING_FILE=${LOGGING_FILE-"/var/log/openmtc/nscl.log"}
LOGGING_LEVEL=${LOGGING_LEVEL-"ERROR"}

# defaults etsi

# defaults onem2m
ONEM2M_SP_ID=${ONEM2M_SP_ID-"openmtc.org"}
ONEM2M_CSE_ID=${ONEM2M_CSE_ID-"in-cse-1"}

# defaults transport
HTTP_DISABLED=${HTTP_DISABLED-true}
COAP_DISABLED=${COAP_DISABLED-true}
APP_PORT=${APP_PORT-14000}
SERVICE_PORT=${SERVICE_PORT-15000}
SSL_ENABLED=${SSL_ENABLED-false}
SSL_PORT=${SSL_PORT-16000}

# defaults etsi plugins
ETSI_NOTIFICATION_DISABLED=${ETSI_NOTIFICATION_DISABLED-true}
ETSI_REGISTRATION_DISABLED=${ETSI_REGISTRATION_DISABLED-true}
ETSI_RETARGET_DISABLED=${ETSI_RETARGET_DISABLED-true}
ETSI_ANNC_DISABLED=${ETSI_ANNC_DISABLED-true}
ETSI_ANNC_AUTO=${ETSI_ANNC_AUTO-false}
ETSI_NOTIFICATION_CHAN_DISABLED=${ETSI_NOTIFICATION_CHAN_DISABLED-true}

# defaults onem2m plugins
ONEM2M_HTTP_TRANSPORT_DISABLED=${ONEM2M_HTTP_TRANSPORT_DISABLED-false}
ONEM2M_HTTP_TRANSPORT_PORT=${ONEM2M_HTTP_TRANSPORT_PORT-18000}
ONEM2M_NOTIFICATION_DISABLED=${ONEM2M_NOTIFICATION_DISABLED-true}

# ensure correct level
case ${LOGGING_LEVEL} in
    FATAL|ERROR|WARN|INFO|DEBUG)
    ;;
    *)
    LOGGING_LEVEL="ERROR"
    ;;
esac

# if ports are the same, decrement the APP_PORT
if [ ${APP_PORT} -eq ${SERVICE_PORT} ]; then
    APP_PORT=$((${APP_PORT} - 1))
fi

# local ip
LOCAL_IP=$(ip r get 8.8.8.8 | awk 'NR==1 {print $NF}')

# set hostname
HOST_NAME=${EXTERNAL_IP-${LOCAL_IP}}

# Configuration of the service.
CONFIG_TEMP=${CONFIG_FILE}".tmp"
echo -n "Configuring M2M backend..."
JQ_STRING='.'

# basics
JQ_STRING=${JQ_STRING}' |
    .global.require_auth = '${REQUIRE_AUTH}' |
    .logging.file |= "'${LOGGING_FILE}'" |
    .logging.level |= "'${LOGGING_LEVEL}'"
'

# onem2m
JQ_STRING=${JQ_STRING}' |
    .onem2m.sp_id = "'${ONEM2M_SP_ID}'" |
    .onem2m.cse_id |= "'${ONEM2M_CSE_ID}'"
'

# set IPs
PORT=$(cat ${CONFIG_FILE} | jq -M -r '.plugins.openmtc_server[] | select(.name == "HTTPTransportPlugin") | .config.connectors[] | select((.is_wan and (.key | not) and (.key | not)) == true).port')
SCL_BASE=$(cat ${CONFIG_FILE} | jq -M -r '.etsi.scl_base')
URI="http://${LOCAL_IP}:${PORT}/${SCL_BASE}"
JQ_STRING=${JQ_STRING}' |
    .etsi.scl_base_uri = "'${URI}'" |
    ((.plugins.openmtc_server[] | select(.name == "HTTPTransportPlugin") | .config).connectors[] | .host) |= "'${HOST_NAME}'" |
    ((.plugins.openmtc_server[] | select(.name == "COAPTransportPlugin") | .config).connectors[] | .host) |= "'${HOST_NAME}'"
'

# transport
JQ_STRING=${JQ_STRING}' |
    (.plugins.openmtc_server[] | select(.name == "HTTPTransportPlugin") | .disabled) |= '${HTTP_DISABLED}' |
    (.plugins.openmtc_server[] | select(.name == "COAPTransportPlugin") | .disabled) |= '${COAP_DISABLED}' |
    ((.plugins.openmtc_server[] | select(.name == "HTTPTransportPlugin") | .config).connectors[] | select(.is_wan == false) | .port) |= '${APP_PORT}' |
    ((.plugins.openmtc_server[] | select(.name == "COAPTransportPlugin") | .config).connectors[] | select(.is_wan == false) | .port) |= '${APP_PORT}' |
    ((.plugins.openmtc_server[] | select(.name == "HTTPTransportPlugin") | .config).connectors[] | select((.is_wan and (.key | not) and (.crt | not)) == true) | .port) |= '${SERVICE_PORT}' |
    ((.plugins.openmtc_server[] | select(.name == "COAPTransportPlugin") | .config).connectors[] | select((.is_wan and (.key | not) and (.crt | not)) == true) | .port) |= '${SERVICE_PORT}'
'

# ssl
if ${SSL_ENABLED}; then
    JQ_STRING=${JQ_STRING}' |
    ((.plugins.openmtc_server[] | select(.name == "HTTPTransportPlugin") | .config).connectors[] | select((.is_wan and (.key) and (.crt)) == true) | .port) |= '${SSL_PORT}' |
    ((.plugins.openmtc_server[] | select(.name == "COAPTransportPlugin") | .config).connectors[] | select((.is_wan and (.key) and (.crt)) == true) | .port) |= '${SSL_PORT}'
'
else
    JQ_STRING=${JQ_STRING}' |
        (.plugins.openmtc_server[] | select(.name == "HTTPTransportPlugin") | .config).connectors |= [.[] | select((.key | not) == true)] |
        (.plugins.openmtc_server[] | select(.name == "COAPTransportPlugin") | .config).connectors |= [.[] | select((.key | not) == true)]
    '
fi

# etsi plugins
JQ_STRING=${JQ_STRING}' |
    (.plugins.openmtc_scl[] | select(.name == "NotificationHandler") | .disabled) |= '${ETSI_NOTIFICATION_DISABLED}' |
    (.plugins.openmtc_scl[] | select(.name == "RetargetingHandler") | .disabled) |= '${ETSI_RETARGET_DISABLED}' |
    (.plugins.openmtc_scl[] | select(.name == "AnnouncementHandler") | .disabled) |= '${ETSI_ANNC_DISABLED}' |
    (.plugins.openmtc_scl[] | select(.name == "AnnouncementHandler") | .config.auto_announce) |= '${ETSI_ANNC_AUTO}' |
    (.plugins.openmtc_scl[] | select(.name == "NotificationChannelHandler") | .disabled) |= '${ETSI_NOTIFICATION_CHAN_DISABLED}'
'

# onem2m plugins
JQ_STRING=${JQ_STRING}' |
    (.plugins.openmtc_cse[] | select(.name == "HTTPTransportPlugin") | .disabled) |= '${ONEM2M_HTTP_TRANSPORT_DISABLED}' |
    (.plugins.openmtc_cse[] | select(.name == "HTTPTransportPlugin") | .config.port) |= '${ONEM2M_HTTP_TRANSPORT_PORT}' |
    (.plugins.openmtc_cse[] | select(.name == "NotificationHandler") | .disabled) |= '${ONEM2M_NOTIFICATION_DISABLED}'
'

cat ${CONFIG_FILE} | jq -M "${JQ_STRING}"> ${CONFIG_TEMP}
mv ${CONFIG_TEMP} ${CONFIG_FILE}

echo "done"

exec python -m openmtc_gevent.nscl_main $@
