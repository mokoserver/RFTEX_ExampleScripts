import RFSE as RFSE
from MOSC import stars

RFSE.Stage(stars('*'))
RFSE.Stage(stars('Новый SCRIPT'))
RFSE.Stage(stars('*'))

RFSE.Stage('*Driver*', 'Driver')
RFSE.Messenger('set', 'Driver_info', 'В этом скрипте описывается принцип работы функции Driver. Для примера '
                                 'используется драйвер \'\'ExDriver\'\', имеющий несколько режимов работы, '
                                 'которые будут продемонстрированы далее.')

RFSE.Messenger('set', 'set', 'Режим \'\'set\'\' задает определенную команду в драйвер. Данный драйвер \'\'ExDriver\'\' имеет '
                         'команду - \'\'value\'\'. Таким образом Вы можете ввести значение value в драйвер.')
value = RFSE.Driver('ExDriver', 'get', 'value', 'string')
RFSE.Messenger('set', 'True', f'Вы ввели {value}.')
RFSE.Report("exdriver", 'set', 'string', f'Вы ввели {value}.')

RFSE.Messenger('set', 'init', 'В режиме \'\'init\'\' на экране появляется окно инициализации драйвера. Так как прибора нет, '
                          'следует нажать на кнопку \'\'Cancel\'\'.')
RFSE.Driver('ExDriver', 'init', '')
RFSE.Report("exdriver_1", 'set', 'string', 'Скрипт успешно завершён.')


RFSE.Stage(stars('*'))
RFSE.Stage(stars('Новый SCRIPT'))
RFSE.Stage(stars('*'))

RFSE.EndScript('passed')
