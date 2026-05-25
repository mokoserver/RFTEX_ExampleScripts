import RFSE
import MTLG


RFSE.Telegram('alpha', 'set', f'********START SCRIPT********')
MTLG.TelegramClassic('alpha', 'set', f'********START SCRIPT********')

#Region Status
#hash Greeting


alpha = RFSE.Telegram('alpha', 'get', 'list', 'string')


if len(alpha) != 0:
    MTLG.TelegramMessenger('set', 'Hello', 'The current project will show the interaction between RF-SE and Telegram.')
RFSE.Messenger('set', 'Hello#@hello', 'The current project will show the interaction between RF-SE and Telegram.')

RFSE.Program('tree', 'set', 'select = ' + 'Greeting')
MTLG.TelegramProgram('tree', 'set', 'select = ' + 'Greeting')
RFSE.Program('tree', 'set', 'chosen = passed')
MTLG.TelegramProgram('tree', 'set', 'chosen = passed')

# EndRegion Status

RFSE.EndScript()
MTLG.TelegramEndScript()

if len(alpha) != 0:
    RFSE.Telegram('alpha', 'set', f'********END SCRIPT********')
    MTLG.TelegramClassic('alpha', 'set', f'********END SCRIPT********')
