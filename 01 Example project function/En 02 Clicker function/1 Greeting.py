import RFSE
from MOSC import stars

RFSE.Stage(stars('*'))
RFSE.Stage(stars('RFSE Clicker'))
RFSE.Stage(stars('*'))


RFSE.Messenger('set', 'Greeting#@hello',
               'This presentation will show 3 commands, but there are more commands. '
               'The first command is to get a screenshot of the screen, '
               'the second command is to specify the image path and '
               'the last command is to get the image from the specified path.')

#Region Status
#hash Greeting

RFSE.Program('tree', 'set', 'select = ' + 'Greeting')
RFSE.Program('tree', 'set', 'chosen = passed')

#EndRegion Region Status

RFSE.EndScript()