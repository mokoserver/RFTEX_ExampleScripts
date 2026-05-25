import RFSE as RFSE
from MOSC import stars

RFSE.Stage(stars('*'))
RFSE.Stage(stars('Новый SCRIPT'))
RFSE.Stage(stars('*'))

RFSE.Messenger('set', 'Прощание#@bye', 'Предыдущие сообщения продемонстрировали работу Мессенджера. '
                                      'Спасибо что использовали RF-SE. Приятного пользования!')
RFSE.Stage(stars('Конец'))
RFSE.Stage(stars('*'))

RFSE.EndScript()
