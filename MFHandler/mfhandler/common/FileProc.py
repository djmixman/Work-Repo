# from common.logger import log
import logging
log = logging.getLogger(__name__)

from common.yesno import YNQ as Q

import os, sys

# # Config Setup
# from ConfigParser import SafeConfigParser
# ConfigFile = 'config.ini'
# config = SafeConfigParser()
# config.read(ConfigFile)


# Workflow
# Check if target directory exists:
# If not, ask to create and quit if failure
#
# Check if target file extist:
# if not, copy, if so ask to remove files


def CheckDIR(TARGET):
    log.debug('Checking Target Directory: {0}'.format(TARGET))

    if os.path.isdir(TARGET):
        log.debug('Target Directory Found!')
        return True
    else:
        log.info('Target Directory not found: {0}'.format(TARGET))
        answer = Q('Would you like to create it?')

        # Send exit
        if answer == -1:
            log.info('Quiting per user request.')
            sys.exit()

        if answer == 0:
            return False

        if answer == 1:
            os.makedirs(TARGET)
            return True
    return False


def CheckFILE(TARGET):
    log.debug('Checking Target File: {0}'.format(TARGET))

    if os.path.isfile(TARGET):
        log.info('Target File already exists: {0}'.format(TARGET))

        answer = Q('Would you like to remove file?')
        if answer == -1:
            log.info('Quiting per user request.')
            sys.exit()

        if answer == 0:
            # Dont remove file
            return True

        if answer == 1:
            if RemoveFile(TARGET): return False
            else: return True
    else:
        log.debug('Target file does not exist: {0}'.format(TARGET))
        return False


def RemoveFile(TARGET):
    log.debug('Removing Target: {0}'.format(TARGET))
    answer = Q('Are you sure?')
    if answer == -1:
        log.info('Quiting per user request.')
        sys.exit()

    if answer == 0:
        # Dont remove file
        return False

    if answer == 1:
        os.remove(TARGET)
        log.info('File Removed: {0}'.format(TARGET))
        return True



def MoveFile(SOURCE, TARGET):
    pass



# StartUp
def main():
    log.debug('Module Loaded!')


main()
