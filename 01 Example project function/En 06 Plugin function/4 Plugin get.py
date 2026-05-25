import RFSE
import MGPH

#Region Status
#hash Plugin get

RFSE.Messenger('set', 'Plugin - get.png', 'The current script will demonstrate the \'\'get\'\' command, '
                                          'which receives data from the plugin. '
                                          'In the scripts will be made a screenshot.')


screen = MGPH.GetScreenshotWindow()
RFSE.Report("Screenshot_1_All", 'set', 'picture', screen)

RFSE.Program('tree', 'set', 'select = ' + 'Plugin get')
RFSE.Program('tree', 'set', 'chosen = passed')

RFSE.EndScript()
