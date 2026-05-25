import RFSE

RFSE.Stage("Начало скрипта")

#Region 4.1 Статус
#hash Съем показаний

RFSE.Messenger('set', 'ELait03.jpg', 'В данном скрипте будет продемонстрирована работа с ELait3.', '', '5')
RFSE.Messenger('set', 'ELait03.jpg', 'Узнаем значение светового давления с помощью драйвера.' '', '5')
Lumen = RFSE.Driver('ELait03', 'get', 'Lumen', 'string')

RFSE.Messenger('set', 'ELait03.jpg', f'Текущее значение светового давления - {Lumen} кд/(м^2).', '', '3')

RFSE.Report('Lumen', 'set', 'string', f'{Lumen}')

RFSE.Program('tree', 'set', 'select = ' + 'Съем показаний')
RFSE.Program('tree', 'set', 'chosen = passed')
# EndRegion 4.1 Статус

RFSE.Stage("Конец скрипта")
RFSE.EndScript()

