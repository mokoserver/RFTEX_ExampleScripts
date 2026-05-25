'''
Библиотека MTLG.py
===================

Эта библиотека предоставляет набор функций-оберток для отправки стандартизированных
уведомлений в Telegram о вызовах различных функций из основной библиотеки py.

Каждая функция формирует и отправляет сообщение, содержащее информацию о вызванном
методе и его параметрах, используя для этого `Telegram`.

Пример использования:
--------------------

**1. Прямая отправка сообщения через RFSE:**
```python
import RFSE

# Будет отправлено простое текстовое сообщение "Hello World"
Telegram(role='alpha', mode='set', command='Hello World')
```

**2. Отправка форматированного сообщения через MTLG:**
```python
import MTLG

# Будет отправлено форматированное сообщение с иконками и полями
# "ROLE: alpha", "MODE: set", "COMMAND: Hello World"
MTLG.TelegramClassic(role='alpha', mode='set', command='Hello World')
```
'''

from RFSE import Telegram

# region ### Emoji Constants / Константы эмодзи ###
scull_sml: str = '%E2%98%A0'          # ☠️ (череп и кости)
report_sml: str = '%F0%9F%93%A2'         # 📢 (мегафон)
driver_sml: str = '%F0%9F%96%A8'         # 🖨️ (принтер)
prog_sml: str = '%F0%9F%85%BF'           # 🅿️ (кнопка P)
message_sml: str = '%F0%9F%92%AC'        # 💬 (облако диалога)
mode_sml: str = '%F0%9F%93%97'           # 📗 (зеленая книга)
name_sml: str = '%F0%9F%93%99'           # 📮 (почтовый ящик)
head_sml: str = '%F0%9F%93%92'           # 📒 (блокнот)
command_sml: str = '%F0%9F%93%94'        # 📔 (тетрадь)
type_sml: str = '%F0%9F%93%9A'           # 📜 (свиток)
delay_sml: str = '%E2%8C%9B'           # ⌛ (песочные часы)
body_sml: str = '%F0%9F%93%B0'           # 📱 (мобильный телефон)
data_sml: str = '%F0%9F%93%96'           # 📖 (открытая книга)
# endregion

# region ### Telegram Wrappers / Обертки для Telegram ###

# region --- TelegramReport / Отчет Telegram ---
def TelegramReport(name: str, mode: str, kind: str, data: str, valuetype: str = 'void') -> None:
    """Отправляет уведомление о вызове функции Report."""
    Telegram('alpha', 'set', f'{report_sml} {report_sml} {report_sml} RF-SE REPORT {report_sml} {report_sml} {report_sml}\n'
                                  '\n'
                                  f'{name_sml} NAME: {name}\n'
                                  '\n'
                                  f'{mode_sml} MODE: {mode}\n'
                                  '\n'
                                  f'{type_sml} KIND: {kind}\n'
                                  '\n'
                                  f'{data_sml} DATA: {data}\n'
                                  '\n'
                                  f'{type_sml} VALUETYPE: {valuetype}')
# endregion

# region --- TelegramMessenger / Мессенджер Telegram ---
def TelegramMessenger(mode: str, head: str, body: str, valuetype: str = 'void', delaytime: str = 'void') -> None:
    """Отправляет уведомление о вызове функции Messenger."""
    Telegram('alpha', 'set', f'{message_sml} {message_sml} {message_sml} RF-SE MESSENGER {message_sml} {message_sml} {message_sml}\n'
                                  '\n'
                                  f'{mode_sml} MODE: {mode}\n'
                                  '\n'
                                  f'{head_sml} HEAD: {head}\n'
                                  '\n'
                                  f'{body_sml} BODY: {body}\n'
                                  '\n'
                                  f'{type_sml} VALUETYPE: {valuetype}\n'
                                  '\n'
                                  f'{delay_sml} DELAYTIME: {delaytime}')
# endregion

# region --- TelegramPlugin / Плагин Telegram ---
def TelegramPlugin(name: str, mode: str, command: str, valuetype: str = 'void') -> None:
    """Отправляет уведомление о вызове функции Plugin."""
    Telegram('alpha', 'set', f'{scull_sml} {scull_sml} {scull_sml} RF-SE PLUGIN {scull_sml} {scull_sml} {scull_sml}\n'
                                  '\n'
                                  f'{name_sml} NAME: {name}\n'
                                  '\n'
                                  f'{mode_sml} MODE: {mode}\n'
                                  '\n'
                                  f'{command_sml} COMMAND: {command}\n'
                                  '\n'
                                  f'{type_sml} VALUETYPE: {valuetype}')
# endregion

# region --- TelegramUtility / Утилита Telegram ---
def TelegramUtility(name: str, mode: str, command: str, valuetype: str = 'void') -> None:
    """Отправляет уведомление о вызове функции Utility."""
    Telegram('alpha', 'set', f'{scull_sml} {scull_sml} {scull_sml} RF-SE UTILITY {scull_sml} {scull_sml} {scull_sml}\n'
                                  '\n'
                                  f'{name_sml} NAME: {name}\n'
                                  '\n'
                                  f'{mode_sml} MODE: {mode}\n'
                                  '\n'
                                  f'{command_sml} COMMAND: {command}\n'
                                  '\n'
                                  f'{type_sml} VALUETYPE: {valuetype}')
# endregion

# region --- TelegramProgram / Программа Telegram ---
def TelegramProgram(name: str, mode: str, command: str, valuetype: str = 'void') -> None:
    """Отправляет уведомление о вызове функции Program."""
    Telegram('alpha', 'set', f'{prog_sml} {prog_sml} {prog_sml} RF-SE PROGRAM {prog_sml} {prog_sml} {prog_sml}\n'
                                  '\n'
                                  f'{name_sml} NAME: {name}\n'
                                  '\n'
                                  f'{mode_sml} MODE: {mode}\n'
                                  '\n'
                                  f'{command_sml} COMMAND: {command}\n'
                                  '\n'
                                  f'{type_sml} VALUETYPE: {valuetype}')
# endregion

# region --- TelegramClassic / Классический Telegram ---
def TelegramClassic(role: str, mode: str, command: str, valuetype: str = 'void') -> None:
    """Отправляет уведомление о вызове базовой функции Telegram."""
    Telegram('alpha', 'set', f'{scull_sml} {scull_sml} {scull_sml} RF-SE TELEGRAM {scull_sml} {scull_sml} {scull_sml}\n'
                                  '\n'
                                  f'{name_sml} ROLE: {role}\n'
                                  '\n'
                                  f'{mode_sml} MODE: {mode}\n'
                                  '\n'
                                  f'{command_sml} COMMAND: {command}\n'
                                  '\n'
                                  f'{type_sml} VALUETYPE: {valuetype}')
# endregion

# region --- TelegramDriver / Драйвер Telegram ---
def TelegramDriver(name: str, mode: str, command: str, valuetype: str = 'void') -> None:
    """Отправляет уведомление о вызове функции Driver."""
    Telegram('alpha', 'set', f'{driver_sml} {driver_sml} {driver_sml} RF-SE DRIVER {driver_sml} {driver_sml} {driver_sml}\n'
                                  '\n'
                                  f'{name_sml} NAME: {name}\n'
                                  '\n'
                                  f'{mode_sml} MODE: {mode}\n'
                                  '\n'
                                  f'{command_sml} COMMAND: {command}\n'
                                  '\n'
                                  f'{type_sml} VALUETYPE: {valuetype}')
# endregion

# region --- TelegramStage / Этап Telegram ---
def TelegramStage(stage_string: str, type: str) -> None:
    """Отправляет уведомление о вызове функции Stage."""
    Telegram('alpha', 'set', f'{scull_sml} {scull_sml} {scull_sml} RF-SE STAGE {scull_sml} {scull_sml} {scull_sml}\n'
                                  '\n'
                                  f'STAGE_STRING: {stage_string}\n'
                                  '\n'
                                  f'{type_sml} TYPE: {type}')
# endregion

# region --- TelegramEndScript / Завершение скрипта Telegram ---
def TelegramEndScript(command: str = 'done') -> None:
    """Отправляет уведомление о завершении скрипта (вызове EndScript)."""
    TelegramProgram('script', 'set', command)
# endregion

# endregion
