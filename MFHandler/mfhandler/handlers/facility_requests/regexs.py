import logging
log = logging.getLogger(__name__)

import os, re


class Rex(object):
        def getYear(self):
            match = re.search(r'(\d{4})-\d{2}-\d{2}', self.FILENAME)
            return match.group(1)

        def getMonth(self):
            match = re.search(r'\d{4}-(\d{2})-\d{2}', self.FILENAME)
            return match.group(1)

        def getDay(self):
            match = re.search(r'\d{4}-\d{2}-(\d{2})', self.FILENAME)
            return match.group(1)

        def getStartTime(self):
            match = re.search(r'- (.*?)-.*? -', self.FILENAME)
            return match.group(1)

        def getEndTime(self):
            match = re.search(r'- .*?-(.*?) -', self.FILENAME)
            return match.group(1)

        def getLocations(self):
            match = re.search(r'- .*?-.*? - (.*?)$', self.FILENAME)
            LOCATIONS = match.group(1).split(' - ')[0]
            LOCATIONS = LOCATIONS.split(', ')
            return LOCATIONS

        def getExtraInfo(self):
            match = re.search(r'- .*?-.*? - (.*?)$', self.FILENAME)
            return match.group(1).split(' - ')[0]



        def __init__(self, SOURCE):
            self.FILENAME, self.EXT = os.path.splitext(SOURCE)
            self.YEAR               = int(self.getYear())
            self.MONTH              = int(self.getMonth())
            self.DAY                = int(self.getDay())
            self.START_TIME         = self.getStartTime()
            self.END_TIME           = self.getEndTime()
            self.LOCATIONS          = self.getLocations()
            self.EXTRA_INFO         = self.getExtraInfo()

            log.info('[{0}{1}] FILENAME    : {2}'.format(self.FILENAME, self.EXT, self.FILENAME))
            log.info('[{0}{1}] EXT         : {2}'.format(self.FILENAME, self.EXT, self.EXT))
            log.info('[{0}{1}] YEAR        : {2}'.format(self.FILENAME, self.EXT, self.YEAR))
            log.info('[{0}{1}] MONTH       : {2}'.format(self.FILENAME, self.EXT, self.MONTH))
            log.info('[{0}{1}] DAY         : {2}'.format(self.FILENAME, self.EXT, self.DAY))
            log.info('[{0}{1}] START_TIME  : {2}'.format(self.FILENAME, self.EXT, self.START_TIME))
            log.info('[{0}{1}] END_TIME    : {2}'.format(self.FILENAME, self.EXT, self.END_TIME))
            log.info('[{0}{1}] LOCATIONS   : {2}'.format(self.FILENAME, self.EXT, self.LOCATIONS))
            log.info('[{0}{1}] EXTRA_INFO  : {2}'.format(self.FILENAME, self.EXT, self.EXTRA_INFO))



def main():
    log.debug('Module Loaded!')

main()