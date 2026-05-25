import RFSE as RFSE
from MOSC import stars
import time

RFSE.Stage(stars('*'))
RFSE.Stage(stars('Новый SCRIPT'))
RFSE.Stage(stars('*'))
language = RFSE.Report("language", 'get', 'string', 'string', 'string')

RFSE.Plugin('ExPlugin', 'init', '')

time.sleep(5)

RFSE.Stage('*Plugin*', 'Plugin')
RFSE.Messenger('set', 'Plugin_info', 'В это скрипте описывается принцип работы функции Plugin. Для примера '
                                 'используется плагин \'\'ExPlugin\'\', имеющий 2 режима работы: \'\'set\'\' и \'\'get\'\'.')
RFSE.Messenger('set', 'Set Number1|2', 'Команда \'\'Number1|2\'\' задает число Number1 или Number2 в окне Main. Для этого '
                                   'после команды ставиться = и число, которое нужно записать. ' +
           'По умолчанию числа Number1 и Number2 равны нулю.')
RFSE.Plugin('ExPlugin', 'set', 'Number1=9')
RFSE.Plugin('ExPlugin', 'set', 'Number2=14')
RFSE.Messenger('set', 'Get Sum', 'Команда \'\'Sum\'\' возвращает сумму из поля Sum в окне Main.')
sum = RFSE.Plugin('ExPlugin', 'get', 'Sum', 'string')
RFSE.Messenger('set', 'Sum', 'Сумма: ' + sum)
RFSE.Report("explugin_1", 'set', 'string', sum)

RFSE.Messenger('set', 'Set String', 'Команда \'\'Set String\'\' записывает какую-либо строку в ExPlugin. Для этого после '
                                'команды ставиться = и информация, которую нужно записать. ' +
           'Информация отобразится в поле String в окне Main.')
RFSE.Plugin('ExPlugin', 'set', 'String=Hello, World!')
RFSE.Messenger('set', 'Get String', 'Команда \'\'Get String\'\' возвращает строку из поля String в окне Main.')
a = RFSE.Plugin('ExPlugin', 'get', 'String', 'string')
RFSE.Messenger('set', 'String', 'Строка из ExPlugin: ' + a)
RFSE.Report("explugin", 'set', 'string', a)

RFSE.Messenger('set', 'Set Screenshot', 'Команда \'\'Screenshot\'\' делает скриншот плагина, название которого состоит из '
                                    'даты и времени в момент скриншота. Скриншот сохраняется в отдельную папку '
                                    'App/screenshots в корневом каталоге ExPlugin.')
RFSE.Plugin('ExPlugin', 'set', 'Screenshot')
RFSE.Messenger('set', 'Set ChangeLedLoop', 'Команда \'\'ChangeLedLoop\'\' меняет значение индикатора Led Loop в окне Main.')
RFSE.Plugin('ExPlugin', 'set', 'ChangeLedLoop')

RFSE.Messenger('set', 'Set ShowTab', 'Команда \'\'Showtab\'\' меняте отображает нужное окно плагина (Main | Graph | Info). '
                                 'Для этого после команды ставиться = и название нужного окна.')
RFSE.Plugin('ExPlugin', 'set', 'ShowTab=Info')
time.sleep(10)
RFSE.Plugin('ExPlugin', 'set', 'ShowTab=Graph')
time.sleep(3)
RFSE.Messenger('set', 'Set Graph', 'Команда \'\'Graph\'\' запускает или останавливает график в окне Graph. Для старта после '
                               'команды \'\'Graph\'\' ставиться =start, а для остановки =stop.')
RFSE.Plugin('ExPlugin', 'set', 'Graph=start')

RFSE.Messenger('set', 'Get InstantScreenshot', 'Команда \'\'InstantScreenshot\'\' возвращает скриншот окна ExPlugin.')
screen = RFSE.Plugin('ExPlugin', 'get', 'InstantScreenshot', 'string')
RFSE.Report("explugin_2", 'set', 'picture', screen)
RFSE.Plugin('ExPlugin', 'set', 'Graph=stop')

RFSE.Report("explugin_3", 'set', 'string', 'Скрипт успешно завершён.')

RFSE.Stage(stars('*'))
RFSE.Stage(stars('Следующий SCRIPT'))
RFSE.Stage(stars('*'))

RFSE.EndScript()
