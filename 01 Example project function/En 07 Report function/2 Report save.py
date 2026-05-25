import RFSE

#Region Status
#hash Save table
#hash Save string
#hash Save picture

RFSE.Messenger('set', 'Report - save.jpg', 'This script will demonstrate the \'\'save\'\' command, '
                                           'which saves rows from Report to text files, '
                                           'tables to excel files, and pictures to png files. '
                                           'All this is stored in the \'\'data\'\' folder, which is created '
                                           '(if it does not exist) in the project folder.')

screenshot = RFSE.Program('control', 'get', 'screenshot', 'string')
RFSE.Report('image_screenshot', 'set', 'picture', screenshot)
RFSE.Report('image_screenshot_clear', 'set', 'picture', screenshot)
RFSE.Report('image_screenshot_delete', 'set', 'picture', screenshot)

RFSE.Report("Report", 'save', 'string', 'csv')    
RFSE.Program('tree', 'set', 'select = ' + 'Save table')
RFSE.Program('tree', 'set', 'chosen = passed')

RFSE.Report("language", 'save', 'string', 'txt')     
RFSE.Program('tree', 'set', 'select = ' + 'Save string')
RFSE.Program('tree', 'set', 'chosen = passed')

RFSE.Report("image_screenshot", 'save', 'picture', 'png')  
RFSE.Program('tree', 'set', 'select = ' + 'Save picture')
RFSE.Program('tree', 'set', 'chosen = passed')

RFSE.EndScript()
