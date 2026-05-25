
import RFSE

#Region Сбор данных
RFSE.Report(f'test1', 'set',  'string', 'Hello Dolly') #hash Измерение 1
RFSE.Program("tree", "set", "select = Измерение 1")
RFSE.Program('tree', 'set', 'chosen=passed')
RFSE.Report(f'test2', 'set',  'string', 'Hello World') #hash Измерение 2
RFSE.Program("tree", "set", "select = Измерение 2")
RFSE.Program('tree', 'set', 'chosen=passed')
RFSE.Report(f'test3', "info", "table", "Column1#50;" + "Column2#50;" + "Column3#50;" + "Column4#50;") #hash Измерение 3
RFSE.Program("tree", "set", "select = Измерение 3")
RFSE.Report(f'test3', "set",  "table", "T-800;" + "T-1000;" + "TX;" + "T-3000;")

RFSE.Program('tree', 'set', 'chosen=passed')
#EndRegion Сбор данных


#Region Сбор пользовательских значений
#hash Выбор имени протокола
RFSE.Program("tree", "set", "select = Выбор имени протокола")
ReportName = RFSE.Messenger("get", "Имя", "Введите желаемое имя протокола испытаний", "string")

RFSE.Program("control", "set", "UseCustomReportName = true")
RFSE.Program("control", "set", f"UserReportName = {ReportName}")

RFSE.Program('tree', 'set', 'chosen=passed')

#hash Выбор месторасположения протокола
RFSE.Program("tree", "set", "select = Выбор месторасположения протокола")
RFSE.Program("control", "set", "UseCustomPathName = true")
RFSE.Program("control", "set", "UserPathName = C:\RF-SE\Projects\Tests\WordReport")

RFSE.Program('tree', 'set', 'chosen=passed')
#EndRegion Сбор пользовательских значений

#Region Формирование отчета
#hash Составление протокола
RFSE.Program("tree", "set", "select = Составление протокола")
RFSE.Program('Control', 'set', 'Save project report')
RFSE.Program('Control', 'set', 'Save word report')

RFSE.Program('tree', 'set', 'chosen=passed')
#EndRegion Формирование отчета


RFSE.EndScript('passed')

