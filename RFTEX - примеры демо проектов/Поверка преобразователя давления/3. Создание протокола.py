from pressurelib import *

#Region 3.1 Этапы формирования:

#hash Автосохранение результатов
#hash Формирование протокола
#EndRegion 3.1 Этапы формирования:

PermissibleError = RFSE.Report('PermissibleError', 'get', 'string', 'string', 'string')  # Пределы допускаемой погрешности
UnitOfMeasure = RFSE.Report('UnitOfMeasure', 'get', 'string', 'string', 'string')  # единицы измерения
RFSE.Report('PermissibleErr;UnitofMeasure;UnitofMeasure1;UnitofMeasure2;UnitofMeasure3;UnitofMeasure4', 'set', 'strings',
            f'{PermissibleError};{UnitOfMeasure};{UnitOfMeasure};{UnitOfMeasure};{UnitOfMeasure};{UnitOfMeasure};')
RFSE.Report('UoM1;UoM2;UoM3;UoM4', 'set', 'strings', f'{UnitOfMeasure};{UnitOfMeasure};{UnitOfMeasure};{UnitOfMeasure};')

RFSE.Program('tree', 'set', 'select = ' + 'Автосохранение результатов')
RFSE.Program('tree', 'set', 'chosen = passed')

report = RFSE.Report('ReportPrint', 'get', 'string', 'string', 'string')
report = 'True'
if report == 'True':
    RFSE.Program('Control', 'set', 'Save word report')
RFSE.Program('Control', 'set', 'Save project report')

RFSE.Program('tree', 'set', 'select = ' + 'Формирование протокола')
RFSE.Program('tree', 'set', 'chosen = passed')

RFSE.Stage('Поверка завершена.', 'info')

RFSE.EndScript()
