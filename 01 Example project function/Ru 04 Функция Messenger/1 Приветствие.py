import RFSE

RFSE.Report('Messenger', 'info', 'table', '№#50;x#70;y#70;№#50;x#70;y#70;№#50;x#70;y#70')
RFSE.Report('Messenger_clear', 'info', 'table', '№#50;x#70;y#70;№#50;x#70;y#70;№#50;x#70;y#70')
RFSE.Report('Messenger_delete', 'info', 'table', '№#50;x#70;y#70;№#50;x#70;y#70;№#50;x#70;y#70')

RFSE.Report(f'Messenger', 'set', 'table', '1;2;3;4;5;6;7;8;9')
RFSE.Report(f'Messenger_clear', 'set', 'table', '1;2;3;4;5;6;7;8;9')
RFSE.Report(f'Messenger_delete', 'set', 'table', '1;2;3;4;5;6;7;8;9')
#Region Status (статус)
#hash Greeting

RFSE.Messenger('set', 'Приветствие#@hello', 'В текущем проекте будут показаны дополнительные возможности Messenger.')

RFSE.Program('tree', 'set', 'select = ' + 'Greeting')
RFSE.Program('tree', 'set', 'chosen = passed')
# EndRegion Status

RFSE.EndScript()