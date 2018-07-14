from common.logger import log
import logging
log = logging.getLogger(__name__)

# Config Setup
ConfigFile = 'config.ini'

from ConfigParser import SafeConfigParser
config = SafeConfigParser()
config.read(ConfigFile)

# Misc Imports
import os

# Setup Various Subject Modules
from subjects import *

# Program Setup
SOURCE_PATH = config.get('FILE_HANDLER','SOURCE_PATH')

class FileHandler(object):
    def __init__(self, SOURCE):
        self.FILENAME           = os.path.basename(SOURCE)
        self.BASE_DIR           = os.path.dirname(SOURCE)
        self.REL_BASE_DIR       = os.path.relpath(self.BASE_DIR, SOURCE_PATH)
        self.SUBJECT, self.TYPE = os.path.split(self.REL_BASE_DIR)

        log.debug('[{0}] BASE_DIR      : {1}'.format(SOURCE, self.BASE_DIR))
        log.debug('[{0}] FILENAME      : {1}'.format(SOURCE, self.FILENAME ))
        log.debug('[{0}] REL_BASE_DIR  : {1}'.format(SOURCE, self.REL_BASE_DIR))
        log.debug('[{0}] SUBJECT       : {1}'.format(SOURCE, self.SUBJECT))
        log.debug('[{0}] TYPE          : {1}'.format(SOURCE, self.TYPE))

    def Subject(self):
        if "Facility Requests" in self.REL_BASE_DIR: return 'Facility Request'
        if 'Employee File' in self.SUBJECT: return 'Employee File'
        return 'Unknown'


def ProcessFile(SOURCE):
  '''
  Detects which "Subject" the file is and sends it to the correct handler
  '''

  log.info(' ')
  log.info('--------------------------------------------')
  log.info('[{0}]: Processing File'.format(SOURCE))

  file = FileHandler(SOURCE)

  log.info('[{0}]: Subject Detection: {1}'.format(SOURCE, file.Subject()))
  if file.Subject() == 'Unknown':
    log.critical('[{0}]: Unable to determine subject!'.format(SOURCE))
    sys.exit()

  elif file.Subject() == 'Facility Request':
    log.debug('[{0}]: Detected Facility Request...'.format(SOURCE))
#    FacilityRequest.Start(SOURCE, PATH_FAC_REQUEST)


  elif file.Subject() == 'Employee File':
    pass

  else:
    log.critical('[{0}]: Unknown error has occured while processing file...'.format(SOURCE))
    sys.exit()
