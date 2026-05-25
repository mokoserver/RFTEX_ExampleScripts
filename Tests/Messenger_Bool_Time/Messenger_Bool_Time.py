import RFSE

#Region Тестирование

# boolean value
value = RFSE.Messenger('get', "Call #@callback", "Attention1! No connection established. Do you want to look?! \nДолжен вернуться True (кнопка Yes)", 'bool=True time=6')
value = RFSE.Messenger('get', "Call #@callback", "Attention2! No connection established. Do you want to look?! \nДолжен вернуться False (кнопка No)", 'bool=False time=6')

value = RFSE.Messenger('get', "Call #@callback", "Attention3! No connection established. Do you want to look?! \nДолжен вернуться True (кнопка Yes)", 'boolean=True time=6')
value = RFSE.Messenger('get', "Call #@callback", "Attention4! No connection established. Do you want to look?! \nДолжен вернуться False (кнопка No)", 'boolean=False time=6')

value = RFSE.Messenger('get', "Call #@callback", "Attention5! No connection established. Do you want to look?! \nДолжен вернуться True (кнопка Yes)", 'bool time=6')
value = RFSE.Messenger('get', "Call #@callback", "Attention6! No connection established. Do you want to look?! \nДолжен вернуться False (кнопка No)", 'boolean time=6')


#EndRegion Тестирование

RFSE.EndScript('passed')