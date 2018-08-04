from datetime import datetime
### Month Formatter

ABBV_BY_NUM   = {  1: 'Jan',      2: 'Feb',       3: 'Mar',   4: 'Apr',   5: 'May', 6: 'Jun',   7: 'Jul',   8: 'Aug',     9: 'Sep',       10: 'Oct',      11: 'Nov',      12: 'Dec'       }
NAME_BY_NUM   = {  1: 'January',  2: 'February',  3: 'March', 4: 'April', 5: 'May', 6: 'June',  7: 'July',  8: 'August',  9: 'September', 10: 'October',  11: 'November', 12: 'December'  }
NUM_BY_MONTH  = {
                  'jan': 1, 'january'   : 1,
                  'feb': 2, 'february'  : 2,
                  'mar': 3, 'march'     : 3,
                  'apr': 4, 'april'     : 4,
                  'may': 5, 'may'       : 5,
                  'jun': 6, 'june'      : 6,
                  'jul': 7, 'july'      : 7,
                  'aug': 8, 'august'    : 8,
                  'sep': 9, 'september' : 9,
                  'oct':10, 'october'   :10,
                  'nov':11, 'november'  :11,
                  'dec':12, 'december'  :12
}

def getFiscalYear(START_MONTH, DATE):
    # if month from date is more than first month incr year by one, if it less than first month keep year
    dt = datetime.strptime(DATE, '%Y-%m-%d')
    FY = dt.year
    if dt.month >= START_MONTH: FY += 1
    return FY

def getNumByValue(value):
    """
    This function will return a number based on value input
    "value"   = Month, Month ABBV

    returns: int of month
    """
    if value.lower() in NUM_BY_MONTH.keys(): return NUM_BY_MONTH[value]
    else: return -1


def getNumDotAbbr(num):
  """
  This function will return the month number
  and the abbv. month name.

  "num" can be a padded string or int

  returns string  ex: '01. Jan'
  """
  i = 0
  try:
    i = int(num)
  except ValueError as verr:  pass
  except Exception  as   ex:  pass

  if i in ABBV_BY_NUM.keys(): return '{0:02d}. {1}'.format(i, ABBV_BY_NUM[i])
  else: raise ValueError('"num" should be in the range of "1 - 12"')


def getNumDotFull(num):
  """
  This function will return the month number
  and the abbv. month name.

  "num" can be a padded string or int

  returns string  ex: '01. January'
  """
  i = 0
  try:
    i = int(num)
  except ValueError as verr:  pass
  except Exception  as   ex:  pass

  if i in NAME_BY_NUM.keys(): return '{0:02d}. {1}'.format(i, NAME_BY_NUM[i])
  else: raise ValueError('"num" should be in the range of "1 - 12"')


def getAbbv(num):
  """
  This function will return the month number
  and the abbv. month name.

  "num" can be a padded string or int

  returns string  ex: 'Jan'
  """
  i = 0
  try:
    i = int(num)
  except ValueError as verr:  pass
  except Exception  as   ex:  pass

  if i in ABBV_BY_NUM.keys(): return '{0}'.format(ABBV_BY_NUM[i])
  else: raise ValueError('"num" should be in the range of "1 - 12"')


def getFull(num):
  """
  This function will return the month number
  and the abbv. month name.

  "num" can be a padded string or int

  returns string  ex: 'January'
  """
  i = 0
  try:
    i = int(num)
  except ValueError as verr:  pass
  except Exception  as   ex:  pass

  if i in NAME_BY_NUM.keys(): return '{0}'.format(NAME_BY_NUM[i])
  else: raise ValueError('"num" should be in the range of "1 - 12"')
