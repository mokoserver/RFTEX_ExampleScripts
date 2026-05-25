import RFSE
import MTLG

#Region Status (статус)
#hash Farewell

RFSE.Telegram('alpha', 'set', f'********Старт скрипта********')
MTLG.TelegramClassic('alpha', 'set', f'********Старт скрипта********')

alpha = RFSE.Telegram('alpha', 'get', 'list', 'string')
MTLG.TelegramClassic('alpha', 'get', 'list', 'string')

RFSE.Messenger('set', 'Прощание#@bye', 'На этом всё! Удачи!')
MTLG.TelegramMessenger('set', 'Прощание', 'На этом всё! Удачи!')

RFSE.Program('tree', 'set', 'select = ' + 'Farewell')
MTLG.TelegramProgram('tree', 'set', 'select = ' + 'Farewell')
RFSE.Program('tree', 'set', 'chosen = passed')
MTLG.TelegramProgram('tree', 'set', 'chosen = passed')
# EndRegion Status


RFSE.EndScript()
MTLG.TelegramEndScript()

if len(alpha) != 0:
    RFSE.Telegram('alpha', 'set', f'********Конец скрипта********')
    MTLG.TelegramClassic('alpha', 'set', f'********Конец скрипта********')