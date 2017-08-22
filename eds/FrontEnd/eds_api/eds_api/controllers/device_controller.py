import connexion
from eds_api.models.device_registration_info import DeviceRegistrationInfo
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def get_devices(skip=None, limit=None):
    """
    get_devices
    returns all registered devices
    :param skip: number of records to skip
    :type skip: int
    :param limit: max number of records to return
    :type limit: int

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
