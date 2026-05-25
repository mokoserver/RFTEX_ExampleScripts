import RFSE

RFSE.Messenger('set', 'Greeting#@hello', 'Dear user! Right now, the work of the Graph plugin will be demonstrated to you. '
                                      'Happy viewing!')

#Region Status
#hash Greeting
RFSE.Program('tree', 'set', 'select = ' + 'Greeting')
RFSE.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Status

RFSE.EndScript()