'''
MOSC.py - RF-SErver Control
=============================

Эта библиотека содержит функции для управления функциями RF-SE, отчетами и утилитами.
Многие из этих функций являются наследием предыдущих проектов RFSE.

Ключевые возможности:
---------------------
- Форматирование строк и заголовков для RF-SE.
- Управление состоянием выполнения скрипта (Done, Passed, Failed).
- Работа с деревом (Hash) и проверкой его состояния.
- Взаимодействие между отчетами и утилитами.
- Создание табличных отчетов.
- Декоратор для итерационной структуры тестов.
- Расчет времени выполнения скрипта.

Зависимости:
-------------
- RFSE.py

История версий:
---------------
- 26.02.2021: Первая версия.
- 15.03.2021: Библиотека переименована в MOSC.py.
- 09.02.2022: Внесены изменения в логику работы.
- 23.11.2022: Добавлены функции для работы с хэшами.
'''

import RFSE
import os
import sys
from datetime import datetime

# region ### Formatting / Форматирование ###

round_3 = '{:.' + str(3) + 'f}'

# -- script_name --
def script_name() -> str:
    """
    Возвращает имя исполняемого скрипта.

    Returns:
        str: Имя исполняемого скрипта.
    """
    scriptname = os.path.basename(sys.argv[0])
    return scriptname

# -- stars --
def stars(word: str) -> str:
    """
    Заполняет строку звездочками с переданным словом посередине.

    Args:
        word (str): Слово для вставки.

    Returns:
        str: Отформатированная строка со звездочками (длиной до 15 символов).
    """
    formated_string = '{:*^15}'.format(word)
    return formated_string

# -- center_50 --
def center_50(message: str) -> str:
    """
    Заполняет строку звездочками с переданным сообщением посередине.

    Args:
        message (str): Сообщение для вставки.

    Returns:
        str: Отформатированная строка со звездочками (длиной до 50 символов).
    """
    return ('{:*^50}'.format(message))

# -- stage_header --
def stage_header(test_name: str, GOST_point: str) -> None:
    """
    Заполняет поля заголовка этапа в RF-SE.

    Args:
        test_name (str): Название измерений.
        GOST_point (str): Точка ГОСТ.
    """
    RFSE.Stage(center_50('*'))
    RFSE.Stage(center_50(' Measurements of ' + test_name + ' '))
    RFSE.Stage(center_50(' check point ' + GOST_point + ' '))
    RFSE.Stage(center_50('*'))
    RFSE.Stage(" ")

# -- format_header --
def format_header(header: str) -> str:
    """
    Вычисляет ширину колонки и возвращает строку заголовка для таблицы.

    Args:
        header (str): Название колонки.

    Returns:
        str: Строка заголовка с вычисленной шириной.
    """
    h = header.split('\\n')
    len_max = 0
    for i in h:
        if len(i) > len_max:
            len_max = len(i)
    return header + '#' + str(len_max * 7.5) + ';'

# -- table_headers --
def table_headers(table_data: list, table_headers: list) -> str:
    """
    Вычисляет ширину всех колонок и возвращает строку заголовков для таблицы.

    Args:
        table_data (list): Данные таблицы RF-SE.
        table_headers (list): Заголовки таблицы RF-SE.

    Returns:
        str: Строка заголовков для всех колонок с вычисленной шириной.
    """
    headers = ""
    for i in range(len(table_data[0].split(","))):
        max_len = len(table_headers[i])
        column = [string.split(",")[i] for string in table_data]
        for cell in column:
            split_cell = cell.split("\n")
            split_cell_lens = [len(item) for item in split_cell]
            if max_len < max(split_cell_lens): max_len = max(split_cell_lens)

        headers += f"{table_headers[i]}#{max_len * 7.5};"
    return headers
# endregion

# region ### Script Control and State / Управление скриптом и состоянием ###

# -- Delay --
def Delay(minutes: int) -> None:
    """
    Задерживает выполнение скрипта на указанное количество минут.

    Args:
        minutes (int): Количество минут задержки.
    """
    RFSE.Stage('Delay script execution time for ' + str(minutes) + ' minutes')
    RFSE.Messenger('set', 'Info', "Please, wait for " + str(minutes) + " minutes while taking a measurement", 'void',
                   str(minutes * 60))

# -- Done --
def Done() -> None:
    """
    Устанавливает в отчете ScriptState значение "Done".
    """
    RFSE.Report('ScriptState', 'set', 'string', 'Done')

# -- Passed --
def Passed():
    """
    Устанавливает в отчете ScriptState значение "Passed".
    """
    RFSE.Report('ScriptState', 'set', 'string', 'Passed')

# -- Failed --
def Failed():
    """
    Устанавливает в отчете ScriptState значение "Failed".
    """
    RFSE.Report('ScriptState', 'set', 'string', 'Failed')

# -- ScriptState --
def ScriptState() -> None:
    """
    Получает значение ScriptState из RF-SE и устанавливает результат выполнения скрипта.

    Возможные значения в RF-SE:
    - 'Done': Завершает скрипт со статусом 'done'.
    - 'Passed': Завершает скрипт со статусом 'passed'.
    - Любое другое (например, 'Failed'): Завершает скрипт со статусом 'failed'.
    """
    state = RFSE.Report('ScriptState', 'get', 'string', 'string', 'string')
    if state == 'Done':
        RFSE.EndScript('done')
    elif state == 'Passed':
        RFSE.EndScript('passed')
    else:
        RFSE.EndScript('failed')
# endregion

# region ### Tree & Hash / Дерево и Хэши ###

# -- hash_failed --
def hash_failed() -> None:
    """
    Устанавливает хэш для прохождения с ошибкой.
    """
    RFSE.Program('tree', 'set', 'chosen=failed')

# -- hash_passed --
def hash_passed() -> None:
    """
    Устанавливает хэш для прохождения без ошибок.
    """
    RFSE.Program('tree', 'set', 'chosen=passed')

# -- status_tree --
def status_tree(hash: str) -> bool:
    """
    Выбирает хэш дерева и проверяет его содержимое.

    Args:
        hash (str): Хэш для проверки.

    Returns:
        bool: True, если статус хэша не равен 'canceled', иначе False.
    """
    RFSE.Program('tree', 'set', 'select = ' + hash)
    status = RFSE.Program('tree', 'get', 'hash ' + hash, 'string')
    if status != 'canceled':
        return True
    return False

# -- get_hashes_status --
def get_hashes_status(hash: str) -> str:
    """
    Возвращает статус указанного хэша.

    Args:
        hash (str): Хэш для проверки.

    Returns:
        str: Статус хэша.
    """
    status = RFSE.Program('tree', 'get', 'hash ' + hash, 'string')
    return status

# -- hashStatus --
def hashStatus(hash: str) -> bool:
    """
    Выбирает хэш дерева и проверяет, является ли он пустым.

    Args:
        hash (str): Хэш для проверки.

    Returns:
        bool: True, если статус хэша 'empty', иначе False.
    """
    RFSE.Program('tree', 'set', 'select = ' + hash)
    status = RFSE.Program('tree', 'get', 'hash ' + hash, 'string')
    if status == 'empty':
        return True
    return False
# endregion

# region ### Utility Control / Управление утилитами ###

# -- Report_Chek_Forcibly --
def Report_Chek_Forcibly(report_name: str, utility: str, report_type: str = 'string') -> str:
    """
    Принудительно проверяет отчет и обновляет утилиту. Если данных нет, запрашивает у пользователя.

    Args:
        report_name (str): Имя отчета.
        utility (str): Имя утилиты.
        report_type (str, optional): Тип отчета. Defaults to 'string'.

    Returns:
        str: Значение отчета.
    """
    NEM = 'And nothing else matters'
    Report = RFSE.Report(report_name, 'get', report_type, report_type, report_type)
    if Report.startswith(NEM):
        Report = RFSE.Utility(utility, 'get', report_name, report_type)
        if Report == '':
            Report = RFSE.Messenger('get', 'Please, enter the value', 'Enter the value of ' + report_name, report_type)
        RFSE.Report(report_name, 'set', report_type, Report)
    RFSE.Utility(utility, 'set', report_name + ' ' + Report)
    return Report

# -- Report_to_Utility --
def Report_to_Utility(report_name: str, utility: str, report_type: str = 'string') -> str:
    """
    Передает данные из отчета в утилиту, если они не пустые.

    Args:
        report_name (str): Имя отчета.
        utility (str): Имя утилиты.
        report_type (str, optional): Тип отчета. Defaults to 'string'.

    Returns:
        str: Значение отчета.
    """
    ECM = 'Empty case in memory'
    Report = RFSE.Report(report_name, 'get', report_type, report_type, report_type)
    if not Report.startswith(ECM):
        RFSE.Utility(utility, 'set', report_name + ' ' + Report)
    return Report

# -- Utility_to_Report --
def Utility_to_Report(report_names: list | str, utility: str, report_type: str = 'string') -> str:
    """
    Получает данные из утилиты и устанавливает их в отчет RF-SE.

    Args:
        report_names (list | str): Имена для команд утилиты и отчетов.
        utility (str): Имя утилиты.
        report_type (str, optional): Тип отчета. Defaults to 'string'.

    Returns:
        str: Данные отчетов.
    """
    if report_type == 'strings':
        reports_names = ''
        data_reports = ''
        for i in report_names:
            reports_names += i + ';'
            report = RFSE.Utility(utility, 'get', i, 'string')
            data_reports += report + ';'
        RFSE.Report(reports_names, 'set', report_type, data_reports)
    else:
        report = RFSE.Utility(utility, 'get', report_names, 'string')
        RFSE.Report(report_names, 'set', report_type, report)
        return report
    return data_reports
# endregion

# region ### Reports / Отчеты ###

# -- table_report --
def table_report(report_name: str, result: list) -> None:
    """
    Создает табличный отчет из массива элементов.

    Args:
        report_name (str): Имя отчета.
        result (list): Данные таблицы.
    """
    dataString = str('')
    for i in result:
        element = str(i)
        dataString += (element + ';')
    dataString = dataString[0:-1]
    RFSE.Report(report_name, 'set', 'table', dataString)
# endregion

# region ### Test iteration structure / Итерационная структура тестов ###

# -- iteration_structure --
def iteration_structure(test_function, iterations: int = 3):
    """
    Декоратор для функций итерационных испытаний.

    Args:
        test_function: Функция испытания. Должна принимать (input_parameters, test_hash)
                      и возвращать список, где [0] - результат ('Good'/'Normal'/'Bad').
        iterations (int, optional): Количество итераций. Defaults to 3.
    """
    def wrapper(input_paremeters, test_hash):
        test_result = 0
        if status_tree(test_hash):
            test_iterator = 0
            while test_iterator < iterations:
                test_result = test_function(input_paremeters, test_hash)
                if test_result[0] == 'Good':
                    Done()
                    test_iterator = iterations
                elif test_result[0] == 'Normal':
                    Passed()
                    test_iterator = iterations
                elif test_result[0] == 'Bad':
                    Failed()
                    test_iterator += 1
                    if test_iterator == iterations:
                        reiteration = RFSE.Messenger('get', 'Test result is unsatisfactory', 'Would you like to restart?', 'boolean')
                        if reiteration:
                            test_iterator = 0
        return test_result
    return wrapper
# endregion

# region ### Utility Functions / Вспомогательные функции ###

# -- formated_value --
def formated_value(value: str, ndigits: int) -> str:
    """
    Форматирует входное значение в соответствии с количеством знаков после запятой.

    Args:
        value (str): Входное значение.
        ndigits (int): Количество знаков после запятой.

    Returns:
        str: Отформатированное значение.
    """
    try:
        value_format: float = round(float(value.replace(",", ".")), ndigits)
        value_format: str = str(value_format).replace('.', ',')
        value_ndigits: int = len(value_format.split(',')[-1])
        if value_ndigits < ndigits:
            value_format += (ndigits-value_ndigits)*'0'
    except:
        value_format: str = value
    return value_format

# -- InitScriptExecutionTime --
def InitScriptExecutionTime() -> None:
    """
    Инициализирует таблицу со временем выполнения скрипта.
    """
    RFSE.Report("ScriptExecutionTime", "info", "table", "Название скрипта#350;"
                                                        "Start time#100;"
                                                        "Stop time#100;"
                                                        "Время исполнения#150")

# -- ScriptExecutionTime --
def ScriptExecutionTime (StartTime: datetime) -> None:
    """
    Вычисляет время выполнения скрипта и записывает его в отчет.

    Args:
        StartTime (datetime): Время начала выполнения скрипта.
    """
    TimeOfCompletion: str = str(datetime.now() - StartTime)
    ScriptName: str = os.path.basename(sys.argv[0])
    StartTime = str(StartTime)
    StopTime = str(datetime.now())
    RepTimeOfCompletion: str = TimeOfCompletion[:TimeOfCompletion.find(".")]
    RepStartTime: str = StartTime[str(StartTime).find(" "):str(StartTime).find(".")]
    RepStopTime: str = StopTime[str(StopTime).find(" "):str(StopTime).find(".")]

    RFSE.Report("ScriptExecutionTime", "set", "table", str(ScriptName) + ";" +
                                                       RepStartTime + ";" +
                                                       RepStopTime + ";" +
                                                       RepTimeOfCompletion)
# endregion
