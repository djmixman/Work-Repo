#!/usr/bin/env python2

# Setup configuration
ConfigFile = 'config.ini'

from ConfigParser import SafeConfigParser
config = SafeConfigParser()
config.read(ConfigFile)

# Setup Logging
from common.logger import log
import logging
log = logging.getLogger(__name__)

from FileHandler import FileHandler

def StartUp():
    log.debug('Script Loaded!')

#    for DIR, SUB, FILES in os.walk(os.path.join(SOURCE_PATH,'Facility Requests')):
#        for FILE in FILES:
#            ProcessFile(os.path.join(DIR, FILE))

    # file = FileHandler('/home/mix-man/Facility Requests/2018-01-01 - DAY-CREW - MPR.pdf')
    file = FileHandler('/home/mix-man/Facility Requests/2018-09-02 - DAY-CREW - MPR, CTE DR, C568 - Extra Info - Here.pdf')
    file.ProcessFile()

#    file = FileHandler('/home/mix-man/Facility Requests/2018-01-02 - DAY-CREW - MPR, CTE DR, C568.pdf')
#    file.ProcessFile()

#    file2 = FileHandler('/home/mix-man/Employee Files/Training/Last, First - 2018-06-09 - EEO.pdf')
#    file2.ProcessFile()

#    ProcessFile('/home/mix-man/Facility Requests/2018-01-01 - 0800-0900 - MPR.pdf')
#    ProcessFile('/home/mix-man/Facility Requests/2018-01-01T1630 - 2018-01-02T1800 - MPR.pdf')
#    ProcessFile('/home/mix-man/Facility Requests/2018-01-01T1630 - 2018-01-02T1800 - MPR - Special Setup.pdf')
#    ProcessFile('/home/mix-man/Employee Files/Training/Last, First - 2018-06-09 - EEO.pdf')
#    ProcessFile('/home/mix-man/Employee Files/Leave Slips/Last, First - 2018-06-09T0700 - 2018-06-09T1600 - Message.pdf')
#    ProcessFile('/home/mix-man/Last, First - 2018-06-09T0700 - 2018-06-09T1600 - Message.pdf')


StartUp()
