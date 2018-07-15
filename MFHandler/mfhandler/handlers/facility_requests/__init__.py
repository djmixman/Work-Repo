# Setup Logging
import logging
log = logging.getLogger(__name__)


def ProcessFile(SOURCE):
    log.debug('Recived file from FileHandler: {0}'.format(SOURCE))


def test(text):
    log.debug('Testing: {0}'.format(text))




# StartUp
def main():
    log.debug('Module Loaded!')


main()
