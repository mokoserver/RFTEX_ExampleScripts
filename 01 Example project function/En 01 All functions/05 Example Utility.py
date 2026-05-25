import RFSE
from MOSC import stars

RFSE.Stage(stars('*'))
RFSE.Stage(stars('NEW SCRIPT'))
RFSE.Stage(stars('*'))


RFSE.Stage('Utility', 'Utility')
RFSE.Messenger('set', 'set', 'This script demonstrates how the Utility function works. For example, '
                             'utility \'\'ExUtility\'\', which has two modes of operation and one command.')
RFSE.Messenger('set', 'set', 'The \'\'set\'\' mode sets a specific command to the utility. '
                             'In this utility, the command is \'\'text\'\'. '
                             'The result of the \'\'text\'\' command is a window with the command name and two buttons: '
                             '\'\'OK\'\' and \'\'Cancel\'\'. Clicking any of them will close the window.')
RFSE.Utility('RFSE_example', 'set', 'text')
RFSE.Messenger('set', 'get', 'The \'\'get\'\' mode returns a value of type \'\'boolean\'\'. Clicking on \'\'OK\'\' returns the value '
                             'True, with \'\'Cancel\'\' - False.')
resp = RFSE.Utility('RFSE_example', 'get', 'text', 'boolean')
if resp:
    RFSE.Messenger('set', 'True', 'You clicked on the \'\'OK\'\' button.')
    RFSE.Report("exutility", 'set', 'string', 'You clicked on \'\'OK\'\' and ExUtility returned True.')
else:
    RFSE.Messenger('set', 'False', 'You clicked on the \'\'Cancel\'\' button.')
    RFSE.Report("exutility", 'set', 'string', 'You clicked on \'\'Cancel\'\' and ExUtility returned False.')

RFSE.Messenger('set', 'command', 'The \'\'text\'\' command has the ability to pass any information to the popup '
                                 'is the same as in the driver. \'\'text = Hello, World!\'\'')
RFSE.Utility('RFSE_example', 'set', 'text=Hello, World!')
RFSE.Report("exutility_1", 'set', 'string', 'The script completed successfully.')


RFSE.Stage(stars('*'))
RFSE.Stage(stars('NEXT SCRIPT'))
RFSE.Stage(stars('*'))

RFSE.EndScript('failed')