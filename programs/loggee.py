import json
import logging
import logging.config

dct = json.loads(open('loggee_config.json').read())
logging.config.dictConfig(dct)

logger = logging.getLogger('multiple')

logger.info("hello world in INFO file")
logger.error("in Error file")
