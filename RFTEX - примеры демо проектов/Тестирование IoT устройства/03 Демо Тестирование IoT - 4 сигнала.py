import RFSE
from MOSC import hashStatus, hash_passed, hash_failed
from Demo_Test_IoT_4_Wave import Testing
import MTLG
RFSE.Max('alpha', 'set', 'Демо Tестирование IoT - 4 сигнала')
RFSE.Stage("*********************************************************************")
RFSE.Stage("*************** Демо Tестирование IoT - 4 сигнала *******************")
RFSE.Stage("*********************************************************************")
RFSE.Stage(" ")

Testing.LoadTablesHeadInfo()
Testing.SET_OUTPUT_OFF()


def VDC(
        value: (str, float, int),
        value_limit: (str, float, int),
        percent_error: (float, int),
        wave: str,
        amplitude: (str, float, int),
        amplitude_limit: int,
        frequency: (str, float, int),
        hash: str,
        remeasurement: bool = False,
        remeasurement_number: int = None,
        time_delay: (float, int) = 0.0

) -> None:

    if hashStatus(hash):

        Testing.CheckConnectDevices()

        Testing.CheckWireConnection(WireConnection='VDC')

        Testing.OutONNCommand()
        Testing.CheckGraphInit()
        Testing.CreateGraphMask(value_limit=value_limit)

        Testing.TimeDelay = time_delay
        Testing.Remeasurement = remeasurement
        Testing.RemeasurementNumber = remeasurement_number

        Testing.MeasurementAndReport(value=value, value_limit=value_limit, wave=wave, percent_error=percent_error,
                                     amplitude=amplitude, amplitude_limit=amplitude_limit, frequency=frequency,
                                     hash=hash, WireConnection='VDC')
        Testing.CreateGraph()

        if Testing.Status == 'Неуспешно':
            hash_failed()
        else:
            hash_passed()


def IDC(
        value: (str, float, int),
        value_limit: (str, float, int),
        percent_error: (float, int),
        wave: str,
        amplitude: (str, float, int),
        amplitude_limit: int,
        frequency: (str, float, int),
        hash: str,
        remeasurement: bool = False,
        remeasurement_number: int = None,
        time_delay: (int, float) = 0.0

) -> None:

    if hashStatus(hash):

        Testing.CheckConnectDevices()

        Testing.CheckWireConnection(WireConnection='IDC')

        Testing.OutONNCommand()
        Testing.CheckGraphInit()
        Testing.CreateGraphMask(value_limit=value_limit)

        Testing.TimeDelay = time_delay
        Testing.Remeasurement = remeasurement
        Testing.RemeasurementNumber = remeasurement_number

        Testing.MeasurementAndReport(value=value, value_limit=value_limit, wave=wave, percent_error=percent_error,
                                     amplitude=amplitude, amplitude_limit=amplitude_limit, frequency=frequency,
                                     hash=hash, WireConnection='IDC')
        Testing.CreateGraph()

        if Testing.Status == 'Неуспешно':
            hash_failed()
        else:
            hash_passed()

#region Измерение напряжения с сигналом генератора sin$VDC_SIN
#description: измеряемое \nзначение, В;предел \nизмерения, В;процент \nдопустимой \nошибки, %;сигнал волны;амплитуда, В;предел\nамплитуды, В;частота, Гц;задержка\nперед\nизмерением, с;повторное \nизмерение,\nДа или Нет;число\nповторных \nизмерений
RFSE.Program('tree', 'set', 'select = Измерение напряжения с сигналом генератора sin$VDC_SIN')

RFSE.Stage('Устанавливаем имя графа => VDC_SIN_GRAPH')
Testing.NameGraph = 'VDC_SIN_GRAPH'
RFSE.Stage(" ")

VDC(value=1,   value_limit=40, percent_error=70, wave='sin',  amplitude=1, amplitude_limit=10, frequency='10к', time_delay=3.00, remeasurement=True, remeasurement_number=3, hash='Измерение 1$VDC_SIN')  #hash Измерение 1$VDC_SIN:   1  ;40  ;70  ;sin ;1  ;10  ;10к  ;0.800  ;Да  ;3
VDC(value=2,   value_limit=40, percent_error=30, wave='sin',  amplitude=1, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 2$VDC_SIN')  #hash Измерение 2$VDC_SIN:   2  ;40  ;30  ;sin ;1  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=3,   value_limit=40, percent_error=20, wave='sin',  amplitude=1, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 3$VDC_SIN')  #hash Измерение 3$VDC_SIN:   3  ;40  ;20  ;sin ;1  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=4,   value_limit=40, percent_error=20, wave='sin',  amplitude=1, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 4$VDC_SIN')  #hash Измерение 4$VDC_SIN:   4  ;40  ;20  ;sin ;1  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=5,   value_limit=40, percent_error=20, wave='sin',  amplitude=1, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 5$VDC_SIN')  #hash Измерение 5$VDC_SIN:   5  ;40  ;20  ;sin ;1  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=6,   value_limit=40, percent_error=20, wave='sin',  amplitude=1, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 6$VDC_SIN')  #hash Измерение 6$VDC_SIN:   6  ;40  ;20  ;sin ;1  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=8,   value_limit=40, percent_error=20, wave='sin',  amplitude=1, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 7$VDC_SIN')  #hash Измерение 7$VDC_SIN:   8  ;40  ;20  ;sin ;1  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=10,  value_limit=40, percent_error=20, wave='sin',  amplitude=1, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 8$VDC_SIN')  #hash Измерение 8$VDC_SIN:   10 ;40  ;20  ;sin ;1  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=12,  value_limit=40, percent_error=20, wave='sin',  amplitude=1, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 9$VDC_SIN')  #hash Измерение 9$VDC_SIN:   12 ;40  ;20  ;sin ;1  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=14,  value_limit=40, percent_error=20, wave='sin',  amplitude=1, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 10$VDC_SIN') #hash Измерение 10$VDC_SIN:  14 ;40  ;20  ;sin ;1  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=16,  value_limit=40, percent_error=20, wave='sin',  amplitude=1, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 11$VDC_SIN') #hash Измерение 11$VDC_SIN:  16 ;40  ;20  ;sin ;1  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=18,  value_limit=40, percent_error=20, wave='sin',  amplitude=2, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 12$VDC_SIN') #hash Измерение 12$VDC_SIN:  18 ;40  ;20  ;sin ;2  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=20,  value_limit=40, percent_error=20, wave='sin',  amplitude=2, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 13$VDC_SIN') #hash Измерение 13$VDC_SIN:  20 ;40  ;20  ;sin ;2  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=22,  value_limit=40, percent_error=20, wave='sin',  amplitude=2, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 14$VDC_SIN') #hash Измерение 14$VDC_SIN:  22 ;40  ;20  ;sin ;2  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=25,  value_limit=40, percent_error=20, wave='sin',  amplitude=3, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 15$VDC_SIN') #hash Измерение 15$VDC_SIN:  25 ;40  ;20  ;sin ;3  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=28,  value_limit=40, percent_error=20, wave='sin',  amplitude=3, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 16$VDC_SIN') #hash Измерение 16$VDC_SIN:  28 ;40  ;20  ;sin ;3  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=31,  value_limit=40, percent_error=20, wave='sin',  amplitude=4, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 17$VDC_SIN') #hash Измерение 17$VDC_SIN:  31 ;40  ;20  ;sin ;4  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=34,  value_limit=40, percent_error=20, wave='sin',  amplitude=5, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 18$VDC_SIN') #hash Измерение 18$VDC_SIN:  34 ;40  ;20  ;sin ;5  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=37,  value_limit=40, percent_error=20, wave='sin',  amplitude=5, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 19$VDC_SIN') #hash Измерение 19$VDC_SIN:  37 ;40  ;20  ;sin ;5  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=40,  value_limit=40, percent_error=20, wave='sin',  amplitude=5, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 20$VDC_SIN') #hash Измерение 20$VDC_SIN:  40 ;40  ;20  ;sin ;5  ;10  ;10к  ;0.050  ;Да  ;3

Testing.GetScreenshot()
Testing.SET_OUTPUT_OFF()
#endregion Измерение напряжения с сигналом генератора sin$VDC_SIN


#region Измерение напряжения с сигналом генератора square$VDC_SQUARE
#description: измеряемое \nзначение, В;предел \nизмерения, В;процент \nдопустимой \nошибки, %;сигнал волны;амплитуда, В;предел\nамплитуды, В;частота, Гц;задержка\nперед\nизмерением, с;повторное \nизмерение,\nДа или Нет;число\nповторных \nизмерений
RFSE.Program('tree', 'set', 'select = Измерение напряжения с сигналом генератора square$VDC_SQUARE')

RFSE.Stage('Устанавливаем имя графа => VDC_SQUARE_GRAPH')
Testing.NameGraph = 'VDC_SQUARE_GRAPH'

VDC(value=1,   value_limit=40, percent_error=70,  wave='square',  amplitude=1, amplitude_limit=10, frequency='10к', time_delay=3.00, remeasurement=True, remeasurement_number=3, hash='Измерение 1$VDC_SQUARE')  #hash Измерение 1$VDC_SQUARE:   1  ;40  ;70  ;square ;1  ;10  ;10к  ;0.800  ;Да  ;3
VDC(value=2,   value_limit=40, percent_error=30,  wave='square',  amplitude=1, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 2$VDC_SQUARE')  #hash Измерение 2$VDC_SQUARE:   2  ;40  ;30  ;square ;1  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=3,   value_limit=40, percent_error=20,  wave='square',  amplitude=1, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 3$VDC_SQUARE')  #hash Измерение 3$VDC_SQUARE:   3  ;40  ;20  ;square ;1  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=4,   value_limit=40, percent_error=20,  wave='square',  amplitude=1, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 4$VDC_SQUARE')  #hash Измерение 4$VDC_SQUARE:   4  ;40  ;20  ;square ;1  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=5,   value_limit=40, percent_error=20,  wave='square',  amplitude=1, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 5$VDC_SQUARE')  #hash Измерение 5$VDC_SQUARE:   5  ;40  ;20  ;square ;1  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=6,   value_limit=40, percent_error=20,  wave='square',  amplitude=1, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 6$VDC_SQUARE')  #hash Измерение 6$VDC_SQUARE:   6  ;40  ;20  ;square ;1  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=8,   value_limit=40, percent_error=20,  wave='square',  amplitude=1, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 7$VDC_SQUARE')  #hash Измерение 7$VDC_SQUARE:   8  ;40  ;20  ;square ;1  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=10,  value_limit=40, percent_error=20,  wave='square',  amplitude=1, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 8$VDC_SQUARE')  #hash Измерение 8$VDC_SQUARE:   10 ;40  ;20  ;square ;1  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=12,  value_limit=40, percent_error=20,  wave='square',  amplitude=1, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 9$VDC_SQUARE')  #hash Измерение 9$VDC_SQUARE:   12 ;40  ;20  ;square ;1  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=14,  value_limit=40, percent_error=20,  wave='square',  amplitude=1, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 10$VDC_SQUARE') #hash Измерение 10$VDC_SQUARE:  14 ;40  ;20  ;square ;1  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=16,  value_limit=40, percent_error=20,  wave='square',  amplitude=1, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 11$VDC_SQUARE') #hash Измерение 11$VDC_SQUARE:  16 ;40  ;20  ;square ;1  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=18,  value_limit=40, percent_error=20,  wave='square',  amplitude=2, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 12$VDC_SQUARE') #hash Измерение 12$VDC_SQUARE:  18 ;40  ;20  ;square ;2  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=20,  value_limit=40, percent_error=20,  wave='square',  amplitude=2, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 13$VDC_SQUARE') #hash Измерение 13$VDC_SQUARE:  20 ;40  ;20  ;square ;2  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=22,  value_limit=40, percent_error=20,  wave='square',  amplitude=2, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 14$VDC_SQUARE') #hash Измерение 14$VDC_SQUARE:  22 ;40  ;20  ;square ;2  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=25,  value_limit=40, percent_error=20,  wave='square',  amplitude=3, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 15$VDC_SQUARE') #hash Измерение 15$VDC_SQUARE:  25 ;40  ;20  ;square ;3  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=28,  value_limit=40, percent_error=20,  wave='square',  amplitude=3, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 16$VDC_SQUARE') #hash Измерение 16$VDC_SQUARE:  28 ;40  ;20  ;square ;3  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=31,  value_limit=40, percent_error=20,  wave='square',  amplitude=4, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 17$VDC_SQUARE') #hash Измерение 17$VDC_SQUARE:  31 ;40  ;20  ;square ;4  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=34,  value_limit=40, percent_error=20,  wave='square',  amplitude=5, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 18$VDC_SQUARE') #hash Измерение 18$VDC_SQUARE:  34 ;40  ;20  ;square ;5  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=37,  value_limit=40, percent_error=20,  wave='square',  amplitude=5, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 19$VDC_SQUARE') #hash Измерение 19$VDC_SQUARE:  37 ;40  ;20  ;square ;5  ;10  ;10к  ;0.050  ;Да  ;3
VDC(value=40,  value_limit=40, percent_error=20,  wave='square',  amplitude=5, amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 20$VDC_SQUARE') #hash Измерение 20$VDC_SQUARE:  40 ;40  ;20  ;square ;5  ;10  ;10к  ;0.050  ;Да  ;3

Testing.GetScreenshot()
Testing.SET_OUTPUT_OFF()
#endregion Измерение напряжения с сигналом генератора square$VDC_SQUARE

#region Измерение тока с сигналом генератора ramp$IDC_RAMP
#description: измеряемое \nзначение, А;предел \nизмерения, А;процент \nдопустимой \nошибки, %;сигнал волны;амплитуда, А;предел\nамплитуды, А;частота, Гц;задержка\nперед\nизмерением, с;повторное \nизмерение,\nДа или Нет;число\nповторных \nизмерений
RFSE.Program('tree', 'set', 'select = Измерение тока с сигналом генератора ramp$IDC_RAMP')

RFSE.Stage('Устанавливаем имя графа => IDC_RAMP_GRAPH')
Testing.NameGraph = 'IDC_RAMP_GRAPH'

IDC(value=0.01, value_limit=5, percent_error=250, wave='ramp', amplitude=1,  amplitude_limit=10, frequency='10к', time_delay=3.00, remeasurement=True, remeasurement_number=3, hash='Измерение 1$IDC_RAMP')   #hash Измерение 1$IDC_RAMP:  0.01 ;5  ;230 ;ramp ;1  ;10  ;10к  ;0.800  ;Да  ;3
IDC(value=0.03, value_limit=5, percent_error=110, wave='ramp', amplitude=1,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 2$IDC_RAMP')   #hash Измерение 2$IDC_RAMP:  0.03 ;5  ;110 ;ramp ;1  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=0.05, value_limit=5, percent_error=55,  wave='ramp', amplitude=1,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 3$IDC_RAMP')   #hash Измерение 3$IDC_RAMP:  0.05 ;5  ;55  ;ramp ;1  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=0.1,  value_limit=5, percent_error=35,  wave='ramp', amplitude=1,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 4$IDC_RAMP')   #hash Измерение 4$IDC_RAMP:  0.1  ;5  ;35  ;ramp ;1  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=0.15, value_limit=5, percent_error=20,  wave='ramp', amplitude=1,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 5$IDC_RAMP')   #hash Измерение 5$IDC_RAMP:  0.15 ;5  ;20  ;ramp ;1  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=0.2,  value_limit=5, percent_error=20,  wave='ramp', amplitude=1,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 6$IDC_RAMP')   #hash Измерение 6$IDC_RAMP:  0.2  ;5  ;20  ;ramp ;1  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=0.25, value_limit=5, percent_error=20,  wave='ramp', amplitude=1,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 7$IDC_RAMP')   #hash Измерение 7$IDC_RAMP:  0.25 ;5  ;20  ;ramp ;1  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=0.3,  value_limit=5, percent_error=20,  wave='ramp', amplitude=1,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 8$IDC_RAMP')   #hash Измерение 8$IDC_RAMP:  0.3  ;5  ;20  ;ramp ;1  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=0.4,  value_limit=5, percent_error=20,  wave='ramp', amplitude=1,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 9$IDC_RAMP')   #hash Измерение 9$IDC_RAMP:  0.4  ;5  ;20  ;ramp ;1  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=0.5,  value_limit=5, percent_error=20,  wave='ramp', amplitude=1,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 10$IDC_RAMP')  #hash Измерение 10$IDC_RAMP: 0.5  ;5  ;20  ;ramp ;1  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=0.6,  value_limit=5, percent_error=20,  wave='ramp', amplitude=1,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 11$IDC_RAMP')  #hash Измерение 11$IDC_RAMP: 0.6  ;5  ;20  ;ramp ;1  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=0.8,  value_limit=5, percent_error=20,  wave='ramp', amplitude=2,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 12$IDC_RAMP')  #hash Измерение 12$IDC_RAMP: 0.8  ;5  ;20  ;ramp ;2  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=1,    value_limit=5, percent_error=20,  wave='ramp', amplitude=2,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 13$IDC_RAMP')  #hash Измерение 13$IDC_RAMP: 1    ;5  ;20  ;ramp ;2  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=1.2,  value_limit=5, percent_error=20,  wave='ramp', amplitude=2,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 14$IDC_RAMP')  #hash Измерение 14$IDC_RAMP: 1.2  ;5  ;20  ;ramp ;2  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=1.5,  value_limit=5, percent_error=20,  wave='ramp', amplitude=3,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 15$IDC_RAMP')  #hash Измерение 15$IDC_RAMP: 1.5  ;5  ;20  ;ramp ;3  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=2,    value_limit=5, percent_error=20,  wave='ramp', amplitude=3,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 16$IDC_RAMP')  #hash Измерение 16$IDC_RAMP: 2    ;5  ;20  ;ramp ;3  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=2.5,  value_limit=5, percent_error=20,  wave='ramp', amplitude=4,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 17$IDC_RAMP')  #hash Измерение 17$IDC_RAMP: 2.5  ;5  ;20  ;ramp ;4  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=3,    value_limit=5, percent_error=20,  wave='ramp', amplitude=5,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 18$IDC_RAMP')  #hash Измерение 18$IDC_RAMP: 3    ;5  ;20  ;ramp ;5  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=4,    value_limit=5, percent_error=20,  wave='ramp', amplitude=5,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 19$IDC_RAMP')  #hash Измерение 19$IDC_RAMP: 4    ;5  ;20  ;ramp ;5  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=5,    value_limit=5, percent_error=20,  wave='ramp', amplitude=5,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 20$IDC_RAMP')  #hash Измерение 20$IDC_RAMP: 5    ;5  ;20  ;ramp ;5  ;10  ;10к  ;0.050  ;Да  ;3

Testing.GetScreenshot()
Testing.SET_OUTPUT_OFF()
#endregion Измерение тока с сигналом генератора ramp$IDC_RAMP

#region Измерение тока с сигналом генератора negative ramp$IDC_NEGRAMP
#description: измеряемое \nзначение, А;предел \nизмерения, А;процент \nдопустимой \nошибки, %;сигнал волны;амплитуда, А;предел\nамплитуды, А;частота, Гц;задержка\nперед\nизмерением, с;повторное \nизмерение,\nДа или Нет;число\nповторных \nизмерений
RFSE.Program('tree', 'set', 'select = Измерение тока с сигналом генератора negative ramp$IDC_NEGRAMP')

RFSE.Stage('Устанавливаем имя графа => IDC_NEGRAMP_GRAPH')
Testing.NameGraph = 'IDC_NEGRAMP_GRAPH'

IDC(value=0.01, value_limit=5, percent_error=250, wave='negramp', amplitude=1,  amplitude_limit=10, frequency='10к', time_delay=3.00, remeasurement=True, remeasurement_number=3, hash='Измерение 1$IDC_NEGRAMP')   #hash Измерение 1$IDC_NEGRAMP:  0.01 ;5  ;230 ;negramp ;1  ;10  ;10к  ;0.800  ;Да  ;3
IDC(value=0.03, value_limit=5, percent_error=110, wave='negramp', amplitude=1,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 2$IDC_NEGRAMP')   #hash Измерение 2$IDC_NEGRAMP:  0.03 ;5  ;110 ;negramp ;1  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=0.05, value_limit=5, percent_error=55,  wave='negramp', amplitude=1,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 3$IDC_NEGRAMP')   #hash Измерение 3$IDC_NEGRAMP:  0.05 ;5  ;55  ;negramp ;1  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=0.1,  value_limit=5, percent_error=35,  wave='negramp', amplitude=1,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 4$IDC_NEGRAMP')   #hash Измерение 4$IDC_NEGRAMP:  0.1  ;5  ;35  ;negramp ;1  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=0.15, value_limit=5, percent_error=20,  wave='negramp', amplitude=1,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 5$IDC_NEGRAMP')   #hash Измерение 5$IDC_NEGRAMP:  0.15 ;5  ;20  ;negramp ;1  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=0.2,  value_limit=5, percent_error=20,  wave='negramp', amplitude=1,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 6$IDC_NEGRAMP')   #hash Измерение 6$IDC_NEGRAMP:  0.2  ;5  ;20  ;negramp ;1  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=0.25, value_limit=5, percent_error=20,  wave='negramp', amplitude=1,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 7$IDC_NEGRAMP')   #hash Измерение 7$IDC_NEGRAMP:  0.25 ;5  ;20  ;negramp ;1  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=0.3,  value_limit=5, percent_error=20,  wave='negramp', amplitude=1,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 8$IDC_NEGRAMP')   #hash Измерение 8$IDC_NEGRAMP:  0.3  ;5  ;20  ;negramp ;1  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=0.4,  value_limit=5, percent_error=20,  wave='negramp', amplitude=1,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 9$IDC_NEGRAMP')   #hash Измерение 9$IDC_NEGRAMP:  0.4  ;5  ;20  ;negramp ;1  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=0.5,  value_limit=5, percent_error=20,  wave='negramp', amplitude=1,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 10$IDC_NEGRAMP')  #hash Измерение 10$IDC_NEGRAMP: 0.5  ;5  ;20  ;negramp ;1  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=0.6,  value_limit=5, percent_error=20,  wave='negramp', amplitude=1,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 11$IDC_NEGRAMP')  #hash Измерение 11$IDC_NEGRAMP: 0.6  ;5  ;20  ;negramp ;1  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=0.8,  value_limit=5, percent_error=20,  wave='negramp', amplitude=2,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 12$IDC_NEGRAMP')  #hash Измерение 12$IDC_NEGRAMP: 0.8  ;5  ;20  ;negramp ;2  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=1,    value_limit=5, percent_error=20,  wave='negramp', amplitude=2,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 13$IDC_NEGRAMP')  #hash Измерение 13$IDC_NEGRAMP: 1    ;5  ;20  ;negramp ;2  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=1.2,  value_limit=5, percent_error=20,  wave='negramp', amplitude=2,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 14$IDC_NEGRAMP')  #hash Измерение 14$IDC_NEGRAMP: 1.2  ;5  ;20  ;negramp ;2  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=1.5,  value_limit=5, percent_error=20,  wave='negramp', amplitude=3,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 15$IDC_NEGRAMP')  #hash Измерение 15$IDC_NEGRAMP: 1.5  ;5  ;20  ;negramp ;3  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=2,    value_limit=5, percent_error=20,  wave='negramp', amplitude=3,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 16$IDC_NEGRAMP')  #hash Измерение 16$IDC_NEGRAMP: 2    ;5  ;20  ;negramp ;3  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=2.5,  value_limit=5, percent_error=20,  wave='negramp', amplitude=4,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 17$IDC_NEGRAMP')  #hash Измерение 17$IDC_NEGRAMP: 2.5  ;5  ;20  ;negramp ;4  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=3,    value_limit=5, percent_error=20,  wave='negramp', amplitude=5,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 18$IDC_NEGRAMP')  #hash Измерение 18$IDC_NEGRAMP: 3    ;5  ;20  ;negramp ;5  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=4,    value_limit=5, percent_error=20,  wave='negramp', amplitude=5,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 19$IDC_NEGRAMP')  #hash Измерение 19$IDC_NEGRAMP: 4    ;5  ;20  ;negramp ;5  ;10  ;10к  ;0.050  ;Да  ;3
IDC(value=5,    value_limit=5, percent_error=20,  wave='negramp', amplitude=5,  amplitude_limit=10, frequency='10к', time_delay=1.50, remeasurement=True, remeasurement_number=3, hash='Измерение 20$IDC_NEGRAMP')  #hash Измерение 20$IDC_NEGRAMP: 5    ;5  ;20  ;negramp ;5  ;10  ;10к  ;0.050  ;Да  ;3

Testing.GetScreenshot()
Testing.SET_OUTPUT_OFF()
#region Измерение тока с сигналом генератора negative ramp$IDC_NEGRAMP

RFSE.Stage(" ")
RFSE.Stage('name: Graph >> mode: close >> command: ', 'Plugin')
RFSE.Plugin("Graph", 'close', '')
RFSE.EndScript()
