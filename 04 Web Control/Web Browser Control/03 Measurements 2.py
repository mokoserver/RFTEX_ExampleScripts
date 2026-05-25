import os
import time
import WebActions as wa
from RFSE import Stage, EndScript, Program, Report
from datetime import datetime
import MOSC

# --- COMMON SETTINGS ---
browser = None

# Fix script start time
StartTime = datetime.now()

try:
    #region Step 1: Initialize and Login (Batch 2)$INIT2
    Program('tree', 'set', 'select = Step 1: Initialize and Login (Batch 2)$INIT2')
    Stage("--- Step 1: Initialize and Login (Batch 2) ---")
    browser = wa.initialize_browser()
    wa.login_to_router(browser, "admin", "password123")
    #endregion

    #region Hide Browser (Batch 2)$HIDE2
    Program('tree', 'set', 'select = Hide Browser (Batch 2)$HIDE2')
    Stage("--- Hide Browser (Batch 2) ---")
    wa.hide_browser(browser)
    #endregion

    # --- MEASUREMENTS SCENARIO (SECOND TEN) ---
    #region Step 2: Perform Measurements (Batch 2)$MEASURE2
    #description: Point ID;Power Level;Channel;
    Program('tree', 'set', 'select = Step 2: Perform Measurements (Batch 2)$MEASURE2')
    Stage("--- Step 2: Perform Measurements (Batch 2) ---")

    Report("WiFi Performance - Batch 2", 'info', 'table', "Point ID#100;Power Level#100;Channel#100;Transmit Power#100;Effective Rate#100")

    wa.run_test_point_batch2(browser, 'Meas 21$MEASURE2', 21, 'low',    'auto') #hash Meas 21$MEASURE2: 21;low;auto
    wa.run_test_point_batch2(browser, 'Meas 22$MEASURE2', 22, 'low',    1)      #hash Meas 22$MEASURE2: 22;low;1
    wa.run_test_point_batch2(browser, 'Meas 23$MEASURE2', 23, 'low',    6)      #hash Meas 23$MEASURE2: 23;low;6
    wa.run_test_point_batch2(browser, 'Meas 24$MEASURE2', 24, 'low',    11)     #hash Meas 24$MEASURE2: 24;low;11
    wa.run_test_point_batch2(browser, 'Meas 25$MEASURE2', 25, 'medium', 'auto') #hash Meas 25$MEASURE2: 25;medium;auto
    wa.run_test_point_batch2(browser, 'Meas 26$MEASURE2', 26, 'medium', 1)      #hash Meas 26$MEASURE2: 26;medium;1
    wa.run_test_point_batch2(browser, 'Meas 27$MEASURE2', 27, 'medium', 6)      #hash Meas 27$MEASURE2: 27;medium;6
    wa.run_test_point_batch2(browser, 'Meas 28$MEASURE2', 28, 'high',   'auto') #hash Meas 28$MEASURE2: 28;high;auto
    wa.run_test_point_batch2(browser, 'Meas 29$MEASURE2', 29, 'high',   1)      #hash Meas 29$MEASURE2: 29;high;1
    wa.run_test_point_batch2(browser, 'Meas 30$MEASURE2', 30, 'high',   11)     #hash Meas 30$MEASURE2: 30;high;11
    #endregion

    Stage("\nMeasurements scenario (Batch 2) completed successfully!", "info")

except Exception as e:
    Stage(f"\nA critical error occurred: {e}", "error")

finally:
    if 'browser' in locals() and browser:
        #region Step 3: Close Browser (Batch 2)$CLOSE2
        Program('tree', 'set', 'select = Step 3: Close Browser (Batch 2)$CLOSE2')
        Stage("--- Step 3: Close Browser (Batch 2) ---")
        wa.close_browser(browser)
        #endregion
    MOSC.ScriptExecutionTime(StartTime)
    EndScript()
