import RFSE

RFSE.Program('control', 'set', 'save word report')

#Region Status (статус)

#hash report
RFSE.Program('tree', 'set', 'select = ' + 'report')
RFSE.Program('tree', 'set', 'chosen = passed')

RFSE.EndScript()