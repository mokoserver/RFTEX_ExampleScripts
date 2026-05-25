import TestActions as ta
from WebActions import initialize_browser, login_to_router, close_browser
import RFSE
from RFSE import EndScript
from RFSE import Stage, StageError, StageInfo,StageSuccess

# region Шаг 1: Инициализация и вход$INIT
RFSE.HashExecuteStep("Шаг 1: Инициализация и вход$INIT")
browser = initialize_browser()

try:
    login_to_router(browser,
                       "admin",
                       "password123")
    #endregion

    #region Шаг 2: Проведение измерений$MEASURE
    #description: ID точки;Уровень мощности;Канал;
    RFSE.HashExecuteStep("Шаг 2: Проведение измерений$MEASURE")
    RFSE.ReportTableCreate("Производительность Wi-Fi Пакет 1",
                         "ID точки;Уровень\n мощности  ;Канал ;Мощность\n передачи   ;Эффективная  \n скорость;")

    ta.run_test_point_batch1(browser, 'Измерение 1$MEASURE', 1, 'low',    'auto') #hash Измерение 1$MEASURE: 1;low;auto
    ta.run_test_point_batch1(browser, 'Измерение 2$MEASURE', 2, 'low',    1)      #hash Измерение 2$MEASURE: 2;low;1
    ta.run_test_point_batch1(browser, 'Измерение 3$MEASURE', 3, 'medium', 6)      #hash Измерение 3$MEASURE: 3;medium;6
    ta.run_test_point_batch1(browser, 'Измерение 4$MEASURE', 4, 'medium', 11)     #hash Измерение 4$MEASURE: 4;medium;11
    ta.run_test_point_batch1(browser, 'Измерение 5$MEASURE', 5, 'high',   'auto') #hash Измерение 5$MEASURE: 5;high;auto
    ta.run_test_point_batch1(browser, 'Измерение 6$MEASURE', 6, 'high',   1)      #hash Измерение 6$MEASURE: 6;high;1
    ta.run_test_point_batch1(browser, 'Измерение 7$MEASURE', 7, 'high',   6)      #hash Измерение 7$MEASURE: 7;high;6
    ta.run_test_point_batch1(browser, 'Измерение 8$MEASURE', 8, 'high',   11)     #hash Измерение 8$MEASURE: 8;high;11
    ta.run_test_point_batch1(browser, 'Измерение 9$MEASURE', 9, 'medium', 'auto') #hash Измерение 9$MEASURE: 9;medium;auto
    ta.run_test_point_batch1(browser, 'Измерение 10$MEASURE', 10, 'low',  6)      #hash Измерение 10$MEASURE: 10;low;6
    #endregion

    #region Шаг 3: Дополнительные измерения$MEASURE2
    #description: ID точки;Уровень мощности;Канал;
    RFSE.HashExecuteStep("Шаг 3: Дополнительные измерения$MEASURE2")
    RFSE.ReportTableCreate("Производительность Wi-Fi Дополнительно",
                         "ID точки;Уровень\n мощности  ;Канал ;Мощность\n передачи   ;Эффективная  \n скорость;")


    RFSE.Port("hghgh","init","Ghbdtn")
    ta.run_test_point_additional(browser, 'Измерение 11$MEASURE2', 11, 'low',    1)        #hash Измерение 11$MEASURE2: 11;low;1
    ta.run_test_point_additional(browser, 'Измерение 12$MEASURE2', 12, 'low',    6)        #hash Измерение 12$MEASURE2: 12;low;6
    ta.run_test_point_additional(browser, 'Измерение 13$MEASURE2', 13, 'low',    11)       #hash Измерение 13$MEASURE2: 13;low;11
    ta.run_test_point_additional(browser, 'Измерение 14$MEASURE2', 14, 'medium', 'auto')   #hash Измерение 14$MEASURE2: 14;medium;auto
    ta.run_test_point_additional(browser, 'Измерение 15$MEASURE2', 15, 'medium', 1)        #hash Измерение 15$MEASURE2: 15;medium;1
    ta.run_test_point_additional(browser, 'Измерение 16$MEASURE2', 16, 'medium', 6)        #hash Измерение 16$MEASURE2: 16;medium;6
    ta.run_test_point_additional(browser, 'Измерение 17$MEASURE2', 17, 'high',   'auto')   #hash Измерение 17$MEASURE2: 17;high;auto
    ta.run_test_point_additional(browser, 'Измерение 18$MEASURE2', 18, 'high',   1)        #hash Измерение 18$MEASURE2: 18;high;1
    ta.run_test_point_additional(browser, 'Измерение 19$MEASURE2', 19, 'high',   6)        #hash Измерение 19$MEASURE2: 19;high;6
    ta.run_test_point_additional(browser, 'Измерение 20$MEASURE2', 20, 'high',   11)       #hash Измерение 20$MEASURE2: 20;high;11
    #endregion

    StageSuccess("Сценарий измерений успешно выполнен!")

except Exception as e:
    StageError(f"Произошла критическая ошибка: {e}")

finally:
    if 'browser' in locals() and browser:
        #region Шаг 4: Закрыть браузер$CLOSE1
        RFSE.HashExecuteStep("Шаг 4: Закрыть браузер$CLOSE1")
        close_browser(browser)
        #endregion

    RFSE.ReportTimeAdd("add","RU")
    EndScript()
