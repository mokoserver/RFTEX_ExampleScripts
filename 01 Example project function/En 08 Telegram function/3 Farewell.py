import RFSE
import MTLG

#Region Status
#hash Farewell

RFSE.Telegram('alpha', 'set', f'********START SCRIPT********')
MTLG.TelegramClassic('alpha', 'set', f'********START SCRIPT********')

alpha = RFSE.Telegram('alpha', 'get', 'list', 'string')
MTLG.TelegramClassic('alpha', 'get', 'list', 'string')

RFSE.Messenger('set', 'Farewell#@bye', 'That\'s all! Good luck!')
MTLG.TelegramMessenger('set', 'Farewell', 'That\'s all! Good luck!')

RFSE.Program('tree', 'set', 'select = ' + 'Farewell')
MTLG.TelegramProgram('tree', 'set', 'select = ' + 'Farewell')
RFSE.Program('tree', 'set', 'chosen = passed')
MTLG.TelegramProgram('tree', 'set', 'chosen = passed')
# EndRegion Status


RFSE.EndScript()
MTLG.TelegramEndScript()

if len(alpha) != 0:
    if language == "English":
        RFSE.Telegram('alpha', 'set', f'********END SCRIPT********')
        MTLG.TelegramClassic('alpha', 'set', f'********END SCRIPT********')