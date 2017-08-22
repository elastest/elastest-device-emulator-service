import connexion
from api.models.api_response import ApiResponse
from api.models.brightness_summary import BrightnessSummary
from api.models.humidity_summary import HumiditySummary
from api.models.pressure_summary import PressureSummary
from api.models.temperature_summary import TemperatureSummary
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def brightness_summary():
    """
    brightness_summary
    

    :rtype: BrightnessSummary
    """
    return 'do some magic!'


def humidity_summary():
    """
    humidity_summary
    

    :rtype: HumiditySummary
    """
    return 'do some magic!'


def pressure_summary():
    """
    pressure_summary
    

    :rtype: PressureSummary
    """
    return 'do some magic!'


def set_brightness(brightness=None):
    """
    set_brightness
    
    :param brightness: 
    :type brightness: dict | bytes

    :rtype: ApiResponse
    """
    if connexion.request.is_json:
        brightness = BrightnessSummary.from_dict(connexion.request.get_json())
    return 'do some magic!'


def set_heater_state(device, state):
    """
    set_heater_state
    turns the actuator on or off
    :param device: 
    :type device: str
    :param state: 
    :type state: str

    :rtype: ApiResponse
    """
    return 'do some magic!'


def set_humidity(humidity=None):
    """
    set_humidity
    
    :param humidity: 
    :type humidity: dict | bytes

    :rtype: ApiResponse
    """
    if connexion.request.is_json:
        humidity = HumiditySummary.from_dict(connexion.request.get_json())
    return 'do some magic!'


def set_pressure(pressure=None):
    """
    set_pressure
    
    :param pressure: 
    :type pressure: dict | bytes

    :rtype: ApiResponse
    """
    if connexion.request.is_json:
        pressure = PressureSummary.from_dict(connexion.request.get_json())
    return 'do some magic!'


def set_temperature(temperature=None):
    """
    set_temperature
    
    :param temperature: 
    :type temperature: dict | bytes

    :rtype: ApiResponse
    """
    if connexion.request.is_json:
        temperature = TemperatureSummary.from_dict(connexion.request.get_json())
    return 'do some magic!'


def temperature_summary():
    """
    temperature_summary
    

    :rtype: TemperatureSummary
    """
    return 'do some magic!'
