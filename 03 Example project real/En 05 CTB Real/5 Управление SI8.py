import RFSE

RFSE.Stage("Начало скрипта")

#Region 5.1 Статус
#hash Управление SI8

RFSE.Messenger('set', 'SI8.jpg', 'В текущем скрипте будет продемонстрирована работа с SI8.', '', '5')
RFSE.Messenger('set', 'SI8.jpg', 'Узнаем текущее время.' '', '5')
TimeNow = RFSE.Driver('SI8', 'get', 'UTC', 'string')
RFSE.Messenger('set', 'SI8.jpg', f'Текущее время - {TimeNow}.', '', '3')

RFSE.Report('TimeNow', 'set', 'string', f'{TimeNow}')

RFSE.Program('tree', 'set', 'select = ' + 'Управление SI8')
RFSE.Program('tree', 'set', 'chosen = passed')
# EndRegion 5.1 Статус

RFSE.Stage("Конец скрипта")
RFSE.EndScript()

