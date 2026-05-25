import RFSE
import time

#Region Status (статус)
#hash Clear table
#hash Clear string
#hash Clear picture

RFSE.Messenger('set', 'Report - clear#@clear', 'В данном скрипте будет продемонстрирована команда \'\'clear\'\', '
                                               'которая очищает содержимое строк, таблиц и картинок в поле Report.')


RFSE.Report("Report_clear", 'clear', 'picture', 'png')  
RFSE.Program('tree', 'set', 'select = ' + 'Clear table')
RFSE.Program('tree', 'set', 'chosen = passed')
time.sleep(1)

RFSE.Report("language_clear", 'clear', 'picture', 'png')  
RFSE.Program('tree', 'set', 'select = ' + 'Clear string')
RFSE.Program('tree', 'set', 'chosen = passed')
time.sleep(1)

RFSE.Report("image_screenshot_clear", 'clear', 'picture', 'png') 
RFSE.Program('tree', 'set', 'select = ' + 'Clear picture')
RFSE.Program('tree', 'set', 'chosen = passed')

RFSE.EndScript()