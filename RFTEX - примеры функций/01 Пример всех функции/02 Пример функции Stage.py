import RFSE as RFSE
from MOSC import stars
import time

RFSE.Stage(stars('*'))
RFSE.Stage(stars('Новый SCRIPT'))
RFSE.Stage(stars('*'))

RFSE.Stage('Добро пожаловать в программу RF-SE.')
RFSE.Stage('Программа RF-SE осуществляет управление программой RFSE NMEA и программами-драйверами')
RFSE.Stage('Управление программой реализуется через выполнение скриптов написанных на Python.')
RFSE.Stage('Данный скрипт демонстрирует работу функции Stage.')
RFSE.Stage('Сообщения в Stage могут иметь определенный тип. Ниже представлен каждый из типов.')
RFSE.Stage('*Info*. Выводит какую-либо информацию в Stage. Обозначен как тип по умолчанию', 'Info')
RFSE.Stage('*Error*. Информирует об ошибке, произошедшей во время выполнения скрипта.', 'Error')
RFSE.Stage('*Plugin*. Выводит информацию, связанную с плагином.', 'Plugin')
RFSE.Stage('*Driver*. Выводит информацию, связанную с драйвером.', 'Driver')
RFSE.Stage('*Report*. Информирует о записи данных в отчёт.', 'Report')
RFSE.Stage('*Utility*. Сообщает об использовании утилиты.', 'Utility')
RFSE.Stage('*Messenger*. Информирует о выводе окна Messenger.', 'Messenger')
RFSE.Stage('*Telegram*. afafafaf', 'Telegram')
RFSE.Stage('*Warning*. Информирует о предупреждении, произошедшем во время выполнения скрипта.', 'Warning')
time.sleep(6)
RFSE.Report("exstage", 'set', 'string', 'Отсутствуют')
RFSE.Report("exstage_1", 'set', 'string', 'Скрипт успешно завершён.')

RFSE.Stage(stars('*'))
RFSE.Stage(stars('Следующий SCRIPT'))
RFSE.Stage(stars('*'))

RFSE.EndScript()
