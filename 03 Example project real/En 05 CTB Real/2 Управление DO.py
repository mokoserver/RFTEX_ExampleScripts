import RFSE

RFSE.Stage("Начало скрипта")

#Region 2.1 Статус
#hash Управление DO

RFSE.Messenger('set', 'МК210-301.png', 'В данном скрипте будет продемонстрирована работа в дискретными выходами (DO) МК210-301', '', '5')
RFSE.Messenger('set', 'МК210-301.png', 'Узнаем состояние DO с помощью драйвера. \'\'1\'\' - выход активен, '
                                      '\'\'0\'\' - выход неактивен.', '', '5')
DO_state = RFSE.Driver('MK210', 'get', 'DO', 'string')
RFSE.Messenger('set', 'МК210-301.png', f'Текущее состояние DO - {DO_state}.', '', '3')

RFSE.Messenger('set', 'МК210-301.png', 'Сделаем все выходы активными.', '', '5')
RFSE.Driver('MK210', 'set', 'DO = ALL ON')
DO_state = RFSE.Driver('MK210', 'get', 'DO', 'string')
RFSE.Messenger('set', 'МК210-301.png', f'Текущее состояние DO - {DO_state}.', '', '3')

RFSE.Messenger('set', 'МК210-301.png', 'Сделаем все выходы неактивными.', '', '5')
RFSE.Driver('MK210', 'set', 'DO = ALL OFF')
DO_state = RFSE.Driver('MK210', 'get', 'DO', 'string')
RFSE.Messenger('set', 'МК210-301.png', f'Текущее состояние DO - {DO_state}.', '', '3')

RFSE.Messenger('set', 'МК210-301.png', 'Теперь сделаем выход 2 активным.', '', '5')
RFSE.Driver('MK210', 'set', 'DO = 2 ON')
DO_state = RFSE.Driver('MK210', 'get', 'DO', 'string')
RFSE.Messenger('set', 'МК210-301.png', f'Текущее состояние DO - {DO_state}.', '', '3')

RFSE.Report('DO_state', 'set', 'string', f'{DO_state}')

RFSE.Program('tree', 'set', 'select = ' + 'Управление DO')
RFSE.Program('tree', 'set', 'chosen = passed')
# EndRegion 2.1 Статус

RFSE.Stage("Конец скрипта")
RFSE.EndScript()

