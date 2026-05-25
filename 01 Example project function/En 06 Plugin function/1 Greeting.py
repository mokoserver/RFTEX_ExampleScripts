import RFSE

#Region Status
#hash Greeting

RFSE.Messenger('set', 'Greeting#@hello', 'The current project will show the plugin\'s control options. '
                                      'In this example, everything will be shown based on the Graph plugin.')

RFSE.Program('tree', 'set', 'select = ' + 'Greeting')
RFSE.Program('tree', 'set', 'chosen = passed')
# EndRegion Status

RFSE.EndScript()
