import RFSE

#Region Status
#hash Make screenshot
#hash Save screenshot
#hash Insert screenshot

RFSE.Messenger('set', 'Messenger - picture#@insert', 'This script will demonstrate how to insert a picture into Messenger. '
                                                     'To do this, take a screenshot of the screen with the command '
                                                     'screenshot = RFSE.Program(\'control\', \'get\', \'screenshot\', \'string\'), '
                                                     'then save it with the '
                                                     'command RFSE.Report(\'screenshot\', \'set\', \'picture\', screenshot).')

screenshot = RFSE.Program('control', 'get', 'screenshot', 'string')
RFSE.Program('tree', 'set', 'select = ' + 'Make screenshot')
RFSE.Program('tree', 'set', 'chosen = passed')

RFSE.Report('image_screenshot', 'set', 'picture', screenshot)
RFSE.Report("image_screenshot", 'save', 'picture', 'png')
RFSE.Program('tree', 'set', 'select = ' + 'Save screenshot')
RFSE.Program('tree', 'set', 'chosen = passed')

RFSE.Program('tree', 'set', 'select = ' + 'Insert screenshot')
RFSE.Program('tree', 'set', 'chosen = passed')

RFSE.Messenger('set', 'image_screenshot.png', 'Screenshot of RF-SE program pasted above.')

RFSE.EndScript()