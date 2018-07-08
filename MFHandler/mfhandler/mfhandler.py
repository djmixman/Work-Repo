#!/usr/bin/env python2



# Importing Logger, See logger.py for configuration.
import os
import sys

from logger import log

from subjects import EmployeeFile
from subjects import FacilityRequest

SOURCE_PATH   = '/home/mix-man/temp/Work/'
# SOURCE_PATH   = '/home/mix-man/temp/Work/Facility Requests'
# SOURCE_PATH   = '/home/mix-man'

PATH_FAC_REQUEST  = '/home/mix-man/temp/Facility Requests'


class ProcessFile(object):

  def __init__(self, SOURCE):
    self.FILENAME           = os.path.basename(SOURCE)
    self.BASE_DIR           = os.path.dirname(SOURCE)
    self.REL_BASE_DIR       = os.path.relpath(self.BASE_DIR, SOURCE_PATH)
    self.SUBJECT, self.TYPE = os.path.split(self.REL_BASE_DIR)

    log.debug('[{0}] FILENAME      : {1}'.format(SOURCE, self.FILENAME ))
    log.debug('[{0}] BASE_DIR      : {1}'.format(SOURCE, self.BASE_DIR))
    log.debug('[{0}] REL_BASE_DIR  : {1}'.format(SOURCE, self.REL_BASE_DIR))
    log.debug('[{0}] SUBJECT       : {1}'.format(SOURCE, self.SUBJECT))
    log.debug('[{0}] TYPE          : {1}'.format(SOURCE, self.TYPE))

  def Subject(self):
    if "Facility Requests" in self.REL_BASE_DIR: return 'Facility Request'
    if 'Employee File' in self.SUBJECT: return 'Employee File'
    return 'Unknown'



def Start(SOURCE):
  '''
  Detects which "Subject" the file is and sends it to the correct handler
  '''

  log.info('[{0}]: Processing File'.format(SOURCE))

  file = ProcessFile(SOURCE)

  if file.Subject() == 'Unknown':
    log.critical('[{0}]: Unable to determine subject!'.format(SOURCE))
    sys.exit()

  elif file.Subject() == 'Facility Request':
    log.debug('[{0}]: Detected Facility Request...'.format(SOURCE))
    FacilityRequest.Start(SOURCE, PATH_FAC_REQUEST)


  elif file.Subject() == 'Employee File':
    pass

  else:
    log.critical('[{0}]: Unknown error has occured while processing file...'.format(SOURCE))
    sys.exit()

for DIR, SUB, FILES in os.walk(os.path.join(SOURCE_PATH,'Facility Requests')):
  for FILE in FILES:
    Start(os.path.join(DIR, FILE))

# for file in os.listdir(SOURCE_PATH):
#  print file

# Start('/home/mix-man/Facility Requests/2018-01-01 - DAY-CREW - MPR.pdf')
# Start('/home/mix-man/Facility Requests/2018-01-01 - 0800-0900 - MPR.pdf')
# Start('/home/mix-man/Facility Requests/2018-01-01T1630 - 2018-01-02T1800 - MPR.pdf')
# Start('/home/mix-man/Facility Requests/2018-01-01T1630 - 2018-01-02T1800 - MPR - Special Setup.pdf')
# Start('/home/mix-man/Employee Files/Training/Last, First - 2018-06-09 - EEO.pdf')
# Start('/home/mix-man/Employee Files/Leave Slips/Last, First - 2018-06-09T0700 - 2018-06-09T1600 - Message.pdf')
# Start('/home/mix-man/Last, First - 2018-06-09T0700 - 2018-06-09T1600 - Message.pdf')

