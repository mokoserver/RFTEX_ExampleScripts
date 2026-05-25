import RFSE
from MOSC import stars

RFSE.Stage(stars('*'))
RFSE.Stage(stars('Новый SCRIPT'))
RFSE.Stage(stars('*'))

RFSE.Stage('Utility', 'Utility')
RFSE.Messenger('set', 'set', 'В этом скрипте демонстрируется принцип работы функции Utility. Для примера используется '
                         'утилита \'\'ExUtility\'\', имеющая два режима работы и одну команду. ')
RFSE.Messenger('set', 'set', 'Режим \'\'set\'\' задает определенную команду в утилиту. В данной утилите - команда \'\'text\'\'. '
                         'Результатом команды \'\'text\'\' является окно с названием команды и  двумя конпками: \'\'OK\'\' и '
                         '\'\'Cancel\'\'. Нажатие любой из них приведёт к закрытию окна.')
RFSE.Utility('RFSE_example', 'set', 'text')

RFSE.Messenger('set', 'get', 'Режим \'\'get\'\' возвращает значение типа \'\'booleanм. При нажатии на \'\'OK\'\' возвращает значение '
                         'True, при \'\'Cancel\'\' - False.')
resp = RFSE.Utility('RFSE_example', 'get', 'text', 'boolean')
if resp:
    RFSE.Messenger('set', 'True', 'Вы нажали на кнопку \'\'OK\'\'.')
    RFSE.Report("exutility", 'set', 'string', 'Вы нажали на \'\'OK\'\' и ExUtility вернула значение True.')
else:
    RFSE.Messenger('set', 'False', 'Вы нажали на кнопку \'\'Cancel\'\'.')
    RFSE.Report("exutility", 'set', 'string', 'Вы нажали на \'\'Cancel\'\' и ExUtility вернула значение False.')
RFSE.Messenger('set', 'command', 'Команда \'\'text\'\' имеет возможность передать какую-либо информацию во всплывающее окно '
                             'так же, как и в драйвере. \'\'text=Hello,World!\'\' ')
RFSE.Utility('RFSE_example', 'set', 'text=Hello, World!')
RFSE.Report("exutility_1", 'set', 'string', 'Скрипт успешно завершён.')

RFSE.Stage(stars('*'))
RFSE.Stage(stars('Следующий SCRIPT'))
RFSE.Stage(stars('*'))

RFSE.EndScript('failed')
