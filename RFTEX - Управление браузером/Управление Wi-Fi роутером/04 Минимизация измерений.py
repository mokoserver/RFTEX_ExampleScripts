import os
import TestActions as ta
from WebActions import initialize_browser, login_to_router, minimize_browser, close_browser
import RFSE
from RFSE import Stage, EndScript, Program, Report
from RFSE import Stage, StageError, StageInfo,StageSuccess
from datetime import datetime

browser = None

StartTime = datetime.now()

try:
    #region Шаг 1: Инициализация и вход (Пакет 3)$INIT3
    RFSE.HashExecuteStep("Шаг 1: Инициализация и вход (Пакет 3)$INIT3")
    browser = initialize_browser()
    login_to_router(browser, "admin", "password123")
    #endregion

    #region Свернуть браузер (Пакет 3)$MIN3
    RFSE.HashExecuteStep("Свернуть браузер (Пакет 3)$MIN3")
    minimize_browser(browser)
    #endregion

    #region Шаг 2: Проведение измерений (Пакет 3)$MEASURE3
    #description: ID точки;Уровень мощности;Канал;
    RFSE.HashExecuteStep("Шаг 2: Проведение измерений (Пакет 3)$MEASURE3")
    RFSE.ReportTableCreate("Производительность Wi-Fi Пакет 3",
                         "ID точки;Уровень\n мощности  ;Канал ;Мощность\n передачи   ;Эффективная  \n скорость;")

    ta.run_test_point_batch3(browser, 'Измерение 31$MEASURE3', 31, 'low',     'auto') #hash Измерение 31$MEASURE3: 31;low;auto
    ta.run_test_point_batch3(browser, 'Измерение 32$MEASURE3', 32, 'low',     1)      #hash Измерение 32$MEASURE3: 32;low;1
    ta.run_test_point_batch3(browser, 'Измерение 33$MEASURE3', 33, 'medium',  6)      #hash Измерение 33$MEASURE3: 33;medium;6
    ta.run_test_point_batch3(browser, 'Измерение 34$MEASURE3', 34, 'high',    11)     #hash Измерение 34$MEASURE3: 34;high;11
    ta.run_test_point_batch3(browser, 'Измерение 35$MEASURE3', 35, 'high',    'auto') #hash Измерение 35$MEASURE3: 35;high;auto
    #endregion

    StageSuccess("Сценарий измерений (Пакет 3) успешно выполнен!")

except Exception as e:
    StageError(f"Произошла критическая ошибка: {e}")

finally:
    if 'browser' in locals() and browser:
        #region Шаг 3: Закрыть браузер (Пакет 3)$CLOSE3
        RFSE.HashExecuteStep("Шаг 3: Закрыть браузер (Пакет 3)$CLOSE3")
        close_browser(browser)
        #endregion

    RFSE.ReportTimeAdd("add","RU")
    EndScript()
