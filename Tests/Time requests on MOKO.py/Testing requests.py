import time

import RFSE

x = 0

start_time = time.time()

for x in range(50):
    RFSE.Stage(f'Test requests number {x + 1}')
    RFSE.Report(f'test {x + 1}', 'set', 'string', 'OK')
    # RFSE.Messenger('set', f'Test number {x + 1}#@repeat', f'Test number {x + 1}: status OK', delaytime='2')

end_time = time.time()
execution_time = end_time - start_time

RFSE.Messenger('set', 'Script executed#@punk', f'Script execution time: '
                                               f'{round(execution_time, 5)} on {x + 1} tests')
RFSE.EndScript()

#129.75547 - с делей
#129.49307 - no delay stage