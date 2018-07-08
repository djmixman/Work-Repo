import sys, os, shutil

from logger import log


def YN(question, default="no"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

def CreateDIR(DIR):
  '''
  Checks and creates dirs if needed.
  '''

  if not os.path.isdir(DIR):
    ANSWER = YN('"{0}" does not exists. Create?'.format(DIR))

    if ANSWER:
      log.info('Creating Directory: {0}'.format(DIR))
      os.makedirs(DIR)
      return True
    else: return False
  else: return True


def CheckFile(FILE):
  '''
  Check if file exists and asks to overwrite
  '''

#  print('FILE EXIST: {0}'.format(os.path.isfile(FILE)))

  if os.path.isfile(FILE):
    ANSWER = YN('[{0}] already exists. Delete file?'.format(FILE))

    if ANSWER:
#      log.info('[MOVE] {0} -> TRASH'.format(FILE))
      RemoveFile(FILE)
      return True
    else:
      return False
  else: return True


def GetMonthByNumber(MONTH):
  if MONTH == 1: return '01. Jan'
  if MONTH == 2: return '02. Feb'
  if MONTH == 3: return '03. Mar'
  if MONTH == 4: return '04. Apr'
  if MONTH == 5: return '05. May'
  if MONTH == 6: return '06. Jun'
  if MONTH == 7: return '07. Jul'
  if MONTH == 8: return '08. Aug'
  if MONTH == 9: return '09. Sep'
  if MONTH == 10: return '10. Oct'
  if MONTH == 11: return '11. Nov'
  if MONTH == 12: return '12. Dec'

def RemoveFile(SOURCE):
  log.info('[DELETE] {0}'.format(SOURCE))
  os.remove(SOURCE)


def TrashFile(SOURCE, DEST):
  log.info('[TRASH] {0} -> {1}'.format(SOURCE))
  MoveFile(SOURCE, DEST)


def MoveFile(SOURCE, DEST):
  log.info('[MOVE] {0} -> {1}'.format(SOURCE, DEST))
  shutil.move(SOURCE, DEST)
