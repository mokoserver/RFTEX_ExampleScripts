import RFSE as RFSE
from MOSC import stars

RFSE.Stage(stars('*'))
RFSE.Stage(stars('NEW SCRIPT'))
RFSE.Stage(stars('*'))


RFSE.Stage('*Program*', 'info')
RFSE.Messenger('set', 'Program_info', 'This script implements one of the many functions of Program.')
RFSE.Messenger('set', 'Program', 'The Program function is intended to control various elements from the script '
                                 'RF-SE programs (scripts, project, control etc). '
                                 'Program has one mode of operation - \'\'set\'\', the function can only write '
                                 'certain commands.')
RFSE.Program('control', 'set', 'save word report')


RFSE.Stage(stars('*'))
RFSE.Stage(stars('NEXT SCRIPT'))
RFSE.Stage(stars('*'))

RFSE.EndScript()