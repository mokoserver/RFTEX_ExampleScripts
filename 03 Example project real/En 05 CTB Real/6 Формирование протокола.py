import RFSE

RFSE.Stage("Начало скрипта")

#Region 6.1 Этапы формирования:
#hash Автосохранение результатов
#hash Формирование протокола

RFSE.Messenger('set', 'Формирование протокола.jpg', 'Сейчас автоматически сформируется протокол.', '', '5')

RFSE.Program('tree', 'set', 'select = ' + 'Автосохранение результатов')
RFSE.Program('tree', 'set', 'chosen = passed')

RFSE.Program('Control', 'set', 'Save word report')
RFSE.Program('Control', 'set', 'Save project report')

RFSE.Program('tree', 'set', 'select = ' + 'Формирование протокола')
RFSE.Program('tree', 'set', 'chosen = passed')

RFSE.Stage('Формирование протокола завершено.', 'info')
#EndRegion 6.1 Этапы формирования:

RFSE.Stage("Конец скрипта")

RFSE.EndScript()
