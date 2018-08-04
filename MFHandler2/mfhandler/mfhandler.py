#!/usr/bin/env python3

# Setup Configuration
ConfigFile = 'config.ini'

from configparser import ConfigParser
config = ConfigParser()
config.read(ConfigFile)

from common.logger import log
import logging
log = logging.getLogger(__name__)

# Detect the working directory
## Go Up a dir until the "Work" directory is found

# Detect the directory "Type"
# Detect the file "Type"
# Move the file to the proper "Type" folder

from handlers.FileHandler import FileHandler

def ProcessFile(SOURCE_FILE):
    log.info('PROCESSING: {0}'.format(SOURCE_FILE))
    run = FileHandler(SOURCE_FILE)
    run.ProcessFile()

def TestData2():
    ProcessFile('S:\\Python\\Work-Repo\\Test-Data\\Work\\Facility Requests\\2018-10-01 - INFO-ONLY - MPR, CTE DR - Extra Notes - With more extra notes.pdf')
    ProcessFile('S:\\Python\\Work-Repo\\Test-Data\\Work\\Employee Files\\Leave\\Lastname, Firstname - YYYY-MM-DD.HHMM - YYYY-MM-DD.HHMM - Stuff Here.pdf')

def TestData():
    import os
    matches = []
    for root, dirnames, filenames in os.walk('S:\\Python\\Work-Repo\\Test-Data\\'):
        for filename in filenames:
            matches.append(os.path.join(root, filename))
    for file in matches:
        log.info('PROCESSING: {0}'.format(file))
        ProcessFile(file)


def StartUp():
    log.debug('Script Loaded!')
#    TestData()
    TestData2()

StartUp()
