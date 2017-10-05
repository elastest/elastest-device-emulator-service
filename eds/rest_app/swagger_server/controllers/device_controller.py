import connexion
from swagger_server.models.device_registration_info import DeviceRegistrationInfo
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def get_devices(deviceName=None):
    """
    get_devices
    returns all registered devices
    :param deviceName: Zigbee sensor information
    :type deviceName: str

    :rtype: List[str]
    """
    return 'do some magic!'


def register(device=None):
    """
    register
    
    :param device: 
    :type device: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        device = DeviceRegistrationInfo.from_dict(connexion.request.get_json())
    return 'do some magic!'
