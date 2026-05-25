
import os

import RFSE
import WebActions as wa
from RFSE import Stage, EndScript, Program, Report
from datetime import datetime
import MOSC

# Fix script start time
StartTime = datetime.now()

try:
    #region Step 1: Initialize and Login$INIT
    Program('tree', 'set', 'select = Step 1: Initialize and Login$INIT')
    Stage("--- Step 1: Initialize and Login ---")
    browser = wa.initialize_browser()
    wa.login_to_router(browser, "admin", "password123")
    #endregion

    # --- MAIN MEASUREMENTS SCENARIO ---
    #region Step 2: Perform Measurements$MEASURE
    #description: Point ID;Power Level;Channel;
    Program('tree', 'set', 'select = Step 2: Perform Measurements$MEASURE')
    Stage("--- Step 2: Perform Measurements ---")

    Report("WiFi Performance - Batch 1", 'info', 'table', "Point ID#100;Power Level#100;Channel#100;Transmit Power#100;Effective Rate#100")

    wa.run_test_point_batch1(browser, 'Meas 1$MEASURE', 1, 'low',    'auto') #hash Meas 1$MEASURE: 1;low;auto
    wa.run_test_point_batch1(browser, 'Meas 2$MEASURE', 2, 'low',    1)      #hash Meas 2$MEASURE: 2;low;1
    wa.run_test_point_batch1(browser, 'Meas 3$MEASURE', 3, 'medium', 6)      #hash Meas 3$MEASURE: 3;medium;6
    wa.run_test_point_batch1(browser, 'Meas 4$MEASURE', 4, 'medium', 11)     #hash Meas 4$MEASURE: 4;medium;11
    wa.run_test_point_batch1(browser, 'Meas 5$MEASURE', 5, 'high',   'auto') #hash Meas 5$MEASURE: 5;high;auto
    wa.run_test_point_batch1(browser, 'Meas 6$MEASURE', 6, 'high',   1)      #hash Meas 6$MEASURE: 6;high;1
    wa.run_test_point_batch1(browser, 'Meas 7$MEASURE', 7, 'high',   6)      #hash Meas 7$MEASURE: 7;high;6
    wa.run_test_point_batch1(browser, 'Meas 8$MEASURE', 8, 'high',   11)     #hash Meas 8$MEASURE: 8;high;11
    wa.run_test_point_batch1(browser, 'Meas 9$MEASURE', 9, 'medium', 'auto') #hash Meas 9$MEASURE: 9;medium;auto
    wa.run_test_point_batch1(browser, 'Meas 10$MEASURE', 10, 'low',  6)      #hash Meas 10$MEASURE: 10;low;6
    #endregion

    #region Step 3: Additional Measurements$MEASURE2
    #description: Point ID;Power Level;Channel;
    Program('tree', 'set', 'select = Step 3: Additional Measurements$MEASURE2')
    Stage("--- Step 3: Additional Measurements ---")

    Report("WiFi Performance - Additional", 'info', 'table', "Point ID#100;Power Level#100;Channel#100;Transmit Power#100;Effective Rate#100")

    wa.run_test_point_additional(browser, 'Meas 11$MEASURE2', 11, 'low',    1)   #hash Meas 11$MEASURE2: 11;low;1
    wa.run_test_point_additional(browser, 'Meas 12$MEASURE2', 12, 'low',    6)   #hash Meas 12$MEASURE2: 12;low;6
    wa.run_test_point_additional(browser, 'Meas 13$MEASURE2', 13, 'low',    11)  #hash Meas 13$MEASURE2: 13;low;11
    wa.run_test_point_additional(browser, 'Meas 14$MEASURE2', 14, 'medium', 'auto') #hash Meas 14$MEASURE2: 14;medium;auto
    wa.run_test_point_additional(browser, 'Meas 15$MEASURE2', 15, 'medium', 1)   #hash Meas 15$MEASURE2: 15;medium;1
    wa.run_test_point_additional(browser, 'Meas 16$MEASURE2', 16, 'medium', 6)   #hash Meas 16$MEASURE2: 16;medium;6
    wa.run_test_point_additional(browser, 'Meas 17$MEASURE2', 17, 'high',   'auto') #hash Meas 17$MEASURE2: 17;high;auto
    wa.run_test_point_additional(browser, 'Meas 18$MEASURE2', 18, 'high',   1)   #hash Meas 18$MEASURE2: 18;high;1
    wa.run_test_point_additional(browser, 'Meas 19$MEASURE2', 19, 'high',   6)   #hash Meas 19$MEASURE2: 19;high;6
    wa.run_test_point_additional(browser, 'Meas 20$MEASURE2', 20, 'high',   11)  #hash Meas 20$MEASURE2: 20;high;11
    #endregion

    Stage("\nMeasurements scenario completed successfully!", "info")

except Exception as e:
    Stage(f"\nA critical error occurred: {e}", "error")

finally:
    if 'browser' in locals() and browser:
        #region Step 4: Close Browser$CLOSE1
        Program('tree', 'set', 'select = Step 4: Close Browser$CLOSE1')
        Stage("--- Step 4: Close Browser ---")
        wa.close_browser(browser)
        #endregion
    MOSC.ScriptExecutionTime(StartTime)
    EndScript()

