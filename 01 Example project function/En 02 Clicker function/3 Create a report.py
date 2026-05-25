import RFSE

#Region Status
#hash Report

RFSE.Program('control', 'set', 'save word report')
RFSE.Program('tree', 'set', 'select = ' + 'Report')
RFSE.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Status


RFSE.EndScript()