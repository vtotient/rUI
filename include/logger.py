import logging
import logging.config
from json import load

# Read logging configuration from file
conf = None
with open('logging.json') as conf_json:
    conf = load(conf_json)

# Apply logging configuration
logging.config.dictConfig(conf)

# Create logger object
logger = logging.getLogger('rUI')
