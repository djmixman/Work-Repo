import re, os

from datetime import datetime

# from logger import log


def getDateGroups(s):
  match = re.search(r'\d{4}-\d{2}-\d{2}', s)
  return match

def getDateInfo(t, s):
  DATE = datetime.strptime(s, "%Y-%m-%d")

  if t == "y": return '{0:04d}'.format(DATE.year)
  if t == "m": return '{0:02d}'.format(DATE.month)
  if t == "d": return '{0:02d}'.format(DATE.day)


def getTimeGroups(s):
  '''
  This will match "1600-1700" or '2018-06-01T1600 - 2018-06-02T1700'
  '''
  match = re.search(r'((\d{4}-\d{4})|(\d{4}-\d{2}-\d{2}T\d{4} - \d{4}-\d{2}-\d{2}T\d{4}))', s)
# match = re.search(r'((\d{4}-\d{4})|(\d{4}-\d{2}-\d{2}T\d{4} - \d{4}-\d{2}-\d{2}T\d{4})|(INFO-ONLY|NIGHT-CREW|DAY-CREW))', s)
  return match

def getTimeInfo(t, s):
  '''
  t = type
    s for start
    e for end
  s = time string to parse
  '''
  if 'T' in s:
    if t == 's' : OUTPUT = s.split(" - ")[0]
    else        : OUTPUT = s.split(" - ")[1]

    TIME = datetime.strptime(OUTPUT, "%Y-%m-%dT%H%M")
    return ('{0:02d}{1:02d}'.format(TIME.hour, TIME.minute))

  else:
    if t == 's' : OUTPUT = s.split("-")[0]
    else        : OUTPUT = s.split("-")[1]
    return OUTPUT



def getName(t, s):
  '''
  Get name from (s)tring
  t = f(irst), l(ast)
  '''
  lastname = re.search(r'([a-zA-Z].*), [A-z]', s)
  firstname = re.search(r'[A-Za-z0-9],\s([A-Za-z0-9\s]+)\s-', s)

  if "f" in t: return firstname.group(1)
  if "l" in t: return lastname.group(1)

def getExtraData(s):
  '''
  Gets the extra data at the end of the file. Rooms, Notes, etc
  '''
  OUTPUT = re.search('- ([A-z][A-Za-z0-9].+)', s)
  return OUTPUT.group(1)


