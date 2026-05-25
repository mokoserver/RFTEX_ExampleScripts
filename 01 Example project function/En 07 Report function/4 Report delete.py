import RFSE
import time

#Region Status
#hash Delete table
#hash Delete string
#hash Delete picture

RFSE.Messenger('set', 'Report - delete.jpg', 'The current script will demonstrate the \'\'delete\'\' command, '
                                             'which deletes rows, tables and pictures in the Report field.')

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
