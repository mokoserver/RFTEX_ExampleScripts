import RFSE

RFSE.Report('Report', 'info', 'table', '№#50;x#70;y#70;№#50;x#70;y#70;№#50;x#70;y#70')
RFSE.Report('Report_clear', 'info', 'table', '№#50;x#70;y#70;№#50;x#70;y#70;№#50;x#70;y#70')
RFSE.Report('Report_delete', 'info', 'table', '№#50;x#70;y#70;№#50;x#70;y#70;№#50;x#70;y#70')

RFSE.Report(f'Report', 'set', 'table', '1;2;3;4;5;6;7;8;9')
RFSE.Report(f'Report_clear', 'set', 'table', '1;2;3;4;5;6;7;8;9')
RFSE.Report(f'Report_delete', 'set', 'table', '1;2;3;4;5;6;7;8;9')
#Region Status
#hash Greeting

RFSE.Messenger('set', 'Greeting#@hello', 'Additional features of Report will be shown in the current project.')


RFSE.Program('tree', 'set', 'select = ' + 'Greeting')
RFSE.Program('tree', 'set', 'chosen = passed')
# EndRegion Status

RFSE.EndScript()
