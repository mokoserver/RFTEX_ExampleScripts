import os
import WebActions as wa
from RFSE import Stage, EndScript, Program, Report
from datetime import datetime
import MOSC

# --- COMMON SETTINGS ---
browser = None

# Fix script start time
StartTime = datetime.now()

try:
    #region Step 1: Initialize and Login (Batch 3)$INIT3
    Program('tree', 'set', 'select = Step 1: Initialize and Login (Batch 3)$INIT3')
    Stage("--- Step 1: Initialize and Login (Batch 3) ---")
    browser = wa.initialize_browser()
    wa.login_to_router(browser, "admin", "password123")
    #endregion

    #region Minimize Browser (Batch 3)$MIN3
    Program('tree', 'set', 'select = Minimize Browser (Batch 3)$MIN3')
    Stage("--- Minimize Browser (Batch 3) ---")
    wa.minimize_browser(browser)
    #endregion

    #region Step 2: Perform Measurements (Batch 3)$MEASURE3
    #description: Point ID;Power Level;Channel;
    Program('tree', 'set', 'select = Step 2: Perform Measurements (Batch 3)$MEASURE3')
    Stage("--- Step 2: Perform Measurements (Batch 3) ---")

    Report("WiFi Performance - Batch 3", 'info', 'table', "Point ID#100;Power Level#100;Channel#100;Transmit Power#100;Effective Rate#100")

    wa.run_test_point_batch3(browser, 'Meas 31$MEASURE3', 31, 'low',     'auto') #hash Meas 31$MEASURE3: 31;low;auto
    wa.run_test_point_batch3(browser, 'Meas 32$MEASURE3', 32, 'low',     1)      #hash Meas 32$MEASURE3: 32;low;1
    wa.run_test_point_batch3(browser, 'Meas 33$MEASURE3', 33, 'medium',  6)      #hash Meas 33$MEASURE3: 33;medium;6
    wa.run_test_point_batch3(browser, 'Meas 34$MEASURE3', 34, 'high',    11)     #hash Meas 34$MEASURE3: 34;high;11
    wa.run_test_point_batch3(browser, 'Meas 35$MEASURE3', 35, 'high',    'auto') #hash Meas 35$MEASURE3: 35;high;auto
    #endregion

    Stage("\nMeasurements scenario (Batch 3) completed successfully!", "info")

except Exception as e:
    Stage(f"\nA critical error occurred: {e}", "error")

finally:
    if 'browser' in locals() and browser:
        #region Step 3: Close Browser (Batch 3)$CLOSE3
        Program('tree', 'set', 'select = Step 3: Close Browser (Batch 3)$CLOSE3')
        Stage("--- Step 3: Close Browser (Batch 3) ---")
        wa.close_browser(browser)
        #endregion
    MOSC.ScriptExecutionTime(StartTime)
    EndScript()
