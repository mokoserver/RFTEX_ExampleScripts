import RFSE

#Region Status
#hash Greeting

path_temp = 'D:\GitHub\RFSE\RFSE_ExScript\Path\data'

RFSE.Messenger('set', 'Greeting.jpg', '', f'path = {path_temp}')

pathFromWindow = RFSE.Messenger('get', 'Greeting.jpg', '', f'path = {path_temp}')

RFSE.Report('pathFromWindow', 'set', 'string', pathFromWindow)


RFSE.Program('tree', 'set', 'select = ' + 'Greeting')
RFSE.Program('tree', 'set', 'chosen = passed')
# EndRegion Status

RFSE.EndScript()
