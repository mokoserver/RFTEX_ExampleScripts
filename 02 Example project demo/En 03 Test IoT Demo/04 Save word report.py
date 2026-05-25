import RFSE
import MTLG
import MOSC

MTLG.TelegramProgram('alpha', 'Word report script', 'set', 'init')

RFSE.Stage("*********************************************************")
RFSE.Stage("***************** Word report script *******************")
RFSE.Stage("*********************************************************")

#region Save word report$Word
MOSC.hashStatus("$Word")
RFSE.Program('tree', 'set', 'select = Save word report$Word')

RFSE.Stage("name: control >> mode: set >> command >> save word report", "Program")
RFSE.Program('control', 'set', 'save word report')

MOSC.hash_passed()
#endregion Save word report$Word

RFSE.EndScript()
