import RFSE

#Region Status (статус)
#hash Plugin close

RFSE.Messenger('set', 'Plugin - close.png', 'В данном скрипте будет продемонстрирована команда \'\'close\'\', '
                                            'которая закрывает плагин.')

RFSE.Plugin('Graph', 'close', '')

RFSE.Program('tree', 'set', 'select = ' + 'Plugin close')
RFSE.Program('tree', 'set', 'chosen = passed')


RFSE.EndScript()
