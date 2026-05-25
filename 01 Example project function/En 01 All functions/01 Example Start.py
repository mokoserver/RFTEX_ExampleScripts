import RFSE
from MOSC import stars

RFSE.Stage(stars('*'))
RFSE.Stage(stars('START'))
RFSE.Stage(stars('*'))

RFSE.Messenger('set', 'Greeting#@hello', 'Dear User!\nThanks for installing RF-SE.\nEnjoyable using!')

RFSE.Stage(stars('*'))
RFSE.Stage(stars('NEXT SCRIPT'))
RFSE.Stage(stars('*'))
RFSE.EndScript()