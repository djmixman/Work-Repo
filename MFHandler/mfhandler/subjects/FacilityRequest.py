import os, sys, re

from datetime import datetime
from logger import log

import regs as RegEx
import common


def Start(INPUT, TARGET_PATH):
  log.info('[{0}]: Facility Request Processor...'.format(INPUT))

  SOURCE = {}
  TARGET = {}

# SETUP
  SOURCE['FILENAME']    = os.path.splitext(os.path.basename(INPUT))[0]
  log.debug('[{0}]: SOURCE FILENAME    : {1}'.format(INPUT, SOURCE['FILENAME']))

  SOURCE['EXT']         = os.path.splitext(INPUT)[1]
  log.debug('[{0}]: SOURCE EXT         : {1}'.format(INPUT, SOURCE['EXT']))

  SOURCE['PATH_BASE']   = os.path.dirname(INPUT)
  log.debug('[{0}]: SOURCE PATH_BASE   : {1}'.format(INPUT, SOURCE['PATH_BASE']))

# DATE
  SOURCE['DATE_GROUPS'] = RegEx.getDateGroups(SOURCE['FILENAME'])
  log.debug('[{0}]: SOURCE DATE_GROUPS : {1}'.format(INPUT, SOURCE['DATE_GROUPS']))

  SOURCE['DATE_FIRST']  = SOURCE['DATE_GROUPS'].group(0)
  log.debug('[{0}]: SOURCE DATE_FIRST  : {1}'.format(INPUT, SOURCE['DATE_FIRST']))

  SOURCE['DATE_YEAR']   = RegEx.getDateInfo('y',SOURCE['DATE_FIRST'])
  log.debug('[{0}]: SOURCE DATE_YEAR   : {1}'.format(INPUT, SOURCE['DATE_YEAR']))

  SOURCE['DATE_MONTH']  = RegEx.getDateInfo('m',SOURCE['DATE_FIRST'])
  log.debug('[{0}]: SOURCE DATE_MONTH  : {1}'.format(INPUT, SOURCE['DATE_MONTH']))

  SOURCE['DATE_DAY']    = RegEx.getDateInfo('d',SOURCE['DATE_FIRST'])
  log.debug('[{0}]: SOURCE DATE_DAY    : {1}'.format(INPUT, SOURCE['DATE_DAY']))

# TIMES

  match = re.search(r'DAY-CREW|INFO-ONLY|NIGHT-CREW', SOURCE['FILENAME'])

  if not match:

    TIMEOFF = False

    SOURCE['TIME_GROUPS'] = RegEx.getTimeGroups(SOURCE['FILENAME'])
    log.debug('[{0}]: SOURCE TIME_GROUPS : {1}'.format(INPUT, SOURCE['TIME_GROUPS']))

    SOURCE['TIME_FIRST']  = SOURCE['TIME_GROUPS'].group(0)
    log.debug('[{0}]: SOURCE TIME_FIRST  : {1}'.format(INPUT, SOURCE['TIME_FIRST']))

    SOURCE['TIME_START']  = RegEx.getTimeInfo('s',SOURCE['TIME_FIRST'])
    log.debug('[{0}]: SOURCE TIME_START  : {1}'.format(INPUT, SOURCE['TIME_START']))

    SOURCE['TIME_END']    = RegEx.getTimeInfo('e',SOURCE['TIME_FIRST'])
    log.debug('[{0}]: SOURCE TIME_END    : {1}'.format(INPUT, SOURCE['TIME_END']))

  else: TIMEOFF = True


# EXTRA DATA
  SOURCE['EXTRA_DATA']  = RegEx.getExtraData(SOURCE['FILENAME'])
  log.debug('[{0}]: SOURCE EXTRA_DATA  : {1}'.format(INPUT, SOURCE['EXTRA_DATA']))


  if ' - ' in SOURCE['EXTRA_DATA']:
    SOURCE['ROOMS']  = SOURCE['EXTRA_DATA'].split(' - ')[0]
    SOURCE['EXTRAS'] = SOURCE['EXTRA_DATA'].split(' - ')[1]
  else:
    SOURCE['ROOMS'] = SOURCE['EXTRA_DATA']
    SOURCE['EXTRAS'] = ''

  log.debug('[{0}]: SOURCE ROOMS       : {1}'.format(INPUT, SOURCE['ROOMS']))
  log.debug('[{0}]: SOURCE EXTRAS      : {1}'.format(INPUT, SOURCE['EXTRAS']))


# SETUP TARGET FILENAME
  if TIMEOFF:
    TARGET['FILENAME']    = '{0}-{1}-{2} - {3}{4}'.format(
                                    SOURCE['DATE_YEAR'],
                                    SOURCE['DATE_MONTH'],
                                    SOURCE['DATE_DAY'],
                                    SOURCE['EXTRA_DATA'],
                                    SOURCE['EXT'],
                                    )
  else:
    TARGET['FILENAME']    = '{0}-{1}-{2} - {3}-{4} - {5}{6}'.format(
                                    SOURCE['DATE_YEAR'],
                                    SOURCE['DATE_MONTH'],
                                    SOURCE['DATE_DAY'],
                                    SOURCE['TIME_START'],
                                    SOURCE['TIME_END'],
                                    SOURCE['EXTRA_DATA'],
                                    SOURCE['EXT'],
                                    )

  log.debug('[{0}]: TARGET FILENAME    : {1}'.format(INPUT, TARGET['FILENAME']))


# SETUP TARGET BASE FOLDER
  TARGET['PATH_BASE']   = os.path.join(TARGET_PATH, SOURCE['DATE_YEAR'])
  TARGET['MONTH']       = common.GetMonthByNumber(int(SOURCE['DATE_MONTH']))
  log.debug('[{0}]: TARGET MONTH       : {1}'.format(INPUT, TARGET['MONTH']))

  TARGET['PATH_BASE']   = os.path.join(TARGET_PATH, SOURCE['DATE_YEAR'], TARGET['MONTH'])
  log.debug('[{0}]: TARGET PATH_BASE   : {1}'.format(INPUT, TARGET['PATH_BASE']))

  TARGET['FULLDEST']    = os.path.join(TARGET['PATH_BASE'], TARGET['FILENAME'])
  log.debug('[{0}]: TARGET FULLDEST    : {1}'.format(INPUT, TARGET['FULLDEST']))

#  TARGET['TRASH']       = os.path.join(TARGET_PATH, '.trash', SOURCE['DATE_YEAR'], TARGET['MONTH'])
#  log.debug('[{0}]: TARGET TRASH       : {1}'.format(INPUT, TARGET['TRASH']))




  NOGO = False

# Check if DIR exists
  if not common.CreateDIR(TARGET['PATH_BASE']):
    log.error('[{0}]: Unable to create directory. Aborting!'.format(INPUT))
    NOGO  = True
#   sys.exit()

# Check if FILE exists
  if not NOGO:
    if not common.CheckFile(TARGET['FULLDEST']):
      log.error('[{0}]: Unable to create file. Aborting!'.format(INPUT))
      NOGO  = True
#      sys.exit()

  if not NOGO: common.MoveFile(INPUT, TARGET['FULLDEST'])

  return True