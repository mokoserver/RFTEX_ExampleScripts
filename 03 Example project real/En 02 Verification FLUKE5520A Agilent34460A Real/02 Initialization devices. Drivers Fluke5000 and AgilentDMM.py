import RFSE
from ExFluke5000Agilent34460A import Poverka

RFSE.Stage("*********************************************************")
RFSE.Stage("************ Initialization devices script **************")
RFSE.Stage("*********************************************************")
RFSE.Stage(" ")

RFSE.Stage("*********************************************************")
RFSE.Messenger("set", 'Connect device#FLUKE5520A_AGILENT34460A.jpg',
               'Сonnect the device under test via the interface\n'
               'Reference equipment: FLUKE5520.\n'
               'Verified equipment: AGILENT34460.\n'
               'Verification procedure: example.', delaytime='10')
RFSE.Stage("*********************************************************")
RFSE.Stage(" ")

#region Initialization AGILENT34460$Init
RFSE.Program('tree', 'set', 'select = Initialization AGILENT34460$Init')

Poverka.InitializationAGILENT34460A()

#endregion Initialization AGILENT34460$Init

#region Initialization FLUKE5520A$Init
RFSE.Program('tree', 'set', 'select = Initialization FLUKE5520A$Init')

Poverka.InitializationFluke5520A()

#endregion Initialization FLUKE5520A$Init

RFSE.EndScript()
