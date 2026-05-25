import RFSE

#Region Status (статус)
#hash Make screenshot
#hash Save screenshot
#hash Insert screenshot

RFSE.Messenger('set', 'Messenger - picture#@insert', 'В данном скрипте будет продемонстрирована вставка картинки в Messenger. '
                                                     'Для этого нужно сделать скриншот экрана командой '
                                                     'screenshot = RFSE.Program(\'control\', \'get\', \'screenshot\', \'string\'), '
                                                     'затем сохранить его '
                                                     'командой RFSE.Report(\'screenshot\', \'set\', \'picture\', screenshot).')

screenshot = RFSE.Program('control', 'get', 'screenshot', 'string')
RFSE.Program('tree', 'set', 'select = ' + 'Make screenshot')
RFSE.Program('tree', 'set', 'chosen = passed')

RFSE.Report('image_screenshot', 'set', 'picture', screenshot)
RFSE.Report("image_screenshot", 'save', 'picture', 'png')  
RFSE.Program('tree', 'set', 'select = ' + 'Save screenshot')
RFSE.Program('tree', 'set', 'chosen = passed')

RFSE.Program('tree', 'set', 'select = ' + 'Insert screenshot')
RFSE.Program('tree', 'set', 'chosen = passed')

RFSE.Messenger('set', 'image_screenshot.png', 'Скриншот программы RF-SE вставлен выше.')

RFSE.EndScript()