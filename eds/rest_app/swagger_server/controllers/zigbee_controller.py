import connexion
from swagger_server.models.zigbee_ipe import ZigbeeIPE
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def get_sensor_data(deviceName=None):
    """
    get_sensor_data
    
    :param deviceName: name of device exists
    :type deviceName: str

    :rtype: ZigbeeIPE
    """
    return 'do some magic!'
