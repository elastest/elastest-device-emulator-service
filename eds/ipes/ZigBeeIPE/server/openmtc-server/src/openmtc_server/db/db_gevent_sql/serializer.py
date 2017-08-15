from futile.logging import get_logger
from base64 import b64encode, b64decode

logger = get_logger(__name__)

try:
    from ujson import loads, dumps
except ImportError:
    try:
        from simplejson import loads, dumps
    except ImportError:
        logger.warning("Neither ujson nor simplejson packages are available. Using built-in version.")
        from json import loads, dumps
    else:
        logger.warning("ujson package not available. Using simplejson.")

try:
    from cPickle import loads as unpickle, dumps as pickle
    logger.debug("using cPickle")
except ImportError:
    logger.warning("cPickle is not available. Using pickle.")
    from pickle import loads as unpickle, dumps as pickle
    
loads = loads
dumps = dumps
unpickle = unpickle
pickle = pickle

def b64_pickle(value):
    return b64encode(pickle(value, 2))

def b64_unpickle(value):
    return unpickle(b64decode(value))

