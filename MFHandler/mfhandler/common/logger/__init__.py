import logging

ConfigFile  = 'config.ini'
from configparser import ConfigParser
config = ConfigParser()
config.read(ConfigFile)

LOG_CONSOLE_LEVEL     = logging.INFO
LOG_CONSOLE_FORMAT    = logging.Formatter('%(message)s')

# LOG_FILE_NAME         = '../logs/MFH.log'
LOG_FILE_NAME         = config.get('LOGGING', 'LOG_FILE')
LOG_FILE_LEVEL        = logging.DEBUG
LOG_FILE_MODE         = 'w'
LOG_FILE_FORMAT       = logging.Formatter('%(asctime)s:[%(levelname)-8s]:[%(name)s -> %(funcName)s]: %(message)s')
#LOG_FILE_FORMAT       = logging.Formatter('%(asctime)s : %(name)-10s: [%(levelname)-8s] %(message)s')
LOG_FILE_DATE_FORMAT  = '%y-%m-%d %H%M'

log = logging.getLogger()
# log = logging.getLogger(__name__)

def SetupLogging():
  # Setting up the logging facility...

  log.setLevel(logging.DEBUG)

  log_file    = logging.FileHandler(LOG_FILE_NAME)
  log_file    = logging.FileHandler(LOG_FILE_NAME, mode=LOG_FILE_MODE)
  log_file.setLevel(LOG_FILE_LEVEL)
  log_file.setFormatter(LOG_FILE_FORMAT)

  log_console = logging.StreamHandler()
  log_console.setLevel(LOG_CONSOLE_LEVEL)
  log_console.setFormatter(LOG_CONSOLE_FORMAT)

  log.addHandler(log_file)
  log.addHandler(log_console)

  log.debug('Script Loaded!')


SetupLogging()
