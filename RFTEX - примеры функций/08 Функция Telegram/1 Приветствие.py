import RFSE
import MTLG

#RFSE.Telegram('alpha', 'set', f'{stars("*")}')
#RFSE.Telegram('alpha', 'set', 'START')
#RFSE.Telegram('alpha', 'set', f'{stars("*")}')

#scriptname = MOSC.ScriptName()
RFSE.Telegram('alpha', 'set', f'********Старт скрипта********')
MTLG.TelegramClassic('alpha', 'set', f'********Старт скрипта********')
#RFSE.Telegram('alpha', 'set', f'***{scriptname}***')

#Region Status (статус)
#hash Greeting

alpha = RFSE.Telegram('alpha', 'get', 'list', 'string')

if len(alpha) != 0:
    MTLG.TelegramMessenger('set', 'Приветствие', 'В текущем проекте будет показано взаимодействие RF-SE и Telegram.')
RFSE.Messenger('set', 'Приветствие.png', 'В текущем проекте будет показано взаимодействие RF-SE и Telegram.')


RFSE.Program('tree', 'set', 'select = ' + 'Greeting')
MTLG.TelegramProgram('tree', 'set', 'select = ' + 'Greeting')
RFSE.Program('tree', 'set', 'chosen = passed')
MTLG.TelegramProgram('tree', 'set', 'chosen = passed')
# EndRegion Status

RFSE.EndScript()
MTLG.TelegramEndScript()

if len(alpha) != 0:
    RFSE.Telegram('alpha', 'set', f'********Конец скрипта********')
    MTLG.TelegramClassic('alpha', 'set', f'********Конец скрипта********')
