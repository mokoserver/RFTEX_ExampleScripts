import time

import RFSE

RFSE.Messenger('set', 'Info#@info', 'Open text document Autoit.txt located in '
                                    'C:\\RF-SE\\Data and make any changes to it')

for _ in range(60):
    TextNotepad = RFSE.Autoit('*Autoit.txt', 'Edit1', 'ControlGetText', '')
    RFSE.Stage(f'Your text in Notepad: {TextNotepad}')
    RFSE.Report('TextNotepad','set','table',f'{TextNotepad}')
    time.sleep(1)

RFSE.EndScript()
