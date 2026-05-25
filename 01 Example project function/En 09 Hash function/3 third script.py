import RFSE
from time import sleep

#Region Test script:$3.1
#description: Script;Point;Result

#hash first point$3.1: Third;1;Good
#hash second point$3.1: Third;2;Good
#hash third point$3.1: Third;3;Good

RFSE.Program('tree', 'set', 'select = Test script:$3.1')
sleep(0.5)
RFSE.Program('tree', 'set', 'chosen = passed')

RFSE.Program('tree', 'set', 'select = first point$3.1')
sleep(0.5)
RFSE.Program('tree', 'set', 'chosen = passed')

RFSE.Program('tree', 'set', 'select = second point$3.1')
sleep(0.5)
RFSE.Program('tree', 'set', 'chosen = passed')

RFSE.Program('tree', 'set', 'select = third point$3.1')
sleep(0.5)
RFSE.Program('tree', 'set', 'chosen = passed')

#EndRegion Test script:$3.1

RFSE.EndScript()