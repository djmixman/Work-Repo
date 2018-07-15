# Setup Logging
import logging
log = logging.getLogger(__name__)

from ConfigParser import SafeConfigParser
ConfigFile = 'config.ini'
config = SafeConfigParser()
config.read(ConfigFile)

from regexs import Rex

def ProcessFile(object):
    FULLFILE    = object.FULLFILE
    FILENAME    = object.FILENAME

    log.info('[{0}]: Received file from FileHandler: {1}'.format(FILENAME, FULLFILE))

    regs = Rex(FILENAME)
    log.info('[{0}]: YEAR  : {1}'.format(FILENAME, regs.getYear()))
    log.info('[{0}]: MONTH : {1}'.format(FILENAME, regs.getMonth()))
    log.info('[{0}]: DAY   : {1}'.format(FILENAME, regs.getDay()))









def test(text):
    log.debug('Testing: {0}'.format(text))




# StartUp
def main():
    log.debug('Module Loaded!')


main()
