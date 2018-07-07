 #!/usr/bin/env python2

# Setup Modules
import os
import logging

# Setup Variables

# Choose DEBUGING LEVEL
# DEBUG, INFO, WARNING, ERROR, CRITICAL

LOG_CONSOLE_LEVEL     = logging.INFO
LOG_CONSOLE_FORMAT    = logging.Formatter('%(message)s')

LOG_FILE_LEVEL        = logging.DEBUG
LOG_FILE_NAME         = 'logs/MFH.log'
LOG_FILE_MODE         = 'w'
LOG_FILE_FORMAT       = logging.Formatter('%(asctime)s : %(name)-12s: [%(levelname)-8s] %(message)s')
LOG_FILE_DATE_FORMAT  = '%y-%m-%d %H%M'

# System Variables
log = logging.getLogger(__name__)


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

  log.debug('Logging facility initalized...')


def ProcessFilename(file):
    log.debug('Processing File: "{}"'.format(file))
    DIR_BASE, FILENAME = os.path.split()



# Main screen turn on...

SetupLogging()
