import RFSE

#Region Status (статус)
#hash Greeting

path_temp = 'D:\GitHub\RFSE\RFSE_ExScript\Path\data'

RFSE.Messenger('set', 'Приветствие.jpg', '', f'path = {path_temp}')

pathFromWindow = RFSE.Messenger('get', 'Приветствие.jpg', '', f'path = {path_temp}')

RFSE.Report('pathFromWindow', 'set', 'string', pathFromWindow)


RFSE.Program('tree', 'set', 'select = ' + 'Greeting')
RFSE.Program('tree', 'set', 'chosen = passed')
# EndRegion Status

RFSE.EndScript()
