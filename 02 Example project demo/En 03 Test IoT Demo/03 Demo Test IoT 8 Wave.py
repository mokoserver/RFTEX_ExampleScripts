import RFSE
from MOSC import hashStatus, hash_passed, hash_failed
from SettingsAndMeasurement import Testing
import MTLG
MTLG.TelegramProgram('alpha', 'Measurement script', 'set', 'init')
RFSE.Stage("*********************************************************")
RFSE.Stage("****************** Measurement script *******************")
RFSE.Stage("*********************************************************")
RFSE.Stage(" ")
RFSE.Stage("*********************************************************")
RFSE.Stage('**************** Null flags of system ****************')
RFSE.Stage("*********************************************************")
RFSE.Stage(" ")
Testing.LoadTablesHeadInfo(number_wave=8)

def VDC(
        value: (str | float | int),
        value_limit: (str | float | int),
        percent_error: (float | int),
        wave: str,
        amplitude: (str | float | int),
        amplitude_limit: int,
        frequency: (str | float | int),
        hash: str,
        remeasurement: bool = False,
        remeasurement_number: int = 0,
        time_delay: (float | int) = 0.0

) -> None:

    if hashStatus(hash):

        Testing.CheckConnectDevices()

        Testing.CheckWireConnection(WireConnection='VDC')

        Testing.BK1697B.SET_OUTPUT_ON()
        Testing.CheckGraphInit()
        Testing.CreateGraphMask(value_limit=value_limit)

        Testing.TimeDelay = time_delay
        Testing.Remeasurement = remeasurement
        Testing.RemeasurementNumber = remeasurement_number

        Testing.VDC_Measurement(value=value, value_limit=value_limit, wave=wave, percent_error=percent_error,
                                amplitude=amplitude, amplitude_limit=amplitude_limit, frequency=frequency,
                                hash=hash)
        Testing.CreateGraph()

        if Testing.Status == 'Failed':
            hash_failed()
        else:
            hash_passed()


def IDC(
        value: (str | float | int),
        value_limit: (str | float | int),
        percent_error: (float | int),
        wave: str,
        amplitude: (str | float | int),
        amplitude_limit: int,
        frequency: (str | float | int),
        hash: str,
        remeasurement: bool = False,
        remeasurement_number: int = 0,
        time_delay: (int, float) = 0.0

) -> None:

    if hashStatus(hash):

        Testing.CheckConnectDevices()

        Testing.CheckWireConnection(WireConnection='IDC')

        Testing.BK1697B.SET_OUTPUT_ON()
        Testing.CheckGraphInit()
        Testing.CreateGraphMask(value_limit=value_limit)

        Testing.TimeDelay = time_delay
        Testing.Remeasurement = remeasurement
        Testing.RemeasurementNumber = remeasurement_number

        Testing.IDC_MEASUREMENT(value=value, value_limit=value_limit, wave=wave, percent_error=percent_error,
                                amplitude=amplitude, amplitude_limit=amplitude_limit, frequency=frequency,
                                hash=hash)
        Testing.CreateGraph()

        if Testing.Status == 'Failed':
            hash_failed()
        else:
            hash_passed()

#region Voltage measurement with generator signal sin$VDC_SIN
#description: value \nmeasurement, V;value limit, V;percentage of \nallowed error, %;wave amplitude;amplitude, V;amplitude\nlimit, V;frequency, Hz;delay time \nbefore \nmeasurement, s;remeasure,\nTrue or False;number of \nremeasurements;
RFSE.Program('tree', 'set', 'select = Voltage measurement with generator signal sin$VDC_SIN')

RFSE.Stage('Set NameGraph => VDC_SIN_GRAPH')
Testing.NameGraph = 'VDC_SIN_GRAPH'
RFSE.Stage(" ")

VDC(value=1,   value_limit=40, percent_error=70, wave='sin',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=3.00, remeasurement=True, remeasurement_number=3, hash='Meas 1$VDC_SIN')  #hash Meas 1$VDC_SIN:   1  ;40  ;70  ;sin ;1  ;10  ;10k  ;3.000  ;True  ;3
VDC(value=2,   value_limit=40, percent_error=30, wave='sin',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 2$VDC_SIN')  #hash Meas 2$VDC_SIN:   2  ;40  ;30  ;sin ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=3,   value_limit=40, percent_error=20, wave='sin',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 3$VDC_SIN')  #hash Meas 3$VDC_SIN:   3  ;40  ;20  ;sin ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=4,   value_limit=40, percent_error=20, wave='sin',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 4$VDC_SIN')  #hash Meas 4$VDC_SIN:   4  ;40  ;20  ;sin ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=5,   value_limit=40, percent_error=20, wave='sin',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 5$VDC_SIN')  #hash Meas 5$VDC_SIN:   5  ;40  ;20  ;sin ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=6,   value_limit=40, percent_error=20, wave='sin',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 6$VDC_SIN')  #hash Meas 6$VDC_SIN:   6  ;40  ;20  ;sin ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=8,   value_limit=40, percent_error=20, wave='sin',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 7$VDC_SIN')  #hash Meas 7$VDC_SIN:   8  ;40  ;20  ;sin ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=10,  value_limit=40, percent_error=20, wave='sin',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 8$VDC_SIN')  #hash Meas 8$VDC_SIN:   10 ;40  ;20  ;sin ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=12,  value_limit=40, percent_error=20, wave='sin',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 9$VDC_SIN')  #hash Meas 9$VDC_SIN:   12 ;40  ;20  ;sin ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=14,  value_limit=40, percent_error=20, wave='sin',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 10$VDC_SIN') #hash Meas 10$VDC_SIN:  14 ;40  ;20  ;sin ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=16,  value_limit=40, percent_error=20, wave='sin',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 11$VDC_SIN') #hash Meas 11$VDC_SIN:  16 ;40  ;20  ;sin ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=18,  value_limit=40, percent_error=20, wave='sin',  amplitude=2, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 12$VDC_SIN') #hash Meas 12$VDC_SIN:  18 ;40  ;20  ;sin ;2  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=20,  value_limit=40, percent_error=20, wave='sin',  amplitude=2, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 13$VDC_SIN') #hash Meas 13$VDC_SIN:  20 ;40  ;20  ;sin ;2  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=22,  value_limit=40, percent_error=20, wave='sin',  amplitude=2, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 14$VDC_SIN') #hash Meas 14$VDC_SIN:  22 ;40  ;20  ;sin ;2  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=25,  value_limit=40, percent_error=20, wave='sin',  amplitude=3, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 15$VDC_SIN') #hash Meas 15$VDC_SIN:  25 ;40  ;20  ;sin ;3  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=28,  value_limit=40, percent_error=20, wave='sin',  amplitude=3, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 16$VDC_SIN') #hash Meas 16$VDC_SIN:  28 ;40  ;20  ;sin ;3  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=31,  value_limit=40, percent_error=20, wave='sin',  amplitude=4, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 17$VDC_SIN') #hash Meas 17$VDC_SIN:  31 ;40  ;20  ;sin ;4  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=34,  value_limit=40, percent_error=20, wave='sin',  amplitude=5, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 18$VDC_SIN') #hash Meas 18$VDC_SIN:  34 ;40  ;20  ;sin ;5  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=37,  value_limit=40, percent_error=20, wave='sin',  amplitude=5, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 19$VDC_SIN') #hash Meas 19$VDC_SIN:  37 ;40  ;20  ;sin ;5  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=40,  value_limit=40, percent_error=20, wave='sin',  amplitude=5, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 20$VDC_SIN') #hash Meas 20$VDC_SIN:  40 ;40  ;20  ;sin ;5  ;10  ;10k  ;1.500  ;True  ;3

Testing.GetScreenshot()
Testing.BK1697B.SET_OUTPUT_OFF()
#endregion Voltage measurement with generator signal sin$VDC_SIN


#region Voltage measurement with generator signal square$VDC_SQUARE
#description: value \nmeasurement, V;value limit, V;percentage of \nallowed error, %;wave amplitude;amplitude, V;amplitude\nlimit, V;frequency, Hz;delay time \nbefore \nmeasurement, s;remeasure,\nTrue or False;number of \nremeasurements;
RFSE.Program('tree', 'set', 'select = Voltage measurement with generator signal square$VDC_SQUARE')

RFSE.Stage('Set NameGraph => VDC_SQUARE_GRAPH')
Testing.NameGraph = 'VDC_SQUARE_GRAPH'

VDC(value=1,   value_limit=40, percent_error=70, wave='square',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=3.00, remeasurement=True, remeasurement_number=3, hash='Meas 1$VDC_SQUARE')  #hash Meas 1$VDC_SQUARE:   1  ;40  ;70  ;square ;1  ;10  ;10k  ;3.000  ;True  ;3
VDC(value=2,   value_limit=40, percent_error=30, wave='square',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 2$VDC_SQUARE')  #hash Meas 2$VDC_SQUARE:   2  ;40  ;30  ;square ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=3,   value_limit=40, percent_error=20, wave='square',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 3$VDC_SQUARE')  #hash Meas 3$VDC_SQUARE:   3  ;40  ;20  ;square ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=4,   value_limit=40, percent_error=20, wave='square',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 4$VDC_SQUARE')  #hash Meas 4$VDC_SQUARE:   4  ;40  ;20  ;square ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=5,   value_limit=40, percent_error=20, wave='square',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 5$VDC_SQUARE')  #hash Meas 5$VDC_SQUARE:   5  ;40  ;20  ;square ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=6,   value_limit=40, percent_error=20, wave='square',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 6$VDC_SQUARE')  #hash Meas 6$VDC_SQUARE:   6  ;40  ;20  ;square ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=8,   value_limit=40, percent_error=20, wave='square',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 7$VDC_SQUARE')  #hash Meas 7$VDC_SQUARE:   8  ;40  ;20  ;square ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=10,  value_limit=40, percent_error=20, wave='square',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 8$VDC_SQUARE')  #hash Meas 8$VDC_SQUARE:   10 ;40  ;20  ;square ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=12,  value_limit=40, percent_error=20, wave='square',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 9$VDC_SQUARE')  #hash Meas 9$VDC_SQUARE:   12 ;40  ;20  ;square ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=14,  value_limit=40, percent_error=20, wave='square',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 10$VDC_SQUARE') #hash Meas 10$VDC_SQUARE:  14 ;40  ;20  ;square ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=16,  value_limit=40, percent_error=20, wave='square',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 11$VDC_SQUARE') #hash Meas 11$VDC_SQUARE:  16 ;40  ;20  ;square ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=18,  value_limit=40, percent_error=20, wave='square',  amplitude=2, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 12$VDC_SQUARE') #hash Meas 12$VDC_SQUARE:  18 ;40  ;20  ;square ;2  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=20,  value_limit=40, percent_error=20, wave='square',  amplitude=2, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 13$VDC_SQUARE') #hash Meas 13$VDC_SQUARE:  20 ;40  ;20  ;square ;2  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=22,  value_limit=40, percent_error=20, wave='square',  amplitude=2, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 14$VDC_SQUARE') #hash Meas 14$VDC_SQUARE:  22 ;40  ;20  ;square ;2  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=25,  value_limit=40, percent_error=20, wave='square',  amplitude=3, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 15$VDC_SQUARE') #hash Meas 15$VDC_SQUARE:  25 ;40  ;20  ;square ;3  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=28,  value_limit=40, percent_error=20, wave='square',  amplitude=3, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 16$VDC_SQUARE') #hash Meas 16$VDC_SQUARE:  28 ;40  ;20  ;square ;3  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=31,  value_limit=40, percent_error=20, wave='square',  amplitude=4, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 17$VDC_SQUARE') #hash Meas 17$VDC_SQUARE:  31 ;40  ;20  ;square ;4  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=34,  value_limit=40, percent_error=20, wave='square',  amplitude=5, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 18$VDC_SQUARE') #hash Meas 18$VDC_SQUARE:  34 ;40  ;20  ;square ;5  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=37,  value_limit=40, percent_error=20, wave='square',  amplitude=5, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 19$VDC_SQUARE') #hash Meas 19$VDC_SQUARE:  37 ;40  ;20  ;square ;5  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=40,  value_limit=40, percent_error=20, wave='square',  amplitude=5, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 20$VDC_SQUARE') #hash Meas 20$VDC_SQUARE:  40 ;40  ;20  ;square ;5  ;10  ;10k  ;1.500  ;True  ;3

Testing.GetScreenshot()
Testing.BK1697B.SET_OUTPUT_OFF()
#endregion Voltage measurement with generator signal square$VDC_SQUARE


#region Voltage measurement with generator signal rectangle$VDC_RECTANGLE
#description: value \nmeasurement, V;value limit, V;percentage of \nallowed error, %;wave amplitude;amplitude, V;amplitude\nlimit, V;frequency, Hz;delay time \nbefore \nmeasurement, s;remeasure,\nTrue or False;number of \nremeasurements;
RFSE.Program('tree', 'set', 'select = Voltage measurement with generator signal rectangle$VDC_RECTANGLE')

RFSE.Stage('Set NameGraph => VDC_RECTANGLE_GRAPH')
Testing.NameGraph = 'VDC_RECTANGLE_GRAPH'

VDC(value=1,   value_limit=40, percent_error=70, wave='rectangle',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=3.00, remeasurement=True, remeasurement_number=3, hash='Meas 1$VDC_RECTANGLE')  #hash Meas 1$VDC_RECTANGLE:   1  ;40  ;70  ;rectangle ;1  ;10  ;10k  ;3.000  ;True  ;3
VDC(value=2,   value_limit=40, percent_error=30, wave='rectangle',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 2$VDC_RECTANGLE')  #hash Meas 2$VDC_RECTANGLE:   2  ;40  ;30  ;rectangle ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=3,   value_limit=40, percent_error=20, wave='rectangle',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 3$VDC_RECTANGLE')  #hash Meas 3$VDC_RECTANGLE:   3  ;40  ;20  ;rectangle ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=4,   value_limit=40, percent_error=20, wave='rectangle',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 4$VDC_RECTANGLE')  #hash Meas 4$VDC_RECTANGLE:   4  ;40  ;20  ;rectangle ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=5,   value_limit=40, percent_error=20, wave='rectangle',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 5$VDC_RECTANGLE')  #hash Meas 5$VDC_RECTANGLE:   5  ;40  ;20  ;rectangle ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=6,   value_limit=40, percent_error=20, wave='rectangle',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 6$VDC_RECTANGLE')  #hash Meas 6$VDC_RECTANGLE:   6  ;40  ;20  ;rectangle ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=8,   value_limit=40, percent_error=20, wave='rectangle',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 7$VDC_RECTANGLE')  #hash Meas 7$VDC_RECTANGLE:   8  ;40  ;20  ;rectangle ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=10,  value_limit=40, percent_error=20, wave='rectangle',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 8$VDC_RECTANGLE')  #hash Meas 8$VDC_RECTANGLE:   10 ;40  ;20  ;rectangle ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=12,  value_limit=40, percent_error=20, wave='rectangle',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 9$VDC_RECTANGLE')  #hash Meas 9$VDC_RECTANGLE:   12 ;40  ;20  ;rectangle ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=14,  value_limit=40, percent_error=20, wave='rectangle',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 10$VDC_RECTANGLE') #hash Meas 10$VDC_RECTANGLE:  14 ;40  ;20  ;rectangle ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=16,  value_limit=40, percent_error=20, wave='rectangle',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 11$VDC_RECTANGLE') #hash Meas 11$VDC_RECTANGLE:  16 ;40  ;20  ;rectangle ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=18,  value_limit=40, percent_error=20, wave='rectangle',  amplitude=2, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 12$VDC_RECTANGLE') #hash Meas 12$VDC_RECTANGLE:  18 ;40  ;20  ;rectangle ;2  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=20,  value_limit=40, percent_error=20, wave='rectangle',  amplitude=2, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 13$VDC_RECTANGLE') #hash Meas 13$VDC_RECTANGLE:  20 ;40  ;20  ;rectangle ;2  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=22,  value_limit=40, percent_error=20, wave='rectangle',  amplitude=2, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 14$VDC_RECTANGLE') #hash Meas 14$VDC_RECTANGLE:  22 ;40  ;20  ;rectangle ;2  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=25,  value_limit=40, percent_error=20, wave='rectangle',  amplitude=3, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 15$VDC_RECTANGLE') #hash Meas 15$VDC_RECTANGLE:  25 ;40  ;20  ;rectangle ;3  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=28,  value_limit=40, percent_error=20, wave='rectangle',  amplitude=3, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 16$VDC_RECTANGLE') #hash Meas 16$VDC_RECTANGLE:  28 ;40  ;20  ;rectangle ;3  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=31,  value_limit=40, percent_error=20, wave='rectangle',  amplitude=4, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 17$VDC_RECTANGLE') #hash Meas 17$VDC_RECTANGLE:  31 ;40  ;20  ;rectangle ;4  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=34,  value_limit=40, percent_error=20, wave='rectangle',  amplitude=5, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 18$VDC_RECTANGLE') #hash Meas 18$VDC_RECTANGLE:  34 ;40  ;20  ;rectangle ;5  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=37,  value_limit=40, percent_error=20, wave='rectangle',  amplitude=5, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 19$VDC_RECTANGLE') #hash Meas 19$VDC_RECTANGLE:  37 ;40  ;20  ;rectangle ;5  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=40,  value_limit=40, percent_error=20, wave='rectangle',  amplitude=5, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 20$VDC_RECTANGLE') #hash Meas 20$VDC_RECTANGLE:  40 ;40  ;20  ;rectangle ;5  ;10  ;10k  ;1.500  ;True  ;3

Testing.GetScreenshot()
Testing.BK1697B.SET_OUTPUT_OFF()
#endregion Voltage measurement with generator signal rectangle$VDC_RECTANGLE


#region Voltage measurement with generator signal trapezoid$VDC_TRAPEZOID
#description: value \nmeasurement, V;value limit, V;percentage of \nallowed error, %;wave amplitude;amplitude, V;amplitude\nlimit, V;frequency, Hz;delay time \nbefore \nmeasurement, s;remeasure,\nTrue or False;number of \nremeasurements;
RFSE.Program('tree', 'set', 'select = Voltage measurement with generator signal trapezoid$VDC_TRAPEZOID')

RFSE.Stage('Set NameGraph => VDC_TRAPEZOID_GRAPH')
Testing.NameGraph = 'VDC_TRAPEZOID_GRAPH'

VDC(value=1,   value_limit=40, percent_error=70, wave='trapezoid',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=3.00, remeasurement=True, remeasurement_number=3, hash='Meas 1$VDC_TRAPEZOID')  #hash Meas 1$VDC_TRAPEZOID:   1  ;40  ;70  ;trapezoid ;1  ;10  ;10k  ;3.000  ;True  ;3
VDC(value=2,   value_limit=40, percent_error=30, wave='trapezoid',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 2$VDC_TRAPEZOID')  #hash Meas 2$VDC_TRAPEZOID:   2  ;40  ;30  ;trapezoid ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=3,   value_limit=40, percent_error=20, wave='trapezoid',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 3$VDC_TRAPEZOID')  #hash Meas 3$VDC_TRAPEZOID:   3  ;40  ;20  ;trapezoid ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=4,   value_limit=40, percent_error=20, wave='trapezoid',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 4$VDC_TRAPEZOID')  #hash Meas 4$VDC_TRAPEZOID:   4  ;40  ;20  ;trapezoid ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=5,   value_limit=40, percent_error=20, wave='trapezoid',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 5$VDC_TRAPEZOID')  #hash Meas 5$VDC_TRAPEZOID:   5  ;40  ;20  ;trapezoid ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=6,   value_limit=40, percent_error=20, wave='trapezoid',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 6$VDC_TRAPEZOID')  #hash Meas 6$VDC_TRAPEZOID:   6  ;40  ;20  ;trapezoid ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=8,   value_limit=40, percent_error=20, wave='trapezoid',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 7$VDC_TRAPEZOID')  #hash Meas 7$VDC_TRAPEZOID:   8  ;40  ;20  ;trapezoid ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=10,  value_limit=40, percent_error=20, wave='trapezoid',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 8$VDC_TRAPEZOID')  #hash Meas 8$VDC_TRAPEZOID:   10 ;40  ;20  ;trapezoid ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=12,  value_limit=40, percent_error=20, wave='trapezoid',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 9$VDC_TRAPEZOID')  #hash Meas 9$VDC_TRAPEZOID:   12 ;40  ;20  ;trapezoid ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=14,  value_limit=40, percent_error=20, wave='trapezoid',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 10$VDC_TRAPEZOID') #hash Meas 10$VDC_TRAPEZOID:  14 ;40  ;20  ;trapezoid ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=16,  value_limit=40, percent_error=20, wave='trapezoid',  amplitude=1, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 11$VDC_TRAPEZOID') #hash Meas 11$VDC_TRAPEZOID:  16 ;40  ;20  ;trapezoid ;1  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=18,  value_limit=40, percent_error=20, wave='trapezoid',  amplitude=2, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 12$VDC_TRAPEZOID') #hash Meas 12$VDC_TRAPEZOID:  18 ;40  ;20  ;trapezoid ;2  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=20,  value_limit=40, percent_error=20, wave='trapezoid',  amplitude=2, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 13$VDC_TRAPEZOID') #hash Meas 13$VDC_TRAPEZOID:  20 ;40  ;20  ;trapezoid ;2  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=22,  value_limit=40, percent_error=20, wave='trapezoid',  amplitude=2, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 14$VDC_TRAPEZOID') #hash Meas 14$VDC_TRAPEZOID:  22 ;40  ;20  ;trapezoid ;2  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=25,  value_limit=40, percent_error=20, wave='trapezoid',  amplitude=3, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 15$VDC_TRAPEZOID') #hash Meas 15$VDC_TRAPEZOID:  25 ;40  ;20  ;trapezoid ;3  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=28,  value_limit=40, percent_error=20, wave='trapezoid',  amplitude=3, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 16$VDC_TRAPEZOID') #hash Meas 16$VDC_TRAPEZOID:  28 ;40  ;20  ;trapezoid ;3  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=31,  value_limit=40, percent_error=20, wave='trapezoid',  amplitude=4, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 17$VDC_TRAPEZOID') #hash Meas 17$VDC_TRAPEZOID:  31 ;40  ;20  ;trapezoid ;4  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=34,  value_limit=40, percent_error=20, wave='trapezoid',  amplitude=5, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 18$VDC_TRAPEZOID') #hash Meas 18$VDC_TRAPEZOID:  34 ;40  ;20  ;trapezoid ;5  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=37,  value_limit=40, percent_error=20, wave='trapezoid',  amplitude=5, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 19$VDC_TRAPEZOID') #hash Meas 19$VDC_TRAPEZOID:  37 ;40  ;20  ;trapezoid ;5  ;10  ;10k  ;1.500  ;True  ;3
VDC(value=40,  value_limit=40, percent_error=20, wave='trapezoid',  amplitude=5, amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 20$VDC_TRAPEZOID') #hash Meas 20$VDC_TRAPEZOID:  40 ;40  ;20  ;trapezoid ;5  ;10  ;10k  ;1.500  ;True  ;3

Testing.GetScreenshot()
Testing.BK1697B.SET_OUTPUT_OFF()
#endregion Voltage measurement with generator signal trapezoid$VDC_TRAPEZOID


#region Current measurement with generator signal CMOS$IDC_CMOS
#description: value \nmeasurement, A;value limit, A;percentage of \nallowed error, %;wave amplitude;amplitude, A;amplitude\nlimit, A;frequency, Hz;delay time \nbefore \nmeasurement, s;remeasure,\nTrue or False;number of \nremeasurements;
RFSE.Program('tree', 'set', 'select = Current measurement with generator signal CMOS$IDC_CMOS')

RFSE.Stage('Set NameGraph => IDC_CMOS_GRAPH')
Testing.NameGraph = 'IDC_CMOS_GRAPH'

IDC(value=0.01, value_limit=5, percent_error=220, wave='CMOS', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=3.00, remeasurement=True, remeasurement_number=3, hash='Meas 1$IDC_CMOS')   #hash Meas 1$IDC_CMOS:  0.01 ;5  ;250 ;CMOS ;1  ;10  ;10k  ;3.000  ;True  ;3
IDC(value=0.03, value_limit=5, percent_error=110, wave='CMOS', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 2$IDC_CMOS')   #hash Meas 2$IDC_CMOS:  0.03 ;5  ;110 ;CMOS ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.05, value_limit=5, percent_error=55,  wave='CMOS', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 3$IDC_CMOS')   #hash Meas 3$IDC_CMOS:  0.05 ;5  ;55  ;CMOS ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.1,  value_limit=5, percent_error=35,  wave='CMOS', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 4$IDC_CMOS')   #hash Meas 4$IDC_CMOS:  0.1  ;5  ;35  ;CMOS ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.15, value_limit=5, percent_error=20,  wave='CMOS', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 5$IDC_CMOS')   #hash Meas 5$IDC_CMOS:  0.15 ;5  ;20  ;CMOS ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.2,  value_limit=5, percent_error=20,  wave='CMOS', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 6$IDC_CMOS')   #hash Meas 6$IDC_CMOS:  0.2  ;5  ;20  ;CMOS ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.25, value_limit=5, percent_error=20,  wave='CMOS', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 7$IDC_CMOS')   #hash Meas 7$IDC_CMOS:  0.25 ;5  ;20  ;CMOS ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.3,  value_limit=5, percent_error=20,  wave='CMOS', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 8$IDC_CMOS')   #hash Meas 8$IDC_CMOS:  0.3  ;5  ;20  ;CMOS ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.4,  value_limit=5, percent_error=20,  wave='CMOS', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 9$IDC_CMOS')   #hash Meas 9$IDC_CMOS:  0.4  ;5  ;20  ;CMOS ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.5,  value_limit=5, percent_error=20,  wave='CMOS', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 10$IDC_CMOS')  #hash Meas 10$IDC_CMOS: 0.5  ;5  ;20  ;CMOS ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.6,  value_limit=5, percent_error=20,  wave='CMOS', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 11$IDC_CMOS')  #hash Meas 11$IDC_CMOS: 0.6  ;5  ;20  ;CMOS ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.8,  value_limit=5, percent_error=20,  wave='CMOS', amplitude=2,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 12$IDC_CMOS')  #hash Meas 12$IDC_CMOS: 0.8  ;5  ;20  ;CMOS ;2  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=1,    value_limit=5, percent_error=20,  wave='CMOS', amplitude=2,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 13$IDC_CMOS')  #hash Meas 13$IDC_CMOS: 1    ;5  ;20  ;CMOS ;2  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=1.2,  value_limit=5, percent_error=20,  wave='CMOS', amplitude=2,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 14$IDC_CMOS')  #hash Meas 14$IDC_CMOS: 1.2  ;5  ;20  ;CMOS ;2  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=1.5,  value_limit=5, percent_error=20,  wave='CMOS', amplitude=3,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 15$IDC_CMOS')  #hash Meas 15$IDC_CMOS: 1.5  ;5  ;20  ;CMOS ;3  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=2,    value_limit=5, percent_error=20,  wave='CMOS', amplitude=3,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 16$IDC_CMOS')  #hash Meas 16$IDC_CMOS: 2    ;5  ;20  ;CMOS ;3  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=2.5,  value_limit=5, percent_error=20,  wave='CMOS', amplitude=4,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 17$IDC_CMOS')  #hash Meas 17$IDC_CMOS: 2.5  ;5  ;20  ;CMOS ;4  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=3,    value_limit=5, percent_error=20,  wave='CMOS', amplitude=5,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 18$IDC_CMOS')  #hash Meas 18$IDC_CMOS: 3    ;5  ;20  ;CMOS ;5  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=4,    value_limit=5, percent_error=20,  wave='CMOS', amplitude=5,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 19$IDC_CMOS')  #hash Meas 19$IDC_CMOS: 4    ;5  ;20  ;CMOS ;5  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=5,    value_limit=5, percent_error=20,  wave='CMOS', amplitude=5,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 20$IDC_CMOS')  #hash Meas 20$IDC_CMOS: 5    ;5  ;20  ;CMOS ;5  ;10  ;10k  ;1.500  ;True  ;3

Testing.GetScreenshot()
Testing.BK1697B.SET_OUTPUT_OFF()
#endregion Current measurement with generator signal CMOS$IDC_CMOS


#region Current measurement with generator signal pulse$IDC_PULSE
#description: value \nmeasurement, A;value limit, A;percentage of \nallowed error, %;wave amplitude;amplitude, A;amplitude\nlimit, A;frequency, Hz;delay time \nbefore \nmeasurement, s;remeasure,\nTrue or False;number of \nremeasurements;
RFSE.Program('tree', 'set', 'select = Current measurement with generator signal pulse$IDC_PULSE')

RFSE.Stage('Set NameGraph => IDC_PULSE_GRAPH')
Testing.NameGraph = 'IDC_PULSE_GRAPH'

IDC(value=0.01, value_limit=5, percent_error=220, wave='pulse', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=3.00, remeasurement=True, remeasurement_number=3, hash='Meas 1$IDC_PULSE')   #hash Meas 1$IDC_PULSE:  0.01 ;5  ;250 ;pulse ;1  ;10  ;10k  ;3.000  ;True  ;3
IDC(value=0.03, value_limit=5, percent_error=110, wave='pulse', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 2$IDC_PULSE')   #hash Meas 2$IDC_PULSE:  0.03 ;5  ;110 ;pulse ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.05, value_limit=5, percent_error=55,  wave='pulse', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 3$IDC_PULSE')   #hash Meas 3$IDC_PULSE:  0.05 ;5  ;55  ;pulse ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.1,  value_limit=5, percent_error=35,  wave='pulse', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 4$IDC_PULSE')   #hash Meas 4$IDC_PULSE:  0.1  ;5  ;35  ;pulse ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.15, value_limit=5, percent_error=20,  wave='pulse', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 5$IDC_PULSE')   #hash Meas 5$IDC_PULSE:  0.15 ;5  ;20  ;pulse ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.2,  value_limit=5, percent_error=20,  wave='pulse', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 6$IDC_PULSE')   #hash Meas 6$IDC_PULSE:  0.2  ;5  ;20  ;pulse ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.25, value_limit=5, percent_error=20,  wave='pulse', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 7$IDC_PULSE')   #hash Meas 7$IDC_PULSE:  0.25 ;5  ;20  ;pulse ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.3,  value_limit=5, percent_error=20,  wave='pulse', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 8$IDC_PULSE')   #hash Meas 8$IDC_PULSE:  0.3  ;5  ;20  ;pulse ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.4,  value_limit=5, percent_error=20,  wave='pulse', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 9$IDC_PULSE')   #hash Meas 9$IDC_PULSE:  0.4  ;5  ;20  ;pulse ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.5,  value_limit=5, percent_error=20,  wave='pulse', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 10$IDC_PULSE')  #hash Meas 10$IDC_PULSE: 0.5  ;5  ;20  ;pulse ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.6,  value_limit=5, percent_error=20,  wave='pulse', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 11$IDC_PULSE')  #hash Meas 11$IDC_PULSE: 0.6  ;5  ;20  ;pulse ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.8,  value_limit=5, percent_error=20,  wave='pulse', amplitude=2,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 12$IDC_PULSE')  #hash Meas 12$IDC_PULSE: 0.8  ;5  ;20  ;pulse ;2  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=1,    value_limit=5, percent_error=20,  wave='pulse', amplitude=2,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 13$IDC_PULSE')  #hash Meas 13$IDC_PULSE: 1    ;5  ;20  ;pulse ;2  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=1.2,  value_limit=5, percent_error=20,  wave='pulse', amplitude=2,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 14$IDC_PULSE')  #hash Meas 14$IDC_PULSE: 1.2  ;5  ;20  ;pulse ;2  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=1.5,  value_limit=5, percent_error=20,  wave='pulse', amplitude=3,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 15$IDC_PULSE')  #hash Meas 15$IDC_PULSE: 1.5  ;5  ;20  ;pulse ;3  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=2,    value_limit=5, percent_error=20,  wave='pulse', amplitude=3,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 16$IDC_PULSE')  #hash Meas 16$IDC_PULSE: 2    ;5  ;20  ;pulse ;3  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=2.5,  value_limit=5, percent_error=20,  wave='pulse', amplitude=4,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 17$IDC_PULSE')  #hash Meas 17$IDC_PULSE: 2.5  ;5  ;20  ;pulse ;4  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=3,    value_limit=5, percent_error=20,  wave='pulse', amplitude=5,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 18$IDC_PULSE')  #hash Meas 18$IDC_PULSE: 3    ;5  ;20  ;pulse ;5  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=4,    value_limit=5, percent_error=20,  wave='pulse', amplitude=5,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 19$IDC_PULSE')  #hash Meas 19$IDC_PULSE: 4    ;5  ;20  ;pulse ;5  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=5,    value_limit=5, percent_error=20,  wave='pulse', amplitude=5,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 20$IDC_PULSE')  #hash Meas 20$IDC_PULSE: 5    ;5  ;20  ;pulse ;5  ;10  ;10k  ;1.500  ;True  ;3

Testing.GetScreenshot()
Testing.BK1697B.SET_OUTPUT_OFF()
#endregion Current measurement with generator signal pulse$IDC_PULSE


#region Current measurement with generator signal ramp$IDC_RAMP
#description: value \nmeasurement, A;value limit, A;percentage of \nallowed error, %;wave amplitude;amplitude, A;amplitude\nlimit, A;frequency, Hz;delay time \nbefore \nmeasurement, s;remeasure,\nTrue or False;number of \nremeasurements;
RFSE.Program('tree', 'set', 'select = Current measurement with generator signal ramp$IDC_RAMP')

RFSE.Stage('Set NameGraph => IDC_RAMP_GRAPH')
Testing.NameGraph = 'IDC_RAMP_GRAPH'

IDC(value=0.01, value_limit=5, percent_error=220, wave='ramp', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=3.00, remeasurement=True, remeasurement_number=3, hash='Meas 1$IDC_RAMP')   #hash Meas 1$IDC_RAMP:  0.01 ;5  ;250 ;ramp ;1  ;10  ;10k  ;3.000  ;True  ;3
IDC(value=0.03, value_limit=5, percent_error=110, wave='ramp', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 2$IDC_RAMP')   #hash Meas 2$IDC_RAMP:  0.03 ;5  ;110 ;ramp ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.05, value_limit=5, percent_error=55,  wave='ramp', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 3$IDC_RAMP')   #hash Meas 3$IDC_RAMP:  0.05 ;5  ;55  ;ramp ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.1,  value_limit=5, percent_error=35,  wave='ramp', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 4$IDC_RAMP')   #hash Meas 4$IDC_RAMP:  0.1  ;5  ;35  ;ramp ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.15, value_limit=5, percent_error=20,  wave='ramp', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 5$IDC_RAMP')   #hash Meas 5$IDC_RAMP:  0.15 ;5  ;20  ;ramp ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.2,  value_limit=5, percent_error=20,  wave='ramp', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 6$IDC_RAMP')   #hash Meas 6$IDC_RAMP:  0.2  ;5  ;20  ;ramp ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.25, value_limit=5, percent_error=20,  wave='ramp', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 7$IDC_RAMP')   #hash Meas 7$IDC_RAMP:  0.25 ;5  ;20  ;ramp ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.3,  value_limit=5, percent_error=20,  wave='ramp', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 8$IDC_RAMP')   #hash Meas 8$IDC_RAMP:  0.3  ;5  ;20  ;ramp ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.4,  value_limit=5, percent_error=20,  wave='ramp', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 9$IDC_RAMP')   #hash Meas 9$IDC_RAMP:  0.4  ;5  ;20  ;ramp ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.5,  value_limit=5, percent_error=20,  wave='ramp', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 10$IDC_RAMP')  #hash Meas 10$IDC_RAMP: 0.5  ;5  ;20  ;ramp ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.6,  value_limit=5, percent_error=20,  wave='ramp', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 11$IDC_RAMP')  #hash Meas 11$IDC_RAMP: 0.6  ;5  ;20  ;ramp ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.8,  value_limit=5, percent_error=20,  wave='ramp', amplitude=2,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 12$IDC_RAMP')  #hash Meas 12$IDC_RAMP: 0.8  ;5  ;20  ;ramp ;2  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=1,    value_limit=5, percent_error=20,  wave='ramp', amplitude=2,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 13$IDC_RAMP')  #hash Meas 13$IDC_RAMP: 1    ;5  ;20  ;ramp ;2  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=1.2,  value_limit=5, percent_error=20,  wave='ramp', amplitude=2,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 14$IDC_RAMP')  #hash Meas 14$IDC_RAMP: 1.2  ;5  ;20  ;ramp ;2  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=1.5,  value_limit=5, percent_error=20,  wave='ramp', amplitude=3,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 15$IDC_RAMP')  #hash Meas 15$IDC_RAMP: 1.5  ;5  ;20  ;ramp ;3  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=2,    value_limit=5, percent_error=20,  wave='ramp', amplitude=3,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 16$IDC_RAMP')  #hash Meas 16$IDC_RAMP: 2    ;5  ;20  ;ramp ;3  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=2.5,  value_limit=5, percent_error=20,  wave='ramp', amplitude=4,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 17$IDC_RAMP')  #hash Meas 17$IDC_RAMP: 2.5  ;5  ;20  ;ramp ;4  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=3,    value_limit=5, percent_error=20,  wave='ramp', amplitude=5,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 18$IDC_RAMP')  #hash Meas 18$IDC_RAMP: 3    ;5  ;20  ;ramp ;5  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=4,    value_limit=5, percent_error=20,  wave='ramp', amplitude=5,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 19$IDC_RAMP')  #hash Meas 19$IDC_RAMP: 4    ;5  ;20  ;ramp ;5  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=5,    value_limit=5, percent_error=20,  wave='ramp', amplitude=5,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 20$IDC_RAMP')  #hash Meas 20$IDC_RAMP: 5    ;5  ;20  ;ramp ;5  ;10  ;10k  ;1.500  ;True  ;3

Testing.GetScreenshot()
Testing.BK1697B.SET_OUTPUT_OFF()
#endregion Current measurement with generator signal ramp$IDC_RAMP

#region Current measurement with generator signal negative ramp$IDC_NEGRAMP
#description: value \nmeasurement, A;value limit, A;percentage of \nallowed error, %;wave amplitude;amplitude, A;amplitude\nlimit, A;frequency, Hz;delay time \nbefore \nmeasurement, s;remeasure,\nTrue or False;number of \nremeasurements;
RFSE.Program('tree', 'set', 'select = Current measurement with generator signal negative ramp$IDC_NEGRAMP')

RFSE.Stage('Set NameGraph => IDC_NEGRAMP_GRAPH')
Testing.NameGraph = 'IDC_NEGRAMP_GRAPH'

IDC(value=0.01, value_limit=5, percent_error=220, wave='negramp', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=3.00, remeasurement=True, remeasurement_number=3, hash='Meas 1$IDC_NEGRAMP')   #hash Meas 1$IDC_NEGRAMP:  0.01 ;5  ;250 ;negramp ;1  ;10  ;10k  ;3.000  ;True  ;3
IDC(value=0.03, value_limit=5, percent_error=110, wave='negramp', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 2$IDC_NEGRAMP')   #hash Meas 2$IDC_NEGRAMP:  0.03 ;5  ;110 ;negramp ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.05, value_limit=5, percent_error=55,  wave='negramp', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 3$IDC_NEGRAMP')   #hash Meas 3$IDC_NEGRAMP:  0.05 ;5  ;55  ;negramp ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.1,  value_limit=5, percent_error=35,  wave='negramp', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 4$IDC_NEGRAMP')   #hash Meas 4$IDC_NEGRAMP:  0.1  ;5  ;35  ;negramp ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.15, value_limit=5, percent_error=20,  wave='negramp', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 5$IDC_NEGRAMP')   #hash Meas 5$IDC_NEGRAMP:  0.15 ;5  ;20  ;negramp ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.2,  value_limit=5, percent_error=20,  wave='negramp', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 6$IDC_NEGRAMP')   #hash Meas 6$IDC_NEGRAMP:  0.2  ;5  ;20  ;negramp ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.25, value_limit=5, percent_error=20,  wave='negramp', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 7$IDC_NEGRAMP')   #hash Meas 7$IDC_NEGRAMP:  0.25 ;5  ;20  ;negramp ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.3,  value_limit=5, percent_error=20,  wave='negramp', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 8$IDC_NEGRAMP')   #hash Meas 8$IDC_NEGRAMP:  0.3  ;5  ;20  ;negramp ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.4,  value_limit=5, percent_error=20,  wave='negramp', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 9$IDC_NEGRAMP')   #hash Meas 9$IDC_NEGRAMP:  0.4  ;5  ;20  ;negramp ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.5,  value_limit=5, percent_error=20,  wave='negramp', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 10$IDC_NEGRAMP')  #hash Meas 10$IDC_NEGRAMP: 0.5  ;5  ;20  ;negramp ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.6,  value_limit=5, percent_error=20,  wave='negramp', amplitude=1,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 11$IDC_NEGRAMP')  #hash Meas 11$IDC_NEGRAMP: 0.6  ;5  ;20  ;negramp ;1  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=0.8,  value_limit=5, percent_error=20,  wave='negramp', amplitude=2,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 12$IDC_NEGRAMP')  #hash Meas 12$IDC_NEGRAMP: 0.8  ;5  ;20  ;negramp ;2  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=1,    value_limit=5, percent_error=20,  wave='negramp', amplitude=2,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 13$IDC_NEGRAMP')  #hash Meas 13$IDC_NEGRAMP: 1    ;5  ;20  ;negramp ;2  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=1.2,  value_limit=5, percent_error=20,  wave='negramp', amplitude=2,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 14$IDC_NEGRAMP')  #hash Meas 14$IDC_NEGRAMP: 1.2  ;5  ;20  ;negramp ;2  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=1.5,  value_limit=5, percent_error=20,  wave='negramp', amplitude=3,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 15$IDC_NEGRAMP')  #hash Meas 15$IDC_NEGRAMP: 1.5  ;5  ;20  ;negramp ;3  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=2,    value_limit=5, percent_error=20,  wave='negramp', amplitude=3,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 16$IDC_NEGRAMP')  #hash Meas 16$IDC_NEGRAMP: 2    ;5  ;20  ;negramp ;3  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=2.5,  value_limit=5, percent_error=20,  wave='negramp', amplitude=4,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 17$IDC_NEGRAMP')  #hash Meas 17$IDC_NEGRAMP: 2.5  ;5  ;20  ;negramp ;4  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=3,    value_limit=5, percent_error=20,  wave='negramp', amplitude=5,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 18$IDC_NEGRAMP')  #hash Meas 18$IDC_NEGRAMP: 3    ;5  ;20  ;negramp ;5  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=4,    value_limit=5, percent_error=20,  wave='negramp', amplitude=5,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 19$IDC_NEGRAMP')  #hash Meas 19$IDC_NEGRAMP: 4    ;5  ;20  ;negramp ;5  ;10  ;10k  ;1.500  ;True  ;3
IDC(value=5,    value_limit=5, percent_error=20,  wave='negramp', amplitude=5,  amplitude_limit=10, frequency='10k', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Meas 20$IDC_NEGRAMP')  #hash Meas 20$IDC_NEGRAMP: 5    ;5  ;20  ;negramp ;5  ;10  ;10k  ;1.500  ;True  ;3

Testing.GetScreenshot()
Testing.BK1697B.SET_OUTPUT_OFF()
#endregion Current measurement with generator signal negative ramp$IDC_NEGRAMP

RFSE.Stage(" ")
RFSE.Stage('name: Graph >> mode: close >> command: ', 'Plugin')
RFSE.Plugin("Graph", 'close', '')
RFSE.EndScript()
