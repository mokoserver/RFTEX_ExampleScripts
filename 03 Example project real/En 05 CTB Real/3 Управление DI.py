import RFSE

RFSE.Stage("Начало скрипта")

#Region 3.1 Статус
#hash Управление DI

RFSE.Messenger('set', 'МК210-301.png', 'В текущем скрипте будет продемонстрирована работа в дискретными входами (DI) МК210-301', '', '5')
RFSE.Messenger('set', 'МК210-301.png', 'Узнаем состояние DI с помощью драйвера. \'\'1\'\' - выход активен, '
                                      '\'\'0\'\' - выход неактивен.', '', '5')
DI_state = RFSE.Driver('MK210', 'get', 'DI', 'string')
RFSE.Messenger('set', 'МК210-301.png', f'Текущее состояние DI - {DI_state}.', '', '3')

RFSE.Report('DI_state', 'set', 'string', f'{DI_state}')

RFSE.Program('tree', 'set', 'select = ' + 'Управление DI')
RFSE.Program('tree', 'set', 'chosen = passed')
# EndRegion 3.1 Статус

RFSE.Stage("Конец скрипта")
RFSE.EndScript()

