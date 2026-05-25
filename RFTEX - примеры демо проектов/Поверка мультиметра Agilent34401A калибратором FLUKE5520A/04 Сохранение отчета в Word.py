import RFSE
import MOSC

RFSE.Stage("*********************************************************")
RFSE.Stage("*********** Скрипт сохранения отчета в Word *************")
RFSE.Stage("*********************************************************")

#region Сохранение отчета в Word$Word
MOSC.hashStatus("$Word")
RFSE.Program('tree', 'set', 'select = Сохранение отчета в Word$Word')

RFSE.Program('control', 'set', 'save word report')

MOSC.hash_passed()
#endregion Сохранение отчета в Word$Word

RFSE.EndScript()
