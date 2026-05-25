import RFSE

language = RFSE.Report("language", 'get', 'string', 'string', 'string')

#Region Status (статус)
#hash Plugin init

RFSE.Messenger('set', 'Plugin - init.png', 'В данном скрипте будет продемонстрирована команда \'\'init\'\', '
                                           'которая запускает плагин.')


RFSE.Plugin("Graph", 'init', '')

RFSE.Program('tree', 'set', 'select = ' + 'Plugin init')
RFSE.Program('tree', 'set', 'chosen = passed')

RFSE.EndScript()
