import RFSE
import MTLG
from Real_Test_DC_DC_Converter import Testing

MTLG.TelegramProgram('alpha', 'Initialization devices', 'set', 'init', 'string')

RFSE.Stage("*********************************************************")
RFSE.Stage("***************** Init device  script *******************")
RFSE.Stage("*********************************************************")
RFSE.Stage(" ")
RFSE.Stage("*********************************************************")

RFSE.Messenger("set", 'Test IoT#TestIoT.png',
               'For demo test IoT device. We will use 2 devices:\n'
               'FY6900; BK PRECISION 1697',
               delaytime='5')
RFSE.Stage("*********************************************************")
RFSE.Stage(" ")

RFSE.Report('DevicesUsed', 'info', 'table', 'Devices#300; status#300;')

#region Initialization BK1697B$Init
RFSE.Program('tree', 'set', 'select = Initialization BK1697B$Init')

Testing.InitializationBK1697B()

#endregion Initialization BK1697B$Init

#region Initialization APPA207$Init
RFSE.Program('tree', 'set', 'select = Initialization APPA207$Init')

Testing.InitializationAPPA207()

#endregion Initialization APPA207$Init

RFSE.EndScript()
