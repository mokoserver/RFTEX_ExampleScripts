import RFSE
import MGPH

#Region Status
#hash Plugin set

RFSE.Messenger('set', 'Plugin - set.png', 'The current script will demonstrate the \'\'set\'\' command, '
                                          'which passes data to the plugin. '
                                          'This script will draw a line in the Graph plugin.')

#First Plot
name = "Plot 1"
ArrOy = [300, 300]
ArrOx = [0, 0.04]
LineWidth = "3"
Color = "FF00FF" #Magenta
Visible = "Yes"
MGPH.AddLine(name, ArrOy, ArrOx, LineWidth, Color, Visible)

RFSE.Program('tree', 'set', 'select = ' + 'Plugin set')
RFSE.Program('tree', 'set', 'chosen = passed')


RFSE.EndScript()
