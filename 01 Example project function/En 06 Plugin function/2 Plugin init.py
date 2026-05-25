import RFSE

#Region Status
#hash Plugin init

RFSE.Messenger('set', 'Plugin - init.png', 'This script will demonstrate the \'\'init\'\' command, '
                                           'which starts the plugin.')

RFSE.Plugin("Graph", 'init', '')

RFSE.Program('tree', 'set', 'select = ' + 'Plugin init')
RFSE.Program('tree', 'set', 'chosen = passed')

RFSE.EndScript()
