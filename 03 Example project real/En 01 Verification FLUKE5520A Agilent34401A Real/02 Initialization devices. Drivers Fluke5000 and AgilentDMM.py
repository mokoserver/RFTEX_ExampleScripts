import RFSE
from SettingsAndMeasurement import Poverka

RFSE.Stage("*********************************************************")
RFSE.Stage("************ Initialization devices script **************")
RFSE.Stage("*********************************************************")
RFSE.Stage(" ")

RFSE.Stage("*********************************************************")
RFSE.Messenger("set", 'Connect device#@agilent34401a',
               'Сonnect the device under test via the interface\n'
               'Reference equipment: FLUKE5520.\n'
               'Verified equipment: AGILENT34401.\n'
               'Verification procedure: example.', delaytime='10')
RFSE.Stage("*********************************************************")
RFSE.Stage(" ")

#region Initialization AGILENT34401A$Init
RFSE.Program('tree', 'set', 'select = Initialization AGILENT34401A$Init')

Poverka.Agilent34401A.Initialization()

#endregion Initialization AGILENT34401A$Init

#region Initialization FLUKE5520A$Init
RFSE.Program('tree', 'set', 'select = Initialization FLUKE5520A$Init')

Poverka.Fluke5520A.Initialization()

#endregion Initialization FLUKE5520A$Init

Poverka.check_simulation_mode()

RFSE.EndScript()
