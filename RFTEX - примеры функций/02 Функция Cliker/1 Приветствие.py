import RFSE
from MOSC import stars

RFSE.Stage(stars('*'))
RFSE.Stage(stars('RFSE Clicker'))
RFSE.Stage(stars('*'))

RFSE.Messenger('set', 'Приветствие#@hello', 'В данном презентации будут показаны 3 команды, но команд больше. '
                                         'Первая команда - получение скриншота экрана, '
                                         'вторая команда - указание пути картинки, '
                                         'последняя команда - получение картинки по указанному пути.')

#Region Status (статус)
#hash Greeting
RFSE.Program('tree', 'set', 'select = ' + 'Greeting')
RFSE.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Status

RFSE.EndScript()
