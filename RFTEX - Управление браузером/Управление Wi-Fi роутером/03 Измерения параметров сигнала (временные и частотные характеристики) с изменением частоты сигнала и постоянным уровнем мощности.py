import TestActions as ta
from WebActions import initialize_browser, login_to_router, close_browser,hide_browser
import RFSE
from RFSE import  StageError, StageSuccess

browser = None

try:
    #region Шаг 1: Инициализация и вход (Пакет 2)$INIT2
    RFSE.HashExecuteStep("Шаг 1: Инициализация и вход (Пакет 2)$INIT2")
    browser = initialize_browser()
    login_to_router(browser, "admin", "password123")
    #endregion

    #region Скрыть браузер (Пакет 2)$HIDE2
    RFSE.HashExecuteStep("Скрыть браузер (Пакет 2)$HIDE2")
    hide_browser(browser)
    #endregion

    #region Шаг 2: Проведение измерений (Пакет 2)$MEASURE2
    #description: ID точки;Уровень мощности;Канал;
    RFSE.HashExecuteStep("Шаг 2: Проведение измерений (Пакет 2)$MEASURE2")
    RFSE.ReportTableCreate("Производительность Wi-Fi Пакет 2",
                         "ID точки;Уровень\n мощности  ;Канал ;Мощность\n передачи   ;Эффективная  \n скорость;")

    ta.run_test_point_batch2(browser, 'Измерение 21$MEASURE2', 21, 'low',    'auto') #hash Измерение 21$MEASURE2: 21;low;auto
    ta.run_test_point_batch2(browser, 'Измерение 22$MEASURE2', 22, 'low',    1)      #hash Измерение 22$MEASURE2: 22;low;1
    ta.run_test_point_batch2(browser, 'Измерение 23$MEASURE2', 23, 'low',    6)      #hash Измерение 23$MEASURE2: 23;low;6
    ta.run_test_point_batch2(browser, 'Измерение 24$MEASURE2', 24, 'low',    11)     #hash Измерение 24$MEASURE2: 24;low;11
    ta.run_test_point_batch2(browser, 'Измерение 25$MEASURE2', 25, 'medium', 'auto') #hash Измерение 25$MEASURE2: 25;medium;auto
    ta.run_test_point_batch2(browser, 'Измерение 26$MEASURE2', 26, 'medium', 1)      #hash Измерение 26$MEASURE2: 26;medium;1
    ta.run_test_point_batch2(browser, 'Измерение 27$MEASURE2', 27, 'medium', 6)      #hash Измерение 27$MEASURE2: 27;medium;6
    ta.run_test_point_batch2(browser, 'Измерение 28$MEASURE2', 28, 'high',   'auto') #hash Измерение 28$MEASURE2: 28;high;auto
    ta.run_test_point_batch2(browser, 'Измерение 29$MEASURE2', 29, 'high',   1)      #hash Измерение 29$MEASURE2: 29;high;1
    ta.run_test_point_batch2(browser, 'Измерение 30$MEASURE2', 30, 'high',   11)     #hash Измерение 30$MEASURE2: 30;high;11
    #endregion

    StageSuccess("Сценарий измерений (Пакет 2) успешно выполнен!")

except Exception as e:
    StageError(f"Произошла критическая ошибка: {e}")
finally:
    if 'browser' in locals() and browser:
        #region Шаг 3: Закрыть браузер (Пакет 2)$CLOSE2
        RFSE.HashExecuteStep("Шаг 3: Закрыть браузер (Пакет 2)$CLOSE2")
        close_browser(browser)
        #endregion


    RFSE.ReportTimeAdd("add","RU")

    RFSE.ProjectRestart()


