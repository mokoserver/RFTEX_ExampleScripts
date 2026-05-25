import RFSE
import MTLG

#scriptname = MOSC.ScriptName()
#scriptname = scriptname[0:-3] # delete 3 elements at the end of the string

RFSE.Telegram('alpha', 'set', f'********Старт скрипта********')
MTLG.TelegramClassic('alpha', 'set', f'********Старт скрипта********')

#RFSE.Telegram('alpha', 'set', f'***{scriptname}***')

#Region Status (статус)
#hash Using Telegram

text = ''
id = ''

alpha = RFSE.Telegram('alpha', 'get', 'list', 'string')
MTLG.TelegramClassic('alpha', 'get', 'list', 'string')

if len(alpha) == 0:
    RFSE.Messenger('set', 'Telegram.png', 'Пожалуйста, найдите RF-SE BOT (@RFSESeBot) в Telegram. '
                                          'Затем запустите его и напишите следующее сообщение: \'\'Как подключить тебя к RF-SE?\'\'. '
                                          'После этого следуйте инструкциям!')
    MTLG.TelegramMessenger('set', 'Telegram', 'Пожалуйста, найдите RF-SE BOT (@RFSESeBot) в Telegram. '
                                          'Затем запустите его и напишите следующее сообщение: \'\'Как подключить тебя к RF-SE?\'\'. '
                                          'После этого следуйте инструкциям!')
else:
    text = RFSE.Messenger('get', 'Telegram.png', 'Пожалуйста, введите текст.', 'string')
    MTLG.TelegramMessenger('get', 'Telegram', 'Пожалуйста, введите текст.', 'string')
    if text == '':
        text = "Привет, я RF-SE BOT!"

    RFSE.Telegram('alpha', 'set', f'{text}')
    MTLG.TelegramClassic('alpha', 'set', f'{text}')

RFSE.Program('tree', 'set', 'select = ' + 'Using Telegram')
MTLG.TelegramProgram('tree', 'set', 'select = ' + 'Using Telegram')
RFSE.Program('tree', 'set', 'chosen = passed')
MTLG.TelegramProgram('tree', 'set', 'chosen = passed')


RFSE.EndScript()
MTLG.TelegramEndScript()

if len(alpha) != 0:
    RFSE.Telegram('alpha', 'set', f'********Конец скрипта********')
    MTLG.TelegramClassic('alpha', 'set', f'********Конец скрипта********')