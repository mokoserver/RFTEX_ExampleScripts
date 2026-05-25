import RFSE
import time

#Region Status (статус)
#hash Delete table
#hash Delete string
#hash Delete picture

RFSE.Messenger('set', 'Report - delete.jpg', 'В текущем скрипте будет продемонстрирована команда \'\'delete\'\', '
                                             'которая удаляет строки, таблицы и картинки в поле Report.')

RFSE.Report("Report_delete", 'delete', 'picture', '')   
RFSE.Program('tree', 'set', 'select = ' + 'Delete table')
RFSE.Program('tree', 'set', 'chosen = passed')
time.sleep(1)

RFSE.Report("language_delete", 'delete', 'picture', '')    
RFSE.Program('tree', 'set', 'select = ' + 'Delete string')
RFSE.Program('tree', 'set', 'chosen = passed')
time.sleep(1)

RFSE.Report("image_screenshot_delete", 'delete', 'picture', '')  
RFSE.Program('tree', 'set', 'select = ' + 'Delete picture')
RFSE.Program('tree', 'set', 'chosen = passed')


RFSE.EndScript()