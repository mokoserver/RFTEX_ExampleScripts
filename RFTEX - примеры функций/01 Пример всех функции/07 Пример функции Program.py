import RFSE as RFSE
from MOSC import stars

RFSE.Stage(stars('*'))
RFSE.Stage(stars('Новый SCRIPT'))
RFSE.Stage(stars('*'))

RFSE.Stage('*Program*', 'info')
RFSE.Messenger('set', 'Program_info', 'В этом скрипте реализуется одна из многих функций Program.')
RFSE.Messenger('set', 'Program', 'Функция Program предназначена для управления из скрипта различными элементами '
                                 'программы RF-SE (scripts, project, control etc). ' +
                                 'Program имеет один режим работы - \'\'set\'\', т.е. '
                                 'функция может только записывать определенные команды.')

RFSE.Messenger('set', 'Control', 'Сохраняем Word протокол.')
RFSE.Program('control', 'set', 'save word report')

RFSE.Stage(stars('*'))
RFSE.Stage(stars('Следующий SCRIPT'))
RFSE.Stage(stars('*'))

RFSE.EndScript()
