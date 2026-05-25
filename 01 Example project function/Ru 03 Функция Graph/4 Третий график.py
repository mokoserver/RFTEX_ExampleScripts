import RFSE
import time
import numpy as np
import MGPH

def SinusGenerator(x,Ampl,freq,phase):

    sine = Ampl * np.sin(2 * np.pi * freq * x + phase)
    sine = list(sine)
    return sine

def Filling_the_Table(ArrOx,ArrOy,ArrOx1,ArrOy1):
    i = 0
    number = 8
    sin_with_diff_freq = ''
    while i < 100 + 1:
        if i % 50 == 0 and i > 0:
            RFSE.Report(f'Graph_{number}', 'set', 'table', sin_with_diff_freq)
            sin_with_diff_freq = ''
            number = number + 1

        if i < 100:
            sin_with_diff_freq = sin_with_diff_freq + f'{i + 1};{round(ArrOx[i], 2)};{round(ArrOy[i], 2)};' \
                                                    + f'{i + 1};{round(ArrOx1[i], 2)};{round(ArrOy1[i], 2)};' \
                                                    + '\\r'
        i = i + 1

MGPH.ClearGraph()

Value_OyOx = [-1.1,1.1,-0.01,1]
Name_Oy = "Amplitude"
Name_Ox = "Time"
Autoscale = "No"
MGPH.AddGraphSett(Value_OyOx, Name_Oy, Name_Ox, Autoscale)

#Region Status (статус)
#description: Frequency;(частота);Phase (фаза);Width (толщина);Color;(цвет);Visible;(видимость)

#First Plot
name = "Plot 7" #hash Sinus with frequency 4: 4;(4);0;2;Magenta;(пурпурный);Yes;(да)
RFSE.Report('Name25;Name27;Name29;Name31', 'set', 'strings', f'{name};{name};{name};{name}')
sampling_freq = 1000
start = 0
stop = 0.5
x = np.arange(start,stop,stop/sampling_freq)
freq = 4
Ampl = 1
ArrOy = SinusGenerator(x,Ampl,freq,0)
ArrOx = list(x)

LineWidth = "2"
Color = "FF00FF" #Magenta
Visible = "Yes"
MGPH.AddLine(name, ArrOy, ArrOx,LineWidth,Color,Visible)

RFSE.Program('tree', 'set', 'select = ' + 'Sinus with frequency 4')
RFSE.Program('tree', 'set', 'chosen = passed')

name = "Plot 8"     #hash Sinus with frequency 30:  30;(30);0;2;DarkTurquoise;(темно-голубой);Yes;(да)
RFSE.Report('Name26;Name28;Name30;Name32', 'set', 'strings', f'{name};{name};{name};{name}')
start = 0
stop = 0.5
x = np.arange(start,stop,stop/sampling_freq)
freq = 30
Ampl = 1
ArrOy1 = SinusGenerator(x,Ampl,freq,0)
start = 0.5
stop = 1.0
x = np.arange(start,stop,stop/sampling_freq)
ArrOx1 = list(x)

LineWidth = "2"
Color = "00CED1" #DarkTurquoise
Visible = "Yes"
MGPH.AddLine(name, ArrOy1, ArrOx1,LineWidth,Color,Visible)

RFSE.Program('tree', 'set', 'select = ' + 'Sinus with frequency 30')
RFSE.Program('tree', 'set', 'chosen = passed')
#EndRegion Status

Filling_the_Table(ArrOx,ArrOy,ArrOx1,ArrOy1)

screen = MGPH.GetScreenshotWindow()
RFSE.Report("Screenshot_3_All", 'set', 'picture', screen)
screen = MGPH.GetScreenshotGraph()
RFSE.Report("Screenshot_3_Graph", 'set', 'picture', screen)

time.sleep(3)
MGPH.ClearGraph()

RFSE.EndScript()