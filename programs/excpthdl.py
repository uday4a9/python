import sys
import logging
import logging.config
import traceback

class MyHttpLogHandler(logging.handlers.HTTPHandler):
    def emit(self, record):
        print(record.__dict__)

DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': { 
	'standard': { 
	    'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
	},
    },
    'handlers': { 
	'default': { 
	    'level': 'DEBUG',
	    'formatter': 'standard',
	    'class': 'logging.StreamHandler',
	},
	'central_log': {
	    'level': 'DEBUG',
	    'formatter': 'standard',
	    'class': 'logging.handlers.HTTPHandler',
	    'host':'127.0.0.1:5000',
	    'url':'/',
	    'method':'POST'
	}
    },
    'loggers': {
	'extensive' : {
	    'level': 'DEBUG',
	    'handlers': ['central_log'],
	    'prpogate': True
	 }
    }
}

#logger = logging.getLogger(__name__)
logging.config.dictConfig(DEFAULT_LOGGING)
logger = logging.getLogger('extensive')

num = 0

def fun():
    global num
    num += 1
    if num == 3:
        raise KeyError
    fun()

try:
    logger.info("LOGGING HAPPENING")
    fun()
except Exception:
    logger.exception("Exception received" + traceback.format_exc())
