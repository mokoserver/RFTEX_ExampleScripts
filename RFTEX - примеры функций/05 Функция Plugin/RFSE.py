'''
Библиотека RFSE.py
==================

Эта библиотека представляет собой Python-клиент для взаимодействия с программой RF-SE.
Она позволяет управлять различными компонентами, плагинами и устройствами, подключенными к RF-SE,
путем отправки HTTP-запросов на локальный сервер.

Ключевые возможности:
---------------------
- **Управление устройствами:** Взаимодействие с драйверами (`Driver`) и портами (`Port`).
- **Автоматизация GUI:** Управление элементами интерфейса внешних приложений (`Autoit`).
- **Взаимодействие с пользователем:** Отображение информационных окон и диалогов (`Message`).
- **Логирование и отчеты:** Отправка сообщений в лог (`Stage`) и управление отчетами (`Report`).
- **Управление системой:** Выполнение команд (`CMD`), работа с плагинами (`Plugin`) и утилитами (`Utility`).
- **Синхронизация:** Контроль за состоянием выполнения проекта (`check_project_state`).

Принцип работы:
---------------
Библиотека функционирует как API-обертка, отправляя POST-запросы в формате JSON на
HTTP-сервер, запущенный RF-SE по адресу `http://localhost:55001`.

Зависимости:
-------------
- `requests`
- `json`

История версий:
---------------
- 26.02.2021: Библиотека переименована в RFSE.py.
- 23.06.2021 (v1.5): Изменен формат POST-запросов для драйверов.
- 24.01.2022: Внесены исправления для корректной работы команд start/pause/stop.
- 22.08.2022: Обновлена функция парсинга и проведена рефакторинг.
- 09.09.2022: Параметр 'type' заменен на 'mode' в JSON-запросах (обратная совместимость нарушена).
- 25.03.2026: Добавление регионов и комментариев в новом формате (обратная совместимость нарушена).
- 26.03.2026: Подготовка к исключению библиотеки MOSK (обратная совместимость нарушена).
- 30.03.2026: Добавлены сокращения для Stage (StageError, StageInfo и т.д.).
- 30.03.2026: Добавлены функции  Tree & Hash, Time, Report
- 05.04.2026: Добавлена функции  мессенджера MAX
- 07.04.2026: Испаравлено _request = requests.Session()
- 05.05.2026: Серверный путь исправлен с RFSESE на SE
- 20.05.2026: Добавлено DriverSet и DriverGet
'''

import time
import requests
import json
import sys
import os
from typing import Literal,overload
from functools import partial

_request = requests.Session()

# region ### URLs for RF-SE API / URL-адреса для RF-SE API ###
_BASE_URL = "http://localhost:55001/SE"

# --- Status ---
_UrlProjectStateRead: str = f"{_BASE_URL}/status/projectstate"

# --- Stage ---
_UrlStageWrite: str = f"{_BASE_URL}/stage/stagewrite"

# --- System Components ---
_UrlAutoitWrite: str = f"{_BASE_URL}/system/autoitwrite"
_UrlAutoitRead: str = f"{_BASE_URL}/system/autoitread"

_UrlDriverWrite: str = f"{_BASE_URL}/system/driverwrite"
_UrlDriverRead: str = f"{_BASE_URL}/system/driverread"

_UrlPluginWrite: str = f"{_BASE_URL}/system/pluginwrite"
_UrlPluginRead: str = f"{_BASE_URL}/system/pluginread"

_UrlMessageWrite: str = f"{_BASE_URL}/system/messagewrite"
_UrlMessageRead: str = f"{_BASE_URL}/system/messageread"

_UrlReportWrite: str = f"{_BASE_URL}/system/reportwrite"
_UrlReportRead: str = f"{_BASE_URL}/system/reportread"

_UrlProgramWrite: str = f"{_BASE_URL}/system/programwrite"
_UrlProgramRead: str = f"{_BASE_URL}/system/programread"

_UrlUtilityWrite: str = f"{_BASE_URL}/system/utilitywrite"
_UrlUtilityRead: str = f"{_BASE_URL}/system/utilityread"

_UrlTelegramWrite: str = f"{_BASE_URL}/system/telegramwrite"
_UrlTelegramRead: str = f"{_BASE_URL}/system/telegramread"

_UrlMaxWrite: str = f"{_BASE_URL}/system/maxwrite"
_UrlMaxRead: str = f"{_BASE_URL}/system/maxread"

_UrlCmdWrite: str = f"{_BASE_URL}/system/cmdwrite"
_UrlCmdRead: str = f"{_BASE_URL}/system/cmdread"

_UrlPortWrite: str = f"{_BASE_URL}/system/portwrite"
_UrlPortRead: str = f"{_BASE_URL}/system/portread"
# endregion

# region ### RF-SE API Functions / Функции RF-SE API #####################

# region --- CMD / Командная строка --- +-
def CMD(mode: Literal['set', 'get'],
        command: str) -> ...:
    """
    Выполняет команду в командной строке (CMD) через RF-SE.

    Args:
        mode (str): Режим выполнения команды. Возможные значения: ???.
        command (str): Команда для выполнения.

    Returns:
        str: Результат выполнения команды, возвращенный сервером. Формат: ???.
    """
    check_project_state()
    URLWrite: str = _UrlCmdWrite
    URLRead: str = _UrlCmdRead
    command_to_send: str = f'{{"mode":"{str(mode)}", "command":"{str(command)}"}}'
    send_request(URLWrite, command_to_send)
    cmddata: str = check_status("cmd", mode, URLRead)
    return cmddata
# endregion

# region --- Port / Порт ---
def Port(
    name: str,
    mode: Literal['init', 'interface', 'write', 'read','clear'],
    command: str = '',
    valuetype: Literal['string', 'int', 'float', 'bool', 'arrayint', 'arrayfloat', 'arrayboolean', 'arraystring'] = 'string'
) -> ...:
    """
    Управляет портами и устройствами, настроенными в RF-SE.

    Позволяет инициализировать, настраивать, отправлять и получать данные с устройств,
    подключенных через различные интерфейсы (COM, LPT, и т.д.), используя их логическое имя.

    Args:
        name (str): Логическое имя порта/устройства, заданное в RF-SE.
        mode (str): Режим работы. Основные значения: 'init', 'interface', 'write', 'read'.
        command (str, optional): Команда или данные для отправки в порт (используется в режиме 'write'). Defaults to ''.
        valuetype (str, optional): Ожидаемый тип данных при чтении (используется в режиме 'read'). Defaults to 'string'.

    Returns:
        str: Результат операции. Например:
             - Для 'init' и 'interface': 'ok' в случае успеха, 'error' в случаи не подключения.
             - Для 'write': 'ok' в случае успеха, 'error' в случаи ошибки.
             - Для 'read': прочитанные данные.
             - В случае ошибки может возвращать 'error'.
    """
    check_project_state()
    URLWrite: str = _UrlPortWrite
    URLRead: str = _UrlPortRead
    command_to_send: str = f'{{"name":"{str(name)}","mode":"{str(mode)}","command":"{str(command)}"}}'
    send_request(URLWrite, command_to_send)
    portdata: str = check_status("port", mode, URLRead)
    return parse_data(portdata, mode, valuetype)
# endregion

# region --- Autoit / Автоматизация GUI ---
def Autoit(title: str,
           classname: str,
           method: Literal['ControlClick', 'ControlGetText', 'ControlSetText'],
           attributes: str = 'void') -> ...:
    """
    Взаимодействует с элементами GUI внешних приложений, используя технологию AutoIt.

    Позволяет автоматизировать действия в окнах, например, чтение текста из полей или нажатие кнопок.

    Args:
        title (str): Заголовок окна целевого приложения.
        classname (str): Имя класса элемента управления в окне (например, 'Edit1').
        method (str): Метод для выполнения над элементом (например, 'ControlGetText').
        attributes (str, optional): Дополнительные атрибуты для команды. Defaults to 'void'.

    Returns:
        str: Результат выполнения команды (например, полученный текст).
    """
    check_project_state()
    URLWrite: str = _UrlAutoitWrite
    URLRead: str = _UrlAutoitRead
    command_to_send: str = f'{{"title":"{str(title)}", "classname":"{str(classname)}","method":"{str(method)}","attributes":"{str(attributes)}"}}'
    send_request(URLWrite, command_to_send)
    autoitdata: str = check_status("autoit", method, URLRead)
    return autoitdata
# endregion

# region --- Stage / Логирование этапов ---
def Stage(message: str = '',
          type: Literal['info', 'success', 'fail', 'empty', 'error', 'warning',
                        'telegram', 'message', 'utility', 'cmd', 'port', 'driver', 'plugin', 'report', 'autoit',
                        'project', 'script'] = "info") -> None:
    """
    Отправляет и отображает сообщение в окне "Stage" в RF-SE.

    Используется для логирования и информирования пользователя во время выполнения скрипта.

    Args:
        message (str): Текст сообщения для вывода.
        type (str, optional): Тип сообщения. Влияет на его отображение.
                              Возможные значения: 'Info', 'Error', 'Plugin', 'Driver', 'Report', 'Warning'.
                              Defaults to 'info'.
    """
    type = type.lower()
    check_project_state()
    URLWrite: str = _UrlStageWrite
    command_to_send: str = f'{{"string" :"{str(message)}", "type":"{str(type)}"}}'
    send_request(URLWrite, command_to_send)
# endregion

# region --- Stage Shortcuts / Сокращения для Stage --- <-- ИЗМЕНЕНИЕ 3: Новый регион
# Информационные
StageInfo = partial(Stage, type='info')
StageSuccess = partial(Stage, type='success')
StageFail = partial(Stage, type='fail')
StageEmpty = partial(Stage, type='empty')
StageError = partial(Stage, type='error')
StageWarning = partial(Stage, type='warning')
# Имитирующие
StageTelegram = partial(Stage, type='telegram')
StageMax = partial(Stage, type='max')
StageMessage = partial(Stage, type='message')
StageUtility = partial(Stage, type='utility')
StageAutoit = partial(Stage, type='autoit')
StageCmd = partial(Stage, type='cmd')
StagePort = partial(Stage, type='port')
StageDriver = partial(Stage, type='driver')
StagePlugin = partial(Stage, type='plugin')
StageReport = partial(Stage, type='report')
# Системные
StageProject = partial(Stage, type='project')
StageScript = partial(Stage, type='script')
# endregion

# region --- Driver / Драйвер ---
def Driver(name: str,
           mode: Literal['set', 'get','init','check','close'],
           command: str = 'void',
           valuetype: Literal['string', 'int', 'float', 'bool', 'arrayint', 'arrayfloat', 'arrayboolean', 'arraystring'] = 'string') -> ...:
    """
    Управляет драйверами устройств через RF-SE.

    Args:
        name (str): Имя драйвера.
        mode (str): Режим работы с драйвером ('get', 'set', 'init', 'close').
        command (str, optional): Команда для драйвера. Defaults to 'void'.
        valuetype (str, optional): Ожидаемый тип данных при чтении (только для mode='get'). Defaults to 'string'.

    Returns:
        Зависит от режима:
        - 'set', 'init', 'close': None
        - 'get': Данные, полученные от драйвера, преобразованные к типу `valuetype`.
    """
    check_project_state()
    URLWrite: str = _UrlDriverWrite
    URLRead: str = _UrlDriverRead
    command_to_send: str = f'{{"name":"{str(name)}","mode":"{str(mode)}","command":"{str(command)}"}}'
    send_request(URLWrite, command_to_send)
    drvdata: str = check_status("driver", mode, URLRead)
    return parse_data(drvdata, mode, valuetype)
# endregion

# region --- DriverSet / Установка команды драйверу ---
def DriverSet(name: str, command: str = 'void') -> None:
    """
    Устанавливает команду драйверу (упрощённая обёртка для Driver с mode='set').

    Args:
        name (str): Имя драйвера.
        command (str, optional): Команда для драйвера. Defaults to 'void'.

    Returns:
        None
    """
    Driver(name, mode='set', command=command)
# endregion

# region --- DriverGet / Получение данных от драйвера ---
def DriverGet(name: str,
              command: str = 'void',
              valuetype: Literal['string', 'int', 'float', 'bool',
                                 'arrayint', 'arrayfloat', 'arrayboolean', 'arraystring'] = 'string') -> ...:
    """
    Получает данные от драйвера (упрощённая обёртка для Driver с mode='get').

    Args:
        name (str): Имя драйвера.
        command (str, optional): Команда для драйвера. Defaults to 'void'.
        valuetype (str, optional): Ожидаемый тип данных. Defaults to 'string'.

    Returns:
        Данные от драйвера, преобразованные к типу valuetype.
    """
    return Driver(name, mode='get', command=command, valuetype=valuetype)
# endregion


# region --- Plugin / Плагин ---
def Plugin(name: str,
           mode: Literal['set', 'get','init','check','close'],
           command: str = 'void',
           valuetype: Literal['string', 'int', 'float', 'bool', 'arrayint', 'arrayfloat', 'arrayboolean', 'arraystring'] = 'string') -> ...:
    """
    Управляет плагинами в RF-SE.

    Args:
        name (str): Имя плагина.
        mode (str): Режим работы с плагином ('get', 'set', 'init').
        command (str, optional): Команда для плагина. Defaults to 'void'.
        valuetype (str, optional): Ожидаемый тип данных при чтении (только для mode='get'). Defaults to 'void'.

    Returns:
        Зависит от режима:
        - 'set', 'init': None
        - 'get': Данные, полученные от плагина, преобразованные к типу `valuetype`.
    """
    check_project_state()
    URLWrite: str = _UrlPluginWrite
    URLRead: str = _UrlPluginRead
    command_to_send: str = f'{{"name":"{str(name)}","mode":"{str(mode)}","command":"{str(command)}"}}'
    send_request(URLWrite, command_to_send)
    plgdata: str = check_status("plugin", mode, URLRead)
    return parse_data(plgdata, mode, valuetype)
# endregion

# region --- Message / Сообщения ---
def Message(mode: Literal['set', 'get'],
              head: str = '',
              body: str = '',
              valuetype: str = 'void',
              delaytime: str = 'void') -> ...:
    """
    Отображает всплывающее окно (мессенджер) в RF-SE для взаимодействия с пользователем.

    Args:
        mode (str): Режим окна ('get' для ввода данных, 'set' для отображения информации).
        head (str, optional): Заголовок окна. Defaults to ''.
        body (str, optional): Основной текст сообщения. Defaults to ''.
        valuetype (str, optional): Ожидаемый тип данных при вводе (только для mode='get'). Defaults to 'void'.
        delaytime (str, optional): Время (в секундах), на которое окно задержится на экране. Defaults to 'void'.

    Returns:
        Зависит от режима:
        - 'set': None
        - 'get': Данные, введенные пользователем.
    """
    check_project_state()
    URLWrite: str = _UrlMessageWrite
    URLRead: str = _UrlMessageRead
    if (delaytime == 'void'):
        command_to_send: str = f'{{"mode":"{str(mode)}","head":"{str(head)}","body":"{str(body)}","value":"{str(valuetype)}"}}'
    else:
        command_to_send: str = f'{{"mode":"{str(mode)}","head":"{str(head)}","body":"{str(body)}","time":"{str(delaytime)}"}}'
    send_request(URLWrite, command_to_send)
    msgdata: str = check_status("message", mode, URLRead)
    return parse_data(msgdata, mode, valuetype)


# --- Обратная совместимость со старыми скриптами ---
Messenger = Message
# endregion

# region --- Report / Отчет ---
def Report(name: str,
           mode: Literal['info', 'set','get','clear','delete','save'],
           kind: Literal['string', 'table', 'picture', 'strings'] = 'string',
           data: str = '',
           valuetype: Literal['string', 'int', 'float', 'bool', 'arrayint', 'arrayfloat', 'arrayboolean', 'arraystring'] = 'string') -> ...:
    """
    Работает с данными в отчете RF-SE.

    Args:
        name (str): Имя отчета или закладки в документе Word.
        mode (str): Режим работы ('get', 'set', ???).
        kind (str, optional): Тип записываемых данных ('string', 'table', 'picture'). Defaults to 'string'.
        data (str, optional): Данные для записи в отчет. Defaults to ''.
        valuetype (str, optional): Ожидаемый тип данных при чтении (только для mode='get'). Defaults to 'void'.

    Returns:
        Зависит от режима:
        - 'set': None
        - 'get': Данные, полученные из отчета.
    """
    check_project_state()
    URLWrite: str = _UrlReportWrite
    URLRead: str = _UrlReportRead
    command_to_send: str = f'{{"name":"{str(name)}","mode":"{str(mode)}", "kind":"{str(kind)}", "data":"{str(data)}"}}'
    send_request(URLWrite, command_to_send)
    repdata: str = check_status("report", mode, URLRead)
    return parse_data(repdata, mode, valuetype)
# endregion

# region --- Utility / Утилита ---
def Utility(name: str,
            mode: Literal['set', 'get'],
            command: str = 'void',
            valuetype: Literal['string', 'int', 'float', 'bool', 'arrayint', 'arrayfloat', 'arrayboolean', 'arraystring'] = 'string') -> ...:
    """
    Управляет утилитами в RF-SE.

    Args:
        name (str): Имя утилиты.
        mode (str): Режим работы ('get', 'set', ???).
        command (str, optional): Команда для утилиты. Defaults to 'void'.
        valuetype (str, optional): Ожидаемый тип данных при чтении (только для mode='get'). Defaults to 'void'.

    Returns:
        Зависит от режима:
        - 'set': None
        - 'get': Данные, полученные от утилиты.
    """
    check_project_state()
    URLWrite: str = _UrlUtilityWrite
    URLRead: str = _UrlUtilityRead
    command_to_send: str = f'{{"name" :"{str(name)}", "mode":"{str(mode)}", "command":"{str(command)}"}}'
    send_request(URLWrite, command_to_send)
    utldata: str = check_status("utility", mode, URLRead)
    return parse_data(utldata, mode, valuetype)
# endregion

# region --- Telegram / Мессенджер Телеграм ---
def Telegram(role: Literal['alpha', 'beta', 'gamma', 'delta', 'xi', 'id'] = 'alpha',
             mode: Literal['set','get'] = 'set',
             command: str = '',
             valuetype: Literal['void'] = 'void') -> ...:
    """
    Работает с Telegram ботом RF-SE.

    Args:
        role (str): Принадлежность к группе для отправки сообщений ('alpha', 'beta', 'gamma', 'delta' - разработчик).
        mode (str): Режим работы ('get', 'set').
        command (str): Команда для выполнения.
        valuetype (str, optional): Ожидаемый тип данных при чтении (только для mode='get'). Defaults to 'void'.

    Returns:
        Зависит от режима:
        - 'set': None
        - 'get': Данные, полученные от Telegram.
    """
    check_project_state()
    URLWrite: str = _UrlTelegramWrite
    URLRead: str = _UrlTelegramRead
    command_to_send: str = f'{{"role":"{str(role)}","mode":"{str(mode)}","command":"{str(command)}"}}'
    send_request(URLWrite, command_to_send)
    tgmdata: str = check_status("telegram", mode, URLRead)
    return parse_data(tgmdata, mode, valuetype)
# endregion

# region --- MAX / Мессенджер MAX ---
def Max(role: Literal['alpha', 'beta', 'gamma', 'delta', 'xi', 'id'] = 'alpha',
             mode: Literal['set','get'] = 'set',
             command: str = '',
             valuetype: Literal['void'] = 'void') -> ...:
    """
    Работает с MAX ботом RF-SE.

    Args:
        role (str): Принадлежность к группе для отправки сообщений ('alpha', 'beta', 'gamma', 'delta' - разработчик).
        mode (str): Режим работы ('get', 'set').
        command (str): Команда для выполнения.
        valuetype (str, optional): Ожидаемый тип данных при чтении (только для mode='get'). Defaults to 'void'.

    Returns:
        Зависит от режима:
        - 'set': None
        - 'get': Данные, полученные от Max.
    """
    check_project_state()
    URLWrite: str = _UrlMaxWrite
    URLRead: str = _UrlMaxRead
    command_to_send: str = f'{{"role":"{str(role)}","mode":"{str(mode)}","command":"{str(command)}"}}'
    send_request(URLWrite, command_to_send)
    maxdata: str = check_status("max", mode, URLRead)
    return parse_data(maxdata, mode, valuetype)
# endregion

# region *** Program / Программа *******************************
# region -------   Collection Literal Program
# ==========================================
# 1. ОПИСЫВАЕМ КОМАНДЫ (Type Aliases)
# Это сделает код ниже чистым и читаемым
# ==========================================

# Для tree (есть и set, и get)
TreeGetStaticCmd = Literal['hash =',
                     'script', 'ScriptStatus',
                     'project', 'ProjectStatus']
TreeGetCmd = TreeGetStaticCmd  | str
TreeSetStaticCmd = Literal['select = ', 'info = ', 'chosen = done', 'chosen = failed', 'chosen = passed',
                                                   'chosen = canceled','chosen = frozen',
                                                    'chosen = empty','chosen = reset']
TreeSetCmd = TreeSetStaticCmd | str

# Для control (есть и set, и get)
ControlSetStaticCmd = Literal[# ------- main -------
                        'Minimized', 'OpenProject', 'SaveProject',
                        # ------- Panel Control -------
                        'Start', 'Pause', 'Stop', 'Reset','EditExecution', 'ProjectHistory', 'PersonalProjects',
                        # ------- Project -------
                        'SaveProjectReport', 'SaveTempProjectReport', 'SaveProjectReportAs','LoadProjectReport',
                        # ------- Word / Pdf-------
                        'SaveWordReport', 'SaveWordReportAs', 'SavePdfReport','SavePdfReportAs',
                        # ------- Stage -------
                        'StageClear','SaveStageReport',
                        # ------- Help Links -------
                        'License', 'Documentation','YouTube','Telegram','GitHub','AboutCompany',
                        # ------- Edit Report -------
                        'EditData','AddAllReports','AddNameReports','SaveAllReportsToAFolder',
                        # ------- Report Settings --------
                        'UseCustomReportName = true', 'UseCustomReportName = false','UseCustomPathName = true','UseCustomPathName = false',
                        'UserReportName =','UserPathName = ',
                        # ------- Language -------
                        'Language']
ControlGetCmd = Literal['Version', 'screenshot']

ControlSetCmd = ControlSetStaticCmd | str

# Для script (допустим, ТОЛЬКО set)
ScriptSetStaticCmd = Literal['Script = done', 'Script = failed', 'Script = passed','Script = start','Script = canceled']
ScriptSetCmd = ScriptSetStaticCmd | str

# Для project (есть set)
ProjectSetCmd = Literal['start', 'done', 'pause', 'stop', 'reset']

# Для Time (есть  get)
TimeGetCmd = Literal[# ________ Current _________
                        'Current', 'CurrentDateAndTime', 'CurrentDate', 'CurrentTime',
                        # ________ Project _________
                        'ProjectStart', 'ProjectStartDateAndTime', 'ProjectStartDate', 'ProjectStartTime',
                        'ProjectExecution', 'TotalExecution',
                        'ProjectIdle', 'ProjectStop', 'TotalIdle', 'TotalStop',
                        'ProjectError', 'TotalError',
                        # ________  Script _________
                        "ScriptStart", "ScriptStartDateAndTime",
                        "ScriptStartDate", "ScriptStartTime",
                        "ScriptExecution", "ScriptIdle", "ScriptStop",
                        "ScriptError"]
# endregion

# region  -------   Overload Program ---

# ==========================================
# 2. ПЕРЕГРУЗКИ ФУНКЦИИ (@overload)
# Строго связываем: Имя -> Режим -> Команды
# ==========================================
# --- TREE SET---
@overload
def Program(
    name: Literal['tree'],
    mode: Literal['set'],
    command: TreeSetCmd # Используем SET команду
) -> str: ...

# --- TREE GET---
@overload
def Program(
    name: Literal['tree'],
    mode: Literal['get'],
    command: TreeGetCmd, # Используем GET команду
    valuetype: Literal['string'] = 'string'
) -> str: ...

# --- CONTROL SET---
@overload
def Program(
    name: Literal['control'],
    mode: Literal['set'],
    command: ControlSetCmd
) -> str: ...

# --- CONTROL GET---
@overload
def Program(
    name: Literal['control'],
    mode: Literal['get'], # Исправлен комментарий и режим
    command: ControlGetCmd,
    valuetype: Literal['string'] = 'string'
) -> str: ...

# --- SCRIPT SET---
@overload
def Program(
    name: Literal['script'],
    mode: Literal['set'], # Если name='script', mode может быть ТОЛЬКО 'set'
    command: ScriptSetCmd
) -> str: ...

# --- PROJECT SET---
@overload
def Program(
    name: Literal['project'],
    mode: Literal['set'],
    command: ProjectSetCmd
) -> str: ...

# --- TIME GET---
@overload
def Program(
    name: Literal['time'],
    mode: Literal['get'], # Только 'get'
    command: TimeGetCmd,
    valuetype: Literal['void', 'string'] = 'void'
) -> str: ...
# endregion

# region ------  Program / Программа ---

# ==========================================
# 3. ОСНОВНАЯ РЕАЛИЗАЦИЯ (Ваша логика)
# ==========================================
def Program(
            name: str = 'control',
            mode: str = 'set',
            command: str = '',
            valuetype: str = 'void'
) -> str:
    """
    Центральная функция управления внутренней логикой и интерфейсом RF-SE.
    Работает как маршрутизатор: конкретное действие определяется комбинацией параметров `name`, `mode` и `command`.

    Поддерживаемые подсистемы (параметр `name`):
      - 'tree': Управление деревом проекта (выделение хэшей, установка статусов, получение ScriptStatus).
      - 'control': Программное управление GUI RF-SE (нажатие кнопок Start/Stop, вызов меню сохранения отчетов).
      - 'script': Установка финального статуса выполнения текущего скрипта (например, 'Script = passed').
      - 'project': Глобальное управление состоянием проекта ('start', 'stop', 'pause').
      - 'time': Запрос системных таймеров и метрик времени ('Current', 'ProjectExecution', 'ScriptError' и др.).

    Args:
        name (str): Имя подсистемы, к которой обращается команда.
        mode (str): Режим работы. 'set' (отправить команду/изменить состояние)
                    или 'get' (запросить данные). Допустимые режимы зависят от выбранной подсистемы.
        command (str): Текст команды. Формат строго зависит от `name` и `mode`.
                       Примеры: 'select = <hash>', 'ScriptStatus', 'Start', 'CurrentDate'.
        valuetype (str, optional): Ожидаемый тип данных при mode='get'.
                                   Поддерживаются: 'string', 'int', 'float', 'bool', 'array...'.
                                   При mode='set' игнорируется. Defaults to 'void'.

    Returns:
        str | int | float | bool | list | None:
            - При mode='get' возвращает данные от сервера, приведенные к типу `valuetype`.
            - При mode='set' всегда возвращает None.

    Notes:
        Функция имеет встроенную защиту от рассинхрона: если проект в RF-SE поставлен
        на паузу, выполнение Python-скрипта в этой функции заморозится до снятия паузы.
        Если проект остановлен, скрипт принудительно завершится (sys.exit).
    """
    check_project_state()
    URLWrite: str = _UrlProgramWrite
    URLRead: str = _UrlProgramRead
    command_to_send: str = f'{{"name":"{str(name)}","mode":"{str(mode)}","command":"{str(command)}"}}'
    send_request(URLWrite, command_to_send)
    progdata: str = check_status("program", mode, URLRead)
    return parse_data(progdata, mode, valuetype)
# endregion

# endregion ********************************************************************

# endregion ##################################################################

# region ### Execution Control / Управление выполнением ######################

# region ******* ScriptEnd / Завершает выполнение текущего скрипта. *******
def ScriptEnd(command: str = None) -> None:
    """
    Завершает выполнение текущего скрипта.

    Обязательная функция, которая должна вызываться в конце каждого скрипта,
    чтобы уведомить RF-SE о его завершении.

    Args:
        command (str, optional): Команда, отправляемая серверу при завершении.
                                 Возможные значения:
                                 - 'done': Выполнено (желтый нейтральный цвет).
                                 - 'passed': Пройдено (зеленый цвет).
                                 - 'failed': Не пройдено (красный цвет).

                                 Также поддерживаются синонимы:
                                 - 'good' -> преобразуется в 'passed'
                                 - 'bad' -> преобразуется в 'failed'

                                 Если параметр не передан, автоматически получает
                                 статус из ScriptResult().
                                 Если передано неподдерживаемое значение,
                                 устанавливается статус 'failed'.
                                 Defaults to None.
    """
    if command is None:
        command = ScriptResult()

    # Нормализация значений
    command_lower = str(command).lower()

    # Преобразование синонимов
    if command_lower in {'good', 'passed'}:
        command = 'passed'
    elif command_lower in {'bad', 'failed'}:
        command = 'failed'
    elif command_lower == 'done':
        command = 'done'
    else:
        # Если ничего не подошло, пишем failed
        command = 'failed'

    Program('script', 'set', command)
    sys.exit()

# --- Обратная совместимость со старыми скриптами ---
EndScript = ScriptEnd
# endregion *****************************************

# region ******* ProjectRestart / Перезапускает текущий проект с нуля. *******
def ProjectRestart() -> None:
    """
    Перезапускает текущий проект с нуля.

    Выполняет полный цикл перезапуска проекта в RF-SE, состоящий из трёх этапов:
    1. Очищает текущую стадию выполнения (StageClear).
    2. Сбрасывает все накопленные результаты и состояние проекта (Reset).
    3. Завершает текущий скрипт с нейтральным статусом (Done).

    Функция не принимает аргументов и не возвращает значения.

    Использование:
        Вызовите эту функцию в любой точке скрипта, когда необходимо
        полностью перезапустить проект и начать выполнение заново.
        После вызова скрипт завершается, и RF-SE инициирует
        новый цикл запуска.

    Пример:
        >>> ProjectRestart()
    """
    Program('control', 'set', 'StageClear')
    Program('control', 'set', 'reset')
    Program('script', 'set', 'done')
    sys.exit()
# endregion *****************************************

# region ******* Tree & Hash / Дерево и Хэши *********************

# region --- ScriptResult / Получает результат выполнения текущего скрипта из дерева RF-SE. --
def ScriptResult() -> str:
    """
    Получает результат выполнения текущего скрипта из дерева RF-SE.

    Returns:
        str: Статус выполнения ('passed', 'failed', 'done').
    """
    return Program('tree', 'get', 'ScriptStatus', 'string')
# endregion

# region --- ProjectResult / Получает результат выполнения всего проекта из дерева RF-SE. --
def ProjectResult() -> str:
    """
    Получает результат выполнения всего проекта из дерева RF-SE.

    Returns:
        str: Статус выполнения проекта ('passed', 'failed', 'done').
    """
    return Program('tree', 'get', 'ProjectStatus', 'string')
# endregion

# region --- HashSet / Устанавливает результат выполнения в дереве (Hash). --
def HashSet(command: Literal['done', 'passed', 'failed'] = 'done') -> None:
    """
    Устанавливает результат выполнения в дереве (Hash).

    Args:
        command (str, optional): Статус для установки.
                                 Возможные значения:
                                 - 'done': Выполнено (желтый нейтральный цвет).
                                 - 'passed': Пройдено (зеленый цвет).
                                 - 'failed': Не пройдено (красный цвет).
                                 Defaults to 'done'.
    """
    Program('tree', 'set', f'chosen = {command}')
# endregion

# region --- HashSelect / Выбирает хэш(Hash) в дереве. --
def HashSelect(hash: str) -> None:
    """
    Выбирает хэш в дереве.

    Args:
        hash (str): Хэш для выбора.
    """
    Program('tree', 'set', 'select = ' + hash)
    return
# endregion

# region --- HashExecuteStep / Выполняет шаг: выбирает его в дереве и выводит название в Stage. --
def HashExecuteStep(step_string: str) -> None:
    """
    Выполняет шаг: выбирает его в дереве и выводит название в Stage.

    Ожидает строку в формате 'Название шага$HASH_ID'.
    Если символ '$' отсутствует, вся строка передается как хэш.

    Args:
        step_string (str): Строка с описанием шага и хэшем.
    """
    # Удаляем пробелы в начале и в конце строки во избежание ошибок
    step_string = step_string.strip()

    # Разделяем строку по символу '$' максимум 1 раз
    parts = step_string.split('$', 1)

    if len(parts) == 2:
        step_name = parts[0]
        step_id = parts[1]

        # Выбираем хэш в дереве (склеиваем обратно название и ID)
        HashSelect(f"{step_name}${step_id}")
        # Выводим информационное сообщение о начале шага
        Stage(f"--- {step_name} ---")
    else:
        # Если символа $ в строке нет, используем всю строку как хэш
        HashSelect(step_string)
        # Выводим строку в Stage как есть
        Stage(f"--- {step_string} ---")

    return
# endregion

# region --- HashSelectCheck / Выбирает хэш в дереве и проверяет, является ли он пустым. --
def HashSelectCheck(hash: str) -> bool:
    """
    Выбирает хэш в дереве и проверяет, является ли он пустым.

    Args:
        hash (str): Хэш для выбора и проверки.

    Returns:
        bool: True, если статус хэша 'empty', иначе False.
    """
    Program('tree', 'set', f'select = {hash}')
    status = Program('tree', 'get', f'hash = {hash}', 'string')

    if status == 'empty':
        return True
    return False
# endregion

# endregion *******************************************************

# region ******* Time / Время **************************************

# region --- TimeParameter / Литералы времени RF-SE
TimeParameter = Literal[
    # Текущая дата и время
    "Current", "CurrentDateAndTime",
    # Текущая дата
    "CurrentDate",
    # Текущее время
    "CurrentTime",

    # Дата и время запуска проекта
    "ProjectStart", "ProjectStartDateAndTime",
    # Дата запуска проекта
    "ProjectStartDate", "ProjectStartTime",
    # Время выполнения проекта
    "ProjectExecution", "TotalExecution",
    # Время когда проект не выполнялся
    "ProjectStop", "TotalStop",
    "ProjectIdle", "TotalIdle",
    # Общее время ошибок в проекте
    "ProjectError", "TotalError",

    # Дата и время запуска скрипта
    "ScriptStart", "ScriptStartDateAndTime",
    # Дата запуска скрипта
    "ScriptStartDate", "ScriptStartTime",

    # Время выполнения скрипта
    "ScriptExecution",
    # Время когда скрипт не выполнялся
    "ScriptStop", "ScriptIdle",
    # Время ошибок в скрипте 00:00:00
    "ScriptError"
]
# endregion

# region --- TimeGet / Получает параметры времени через системную функцию RFSE.Program.
def TimeGet(command: TimeParameter = "Current"):
    """
    Получает параметры времени через системную функцию RFSE.Program.

    Args:
        command (TimeParameter, optional): Запрашиваемый параметр времени.
                                           По умолчанию 'Current'.

    Returns:
        Результат выполнения RFSE.Program.
    """
    return Program('time', 'get', command)
# endregion

# region --- ReportTimeAdd / Управляет таблицей со временем выполнения скрипта. ---
def ReportTimeAdd(action: Literal["init", "add", "set"] = "init", lang: Literal["RU", "EN"] = "EN") -> None:
    """
    Управляет таблицей со временем выполнения скрипта.

    Args:
        action (Literal["init", "add", "set"]):
            - 'init': Создает таблицу с заголовками.
            - 'add' или 'set': Добавляет строку с данными о выполнении.
        lang (Literal["RU", "EN"]): Язык заголовков и ID таблицы. По умолчанию 'EN'.
    """
    # Задаем заголовок и ID таблицы в зависимости от языка
    if lang == "RU":
        table_title = "Время выполнения скрипта"
        headers = (
            "Название скрипта#350;"
            "Время запуска#120;"
            "Время окончания#120;"
            "Время исполнения#150"
        )
    else:  # EN (по умолчанию)
        table_title = "Script Execution Time"
        headers = (
            "Script Name#350;"
            "Start Time#120;"
            "End Time#120;"
            "Execution Time#150"
        )

    if action == "init":
        # Используем table_title как визуальный заголовок
        Report(table_title, "info", "table", headers)

    elif action in ("add", "set"):
        # Получаем имя файла и универсально отрезаем любое расширение
        script_name, _ = os.path.splitext(os.path.basename(sys.argv[0]))

        row_data = (
            f"{script_name};"
            f"{TimeGet('ScriptStart')};"
            f"{TimeGet('CurrentDateAndTime')};"
            f"{TimeGet('ScriptExecution')}"
        )
        # Используем тот же table_title как ID для обновления таблицы
        Report(table_title, "set", "table", row_data)
# endregion

# endregion ********************************************************

# region ******* Report / Отчет ************************************

# region --- ReportTableCreate / Упрощенный вызов Report для создания таблиц. ---
def ReportTableCreate(title: str, columns: str, base_width: int = 15) -> None:
    """
    Упрощенный вызов Report для создания таблиц.
    Автоматически рассчитывает ширину колонок (#XX) на основе длины самой длинной строки.
    Формула: base_width + (символы - 1) * 6.

    Поддерживает многострочные заголовки через \\n (ширина считается по самой длинной строке).
    Пробелы справа сохраняются для ручного увеличения ширины.
    Пробелы слева перед \\n автоматически удаляются при сборке финальной строки.

    Args:
        title (str): Заголовок таблицы.
        columns (str): Названия колонок через точку с запятой.
                       Пример: "ID\\n точки;Канал \\n какойто;Мощность      "
        base_width (int): Базовая ширина для колонки из 1 символа. По умолчанию 15.
    """
    column_list = columns.split(';')
    formatted_columns = []

    for col in column_list:
        # Убираем пробелы только СЛЕВА у всей колонки (если они были после ;)
        col = col.lstrip()

        max_len = 0
        cleaned_lines = []  # Сюда будем собирать строки без левых пробелов

        # Разбиваем колонку на отдельные строки по символу переноса
        lines = col.split('\n')

        for line in lines:
            # Убираем пробелы слева у каждой строки, но сохраняем справа
            clean_line = line.lstrip()
            cleaned_lines.append(clean_line)  # Сохраняем очищенную версию для финальной строки

            # Считаем длину этой конкретной строки
            line_len = len(clean_line)

            # Запоминаем максимальную длину среди всех строк колонки
            if line_len > max_len:
                max_len = line_len

        # Применяем формулу с переменной base_width
        width = base_width + (max_len - 1) * 6

        # Склеиваем очищенные строки обратно через \n (пробелы перед \n исчезнут)
        final_col = "\n".join(cleaned_lines)

        # Добавляем рассчитанную ширину
        formatted_columns.append(f"{final_col}#{width}")

    # Собираем всё обратно в одну строку через точку с запятой
    final_string = ";".join(formatted_columns)

    # Вызываем оригинальную функцию Report
    Report(title, 'info', 'table', final_string)

    return
# endregion ****************************************************

# Region --- ReportSave / Сохраняет отчет в указанном формате. ---
def ReportSave(report_format: Literal["Word", "PDF", "Word as", "Pdf as"] = "Word") -> None:
    """
    Сохраняет отчет в указанном формате.

    Args:
        report_format (Literal): Формат сохранения отчета.
                                 Допустимые значения: 'Word', 'PDF', 'Word as', 'Pdf as'.
                                 По умолчанию 'Word'.
    """
    # Точно сопоставляем ввод программиста с тем, что понимает сервер
    server_commands = {
        "Word": "SaveWordReport",
        "PDF": "SavePdfReport",
        "Word as": "SaveWordReportAs",
        "Pdf as": "SavePdfReportAs"
    }

    # Достаем нужную команду из словаря
    command = server_commands[report_format]

    # Вызываем команду
    Program('control', 'set', command)
    return
# endregion ---------------------------------------------------------

# endregion ********************************************************

# endregion ##########################################################################

# region ### Internal Helper Functions / Внутренние вспомогательные функции ###

# region --- check_project_state / Проверка состояния проекта ---
def check_project_state() -> None:
    """
    Проверяет состояние проекта в RF-SE и синхронизирует выполнение скрипта.

    - Если состояние 'run', продолжает выполнение.
    - Если состояние 'pause', приостанавливает скрипт до смены состояния.
    - Если состояние 'stop', немедленно завершает скрипт.
    """
    URLPSRead: str = _UrlProjectStateRead
    projectstate: str = ''
    while (projectstate.lower() != 'run'):
        serverstate = _request.get(URLPSRead)
        JSONprojectstate = json.loads(serverstate.content)
        projectstate: str = JSONprojectstate.get('projectstate')
        if (projectstate.lower() == 'stop'):
            sys.exit()
        if projectstate.lower() == 'pause':
            time.sleep(0.05)
# endregion

# region --- check_status / Проверка статуса ---
def check_status(system: str, mode: str, URLRead: str) -> str:
    """
    Ожидает готовности компонента RF-SE и получает от него данные.

    Функция циклически опрашивает URLRead, пока статус компонента не станет 'ready'.
    Имеет 10 попыток, после чего возвращает пустую строку.

    Args:
        system (str): Имя системы/компонента (например, 'driver', 'plugin').
        mode (str): Режим, в котором была вызвана команда ('get', 'set', и т.д.).
        URLRead (str): URL для чтения статуса и данных.

    Returns:
        str: Строка с данными от компонента или пустая строка в случае ошибки.
    """
    data: str = ""
    badresponse: int = 0
    status: str = "none"
    while ((status.lower() != 'ready') and (badresponse < 10)):
        response = _request.get(URLRead)
        if (response.status_code != 200):
            Stage(f"ERROR IN PYTHON LIBRARY! BAD RESPONSE CODE! {str(response.status_code)}", 'error')
            badresponse += 1
        else:
            y = json.loads(response.content)
            status: str = y.get(f'{system}status')
            if mode.lower() in ('get', 'check', 'init'):
                data: str = y.get(f'{system}data')
        if system in ['message', 'driver', 'plugin', 'utility']:
            time.sleep(0.05)
    if is_bad_response(badresponse): return ""
    return data
# endregion

# region --- parse_data / Разбор данных ---
def parse_data(data: str = '', mode: str = '', valuetype: str = 'void') -> ...:
    """
    Преобразует строковые данные от сервера в нужный тип Python.

    Поддерживает базовые типы (int, float, bool, str) и их массивы (arrayint, ...).

    Args:
        data (str): Входная строка данных от сервера.
        mode (str): Режим, в котором была вызвана команда. Парсинг выполняется только для 'get', 'check', 'init'.
        valuetype (str, optional): Целевой тип данных. Defaults to 'void'.

    Returns:
        Преобразованные данные или None, если парсинг не требуется или невозможен.
    """
    if mode.lower() not in ["get", "check", "init"]: return None
    splitter: str = ";"
    if is_semicolon_error(data, splitter, valuetype): return None
    data: str = check_data(data, splitter)
    if valuetype.lower() == 'arrayboolean':
        return to_list(bool, data, splitter)
    elif valuetype.lower() == 'arrayfloat':
        return to_list(float, data, splitter)
    elif valuetype.lower() == 'arrayint':
        return to_list(int, data, splitter)
    elif valuetype.lower() == 'arraystring':
        return to_list(str, data, splitter)
    elif "bool" in valuetype.lower():
        data: str = data.split(splitter)[0]
        return True if data.lower() == "true" else False
    elif valuetype.lower() == 'float':
        data: str = data.split(splitter)[0]
        return float(data.replace(",", "."))
    elif valuetype.lower() == 'int':
        data: str = data.split(splitter)[0]
        data: str = data.split(".")[0]
        return int(data.split(",")[0])
    else:  # Используется в качестве valuetype = 'string'
        return data.split(splitter)[0]
# endregion

# region --- check_data / Проверка данных ---
def check_data(data: str, splitter: str = ";") -> str:
    """
    Удаляет лишний символ-разделитель (';') в конце строки, если он есть.

    Args:
        data (str): Входная строка.
        splitter (str, optional): Символ-разделитель. Defaults to ";".

    Returns:
        str: Очищенная строка.
    """
    if data.rfind(splitter) == len(data)-1:
        data: str = data[:-1]
    return data
# endregion

# region --- to_list / Преобразовать в список ---
def to_list(func, data: str, splitter: str = ";") -> ...:
    """
    Разделяет строку на список и преобразует каждый элемент к заданному типу.

    Args:
        func: Функция преобразования типа (int, float, bool, str).
        data (str): Входная строка с данными, разделенными `splitter`.
        splitter (str, optional): Символ-разделитель. Defaults to ";".

    Returns:
        list: Список с преобразованными значениями.
    """
    split_data: list = data.split(splitter)
    result: list = []
    for spl in split_data:
        if func is bool:
            result.append(True if spl.lower() == "true" else False)
        elif func is int:
            spl: str = spl.split(".")[0]
            result.append(func(spl.split(",")[0]))
        elif func is float:
            result.append(func(spl.replace(",", ".")))
        else:
            result.append(func(spl))
    return result
# endregion

# region --- is_semicolon_error / Ошибка с точкой с запятой ---
def is_semicolon_error(data: str, splitter: str, valuetype: str) -> bool:
    """
    Проверяет наличие двойного разделителя (';;') в конце строки.

    Это считается ошибкой формата данных. При обнаружении выводит ошибку в Stage.

    Args:
        data (str): Входная строка.
        splitter (str): Символ-разделитель.
        valuetype (str): Тип значения, для которого производится проверка.

    Returns:
        bool: True, если ошибка найдена, иначе False.
    """
    if data[-2:] == f"{2*splitter}":
        Stage(f'ERROR IN PYTHON LIBRARY!', 'error')
        Stage(f'INPUT DATA CONTAINS MORE THAN 1 \'\'{splitter}\'\' AT THE END!', 'error')
        Stage(f'DATA: {data}     =>     VALUETYPE: {valuetype.upper()}', 'error')
        return True
    return False
# endregion

# region --- is_bad_response / Проверка плохого ответа ---
def is_bad_response(badresponse: int) -> bool:
    """
    Проверяет, не превышено ли количество неудачных ответов от сервера.

    Args:
        badresponse (int): Счетчик неудачных ответов.

    Returns:
        bool: True, если количество ошибок >= 10, иначе False.
    """
    if (badresponse >= 10):
        Stage("ERROR IN PYTHON LIBRARY! FUNCTION EXIT BECAUSE OF BAD RESPONSES", 'error')
        return True
    return False
# endregion

# region --- send_request / Отправка запроса ---
def send_request(URLWrite: str, request: str) -> None:
    """
    Отправляет POST-запрос на указанный URL с данными в формате JSON.

    Args:
        URLWrite (str): URL для отправки запроса.
        request (str): Тело запроса в виде строки JSON.
    """
    headers: dict = {'Content-Type': 'application/json; charset=utf-8'}
    response = _request.post(URLWrite, headers=headers, data=request.encode('utf-8'))
# endregion

# endregion