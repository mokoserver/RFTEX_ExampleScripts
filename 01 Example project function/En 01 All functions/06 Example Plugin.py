import RFSE as RFSE
from MOSC import stars
import time

RFSE.Stage(stars('*'))
RFSE.Stage(stars('NEW SCRIPT'))
RFSE.Stage(stars('*'))
language = RFSE.Report("language", 'get', 'string', 'string', 'string')

RFSE.Plugin('ExPlugin', 'init', '')

time.sleep(5)

RFSE.Stage('*Plugin*', 'Plugin')
RFSE.Messenger('set', 'Plugin_info', 'This script describes how the Plugin function works. For example '
                                     'the plugin \'\'ExPlugin\'\' is used, which has 2 modes of operation: '
                                     '\'\'set\'\' and \'\'get\'\'.')
RFSE.Messenger('set', 'Set Number1|2', 'The \'\'Number1|2\'\' command sets the number to Number1 or Number2 '
                                       'in the Main window. For this after the command = and the number '
                                       'to be written. By default, the numbers Number1 and Number2 are zero.')
RFSE.Plugin('ExPlugin', 'set', 'Number1=9')
RFSE.Plugin('ExPlugin', 'set', 'Number2=14')
RFSE.Messenger('set', 'Get Sum', 'The \'\'Sum\'\' command returns the sum from the Sum field in the Main window.')
sum = RFSE.Plugin('ExPlugin', 'get', 'Sum', 'string')
RFSE.Messenger('set', 'Sum', 'Sum: ' + sum)
RFSE.Report("explugin_1", 'set', 'string', sum)
RFSE.Messenger('set', 'Set String', 'The \'\'Set String\'\' command writes a string to the ExPlugin. To do this, after '
                                    'command is set = and the information to be recorded. '
                                    'The information is displayed in the String field in the Main window.')
RFSE.Plugin('ExPlugin', 'set', 'String=Hello, World!')
RFSE.Messenger('set', 'Get String', 'The Get String command returns a string from the String field '
                                    'in the Main window.')
a = RFSE.Plugin('ExPlugin', 'get', 'String', 'string')
RFSE.Messenger('set', 'String', 'String from ExPlugin: ' + a)
RFSE.Report("explugin", 'set', 'string', a)
RFSE.Messenger('set', 'Set Screenshot', 'The \'\'Screenshot\'\' command takes a screenshot of the plugin, '
                                        'whose name consists of'
                                        'date and time at the moment of the screenshot. '
                                        'The screenshot is saved in a separate folder '
                                        'App/screenshots in ExPlugin root directory')
RFSE.Plugin('ExPlugin', 'set', 'Screenshot')
RFSE.Messenger('set', 'Set ChangeLedLoop', 'The \'\'ChangeLedLoop\'\' command changes the value'
                                           ' of the Led Loop indicator in the main window.')
RFSE.Plugin('ExPlugin', 'set', 'ChangeLedLoop')
RFSE.Messenger('set', 'Set ShowTab', 'The command \'\'Showtab\'\' change displays the desired plugin '
                                     'window (Main | Graph | Info). '
                                     'To do this, after the command, put = and the name of the required window.')
RFSE.Plugin('ExPlugin', 'set', 'ShowTab=Info')
time.sleep(10)
RFSE.Plugin('ExPlugin', 'set', 'ShowTab=Graph')
time.sleep(3)
RFSE.Messenger('set', 'Set Graph', 'The \'\'Graph\'\' command starts or stops a graph in the Graph window. '
                                   'To start after command \'\'Graph\'\' is set =start, and for stop =stop.')
RFSE.Plugin('ExPlugin', 'set', 'Graph=start')
RFSE.Messenger('set', 'Get InstantScreenshot', 'The \'\'InstantScreenshot\'\' command returns a screenshot'
                                               ' of the ExPlugin window.')
screen = RFSE.Plugin('ExPlugin', 'get', 'InstantScreenshot', 'string')
RFSE.Report("explugin_2", 'set', 'picture', screen)
RFSE.Plugin('ExPlugin', 'set', 'Graph=stop')
RFSE.Report("explugin_3", 'set', 'string', 'The script completed successfully.')

RFSE.Stage(stars('*'))
RFSE.Stage(stars('NEXT SCRIPT'))
RFSE.Stage(stars('*'))

RFSE.EndScript()