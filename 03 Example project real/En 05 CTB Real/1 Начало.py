import RFSE

#Region 1.1 Статус
#hash Приветствие

RFSE.Stage("Начало скрипта")
RFSE.Messenger('set', 'Greeting#@hello', 'В данном проекте будут показаны возможности чего-то там. Приятного просмотра!', '', '7')

RFSE.Program('tree', 'set', 'select = ' + 'Приветствие')
RFSE.Program('tree', 'set', 'chosen = passed')
# EndRegion 1.1 Статус

RFSE.Stage("Конец скрипта")

RFSE.EndScript()