from ExFluke5000Agilent34401A_Demo import ExFluke5000Agilent34401A
import RFSE
import MOSC

RFSE.Stage("*********************************************************")
RFSE.Stage("************ Measurement Fluke5520 script ***************")
RFSE.Stage("*********************************************************")
RFSE.Stage(" ")

RFSE.Stage("*********************************************************")
RFSE.Stage('**************** Null flags of system ****************')
RFSE.Stage("*********************************************************")
RFSE.Stage(" ")

Poverka = ExFluke5000Agilent34401A()
Poverka.LoadTablesHeadInfo()


def VDC(range: (str, float, int), verified: (str, float, int), error: (str, float, int), hash: str,
        remeasurement: bool = False, remeasurement_number: int = None, time_delay: (float, int) = 0):

    if MOSC.hashStatus(hash):
        Poverka.CheckConnectDevices()

        Poverka.CheckWireConnection(WireConnection='VDC')
        Poverka.MeasurementStartCommand(WireConnection='VDC')

        Poverka.TimeDelay = time_delay
        Poverka.Remeasurement = remeasurement
        Poverka.RemeasurementNumber = remeasurement_number

        Poverka.MeasurementAndReport(range=range, verified=verified, error=error, WireConnection="VDC")

        if Poverka.Status == 'Failed':
            MOSC.hash_failed()
        else:
            MOSC.hash_passed()


def VAC(range: (str, float, int), verified: (str, float, int), frequency: (str, float, int), error: (str, float, int),
        hash: str, remeasurement: bool = False, remeasurement_number: int = None, time_delay: (float, int) = 0):

    if MOSC.hashStatus(hash):

        Poverka.CheckConnectDevices()

        Poverka.CheckWireConnection(WireConnection='VAC')
        Poverka.MeasurementStartCommand(WireConnection='VAC')

        Poverka.TimeDelay = time_delay
        Poverka.Remeasurement = remeasurement
        Poverka.RemeasurementNumber = remeasurement_number

        Poverka.MeasurementAndReport(range=range, verified=verified, error=error, frequency=frequency,
                                     WireConnection="VAC")

        if Poverka.Status == 'Failed':
            MOSC.hash_failed()
        else:
            MOSC.hash_passed()


def R2(range: (str, float, int), verified: (str, float, int), error: (str, float, int), hash: str,
       remeasurement: bool = False, remeasurement_number: int = None, time_delay: (float, int) = 0):

    if MOSC.hashStatus(hash):

        Poverka.CheckConnectDevices()
        Poverka.CheckWireConnection(WireConnection='R2')
        Poverka.MeasurementStartCommand(WireConnection='R2')

        Poverka.TimeDelay = time_delay
        Poverka.Remeasurement = remeasurement
        Poverka.RemeasurementNumber = remeasurement_number

        Poverka.MeasurementAndReport(range=range, verified=verified, error=error, WireConnection="R2")

        if Poverka.Status == 'Failed':
            MOSC.hash_failed()
        else:
            MOSC.hash_passed()


def R4(range: (str, float, int), verified: (str, float, int), error: (str, float, int), hash: str,
       remeasurement: bool = False, remeasurement_number: int = None, time_delay: (float, int) = 0):

    if MOSC.hashStatus(hash):

        Poverka.CheckConnectDevices()
        Poverka.CheckWireConnection(WireConnection='R4')
        Poverka.MeasurementStartCommand(WireConnection='R4')

        Poverka.TimeDelay = time_delay
        Poverka.Remeasurement = remeasurement
        Poverka.RemeasurementNumber = remeasurement_number

        Poverka.MeasurementAndReport(range=range, verified=verified, error=error, WireConnection="R4")

        if Poverka.Status == 'Failed':
            MOSC.hash_failed()
        else:
            MOSC.hash_passed()


def IDC(range: (str, float, int), verified: (str, float, int), error: (str, float, int), hash: str,
        remeasurement: bool = False, remeasurement_number: int = None, time_delay: (float, int) = 0):
    if MOSC.hashStatus(hash):

        Poverka.CheckConnectDevices()

        Poverka.CheckWireConnection(WireConnection='IDC')
        Poverka.MeasurementStartCommand(WireConnection='IDC')

        Poverka.TimeDelay = time_delay
        Poverka.Remeasurement = remeasurement
        Poverka.RemeasurementNumber = remeasurement_number

        Poverka.MeasurementAndReport(range=range, verified=verified, error=error, WireConnection="IDC")

        if Poverka.Status == 'Failed':
            MOSC.hash_failed()
        else:
            MOSC.hash_passed()


def IAC(range: (str, float, int), verified: (str, float, int), frequency: (str, float, int), error: (str, float, int),
        hash: str, remeasurement: bool = False, remeasurement_number: int = None, time_delay: (float, int) = 0):

    if MOSC.hashStatus(hash):

        Poverka.CheckConnectDevices()

        Poverka.CheckWireConnection(WireConnection='IAC')
        Poverka.MeasurementStartCommand(WireConnection='IAC')

        Poverka.TimeDelay = time_delay
        Poverka.Remeasurement = remeasurement
        Poverka.RemeasurementNumber = remeasurement_number

        Poverka.MeasurementAndReport(range=range, verified=verified, error=error, frequency=frequency,
                                     WireConnection="IAC")

        if Poverka.Status == 'Failed':
            MOSC.hash_failed()
        else:
            MOSC.hash_passed()


#region Determining the absolute error of AC voltage measurement$VAC
#description: range of \nmeasurement,\nV;verified point, V;frequency, Hz;permissible \nmeasurement \nerror, V;delay time \nbefore \nmeasurement, s;remeasure,\nTrue or False;number of \nremeasurements
RFSE.Program('tree', 'set', 'select = Determining the absolute error of AC voltage measurement$VAC')

VAC(range="100m", verified="10,0000m",  frequency="1k",    error="46u",   time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 1$VAC')   #hash Meas 1$VAC:   100m  ;10,0000m   ;1k    ;46u   ;1.000000  ;True  ;3
VAC(range="100m", verified="100,0000m", frequency="1k",    error="100u",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 2$VAC')   #hash Meas 2$VAC:   100m  ;100,0000m  ;1k    ;100u  ;1.000000  ;True  ;3
VAC(range="100m", verified="100,0000m", frequency="50k",   error="170u",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 3$VAC')   #hash Meas 3$VAC:   100m  ;100,0000m  ;50k   ;170u  ;1.000000  ;True  ;3
VAC(range="1",    verified="1,000000",  frequency="1k",    error="900u",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 4$VAC')   #hash Meas 4$VAC:   1     ;1,000000   ;1k    ;900u  ;1.000000  ;True  ;3
VAC(range="1",    verified="1,000000",  frequency="50k",   error="1,7m",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 5$VAC')   #hash Meas 5$VAC:   1     ;1,000000   ;50k   ;1,7m  ;1.000000  ;True  ;3
VAC(range="10",   verified="10,00000",  frequency="0,01k", error="9m",    time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 6$VAC')   #hash Meas 6$VAC:   10    ;10,00000   ;0,01k ;9m    ;1.000000  ;True  ;3
VAC(range="10",   verified="10,00000",  frequency="1k",    error="9m",    time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 7$VAC')   #hash Meas 7$VAC:   10    ;10,00000   ;1k    ;9m    ;1.000000  ;True  ;3
VAC(range="10",   verified="10,00000",  frequency="50k",   error="17m",   time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 8$VAC')   #hash Meas 8$VAC:   10    ;10,00000   ;50k   ;17m   ;1.000000  ;True  ;3
VAC(range="100",  verified="100,0000",  frequency="1k",    error="90m",   time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 9$VAC')   #hash Meas 9$VAC:   100   ;100,0000   ;1k    ;90m   ;1.000000  ;True  ;3
VAC(range="100",  verified="100,0000",  frequency="50k",   error="170m",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 10$VAC')  #hash Meas 10$VAC:  100   ;100,0000   ;50k   ;170m  ;1.000000  ;True  ;3
VAC(range="750",  verified="750,000",   frequency="1k",    error="675m",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 11$VAC')  #hash Meas 11$VAC:  750   ;750,000    ;1k    ;675m  ;1.000000  ;True  ;3
VAC(range="750",  verified="750,000",   frequency="5k",    error="1275m", time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 12$VAC')  #hash Meas 12$VAC:  750   ;750,000    ;5k    ;1275m ;1.000000  ;True  ;3

Poverka.MeasurementStopCommand()
#endregion Determining the absolute error of AC voltage measurement$VAC

#region Determining the absolute error of DC voltage measurement$VDC
#description: range of \nmeasurement,\nV;verified point, V;frequency, Hz;permissible \nmeasurement \nerror, V;delay time \nbefore \nmeasurement, s;remeasure,\nTrue or False;number of \nremeasurements;
RFSE.Program('tree', 'set', 'select = Determining the absolute error of DC voltage measurement$VDC')

VDC(range='100m', verified='100,0000m',  error='8,5u', time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 1$VDC')   #hash Meas 1$VDC:  100m   ;100,0000m   ;-   ;8,5u  ;1.000000  ;True  ;3
VDC(range='100m', verified='-100,0000m', error='8,5u', time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 2$VDC')   #hash Meas 2$VDC:  100m   ;-100,0000m  ;-   ;8,5u  ;1.000000  ;True  ;3
VDC(range='1',    verified='1,000000',   error='47u',  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 3$VDC')   #hash Meas 3$VDC:  1      ;1,000000    ;-   ;47u   ;1.000000  ;True  ;3
VDC(range='1',    verified='-1,000000',  error='47u',  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 4$VDC')   #hash Meas 4$VDC:  1      ;-1,000000   ;-   ;47u   ;1.000000  ;True  ;3
VDC(range='10',   verified='10,00000',   error='400u', time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 5$VDC')   #hash Meas 5$VDC:  10     ;10,00000    ;-   ;400u  ;1.000000  ;True  ;3
VDC(range='10',   verified='-10,00000',  error='400u', time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 6$VDC')   #hash Meas 6$VDC:  10     ;-10,00000   ;-   ;400u  ;1.000000  ;True  ;3
VDC(range='100',  verified='100,0000',   error='5,1m', time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 7$VDC')   #hash Meas 7$VDC:  100    ;100,0000    ;-   ;5,1m  ;1.000000  ;True  ;3
VDC(range='100',  verified='-100,0000',  error='5,1m', time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 8$VDC')   #hash Meas 8$VDC:  100    ;-100,0000   ;-   ;5,1m  ;1.000000  ;True  ;3
VDC(range='1000', verified='1000,000',   error='55m',  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 9$VDC')   #hash Meas 9$VDC:  1000   ;1000,000    ;-   ;55m   ;1.000000  ;True  ;3
VDC(range='1000', verified='-1000,000',  error='55m',  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 10$VDC')  #hash Meas 10$VDC: 1000   ;-1000,000   ;-   ;55m   ;1.000000  ;True  ;3

Poverka.MeasurementStopCommand()
#endregion Determining the absolute error of DC voltage measurement$VDC

#region Determination of the measurement error of the resistance of a 4-wire circuit$R4
#description: range of \nmeasurement,\nOm;verified \npoint, Om;frequency, Hz;permissible \nmeasurement \nerror, Om;delay time \nbefore \nmeasurement, s;remeasure,\nTrue or False;number of \nremeasurements;
RFSE.Program('tree', 'set', 'select = Determination of the measurement error of the resistance of a 4-wire circuit$R4')

R4(range="100",  verified="100,000",   error="14m",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 1$R4')  #hash Meas 1$R4:  100    ;100,000    ;-   ;14m  ;1.000000  ;True  ;3
R4(range="1k",   verified="1,00000k",  error="110m", time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 2$R4')  #hash Meas 2$R4:  1k     ;1,00000K   ;-   ;110m ;1.000000  ;True  ;3
R4(range="10k",  verified="10,0000k",  error="1,1",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 3$R4')  #hash Meas 3$R4:  10k    ;10,0000K   ;-   ;1,1  ;1.000000  ;True  ;3
R4(range="100k", verified="100,000k",  error="11",   time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 4$R4')  #hash Meas 4$R4:  100k   ;100,000K   ;-   ;11   ;1.000000  ;True  ;3

Poverka.MeasurementStopCommand()
#endregion Determination of the measurement error of the resistance of a 4-wire circuit$R4

#region Determination of the measurement error of the resistance of a 2-wire circuit$R2
#description: range of \nmeasurement,\nOm;verified \npoint, Om;frequency, Hz;permissible \nmeasurement \nerror, Om;delay time \nbefore \nmeasurement, s;remeasure,\nTrue or False;number of \nremeasurements;
RFSE.Program('tree', 'set', 'select = Determination of the measurement error of the resistance of a 2-wire circuit$R2')

R2(range="1M",    verified="1,00000M", error="110",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 1$R2')  #hash Meas 1$R2:  1M     ;1,00000M  ;-   ;110   ;1.000000  ;True  ;3
R2(range="10M",   verified="10,0000M", error="4,1k", time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 2$R2')  #hash Meas 2$R2:  10M    ;10,0000M  ;-   ;4,1k  ;1.000000  ;True  ;3
R2(range="100M",  verified="100,000M", error="810k", time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 3$R2')  #hash Meas 3$R2:  100M   ;100,000M  ;-   ;810k  ;1.000000  ;True  ;3

Poverka.MeasurementStopCommand()
#endregion Determination of the measurement error of the resistance of a 2-wire circuit$R2

#region Determination of the absolute error of measuring the strength of alternating current$IAC
#description: range of \nmeasurement,\nA;verified point, A;frequency, Hz;permissible \nmeasurement \nerror, A;delay time \nbefore \nmeasurement, s;remeasure,\nTrue or False;number of \nremeasurements;
RFSE.Program('tree', 'set', 'select = Determination of the absolute error of measuring the strength of alternating current$IAC')

IAC(range="1", verified="1,00000", frequency="1k",  error="1,4m",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 1$IAC')  #hash Meas 1$IAC: 1 ;1,00000   ;1k  ;1,4m  ;1.000000  ;True  ;3
IAC(range="3", verified="0,30000", frequency="1k",  error="4,8m",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 2$IAC')  #hash Meas 2$IAC: 3 ;0,30000   ;1k  ;4,8m  ;1.000000  ;True  ;3

Poverka.MeasurementStopCommand()
#endregion Determination of the absolute error of measuring the strength of alternating current$IAC


#region Determination of the absolute error in the measurement of direct current$IDC
#description: range of \nmeasurement,\nA;verified point, A;frequency, Hz;permissible \nmeasurement \nerror, A;delay time \nbefore \nmeasurement, s;remeasure,\nTrue or False;number of \nremeasurements;
RFSE.Program('tree', 'set', 'select = Determination of the absolute error in the measurement of direct current$IDC')

IDC(range="10m",   verified="10,00000m",  error="7u",    time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 1$IDC')  #hash Meas 1$IDC: 10m    ;10,00000m   ;-   ;7u   ;1.000000  ;True  ;3
IDC(range="100m",  verified="100,0000m",  error="55u",   time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 2$IDC')  #hash Meas 2$IDC: 100m   ;100,0000m   ;-   ;55u  ;1.000000  ;True  ;3
IDC(range="1",     verified="1,00000",    error="1,1m",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 3$IDC')  #hash Meas 3$IDC: 1      ;1,00000     ;-   ;1,1m ;1.000000  ;True  ;3
IDC(range="3",     verified="2,00000",    error="3,0m",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hash='Meas 4$IDC')  #hash Meas 4$IDC: 3      ;2,00000     ;-   ;3,0m ;1.000000  ;True  ;3

Poverka.MeasurementStopCommand()
#endregion Determination of the absolute error in the measurement of direct current$IDC

RFSE.EndScript()
