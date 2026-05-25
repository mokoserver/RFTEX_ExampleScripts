import RFSE
import MOSC

RFSE.Stage("*********************************************************")
RFSE.Stage("*************** Save word report script *****************")
RFSE.Stage("*********************************************************")

#region Save word report$Word
MOSC.hashStatus("$Word")
RFSE.Program('tree', 'set', 'select = Save word report$Word')

RFSE.Program('control', 'set', 'save word report')

MOSC.hash_passed()
#endregion Save word report$Word

RFSE.EndScript()
