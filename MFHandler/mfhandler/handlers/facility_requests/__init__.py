# Setup Logging
import logging
log = logging.getLogger(__name__)

from ConfigParser import SafeConfigParser
ConfigFile = 'config.ini'
config = SafeConfigParser()
config.read(ConfigFile)

from regexs import Rex
from common import FileProc
from common import MonthAttr
import os

TARGET          = config.get('FACILITY_REQUESTS', 'TARGET')
FY_START_MONTH  = int(config.get('COMMON', 'FY_START_MONTH'))

class FacilityRequest(object):
    def CheckDIR(self):
        '''
        Checks if TARGET_PATH exists and asks to create if not
        '''
        if FileProc.CheckDIR(self.TARGET_PATH):
            return True
        else:
            log.warn('[{0}]: There was a problem while creating TARGET_PATH. Skipping file.'.format(self.FILENAME, self.TARGET_PATH))
            return False

    def CheckFILE(self):
        '''
        Checks if TARGET_PATH/FILENAME exists and handles needed tasks to prepare for move.
        '''
        if FileProc.CheckFILE(self.TARGET_FULL):
            log.warn('[{0}]: File already exists at {1}'.format(self.FILENAME, self.TARGET_FULL))
            return False
        else:
            return True

    def buildFileName(self):
        self.TARGET_FILENAME = self.FILENAME
        return True

    def buildFullTarget(self):
        if not self.setTargetPath(): return False
        if not self.buildFileName(): return False
        self.TARGET_FULL    = os.path.join(self.TARGET_PATH, self.TARGET_FILENAME)
        return True

    def setTargetPath(self):
        self.TARGET_PATH    = os.path.join(TARGET, self.FY_TEXT, self.MONTH_NICE)
        log.debug('[{0}]: TARGET_PATH CHANGED   : {1}'.format(self.FILENAME, self.TARGET_PATH))
        return True

    def __init__(self, FH_OBJ):
        log.info('------------- FACILITY REQUEST PROCESSOR -------------')
        self.FULLFILE       = FH_OBJ.FULLFILE
        self.FILENAME       = FH_OBJ.FILENAME
        log.debug('[{0}]: Received file from FileHandler: {1}'.format(self.FILENAME, self.FULLFILE))

        self.REG_OBJ        = Rex(self.FILENAME)
        self.YEAR           = self.REG_OBJ.getYear()
        self.MONTH          = self.REG_OBJ.getMonth()
        self.DAY            = self.REG_OBJ.getDay()
        self.DATE           = '{0}-{1}-{2}'.format(self.YEAR, self.MONTH, self.DAY)

        self.FY             = MonthAttr.getFiscalYear(FY_START_MONTH, self.DATE)

        self.FY_TEXT        = 'FY{0}'.format(self.FY)
        self.MONTH_NICE     = MonthAttr.getNumDotAbbr(self.MONTH)

        log.debug('[{0}]: REG_OBJ   : {1}'.format(self.FILENAME, self.REG_OBJ))
        log.debug('[{0}]: YEAR      : {1}'.format(self.FILENAME, self.YEAR))
        log.debug('[{0}]: MONTH     : {1}'.format(self.FILENAME, self.MONTH))
        log.debug('[{0}]: DAY       : {1}'.format(self.FILENAME, self.DAY))
        log.debug('[{0}]: DATE      : {1}'.format(self.FILENAME, self.DATE))
        log.debug('[{0}]: FY        : {1}'.format(self.FILENAME, self.FY))
        log.debug('[{0}]: FY_TEXT   : {1}'.format(self.FILENAME, self.FY_TEXT))

        if self.buildFullTarget():
            log.info('Full Target Built: {0}'.format(self.TARGET_FULL))
            if self.CheckDIR():
                log.info('DIR Check Passed...')
                if self.CheckFILE():
                    log.info('FILE Check Passed...')
                    FileProc.MoveFile(self.FULLFILE, self.TARGET_FULL)
        log.info('------------------------------------------------------')


# StartUp
def main():
    log.debug('Module Loaded!')


main()
