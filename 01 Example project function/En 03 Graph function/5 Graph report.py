import RFSE

RFSE.Program('control', 'set', 'save word report')

#Region Status

#hash report
RFSE.Program('tree', 'set', 'select = ' + 'report')
RFSE.Program('tree', 'set', 'chosen = passed')

RFSE.EndScript()