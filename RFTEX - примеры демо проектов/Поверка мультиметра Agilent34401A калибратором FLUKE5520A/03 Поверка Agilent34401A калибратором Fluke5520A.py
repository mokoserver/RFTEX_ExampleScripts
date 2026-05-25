from SettingsAndMeasurement import Poverka
import RFSE
import MOSC

RFSE.Stage("*********************************************************")
RFSE.Stage("************ Скрипт измерений Fluke5520 ***************")
RFSE.Stage("*********************************************************")
RFSE.Stage(" ")

RFSE.Stage("*********************************************************")
RFSE.Stage('**************** Обнуление флагов системы ****************')
RFSE.Stage("*********************************************************")
RFSE.Stage(" ")

Poverka.LoadTablesHeadInfo()


def VDC(
        range: (str | float | int),
        verified: (str | float | int),
        error: (str | float | int),
        hash: str,
        remeasurement: bool = False,
        remeasurement_number: int = None,
        time_delay: (float | int) = 0

) -> None:

    if MOSC.hashStatus(hash):

        Poverka.CheckConnectDevices()
        
        Poverka.CheckWireConnection(WireConnection='VDC')
        Poverka.MeasurementStartCommand(WireConnection='VDC')
        
        Poverka.TimeDelay = time_delay
        Poverka.Remeasurement = remeasurement
        Poverka.RemeasurementNumber = remeasurement_number
        
        Poverka.VDC_Measurement(range=range, verified=verified, error=error)


def VAC(
        range: (str | float | int),
        verified: (str | float | int),
        frequency: (str | float | int),
        error: (str | float | int),
        hash: str,
        remeasurement: bool = False,
        remeasurement_number: int = None,
        time_delay: (float | int) = 0

) -> None:

    if MOSC.hashStatus(hash):
        
        Poverka.CheckConnectDevices()
        
        Poverka.CheckWireConnection(WireConnection='VAC')
        Poverka.MeasurementStartCommand(WireConnection='VAC')
        
        Poverka.TimeDelay = time_delay
        Poverka.Remeasurement = remeasurement
        Poverka.RemeasurementNumber = remeasurement_number
        
        Poverka.VAC_Measurement(range=range, verified=verified, error=error, frequency=frequency)


def R2(
        range: (str | float | int),
        verified: (str | float | int),
        error: (str | float | int),
        hash: str,
        remeasurement: bool = False,
        remeasurement_number: int = None,
        time_delay: (float | int) = 0

) -> None:

    if MOSC.hashStatus(hash):
        
        Poverka.CheckConnectDevices()
        Poverka.CheckWireConnection(WireConnection='R2')
        Poverka.MeasurementStartCommand(WireConnection='R2')
        
        Poverka.TimeDelay = time_delay
        Poverka.Remeasurement = remeasurement
        Poverka.RemeasurementNumber = remeasurement_number
        
        Poverka.R2_Measurement(range=range, verified=verified, error=error)


def R4(
        range: (str | float | int),
        verified: (str | float | int),
        error: (str | float | int),
        hash: str,
        remeasurement: bool = False,
        remeasurement_number: int = None,
        time_delay: (float | int) = 0

) -> None:

    if MOSC.hashStatus(hash):
        
        Poverka.CheckConnectDevices()
        Poverka.CheckWireConnection(WireConnection='R4')
        Poverka.MeasurementStartCommand(WireConnection='R4')
        
        Poverka.TimeDelay = time_delay
        Poverka.Remeasurement = remeasurement
        Poverka.RemeasurementNumber = remeasurement_number
        
        Poverka.R4_Measurement(range=range, verified=verified, error=error)


def IDC(
        range: (str | float | int),
        verified: (str | float | int),
        error: (str | float | int),
        hash: str,
        remeasurement: bool = False,
        remeasurement_number: int = None,
        time_delay: (float | int) = 0

) -> None:

    if MOSC.hashStatus(hash):

        Poverka.CheckConnectDevices()
        
        Poverka.CheckWireConnection(WireConnection='IDC')
        Poverka.MeasurementStartCommand(WireConnection='IDC')
        
        Poverka.TimeDelay = time_delay
        Poverka.Remeasurement = remeasurement
        Poverka.RemeasurementNumber = remeasurement_number
        
        Poverka.IDC_Measurement(range=range, verified=verified, error=error)


def IAC(
        range: (str | float | int),
        verified: (str | float | int),
        frequency: (str | float | int),
        error: (str | float | int),
        hash: str,
        remeasurement: bool = False,
        remeasurement_number: int = None,
        time_delay: (float | int) = 0

) -> None:

    if MOSC.hashStatus(hash):

        Poverka.CheckConnectDevices()
        
        Poverka.CheckWireConnection(WireConnection='IAC')
        Poverka.MeasurementStartCommand(WireConnection='IAC')

        Poverka.TimeDelay = time_delay
        Poverka.Remeasurement = remeasurement
        Poverka.RemeasurementNumber = remeasurement_number
        
        Poverka.IAC_Measurement(range=range, verified=verified, error=error, frequency=frequency)


#region Определение абсолютной погрешности измерения напряжения переменного тока$VAC
#description: диапазон \nизмерения,\nВ;поверяемая точка, В;частота, Гц;допускаемая \nпогрешность \nизмерения, В;время задержки \nперед \nизмерением, с;переизмерять,\nДа или Нет;количество \nпереизмерений
RFSE.Program('tree', 'set', 'select = Определение абсолютной погрешности измерения напряжения переменного тока$VAC')

VAC(range="100m", verified="10,0000m",  frequency="1k",    error="46u",   time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 1$VAC')   #hash Meas 1$VAC:   100m  ;10,0000m   ;1k    ;46u   ;3.000000  ;True  ;3
VAC(range="100m", verified="100,0000m", frequency="1k",    error="100u",  time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 2$VAC')   #hash Meas 2$VAC:   100m  ;100,0000m  ;1k    ;100u  ;3.000000  ;True  ;3
VAC(range="100m", verified="100,0000m", frequency="50k",   error="170u",  time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 3$VAC')   #hash Meas 3$VAC:   100m  ;100,0000m  ;50k   ;170u  ;3.000000  ;True  ;3
VAC(range="1",    verified="1,000000",  frequency="1k",    error="900u",  time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 4$VAC')   #hash Meas 4$VAC:   1     ;1,000000   ;1k    ;900u  ;3.000000  ;True  ;3
VAC(range="1",    verified="1,000000",  frequency="50k",   error="1,7m",  time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 5$VAC')   #hash Meas 5$VAC:   1     ;1,000000   ;50k   ;1,7m  ;3.000000  ;True  ;3
VAC(range="10",   verified="10,00000",  frequency="0,01k", error="9m",    time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 6$VAC')   #hash Meas 6$VAC:   10    ;10,00000   ;0,01k ;9m    ;3.000000  ;True  ;3
VAC(range="10",   verified="10,00000",  frequency="1k",    error="9m",    time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 7$VAC')   #hash Meas 7$VAC:   10    ;10,00000   ;1k    ;9m    ;3.000000  ;True  ;3
VAC(range="10",   verified="10,00000",  frequency="50k",   error="17m",   time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 8$VAC')   #hash Meas 8$VAC:   10    ;10,00000   ;50k   ;17m   ;3.000000  ;True  ;3
VAC(range="100",  verified="100,0000",  frequency="1k",    error="90m",   time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 9$VAC')   #hash Meas 9$VAC:   100   ;100,0000   ;1k    ;90m   ;3.000000  ;True  ;3
VAC(range="100",  verified="100,0000",  frequency="50k",   error="170m",  time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 10$VAC')  #hash Meas 10$VAC:  100   ;100,0000   ;50k   ;170m  ;3.000000  ;True  ;3
VAC(range="750",  verified="750,000",   frequency="1k",    error="675m",  time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 11$VAC')  #hash Meas 11$VAC:  750   ;750,000    ;1k    ;675m  ;3.000000  ;True  ;3
VAC(range="750",  verified="750,000",   frequency="5k",    error="1275m", time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 12$VAC')  #hash Meas 12$VAC:  750   ;750,000    ;5k    ;1275m ;3.000000  ;True  ;3

Poverka.MeasurementStopCommand()
#endregion Определение абсолютной погрешности измерения напряжения переменного тока$VAC

#region Определение абсолютной погрешности измерения напряжения постоянного тока$VDC
#description: диапазон \nизмерения,\nВ;поверяемая точка, В;частота, Гц;допускаемая \nпогрешность \nизмерения, В;время задержки \nперед \nизмерением, с;переизмерять,\nДа или Нет;количество \nпереизмерений;
RFSE.Program('tree', 'set', 'select = Определение абсолютной погрешности измерения напряжения постоянного тока$VDC')

VDC(range='100m', verified='100,0000m',  error='8,5u', time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 1$VDC')   #hash Meas 1$VDC:  100m   ;100,0000m   ;-   ;8,5u  ;3.000000  ;True  ;3
VDC(range='100m', verified='-100,0000m', error='8,5u', time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 2$VDC')   #hash Meas 2$VDC:  100m   ;-100,0000m  ;-   ;8,5u  ;3.000000  ;True  ;3
VDC(range='1',    verified='1,000000',   error='47u',  time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 3$VDC')   #hash Meas 3$VDC:  1      ;1,000000    ;-   ;47u   ;3.000000  ;True  ;3
VDC(range='1',    verified='-1,000000',  error='47u',  time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 4$VDC')   #hash Meas 4$VDC:  1      ;-1,000000   ;-   ;47u   ;3.000000  ;True  ;3
VDC(range='10',   verified='10,00000',   error='400u', time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 5$VDC')   #hash Meas 5$VDC:  10     ;10,00000    ;-   ;400u  ;3.000000  ;True  ;3
VDC(range='10',   verified='-10,00000',  error='400u', time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 6$VDC')   #hash Meas 6$VDC:  10     ;-10,00000   ;-   ;400u  ;3.000000  ;True  ;3
VDC(range='100',  verified='100,0000',   error='5,1m', time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 7$VDC')   #hash Meas 7$VDC:  100    ;100,0000    ;-   ;5,1m  ;3.000000  ;True  ;3
VDC(range='100',  verified='-100,0000',  error='5,1m', time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 8$VDC')   #hash Meas 8$VDC:  100    ;-100,0000   ;-   ;5,1m  ;3.000000  ;True  ;3
VDC(range='1000', verified='1000,000',   error='55m',  time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 9$VDC')   #hash Meas 9$VDC:  1000   ;1000,000    ;-   ;55m   ;3.000000  ;True  ;3
VDC(range='1000', verified='-1000,000',  error='55m',  time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 10$VDC')  #hash Meas 10$VDC: 1000   ;-1000,000   ;-   ;55m   ;3.000000  ;True  ;3

Poverka.MeasurementStopCommand()
#endregion Определение абсолютной погрешности измерения напряжения постоянного тока$VDC

#region Определение погрешности измерения сопротивления 4-х проводной схемы$R4
#description: диапазон \nизмерения,\nОм;поверяемая \nточка, Ом;частота, Гц;допускаемая \nпогрешность \nизмерения, Ом;время задержки \nперед \nизмерением, с;переизмерять,\nДа или Нет;количество \nпереизмерений;
RFSE.Program('tree', 'set', 'select = Определение погрешности измерения сопротивления 4-х проводной схемы$R4')

R4(range="100",  verified="100,000",   error="14m",  time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 1$R4')  #hash Meas 1$R4:  100    ;100,000    ;-   ;14m  ;3.000000  ;True  ;3
R4(range="1k",   verified="1,00000k",  error="110m", time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 2$R4')  #hash Meas 2$R4:  1k     ;1,00000K   ;-   ;110m ;3.000000  ;True  ;3
R4(range="10k",  verified="10,0000k",  error="1,1",  time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 3$R4')  #hash Meas 3$R4:  10k    ;10,0000K   ;-   ;1,1  ;3.000000  ;True  ;3
R4(range="100k", verified="100,000k",  error="11",   time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 4$R4')  #hash Meas 4$R4:  100k   ;100,000K   ;-   ;11   ;3.000000  ;True  ;3

Poverka.MeasurementStopCommand()
#endregion Определение погрешности измерения сопротивления 4-х проводной схемы$R4

#region Определение погрешности измерения сопротивления 2-х проводной схемы$R2
#description: диапазон \nизмерения,\nОм;поверяемая \nточка, Ом;частота, Гц;допускаемая \nпогрешность \nизмерения, Ом;время задержки \nперед \nизмерением, с;переизмерять,\nДа или Нет;количество \nпереизмерений;
RFSE.Program('tree', 'set', 'select = Определение погрешности измерения сопротивления 2-х проводной схемы$R2')

R2(range="1M",    verified="1,00000M", error="110",  time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 1$R2')  #hash Meas 1$R2:  1M     ;1,00000M  ;-   ;110   ;3.000000  ;True  ;3
R2(range="10M",   verified="10,0000M", error="4,1k", time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 2$R2')  #hash Meas 2$R2:  10M    ;10,0000M  ;-   ;4,1k  ;3.000000  ;True  ;3
R2(range="100M",  verified="100,000M", error="810k", time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 3$R2')  #hash Meas 3$R2:  100M   ;100,000M  ;-   ;810k  ;3.000000  ;True  ;3

Poverka.MeasurementStopCommand()
#endregion Определение погрешности измерения сопротивления 2-х проводной схемы$R2

#region Определение абсолютной погрешности измерения силы переменного тока$IAC
#description: диапазон \nизмерения,\nА;поверяемая точка, А;частота, Гц;допускаемая \nпогрешность \nизмерения, А;время задержки \nперед \nизмерением, с;переизмерять,\nДа или Нет;количество \nпереизмерений;
RFSE.Program('tree', 'set', 'select = Определение абсолютной погрешности измерения силы переменного тока$IAC')

IAC(range="1", verified="1,00000", frequency="1k",  error="1,4m",  time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 1$IAC')  #hash Meas 1$IAC: 1 ;1,00000   ;1k  ;1,4m  ;3.000000  ;True  ;3
IAC(range="3", verified="0,30000", frequency="1k",  error="4,8m",  time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 2$IAC')  #hash Meas 2$IAC: 3 ;0,30000   ;1k  ;4,8m  ;3.000000  ;True  ;3

Poverka.MeasurementStopCommand()
#endregion Определение абсолютной погрешности измерения силы переменного тока$IAC


#region Определение абсолютной погрешности при измерении постоянного тока$IDC
#description: диапазон \nизмерения,\nА;поверяемая точка, А;частота, Гц;допускаемая \nпогрешность \nизмерения, А;время задержки \nперед \nизмерением, с;переизмерять,\nДа или Нет;количество \nпереизмерений;
RFSE.Program('tree', 'set', 'select = Определение абсолютной погрешности при измерении постоянного тока$IDC')

IDC(range="10m",   verified="10,00000m",  error="7u",    time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 1$IDC')  #hash Meas 1$IDC: 10m    ;10,00000m   ;-   ;7u   ;3.000000  ;True  ;3
IDC(range="100m",  verified="100,0000m",  error="55u",   time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 2$IDC')  #hash Meas 2$IDC: 100m   ;100,0000m   ;-   ;55u  ;3.000000  ;True  ;3
IDC(range="1",     verified="1,00000",    error="1,1m",  time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 3$IDC')  #hash Meas 3$IDC: 1      ;1,00000     ;-   ;1,1m ;3.000000  ;True  ;3
IDC(range="3",     verified="2,00000",    error="3,0m",  time_delay=3.0000, remeasurement=True, remeasurement_number=3, hash='Meas 4$IDC')  #hash Meas 4$IDC: 3      ;2,00000     ;-   ;3,0m ;3.000000  ;True  ;3

Poverka.MeasurementStopCommand()
#endregion Определение абсолютной погрешности при измерении постоянного тока$IDC

RFSE.EndScript()
