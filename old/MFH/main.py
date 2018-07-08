#!/usr/bin/env python2

# Setup Modules
import logging          # Logging Facility
import os               # OS Lib
import re               # Regex Libs

# from subjects import FacilityRequest
import subjects

# import subjects.FacilityRequest

# Setup Variables

# Full path to target directories ... DO NOT USE RELATIVE PATHS HERE
TARGET                      = {}
TARGET['FACILITY REQUESTS'] = '/home/mix-man/temp/Dest1/Facility Requests'
TARGET['EMPLOYEE FILES']    = '/home/mix-man/temp/Dest2/Employee Files'

SOURCE_PATH           = '/home/mix-man'
# SOURCE_PATH           = 'C:\\home\\mix-man\\'

# SOURCE['BASE']              = '/home/mix-man/temp/Source/'
# SOURCE['FACILITY REQUESTS'] = 'Facility Requests'
# SOURCE['EMPLOYEE FILES']    = 'Employee Files'

# Choose DEBUGING LEVEL
# DEBUG, INFO, WARNING, ERROR, CRITICAL

LOG_CONSOLE_LEVEL     = logging.INFO
LOG_CONSOLE_FORMAT    = logging.Formatter('%(message)s')

LOG_FILE_LEVEL        = logging.DEBUG
LOG_FILE_NAME         = 'logs/MFH.log'
LOG_FILE_MODE         = 'w'
LOG_FILE_FORMAT       = logging.Formatter('%(asctime)s : %(name)-10s: [%(levelname)-8s] %(message)s')
LOG_FILE_DATE_FORMAT  = '%y-%m-%d %H%M'

# System Variables

log = logging.getLogger(__name__)
# log = logging.getLogger('MFHandler')

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

  log.debug('+--------------------------------+')
  log.debug('|Logging facility initalized...  |')
  log.debug('+--------------------------------+')
  log.debug('')


def GetDatesFromString(string):
  match     = re.search(r'\d{4}-\d{2}-\d{2}', string)
  return match

def MoveFile (DEST, SOURCE):
  pass



def Process_Facility_Request(FILE):
  log.debug('+--------------------------------+')
  log.debug('|Processing Facility Request for : {0}'.format(FILE))

  NEWFILE     = os.path.basename(FILE)
  DEST        = os.path.join(TARGET['FACILITY REQUESTS'], NEWFILE)

  log.debug('|NEWFILE                         : {0}'.format(NEWFILE))
  log.debug('|DEST                            : {0}'.format(DEST))

#  DATES       = GetDatesFromString(NEWFILE)
#  START_DATE  = DATES.group(0)

#  START_DATE  = FacilityRequest.GetDatesFromFile(NEWFILE).group(0)
#  START_DATE = types.FacilityRequest(NEWFILE).getDate()

#  log.debug('|START_DATE                      : {0}'.format(START_DATE))
  pass






def Process_Employee_File(TYPE, FILE):
  log.debug('+--------------------------------+')
  log.debug('|Processing Employee File        : {0}'.format(FILE))
  log.debug('|File Type                       : {0}'.format(TYPE))

  DEST        = os.path.join(TARGET['EMPLOYEE FILES'])

# GET NAME HERE

  if 'Leave Slips' in TYPE: pass


  if 'Training' in TYPE: pass

  if 'Notes' in TYPE: pass


#  log.debug('|NEWFILE                         : {0}'.format(NEWFILE))
  log.debug('|DEST                            : {0}'.format(DEST))

  pass


def ProcessFilename(FILE):
  log.debug('+--------------------------------+')
  log.info('|Processing File                 : {0}'.format(FILE))

  FILENAME      = os.path.basename(FILE)
  BASE_DIR      = os.path.dirname(FILE)
  REL_BASE_DIR  = os.path.relpath(BASE_DIR, SOURCE_PATH)
  SUBJECT, TYPE = os.path.split(REL_BASE_DIR)

  log.debug('|FILENAME                        : {0}'.format(FILENAME))
  log.debug('|BASE_DIR                        : {0}'.format(BASE_DIR))
  log.debug('|REL_BASE_DIR                    : {0}'.format(REL_BASE_DIR))
  log.debug('|SUBJECT                         : {0}'.format(SUBJECT))
  log.debug('|TYPE                            : {0}'.format(TYPE))

  if "Facility Requests" in REL_BASE_DIR: Process_Facility_Request(FILE)

  if "Employee Files" in SUBJECT: Process_Employee_File(TYPE, FILE)

  log.debug('+--------------------------------+')
  log.debug(' ')


# Main screen turn on...

SetupLogging()

log.warn(subjects.FacilityRequest.Test('TEST!'))

# LINUX
ProcessFilename('/home/mix-man/Facility Requests/2018-01-01 - 0800-0900 - MPR.pdf')
ProcessFilename('/home/mix-man/Employee Files/Training/Last, First - 2018-06-09 - EEO.pdf')
ProcessFilename('/home/mix-man/Employee Files/Leave Slips/Last, First - 2018-06-09T0700 - 2018-06-09T1600 - Message.pdf')

# WINDOWS
# ProcessFilename('C:\\home\\mix-man\\Facility Requests\\2018-01-01 - 0800-0900 - MPR.pdf')
# ProcessFilename('C:\\home\\mix-man\\Employee Files\\Training\\Last, First - 2018-06-09 - EEO.pdf')
# ProcessFilename('C:\\home\\mix-man\\Employee Files\\Leave Slips\\Last, First - 2018-06-09T0700 - 2018-06-09T1600 - Message')
