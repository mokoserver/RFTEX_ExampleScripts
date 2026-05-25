import RFSE
import MTLG
import MOSC

MTLG.TelegramProgram('alpha', 'Сохранение Word отчета', 'set', 'init')

RFSE.Stage("*********************************************************")
RFSE.Stage("*************** Сохранение Word отчета ******************")
RFSE.Stage("*********************************************************")

#region Word отчет$Word
MOSC.hashStatus("$Word")
RFSE.Program('tree', 'set', 'select = Word отчет$Word')

RFSE.Stage("name: control >> mode: set >> command >> save word report", "Program")
RFSE.Program('control', 'set', 'save word report')

MOSC.hash_passed()
#endregion Word отчет$Word

RFSE.EndScript()
