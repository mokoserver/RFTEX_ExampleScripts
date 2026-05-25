import RFSE as RFSE
from MOSC import stars

RFSE.Stage(stars('*'))
RFSE.Stage(stars('Старт'))
RFSE.Stage(stars('*'))

RFSE.Messenger('set', 'Приветствие#@hello', 'Дорогой пользователь!\n'
                                            'Спасибо, что установили RF-SE.\n'
                                            'Приятного пользования!')

RFSE.Stage(stars('*'))
RFSE.Stage(stars('Следующий SCRIPT'))
RFSE.Stage(stars('*'))
RFSE.EndScript()