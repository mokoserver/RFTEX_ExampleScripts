
from datetime import datetime
import RFSE
import MOSC

# Fix script start time
StartTime = datetime.now()

# Initialize execution time report table
MOSC.InitScriptExecutionTime()

RFSE.Stage("Welcome to the Web Browser Control Project")

# Report execution time at the end
MOSC.ScriptExecutionTime(StartTime)

RFSE.EndScript()
