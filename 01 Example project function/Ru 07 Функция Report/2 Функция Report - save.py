import RFSE


#Region Status (статус)
#hash Save table
#hash Save string
#hash Save picture

RFSE.Messenger('set', 'Report - save.jpg', 'В данном скрипте будет продемонстрирована команда \'\'save\'\', '
                                           'которая сохраняет строки из Report в текстовые файлы, '
                                           'таблицы в excel файлы, а картинки в png файлы. '
                                           'Всё это хранится в папке \'\'data\'\', которая создается (если не существует) '
                                           'в папке с проектом.')

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
