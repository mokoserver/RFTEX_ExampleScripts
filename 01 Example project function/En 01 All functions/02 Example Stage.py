import RFSE
from MOSC import stars
import time

RFSE.Stage(stars('*'))
RFSE.Stage(stars('NEW SCRIPT'))
RFSE.Stage(stars('*'))

RFSE.Stage('Welcome to RF-SE.')
RFSE.Stage('RF-SE manages RFSE NMEA program and driver software.')
RFSE.Stage('Program control is implemented through the execution of scripts written in Python.')
RFSE.Stage('This script shows how the Stage function works.')
RFSE.Stage('Stage messages can be of a specific type. Each of the types is presented below.')
RFSE.Stage('*Info*. Outputs any information to Stage. Designated as default type', 'Info')
RFSE.Stage('*Success*. Outputs any information to Stage. Designated as default type', 'Success')
RFSE.Stage('*Fail*. Outputs any information to Stage. Designated as default type', 'Fail')
RFSE.Stage('*Error*. Informs about an error that occurred during script execution.', 'Error')
RFSE.Stage('*Plugin*. Displays information related to a plugin.', 'Plugin')
RFSE.Stage('*Driver*. Displays information related to the driver.', 'Driver')
RFSE.Stage('*Report*. Informs about data recording in the report.', 'Report')
RFSE.Stage('*Utility*. Reports the use of the utility.', 'Utility')
RFSE.Stage('*Message*. Informs about the Messenger window display.', 'Message')
RFSE.Stage('*Telegram*. afafafaf', 'Telegram')
RFSE.Stage('*Warning*. Informs about an warning that occurred during script execution.', 'Warning')
time.sleep(6)
RFSE.Report("exstage", 'set', 'string', 'Absent')
RFSE.Report("exstage_1", 'set', 'string', 'The script completed successfully.')

RFSE.Stage(stars('*'))
RFSE.Stage(stars('NEXT SCRIPT'))
RFSE.Stage(stars('*'))

RFSE.EndScript()