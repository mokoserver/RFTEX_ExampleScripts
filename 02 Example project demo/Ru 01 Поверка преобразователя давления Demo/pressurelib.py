# Library for Pressure Tests
import RFSE
import random


def final_checkpoints(checkpoints):
    if len(checkpoints) == 8:
        del checkpoints[2:7:2]
    elif len(checkpoints) == 7:
        del checkpoints[2:5:2]
    elif len(checkpoints) == 6:
        del checkpoints[3]
    return checkpoints


##########################  Here will be functions for working with Drivers   ####################
# driver initialisation
def driver_choice(driver):
    if driver == 'XP2i':
        RFSE.Driver('XP2i', 'init', '')
    elif driver == 'ADT681':
        RFSE.Driver('ADT681', 'init', '')
    elif driver == 'Simulation':
        return True
    return False


def set_unit_of_measure(driver, unitofmeasure):
    if unitofmeasure == 'МПа':
        RFSE.Driver(driver, 'set', 'UNITS=KPa')  # XP2i не измеряет в МПа
    else:
        RFSE.Driver(driver, 'set', 'UNITS=' + unitofmeasure)


##########################  Here will be functions for working with Utility   ####################
def from_zero_to_max(checkpoints, driver, unitofmeasure, simulation):
    res_up = []
    for i in checkpoints:
        RFSE.Utility('PressureGauge', 'set', 'show=' + str(i))
        if RFSE.Utility('PressureGauge', 'get', 'defect', 'string') == 'True':
            for x in range(len(checkpoints) - len(res_up)):
                res_up.append('–')
            break
        else:
            if simulation:
                res_up.append(Get_Fake_Pressure(i, 0.15))
            else:
                res_up.append(round(Get_Pressure(driver, unitofmeasure), 3))
    return res_up


def from_max_to_zero(checkpoints, driver, unitofmeasure, simulation):
    res_down = []
    for i in reversed(checkpoints):
        RFSE.Utility('PressureGauge', 'set', 'show=' + str(i))
        if RFSE.Utility('PressureGauge', 'get', 'defect', 'string') == 'True':
            for x in range(len(checkpoints) - len(res_down)):
                res_down.append('–')
            break
        else:
            if simulation:
                res_down.append(Get_Fake_Pressure(i, 0.15))
            else:
                res_down.append(round(Get_Pressure(driver, unitofmeasure), 3))
    return res_down


##########################  Calculating absolute measurement error and variation   ####################
def calc_err_variation(checkpoints, res_up, res_down):
    err_up, err_down, variation = [], [], []
    for i in range(len(checkpoints)):
        try:
            err_up.append(round((res_up[i] - checkpoints[i]), 3))
        except TypeError:
            for x in range(len(checkpoints) - len(err_up)):
                err_up.append('–')
                break
    checkpoints = list(reversed(checkpoints))
    res_down = list(reversed(res_down))
    for i in range(len(checkpoints)):
        try:
            err_down.append(round((res_down[i] - checkpoints[::1][i]), 3))
        except TypeError:
            for x in range(len(checkpoints) - len(err_down)):
                err_down.append('–')
                break
    err_down = list(reversed(err_down))
    for i in range(len(checkpoints)):
        try:
            variation.append(round(err_up[i] - err_down[i], 3))
        except TypeError:
            for x in range(len(checkpoints) - len(variation)):
                variation.append('–')
            break
    return err_up, err_down, variation


def conclusion(max_err, permissible_err, appearance):
    if max_err == '-':
        result = 'не соответствует'
        RFSE.Report('Result', 'set', 'string', 'не соответствует')
    else:
        if abs(max_err) < abs(permissible_err):
            result = 'соответствует'
            RFSE.Report('Result', 'set', 'string', 'соответствует')
        else:
            result = 'не соответствует'
            RFSE.Report('Result', 'set', 'string', 'не соответствует')
        RFSE.Report('MaxErr', 'set', 'string', str(max_err).replace('.', ','))
    if result == 'соответствует' and appearance == 'соответствует':
        conclusion = 'годен'
    else:
        conclusion = 'не годен'
    return result, conclusion


def max_err(err_up, err_down):
    max_err_up_l = []
    max_err_down_l = []
    for x in err_up:
        if x != '–':
            max_err_up_l.append(x)
    for x in err_down:
        if x != '–':
            max_err_down_l.append(x)
    if len(max_err_up_l) > 0:
        max_err_up = max(max_err_up_l, key=abs)
    else:
        max_err_up = '-'
    if len(max_err_down_l) > 0:
        max_err_down = max(max_err_down_l, key=abs)
    else:
        max_err_down = '-'
    return max_err_up, max_err_down


#workplacenumber, typeofunit, scalemax, accuracyclass, valueofdivision, appearance, result, stampnumber
def results(*args):
    results_1 = 'Номер рабочего места ' + args[0] + ';' + 'Тип ' + args[1] + ';' + 'Диапазон ' + \
                '(0-' + str(args[2]).replace('.', ',') + ')' + ';' + 'Класс точности ' + \
                str(args[3]).replace(',', '.') + ';' + 'Ц.д. ' + args[4] + ';' + ' ' + ';' + ' '
    results_2 = 'Показания эталона, ед. изм.' + ';' + 'Показания поверяемого прибора ед. изм. при повышении давления' + \
                ';' + 'Показания поверяемого прибора ед. изм. при понижении давления' + ';' + \
                'Абсолютная погрешность, ед. изм. при повышении' + ';' \
                + 'Показания поверяемого прибора ед. изм. при понижении' + ';' + 'Вариация ед. изм.' + ';' + \
                'Результаты погрешности. Заключение'
    results_3 = 'Внешний осмотр ' + args[5] + ';' + 'Опробование ' + args[6] + ';' + 'Номер клейма ' + args[7] + ';' \
                + ' ' + ';' + ' ' + ';' + 'Подпись' + ';' + ' '
    RFSE.Report('Res_table1', 'set', 'table', results_1)
    RFSE.Report('Res_table1', 'set', 'table', results_2)
    RFSE.Report('Res_table1', 'set', 'table', results_3)
    return


def reports(*args):
    results_1 = ''
    for i in range(len(args[0])):
        if i == 0:
            results_1 += str(args[0][i]).replace('.', ',') + ';' + str(args[1][i]).replace('.', ',') + ';' + \
                      str(args[2][i]).replace('.', ',') + ';' + str(args[3][i]).replace('.', ',') + \
                      ';' + str(args[4][i]).replace('.', ',') + ';' + str(args[5][i]).replace('.', ',') + ';' + \
                      '[Delta]max= ' + str(args[8]).replace('.', ',') + args[6] + '\\r'
        elif i == range(len(args[0]))[-1]:
            results_1 += str(args[0][i]).replace('.', ',') + ';' + str(args[1][i]).replace('.', ',') + ';' + \
                      str(args[2][i]).replace('.', ',') + ';' + str(args[3][i]).replace('.', ',') + \
                      ';' + str(args[4][i]).replace('.', ',') + ';' + str(args[5][i]).replace('.',
                                                                                                 ',') + ';' + '[Delta]доп= ±' \
                      + args[7] + '\\r'
        else:
            results_1 += str(args[0][i]).replace('.', ',') + ';' + str(args[1][i]).replace('.', ',') + ';' + \
                      str(args[2][i]).replace('.', ',') + ';' + str(args[3][i]).replace('.', ',') + \
                      ';' + str(args[4][i]).replace('.', ',') + ';' + str(args[5][i]).replace('.', ',') + ';' + ' ' + '\\r'
    RFSE.Report('Res_table1', 'set', 'table', results_1)
    results = ''
    for i in range(len(args[0])):
        results += str(args[0][i]).replace('.', ',') + ';' + str(args[1][i]).replace('.', ',') + ';' + \
                  str(args[2][i]).replace('.', ',') + ';' + str(args[3][i]).replace('.', ',') + \
                  ';' + str(args[4][i]).replace('.', ',') + ';' + str(args[5][i]).replace('.', ',') + '\\r'
    RFSE.Report('Res_table', 'set', 'table', results)
    return


def Get_Pressure(driver, UnitOfMeasure):
    pressure = float(RFSE.Driver(driver, 'get', 'PRESSURE', 'string'))
    if UnitOfMeasure == 'МПа':
        pressure = float(pressure) * 0.001
    return pressure


def Get_Fake_Pressure(pressure, pressure_range):
    fake_pressure = round(random.uniform(pressure - pressure_range, pressure + pressure_range), 3)
    return fake_pressure


##########################  Here will be functions for working with Utility    ####################
# Script State functions
def Done():
    RFSE.Report('ScriptState', 'set', 'string', 'Done')
    return


def Passed():
    RFSE.Report('ScriptState', 'set', 'string', 'Passed')
    return


def Failed():
    RFSE.Report('ScriptState', 'set', 'string', 'Failed')
    return


def ScriptState():
    state = RFSE.Report('ScriptState', 'get', 'string', 'string', 'string')
    if state == 'Done':
        RFSE.EndScript('done')
    elif state == 'Passed':
        RFSE.EndScript('passed')
    else:
        RFSE.EndScript('failed')
    return
