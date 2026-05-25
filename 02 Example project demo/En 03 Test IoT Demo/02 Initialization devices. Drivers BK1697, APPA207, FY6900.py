import RFSE
import MTLG
from SettingsAndMeasurement import Testing

MTLG.TelegramProgram('alpha', 'Initialization devices', 'set', 'init')

RFSE.Stage("*********************************************************")
RFSE.Stage("***************** Init device  script *******************")
RFSE.Stage("*********************************************************")
RFSE.Stage(" ")
RFSE.Stage("*********************************************************")

RFSE.Messenger("set", 'Test IoT#TestIoT.png',
               'For demo test IoT device. We will use 4 devices:\n'
               'FY6900; APPA207; BK PRECISION 1697; SDS1102',
               delaytime='5')
RFSE.Stage("*********************************************************")
RFSE.Stage(" ")

RFSE.Report('DevicesUsed', 'info', 'table', 'Devices#300; Status#300;')

#region Initialization BK1697B$Init
RFSE.Program('tree', 'set', 'select = Initialization BK1697B$Init')

Testing.BK1697B.Initialization()

#endregion Initialization BK1697B$Init

#region Initialization FY6900$Init
RFSE.Program('tree', 'set', 'select = Initialization FY6900$Init')

Testing.FY6900.Initialization()

#endregion Initialization FY6900$Init

#region Initialization APPA207$Init
RFSE.Program('tree', 'set', 'select = Initialization APPA207$Init')

Testing.APPA207.Initialization()

#endregion Initialization APPA207$Init

Testing.BK1697B.SET_OUTPUT_OFF()

RFSE.EndScript()
