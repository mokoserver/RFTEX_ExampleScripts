from pressurelib import *
from MOSC import Utility_to_Report

#Region 1.1 Этапы регистрации:
#hash Заполнение формы
#EndRegion 1.1 Этапы регистрации:


UN = 'RFSE_pressure_gauge'  # Utility Name
reports = ['AccuracyClass',  # класс точности
           'UnitOfMeasure',  # единицы измерения
           'ScaleMax',  # Предельное значение давления на шкале прибора
           'FirstPoint',  # Первая поверяемая точка на шкале прибора после нуля
           'FirstMultiplePoint',  # Первая кратная пределу поверяемая точка на шкале
           'ValueofDivision',  # цена деления
           'TypeofUnit',  # Тип образца
           'PermissibleError',  # Пределы допускаемой погрешности
           'StampNumber',  # Номер штампа
           'Owner',  # Владелец
           'Verifier',  # ФИО поверителя
           'VerificationLocation',  # Место проведения поверки
           'WorkplaceNumber',  # Номер рабочего места
           'OrderNumber',  # Номер заказа
           'Day',       ###########
           'Month',     ####ДАТА###
           'Year',      ###########
           'ProtocolNumber',  # Номер протокола
           'Temperature',  # Температура
           'Humidity',  # Влажность
           'AmbientPressure',  # Давление окружающей среды
           'Driver',  # Драйвер
           'UnitNumber'  # Номер образца
           ]

RFSE.Stage('Подключение ADT761')
RFSE.Messenger('set', 'Подключение ADT761.png', 'Пожалуйста, подключите ADT761 к испытуемому образцу.')
RFSE.Stage('Проверка формы поверки')
RFSE.Messenger('set', 'Заполнение формы.png', 'Пожалуйста, заполните форму поверки.', '','3')
RFSE.Utility(UN, 'set', 'info')
Utility_to_Report(reports, UN, 'strings')

RFSE.Program('tree', 'set', 'select = ' + 'Заполнение формы')
RFSE.Program('tree', 'set', 'chosen = passed')


RFSE.EndScript()
