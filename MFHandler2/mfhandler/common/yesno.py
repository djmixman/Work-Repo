import sys

def YNQ(question, default="no"):
    """
    Ask a yes/no/retry/quit question via raw_input() and return their answer.

    "question"    = a string that is presented to the user.
    "default"     = is the presumed answer if the user just hits <Enter>.
                    By default the script will retry and can be any one of the following;
                    "yes", "no", "retry", "quit", or None.

    script will return an int with the following values;
        retry =  2
        yes   =  1
        no    =  0
        quit  = -1
    """
    valid = {
#      'retry': 2,  'retr': 2,  'ret': 2, 're':2, 'r':2,
      'yes'  : 1,  'ye'  : 1,  'y'  : 1,
      'no'   : 0,  'n'   : 0,
      'quit' :-1,  'qui' :-1,  'qu' :-1,  'q':-1
    }

    if   default == None    : prompt = ' [y/n/q]: '
    elif default == "yes"   : prompt = ' [Y/n/q]: '
    elif default == "no"    : prompt = ' [y/N/q]: '
#    elif default == "retry" : prompt = ' [y/n/R/q]: '
    elif default == "quit"  : prompt = ' [y/n/Q]: '
    else: raise ValueError("invalid default answer: '%s'" % default)

    while 1:
        sys.stdout.write(question + prompt)
        choice      = input().lower()

        if default is not None and choice == '': return valid[default]
        elif choice in valid.keys(): return valid[choice]
        else: sys.stdout.write("Invalid Response. Please use 'yes', 'no', or 'quit'.\n")
