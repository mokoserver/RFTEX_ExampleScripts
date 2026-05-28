import RFSE
import MTLG
from Demo_Test_IoT_4_Wave import Testing

RFSE.Max('alpha', 'set', 'Инициализация устройств')

RFSE.Stage("*********************************************************")
RFSE.Stage("*************** Инициализация устройств *****************")
RFSE.Stage("*********************************************************")
RFSE.Stage(" ")
RFSE.Stage("*********************************************************")

RFSE.Messenger("set", 'Тестирование IoT#TestIoT.png',
               'Tестированиe устройств IoT. Мы будем использовать 4 устройства\n'
               'FY6900; APPA207; BK PRECISION 1697; SDS1102',
               delaytime='5')
RFSE.Stage("*********************************************************")
RFSE.Stage(" ")

RFSE.Report('DevicesUsed', 'info', 'table', 'Devices#300; Status#300;')

#region Инициализация BK1697B$Init
RFSE.Program('tree', 'set', 'select = Инициализация BK1697B$Init')

Testing.InitializationBK1697B()

#endregion Инициализация BK1697B$Init

#region Инициализация FY6900$Init
RFSE.Program('tree', 'set', 'select = Инициализация FY6900$Init')

Testing.InitializationFY6900()

#endregion Инициализация FY6900$Init

#region Инициализация APPA207$Init
RFSE.Program('tree', 'set', 'select = Инициализация APPA207$Init')

Testing.InitializationAPPA207()

#endregion Инициализация APPA207$Init

RFSE.EndScript()
