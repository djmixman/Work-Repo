# Setup Logging
import logging
log = logging.getLogger(__name__)

from configparser import ConfigParser
ConfigFile = 'config.ini'
config = ConfigParser()
config.read(ConfigFile)

# from regexs import Rex
from common import FileProc
from common import MonthAttr
import os

TARGET          = config.get('EMPLOYEE_FILES', 'TARGET')
FY_START_MONTH  = int(config.get('COMMON', 'FY_START_MONTH'))

'''
Workflow
Step 1: Grab the details from the file name
Step 2: Setup target path
Setp 3: Move file to new path
'''




class EmployeeFiles(object):
    def __init__(self, FH_OBJ):
        log.info('------------- EMPLOYEE  FILES  PROCESSOR -------------')

        self.TYPE = FH_OBJ.TYPE



        log.info('------------------------------------------------------')
# StartUp
def main():
    log.debug('Module Loaded!')


main()
