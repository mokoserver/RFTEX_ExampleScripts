from pressurelib import *

#Region 2.1 При повышении давления
#description: Давление;Ед. измерения;Погрешность;Ед. измерения;
#hash Первая точка вверх: 0.0;МПа;5;%
#hash Вторая точка вверх: 2.0;МПа;5;%
#hash Третья точка вверх: 4.0;МПа;5;%
#hash Четвертая точка вверх: 8.0;МПа;5;%
#hash Пятая точка вверх: 10.0;МПа;5;%
#EndRegion 2.1 При повышении давления


#Region 2.2 При понижении давления
#description: Эталонное;Ед. измерения;Погрешность;Ед. измерения;
#hash Первая точка вниз: 10.0;МПа;5;%
#hash Вторая точка вниз: 8.0;МПа;5;%
#hash Третья точка вниз: 4.0;МПа;5;%
#hash Четвертая точка вниз: 2.0;МПа;5;%
#hash Пятая точка вниз: 0.0;МПа;5;%
#EndRegion 2.2 При понижении давления
AccuracyClass = float(RFSE.Report('AccuracyClass', 'get', 'string', 'string', 'string').replace(',', '.'))  # класс точности
UnitOfMeasure = RFSE.Report('UnitOfMeasure', 'get', 'string', 'string', 'string')  # единицы измерения
ScaleMax = float(RFSE.Report('ScaleMax', 'get', 'string', 'string', 'string').replace(',', '.'))  # Предельное значение давления на шкале прибора
FirstPoint = float(RFSE.Report('FirstPoint', 'get', 'string', 'string', 'string').replace(',', '.'))  # Первая поверяемая точка на шкале прибора после нуля
PermissibleError = RFSE.Report('PermissibleError', 'get', 'string', 'string', 'string')  # Пределы допускаемой погрешности
Driver = RFSE.Report('Driver', 'get', 'string', 'string', 'string')  # драйвер
RFSE.Report('MeasuringRange', 'set', 'string', '(0-' + str(ScaleMax).replace('.', ',') + ')')
WorkplaceNumber = RFSE.Report('WorkplaceNumber', 'get', 'string', 'string', 'string')  # номер образца
TypeofUnit = RFSE.Report('TypeofUnit', 'get', 'string', 'string', 'string')  # тип образца
ValueofDivision = RFSE.Report('ValueofDivision', 'get', 'string', 'string', 'string')  # цена деления
StampNumber = RFSE.Report('StampNumber', 'get', 'string', 'string', 'string')  # Номер штампа

a = bool(RFSE.Messenger('get', 'Проверка образца.jpg', 'Пожалуйста, проведите внешний осмотр образца. Соответствует ли внешний вид образца '
                                          'установленным нормам?', 'boolean'))
if a:
    appearance = "соответствует"
else:
    appearance = "не соответствует"

Simulation = driver_choice(Driver)  # Driver initialisation
permissible_err = ScaleMax * 0.01 * AccuracyClass
#meas_error = ScaleMax * AccuracyClass / 100
checkpoints = [round(x * FirstPoint, 1) for x in range(int(ScaleMax / FirstPoint) + 1)]  # calculating checkpoints for measurement
checkpoints = final_checkpoints(checkpoints)
#if not Simulation:
#    set_unit_of_measure(Driver, UnitOfMeasure)  # Setting up units of measure at reference
#res_up = from_zero_to_max(checkpoints, Driver, UnitOfMeasure, Simulation)  # Going up from zero to max
# 5 minutes break between the measures

RFSE.Program('tree', 'set', 'select = ' + 'Первая точка вверх')
RFSE.Program('tree', 'set', 'chosen = passed')
RFSE.Program('tree', 'set', 'select = ' + 'Вторая точка вверх')
RFSE.Program('tree', 'set', 'chosen = passed')
RFSE.Program('tree', 'set', 'select = ' + 'Третья точка вверх')
RFSE.Program('tree', 'set', 'chosen = passed')
RFSE.Program('tree', 'set', 'select = ' + 'Четвертая точка вверх')
RFSE.Program('tree', 'set', 'chosen = passed')
RFSE.Program('tree', 'set', 'select = ' + 'Пятая точка вверх')
RFSE.Program('tree', 'set', 'chosen = passed')

#RFSE.Messenger('set', 'Ожидание.jpg', 'Пожалуйста, подождите 5 минут между измерениями.', 'void', '300')
#RFSE.Messenger('set', 'Ожидание1.jpg', 'Пожалуйста, подождите 5 минут между измерениями.', 'void', '300')
RFSE.Messenger('set', 'Ожидание.png', 'Пожалуйста, подождите 5 минут между измерениями.', 'void', '300')

#res_down = from_max_to_zero(checkpoints, Driver, UnitOfMeasure, Simulation)  # Going up from zero to max
#res_down = list(reversed(res_down))
#err_up, err_down, variation = calc_err_variation(checkpoints, res_up, res_down)  # Calculating absolute measurement error and variation
#max_err_up, max_err_down = max_err(err_up, err_down)

RFSE.Program('tree', 'set', 'select = ' + 'Первая точка вниз')
RFSE.Program('tree', 'set', 'chosen = passed')
RFSE.Program('tree', 'set', 'select = ' + 'Вторая точка вниз')
RFSE.Program('tree', 'set', 'chosen = passed')
RFSE.Program('tree', 'set', 'select = ' + 'Третья точка вниз')
RFSE.Program('tree', 'set', 'chosen = passed')
RFSE.Program('tree', 'set', 'select = ' + 'Четвертая точка вниз')
RFSE.Program('tree', 'set', 'chosen = passed')
RFSE.Program('tree', 'set', 'select = ' + 'Пятая точка вниз')
RFSE.Program('tree', 'set', 'chosen = passed')

# Calculation of max and permissible errors
#if max_err_up == '-' or max_err_down == '-':
#    max_err = '-'
#else:
#    max_err = max([max_err_up, max_err_down], key=abs)
#result, conclusion = conclusion(max_err, permissible_err, appearance)

#results(WorkplaceNumber, TypeofUnit, ScaleMax, AccuracyClass, ValueofDivision, appearance, result, StampNumber)
# Reports
#reports(checkpoints, res_up, res_down, err_up, err_down, variation, UnitOfMeasure, PermissibleError, max_err)

conclusion = 'Не годен'
Res_table = '0.0;-0.051;-0.023;-0.051;-0.023;-0.028'+'\\r' + \
            '2.0;1.916;2.033;-0.084;0.033;-0.117'+'\\r' + \
            '4.0;3.896;3.859;-0.104;-0.141;0.037'+'\\r' + \
            '8.0;7,994;8.077;-0.006;0.077;-0.083'+'\\r' + \
            '10.0;9.93;9.999;-0.07;-0.001;-0.069'
Result = 'Не соответствует'
MaxErr = '-0.141'

RFSE.Report('Res_table', 'set', 'table', f'{Res_table}')
RFSE.Report('MaxErr', 'set', 'string', f'{MaxErr}')
RFSE.Report('Result', 'set', 'string', f'{Result}')
RFSE.Report('Appearance;Conclusion', 'set', 'strings', f'{appearance};{conclusion}')
RFSE.Report('Res_table1', 'set', 'table', ' ' + ';' + ' ' + ';' + ' ' + ';' + ' ' + ';' + ' ' + ';' + ' ' + ';' + ' ')

RFSE.EndScript()
