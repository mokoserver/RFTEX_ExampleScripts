import RFSE as RFSE
from MOSC import stars

RFSE.Stage(stars('*'))
RFSE.Stage(stars('NEW SCRIPT'))
RFSE.Stage(stars('*'))

RFSE.Messenger('set', 'Farewell#@bye', 'Previous messages demonstrated the work of the Messenger. '
                                       'Thanks for using RF-SE. Good luck!')
RFSE.Stage(stars('*'))
RFSE.Stage(stars('END'))
RFSE.Stage(stars('*'))

RFSE.EndScript()
