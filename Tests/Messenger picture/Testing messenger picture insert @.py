import RFSE

#Region Status
#hash Messenger Testing

RFSE.Stage('mode -> set, head -> Attention#@attention')
RFSE.Messenger('set', 'Attention#@attention',
               'To insert an image, after the head name, write #@attention', delaytime='5')

RFSE.Stage('mode -> set, head -> Bye#@bye')
RFSE.Messenger('set', 'Bye#@bye',
               'To insert an image, after the head name, write #@bye', delaytime='5')

RFSE.Stage('mode -> set, head -> Call#@call')
RFSE.Messenger('set', 'Call#@call',
               'To insert an image, after the head name, write #@call', delaytime='5')

RFSE.Stage('mode -> set, head -> Callback#@callback')
RFSE.Messenger('set', 'Callback#@callback',
               'To insert an image, after the head name, write #@callback', delaytime='5')

RFSE.Stage('mode -> set, head -> Clear#@clear')
RFSE.Messenger('set', 'Clear#@clear',
               'To insert an image, after the head name, write #@clear', delaytime='5')

RFSE.Stage('mode -> set, head -> Delete#@delete')
RFSE.Messenger('set', 'Delete#@delete',
               'To insert an image, after the head name, write #@delete', delaytime='5')

RFSE.Stage('mode -> set, head -> Failed#@failed')
RFSE.Messenger('set', 'Failed#@failed',
               'To insert an image, after the head name, write #@failed', delaytime='5')

RFSE.Stage('mode -> set, head -> File#@file')
RFSE.Messenger('set', 'File#@file',
               'To insert an image, after the head name, write #@file', delaytime='5')

RFSE.Stage('mode -> set, head -> Hello#@hello')
RFSE.Messenger('set', 'Hello#@hello',
               'To insert an image, after the head name, write #@hello', delaytime='5')

RFSE.Stage('mode -> set, head -> Idea#@idea')
RFSE.Messenger('set', 'Idea#@idea',
               'To insert an image, after the head name, write #@idea', delaytime='5')

RFSE.Stage('mode -> set, head -> Insert#@insert')
RFSE.Messenger('set', 'Insert#@insert',
               'To insert an image, after the head name, write #@insert', delaytime='5')

RFSE.Stage('mode -> set, head -> Info#@info')
RFSE.Messenger('set', 'Info#@info',
               'To insert an image, after the head name, write #@info', delaytime='5')


RFSE.Stage('mode -> set, head -> Language#@language')
RFSE.Messenger('set', 'Language#@language',
               'To insert an image, after the head name, write #@language', delaytime='5')

RFSE.Stage('mode -> set, head -> Link#@link')
RFSE.Messenger('set', 'Link#@link',
               'To insert an image, after the head name, write #@link', delaytime='5')

RFSE.Stage('mode -> set, head -> Notes#@notes')
RFSE.Messenger('set', 'Notes#@notes',
               'To insert an image, after the head name, write #@notes', delaytime='5')

RFSE.Stage('mode -> set, head -> Printer#@printer')
RFSE.Messenger('set', 'Printer#@printer',
               'To insert an image, after the head name, write #@printer', delaytime='5')

RFSE.Stage('mode -> set, head -> Punk#@punk')
RFSE.Messenger('set', 'Punk#@punk',
               'To insert an image, after the head name, write #@punk', delaytime='5')

RFSE.Stage('mode -> set, head -> Question#@question')
RFSE.Messenger('set', 'Question#@question',
               'To insert an image, after the head name, write #@question', delaytime='5')


RFSE.Stage('mode -> set, head -> Repeat#@repeat')
RFSE.Messenger('set', 'Repeat#@repeat',
               'To insert an image, after the head name, write #@repeat', delaytime='5')


RFSE.Stage('mode -> set, head -> Save#@save')
RFSE.Messenger('set', 'Save#@save',
               'To insert an image, after the head name, write #@save', delaytime='5')


RFSE.Stage('mode -> set, head -> Time#@time')
RFSE.Messenger('set', 'Time#@time',
               'To insert an image, after the head name, write #@time', delaytime='5')


RFSE.Stage('mode -> set, head -> Warning#@warning')
RFSE.Messenger('set', 'Warning#@warning',
               'To insert an image, after the head name, write #@warning', delaytime='5')

RFSE.Stage('mode -> set, head -> Agilent34401A#@agilent34401a')
RFSE.Messenger('set', 'Agilent34401A#@agilent34401a',
               'To insert an image, after the head name, write #@agilent34401a', delaytime='5')

RFSE.Stage('mode -> set, head -> Fluke5520A#@fluke5520a')
RFSE.Messenger('set', 'Fluke5520A#@fluke5520a',
               'To insert an image, after the head name, write #@fluke5520a', delaytime='5')

RFSE.Stage('mode -> set, head -> Fluke5522A#@fluke5522a')
RFSE.Messenger('set', 'Fluke5522A#@fluke5522a',
               'To insert an image, after the head name, write #@fluke5522a', delaytime='5')

RFSE.Stage('mode -> set, head -> Keysight34460A#@keysight34460a')
RFSE.Messenger('set', 'Keysight34460A#@keysight34460a',
               'To insert an image, after the head name, write #@keysight34460a', delaytime='5')

RFSE.Stage('mode -> set, head -> Keysight34465a#@keysight34465a')
RFSE.Messenger('set', 'Keysight34465A#@keysight34465a',
               'To insert an image, after the head name, write #@keysight34465a', delaytime='5')


RFSE.Program('tree', 'set', 'select = ' + 'Messenger Testing')
RFSE.Program('tree', 'set', 'chosen = passed')

#EndRegion Region Status
RFSE.EndScript()
