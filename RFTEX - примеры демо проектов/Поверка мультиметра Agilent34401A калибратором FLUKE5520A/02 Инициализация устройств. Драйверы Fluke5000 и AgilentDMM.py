import RFSE
from SettingsAndMeasurement import Poverka

RFSE.Stage("*********************************************************")
RFSE.Stage("************ Скрипт инициализации устройств *************")
RFSE.Stage("*********************************************************")
RFSE.Stage(" ")

RFSE.Stage("*********************************************************")
RFSE.Messenger("set", 'Подключите устройство#@agilent34401a',
               'Подключите поверяемый прибор через интерфейс\n'
               'Эталонное оборудование: FLUKE5520.\n'
               'Поверяемое оборудование: AGILENT34401.\n'
               'Процедура поверки: пример.', delaytime='10')
RFSE.Stage("*********************************************************")
RFSE.Stage(" ")

#region Инициализация AGILENT34401A$Init
RFSE.Program('tree', 'set', 'select = Инициализация AGILENT34401A$Init')

Poverka.Agilent34401A.Initialization()

#endregion Инициализация AGILENT34401A$Init

#region Инициализация FLUKE5520A$Init
RFSE.Program('tree', 'set', 'select = Инициализация FLUKE5520A$Init')

Poverka.Fluke5520A.Initialization()

#endregion Инициализация FLUKE5520A$Init

RFSE.EndScript()
