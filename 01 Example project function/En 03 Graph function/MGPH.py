'''
MGPH.py - RFSE Graph Library
============================

Эта библиотека предоставляет высокоуровневый интерфейс для плагина "RFSE Graph".
Она упрощает создание, настройку и управление графиками и их элементами.

Ключевые возможности:
---------------------
- Добавление, изменение и удаление линий на графике.
- Настройка осей, автомасштабирования и легенды.
- Создание скриншотов всего окна плагина или только области графика.

Пример использования:
--------------------
```python
import MGPH

# Инициализация плагина
MGPH.GraphInit()

# Данные для графика
x_data = [0, 1, 2, 3, 4, 5]
y_data_sin = [0, 0.84, 0.9, 0.14, -0.75, -0.95]

# Добавление линии на график
MGPH.AddLine(
    name="Синусоида",
    ArrOx=x_data,
    ArrOy=y_data_sin,
    Color="0000FF"  # Синий цвет
)

# Настройка осей
MGPH.AddGraphSett(
    Value_OyOx=[-1, 1, 0, 5],  # [Ymin, Ymax, Xmin, Xmax]
    Name_Oy="Амплитуда",
    Name_Ox="Время, с"
)
```
'''
from RFSE import Plugin

PLUGIN_NAME: str = "Graph"

# region ### Initialization / Инициализация ###

# region --- GraphInit / Инициализация Графика ---

# -- GraphInit --
def GraphInit() -> None:
    """
    Инициализирует плагин RFSE Graph.
    Этот метод должен быть вызван перед использованием любых других функций из этой библиотеки.
    """
    Plugin(PLUGIN_NAME, "init", "")
# endregion

# endregion

# region ### Set Commands (Actions) / Команды Установки (Действия) ###

# region --- Line Management / Управление Линиями ---

# -- AddLine --
def AddLine(name: str,
            ArrOy: list,
            ArrOx: list,
            LineWidth: str = "3",
            Color: str = "000000",
            Visible: str = "True") -> None:
    """
    Добавляет новую линию на график.

    Args:
        name (str): Имя линии (будет отображаться в легенде).
        ArrOy (list): Список значений по оси Y.
        ArrOx (list): Список значений по оси X.
        LineWidth (str, optional): Толщина линии. Defaults to "3".
        Color (str, optional): Цвет линии в HEX-формате (например, "0000FF" для синего). Defaults to "000000".
        Visible (str, optional): Видимость линии ("True" или "False"). Defaults to "True".
    """
    Plugin(PLUGIN_NAME, 'set', f"Add Line={name};{ArrOy};{ArrOx};{LineWidth};{Color};{Visible}")
    Plugin(PLUGIN_NAME, 'set', "Write Graph")

# -- ChangeLine --
def ChangeLine(numLine: str,
               name: str,
               ArrOy: list,
               ArrOx: list,
               LineWidth: str = "3",
               Color: str = "000000",
               Visible: str = "True") -> None:
    """
    Изменяет существующую линию на графике.

    Args:
        numLine (str): Порядковый номер (начиная с 0) или имя линии для изменения.
        name (str): Новое имя линии.
        ArrOy (list): Новый список значений по оси Y.
        ArrOx (list): Новый список значений по оси X.
        LineWidth (str, optional): Новая толщина линии. Defaults to "3".
        Color (str, optional): Новый цвет линии в HEX-формате. Defaults to "000000".
        Visible (str, optional): Новая видимость линии. Defaults to "True".
    """
    Plugin(PLUGIN_NAME, 'set', f"Change Line={numLine};{name};{ArrOy};{ArrOx};{LineWidth};{Color};{Visible}")

# -- DeleteLine --
def DeleteLine(numLine: list | str | int) -> None:
    """
    Удаляет одну или несколько линий с графика.

    Args:
        numLine: Может быть:
                 - "All": для удаления всех линий.
                 - int: номер одной линии для удаления.
                 - list: список номеров или имен линий для удаления.
    """
    Plugin(PLUGIN_NAME, 'set', f"Delete Line={numLine}")

# -- HideLine --
def HideLine(numLine: list | str | int) -> None:
    """
    Скрывает одну или несколько линий на графике.

    Args:
        numLine: "All", номер линии (int) или список номеров/имен (list).
    """
    Plugin(PLUGIN_NAME, 'set', f"Hide Line={numLine}")

# -- ShowLine --
def ShowLine(numLine: list | str | int) -> None:
    """
    Показывает одну или несколько ранее скрытых линий.

    Args:
        numLine: "All", номер линии (int) или список номеров/имен (list).
    """
    Plugin(PLUGIN_NAME, 'set', f"Show Line={numLine}")

# -- ShowLineOnly --
def ShowLineOnly(numLine: list | str | int) -> None:
    """
    Показывает только выбранные линии, скрывая все остальные.

    Args:
        numLine: Номер линии (int) или список номеров/имен (list) для отображения.
    """
    Plugin(PLUGIN_NAME, 'set', f"Show Line=Only;{numLine}")
# endregion

# region --- Graph & Axis Settings / Настройки Графика и Осей ---

# -- AddGraphSett --
def AddGraphSett(Value_OyOx: list, Name_Oy: str, Name_Ox: str, Autoscale: str = "Yes") -> None:
    """
    Устанавливает основные параметры графика и осей.

    Args:
        Value_OyOx (list): Список из 4 значений [Ymin, Ymax, Xmin, Xmax].
        Name_Oy (str): Название оси Y.
        Name_Ox (str): Название оси X.
        Autoscale (str, optional): Режим автомасштабирования ("Yes", "No", "OnlyOy", "OnlyOx"). Defaults to "Yes".
    """
    Plugin(PLUGIN_NAME, 'set', f"Add Graph Settings={Value_OyOx};{Name_Oy};{Name_Ox};{Autoscale}")

# -- Autoscale --
def Autoscale(mode: str = "Yes") -> None:
    """
    Управляет режимом автомасштабирования графика.

    Args:
        mode (str, optional): Режим ("Yes", "No", "OnlyOy", "OnlyOx"). Defaults to "Yes".
    """
    Plugin(PLUGIN_NAME, 'set', f"Autoscale={mode}")

# -- Legend --
def Legend() -> None:
    """
    Переключает видимость легенды графика (показать/скрыть).
    """
    Plugin(PLUGIN_NAME, 'set', "Legend")
# endregion

# region --- General Commands / Общие Команды ---

# -- WriteGraph --
def WriteGraph() -> None:
    """
    Принудительно перерисовывает график, отображая все последние изменения.
    """
    Plugin(PLUGIN_NAME, 'set', "Write Graph")

# -- ClearGraph --
def ClearGraph() -> None:
    """
    Полностью очищает область графика, удаляя все линии и настройки.
    """
    Plugin(PLUGIN_NAME, 'set', "Clear Graph")
# endregion

# region --- Screenshot Commands / Команды Скриншотов ---

# -- ScreenshotWindow --
def ScreenshotWindow() -> None:
    """
    Делает скриншот всего окна плагина "RFSE Graph".
    Файл сохраняется в стандартную директорию плагина.
    """
    Plugin(PLUGIN_NAME, 'set', "Screenshot Window")

# -- ScreenshotGraph --
def ScreenshotGraph() -> None:
    """
    Делает скриншот только области самого графика.
    Файл сохраняется в стандартную директорию плагина.
    """
    Plugin(PLUGIN_NAME, 'set', "Screenshot Graph")
# endregion

# endregion

# region ### Get Commands (Data Retrieval) / Команды Получения Данных ###

# region --- GetScreenshotWindow / Получить Скриншот Окна ---

# -- GetScreenshotWindow --
def GetScreenshotWindow() -> str:
    """
    Делает скриншот всего окна плагина и возвращает его в формате Base64.

    Returns:
        str: Строка с изображением в кодировке Base64.
    """
    return Plugin(PLUGIN_NAME, 'get', "ScreenshotWindow", 'string')
# endregion

# region --- GetScreenshotGraph / Получить Скриншот Графика ---

# -- GetScreenshotGraph --
def GetScreenshotGraph() -> str:
    """
    Делает скриншот области графика и возвращает его в формате Base64.

    Returns:
        str: Строка с изображением в кодировке Base64.
    """
    screen = Plugin(PLUGIN_NAME, 'get', "ScreenshotGraph", 'string')
    return screen
# endregion

# endregion
