from datetime import datetime
import RFSE
import MOSC

StartTime = datetime.now()

RFSE.Program('tree', 'set', 'select = Step 4: Save Report$REPORT')
RFSE.Stage("--- Step 4: Save Report ---")
if MOSC.hashStatus('Step 4: Save Report$REPORT'):
    try:
        RFSE.Program('control', 'set', 'save word report')
        RFSE.Stage("Word report generation command sent.")
        MOSC.hash_passed()
    except Exception as e:
        RFSE.Stage(f"Error during report generation: {e}", "error")
        MOSC.hash_failed()

MOSC.ScriptExecutionTime(StartTime)
RFSE.EndScript()
