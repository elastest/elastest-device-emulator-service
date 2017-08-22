import connexion
from api.models.api_response import ApiResponse
from api.models.device_state import DeviceState
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def get_switch_state(deviceName):
    """
    get_switch_state
    
    :param deviceName: 
    :type deviceName: str

    :rtype: DeviceState
    """
    return 'do some magic!'


def set_switch(deviceName, value):
    """
    set_switch
    
    :param deviceName: 
    :type deviceName: str
    :param value: 
    :type value: str

    :rtype: ApiResponse
    """
    return 'do some magic!'
