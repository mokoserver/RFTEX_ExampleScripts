import RFSE
import MTLG

RFSE.Telegram('alpha', 'set', f'********START SCRIPT********')
MTLG.TelegramClassic('alpha', 'set', f'********START SCRIPT********')

#Region Status
#hash Using Telegram

text = ''
id = ''

alpha = RFSE.Telegram('alpha', 'get', 'list', 'string')
MTLG.TelegramClassic('alpha', 'get', 'list', 'string')

if len(alpha) == 0:
    RFSE.Messenger('set', 'Telegram.png', 'Please, find the RF-SE BOT (@RFSESeBot) in Telegram. '
                                          'Then run it and write the following message:\'\'. '
                                          'After that follow the instructions!')
    MTLG.TelegramMessenger('set', 'Telegram', 'Please, find the RF-SE BOT (@RFSESeBot) in Telegram. '
                                              'Then run it and write the following message: \'\'. '
                                              'After that follow the instructions!')
else:
    text = RFSE.Messenger('get', 'Telegram.png', 'Please, enter text.', 'string')
    MTLG.TelegramMessenger('get', 'Telegram', 'Please, enter text.', 'string')
    if text == '':
        text = "Hello, I'm a RF-SE BOT!"

    RFSE.Telegram('alpha', 'set', f'{text}')
    MTLG.TelegramClassic('alpha', 'set', f'{text}')

RFSE.Program('tree', 'set', 'select = ' + 'Using Telegram')
MTLG.TelegramProgram('tree', 'set', 'select = ' + 'Using Telegram')
RFSE.Program('tree', 'set', 'chosen = passed')
MTLG.TelegramProgram('tree', 'set', 'chosen = passed')


RFSE.EndScript()
MTLG.TelegramEndScript()

if len(alpha) != 0:
    RFSE.Telegram('alpha', 'set', f'********END SCRIPT********')
    MTLG.TelegramClassic('alpha', 'set', f'********END SCRIPT********')