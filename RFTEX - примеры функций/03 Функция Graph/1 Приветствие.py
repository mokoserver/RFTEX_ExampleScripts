import RFSE

RFSE.Messenger('set', 'Приветствие#@hello', 'Дорогой пользователь!\nПрямо сейчас Вам будет продемонстрирована работа '
                                         'плагина Graph.\nПриятного просмотра!')

#Region Status
#hash Greeting
RFSE.Program('tree', 'set', 'select = ' + 'Greeting')
RFSE.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Status

RFSE.EndScript()