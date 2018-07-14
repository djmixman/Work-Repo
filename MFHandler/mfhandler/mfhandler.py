#!/usr/bin/env python2

# Setting up Logging
from common.logger import log
import logging
log = logging.getLogger(__name__)

from subjects import *

log.info('[{0}] Loaded!'.format(__name__))
