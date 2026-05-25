import RFSE

#Region Status (статус)
#hash Greeting

RFSE.Messenger('set', 'Приветствие#@hello', 'В текущем проекте будут показаны возможности управления плагином. '
                                         'В данном примере всё будет показываться на основе плагина Graph.')

RFSE.Program('tree', 'set', 'select = ' + 'Greeting')
RFSE.Program('tree', 'set', 'chosen = passed')
# EndRegion Status

RFSE.EndScript()
