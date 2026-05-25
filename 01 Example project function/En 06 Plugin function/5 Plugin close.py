import RFSE

#Region Status
#hash Plugin close

RFSE.Messenger('set', 'Plugin - close.png', 'This script will demonstrate the \'\'close\'\' command, '
                                            'which closes the plugin.')

RFSE.Plugin('Graph', 'close', '')

RFSE.Program('tree', 'set', 'select = ' + 'Plugin close')
RFSE.Program('tree', 'set', 'chosen = passed')


RFSE.EndScript()
