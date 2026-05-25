import RFSE
from time import sleep

#Region Test script:$4.1
#description: Script;Point;Result

#hash  $4.1: Fourth;1;Good
#hash  $4.2: Fourth;2;Good
#hash  $4.3: Fourth;3;Good

RFSE.Program('tree', 'set', 'select = Test script:$4.1')
sleep(0.5)
RFSE.Program('tree', 'set', 'chosen = passed')

RFSE.Program('tree', 'set', 'select =  $4.1')
sleep(0.5)
RFSE.Program('tree', 'set', 'chosen = passed')

RFSE.Program('tree', 'set', 'select =  $4.2')
sleep(0.5)
RFSE.Program('tree', 'set', 'chosen = passed')

RFSE.Program('tree', 'set', 'select =  $4.3')
sleep(0.5)
RFSE.Program('tree', 'set', 'chosen = passed')

#EndRegion Test script:$4.1

RFSE.EndScript()