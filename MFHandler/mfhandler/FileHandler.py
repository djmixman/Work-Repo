# from common.logger import log
import logging
log = logging.getLogger(__name__)

# Config Setup
from ConfigParser import SafeConfigParser
ConfigFile = 'config.ini'
config = SafeConfigParser()
config.read(ConfigFile)

# Misc Imports
import os, sys

# Setup Various Subject Modules
# from subjects import *
from handlers import *

# facility_requests.test('This is a test!')
# employee_files.test('This is a test!')

# Program Setup
SOURCE_PATH = config.get('FILE_HANDLER','SOURCE_PATH')

SUBJECT_TYPES       = {
    'facility requests' : 1,
    'employee files'    : 2,
    'unknown'           : 99,
}

def GetSubjectType(value):
    for subject in SUBJECT_TYPES.keys():
        log.debug('Does {0} = {1}?'.format(subject.lower(), value.lower()))
        if subject.lower() == value.lower():
            log.debug('MATCH! Returning: {0}'.format(SUBJECT_TYPES[subject]))
            return SUBJECT_TYPES[subject]
    return 99


class FileHandler(object):

    def __init__(self, SOURCE):
        self.FULLFILE           = SOURCE
        self.FILENAME           = os.path.basename(SOURCE)
        self.BASE_DIR           = os.path.dirname(SOURCE)
        self.REL_BASE_DIR       = os.path.relpath(self.BASE_DIR, SOURCE_PATH)
        self.SUBJECT, self.TYPE = os.path.split(self.REL_BASE_DIR)

        if self.SUBJECT == "": self.SUBJECT = self.TYPE

        self.SUBJECT_TYPE       = GetSubjectType(self.SUBJECT)

        log.debug('[{0}] FULLFILE      : {1}'.format(self.FILENAME, self.FULLFILE))
        log.debug('[{0}] BASE_DIR      : {1}'.format(self.FILENAME, self.BASE_DIR))
        log.debug('[{0}] FILENAME      : {1}'.format(self.FILENAME, self.FILENAME ))
        log.debug('[{0}] REL_BASE_DIR  : {1}'.format(self.FILENAME, self.REL_BASE_DIR))
        log.debug('[{0}] SUBJECT       : {1}'.format(self.FILENAME, self.SUBJECT))
        log.debug('[{0}] TYPE          : {1}'.format(self.FILENAME, self.TYPE))
        log.debug('[{0}] SUBJECT TYPE  : {1}'.format(self.FILENAME, self.SUBJECT_TYPE))

    def ProcessFile(self):
        '''
        Sends the file to the correct handler.
        '''
        log.info(' ')
        log.info('--------------------------------------------')
        log.info('[{0}]: Processing File'.format(self.FILENAME))

        log.debug('[{0}]: Subject Detection: {1}'.format(self.FILENAME, self.SUBJECT_TYPE))

        if self.SUBJECT_TYPE == 1:
            log.info('[{0}]: Sending to Facility Request Processor...'.format(self.FILENAME))
#           facility_requests.ProcessFile(self.FULLFILE)
            facility_requests.ProcessFile(self)
            #    FacilityRequest.Start(SOURCE, PATH_FAC_REQUEST)

        elif self.SUBJECT_TYPE == 2:
            log.info('[{0}]: Sending to Employee Files Processor...'.format(self.FILENAME))
            pass

        elif self.SUBJECT_TYPE == 99:
            log.critical('[{0}]: Unable to determine subject! Check the file and try again.'.format(self.FILENAME))
            sys.exit()

        else:
            log.critical('[{0}]: Unknown error has occured while processing file.'.format(self.FILENAME))
            sys.exit()
