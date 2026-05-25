import RFSE as RFSE
from MOSC import stars

RFSE.Stage(stars('*'))
RFSE.Stage(stars('NEW SCRIPT'))
RFSE.Stage(stars('*'))

RFSE.Stage('*Driver*', 'Driver')
RFSE.Messenger('set', 'Driver_info', 'This script describes how the Driver function works. For example '
                                     'the \'\'ExDriver\'\' driver is used, which has several modes of operation,'
                                     'which will act further.')
RFSE.Messenger('set', 'set', 'The \'\'set\'\' mode sets a specific command to the driver. This ExDriver driver has'
                             'the command \'\'value\'\'. '
                             'This way you can enter your own value into the driver')
RFSE.Driver('ExDriver', 'set', 'value = 5')
RFSE.Messenger('set', 'get', 'The \'\'get\'\' mode returns the value you entered.')
value = RFSE.Driver('ExDriver', 'get', 'value', 'string')
RFSE.Messenger('set', 'True', f'You entered {value}.')
RFSE.Report("exdriver", 'set', 'string', f'You entered {value}.')
RFSE.Messenger('set', 'init', 'In \'\'init\'\' mode, the driver initialization window appears on the screen. '
                              'Since there is no device, click on the \'\'Cancel\'\' button.')
RFSE.Driver('ExDriver', 'init', '')
RFSE.Report("exdriver_1", 'set', 'string', 'The script completed successfully.')

RFSE.Stage(stars('*'))
RFSE.Stage(stars('NEXT SCRIPT'))
RFSE.Stage(stars('*'))

RFSE.EndScript('passed')