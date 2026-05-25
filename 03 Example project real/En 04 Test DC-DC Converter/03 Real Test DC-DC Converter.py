import RFSE
from MOSC import hashstatus, hash_passed, hash_failed
from Real_Test_DC_DC_Converter import Testing
import MTLG
MTLG.TelegramProgram('alpha', 'Measurement script', 'set', 'init', 'string')
RFSE.Stage("*********************************************************")
RFSE.Stage("****************** Measurement script *******************")
RFSE.Stage("*********************************************************")
RFSE.Stage(" ")
RFSE.Stage("*********************************************************")
RFSE.Stage('**************** Null flags of system ****************')
RFSE.Stage("*********************************************************")
RFSE.Stage(" ")
Testing.LoadTablesHeadInfo()
Testing.SET_OUTPUT_OFF()


def VDC(
        value: (str | float | int),
        range_value: (str | float | int),
        allowable_stabilization_factor: (float | int),
        is_operating_range: bool,
        hash: str,
        time_delay: (float | int) = 0.0

) -> None:

    if hashstatus(hash):

        Testing.CheckConnectDevices()

        Testing.CheckWireConnection(WireConnection='VDC')

        Testing.OutONNCommand()
        Testing.CheckGraphInit()
        Testing.CreateGraphMask(range_value=range_value)

        Testing.TimeDelay = time_delay

        Testing.MeasurementAndReport(value=value, range_value=range_value, is_operating_range=is_operating_range,
                                     allowable_stabilization_factor=allowable_stabilization_factor, hash=hash,
                                     WireConnection='VDC')

        Testing.CreateGraph(WireConnection='VDC')

        if Testing.status == 'Failed':
            hash_failed()
        else:
            hash_passed()


def IDC(
        value: (str | float | int),
        range_value: (str | float | int),
        allowable_stabilization_factor: (float | int),
        is_operating_range: bool,
        hash: str,
        time_delay: (int, float) = 0.0

) -> None:

    if hashstatus(hash):

        Testing.CheckConnectDevices()

        Testing.CheckWireConnection(WireConnection='IDC')

        Testing.OutONNCommand()
        Testing.CheckGraphInit()
        Testing.CreateGraphMask(range_value=range_value)

        Testing.TimeDelay = time_delay

        Testing.MeasurementAndReport(value=value, range_value=range_value, is_operating_range=is_operating_range,
                                     allowable_stabilization_factor=allowable_stabilization_factor, hash=hash, 
                                     WireConnection='IDC')

        Testing.CreateGraph(WireConnection='IDC')

        if Testing.status == 'Failed':
            hash_failed()
        else:
            hash_passed()

#region Voltage measurement$VDC
#description: value \nmeasurement, V;range value, V;allowable\nstabilization\nfactor;is operating\nrange,\nTrue or False;delay time \nbefore \nmeasurement, s;
RFSE.Program('tree', 'set', 'select = Voltage measurement$VDC')

RFSE.Stage('Set NameGraph => VDC_GRAPH')
Testing.NameGraph = 'VDC_GRAPH'
RFSE.Stage(" ")

VDC(value=1,   range_value=40, allowable_stabilization_factor=0,   is_operating_range=False, time_delay=3, hash='Meas 1$VDC')   #hash Meas 1$VDC:   1  ;40  ;0    ;False;3.000
VDC(value=1,   range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hash='Meas 2$VDC')   #hash Meas 2$VDC:   1  ;40  ;0.1  ;False;3.000
VDC(value=2,   range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hash='Meas 3$VDC')   #hash Meas 3$VDC:   2  ;40  ;0.1  ;False;3.000
VDC(value=3,   range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hash='Meas 4$VDC')   #hash Meas 4$VDC:   3  ;40  ;0.1  ;False;3.000
VDC(value=4,   range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hash='Meas 5$VDC')   #hash Meas 5$VDC:   4  ;40  ;0.1  ;False;3.000
VDC(value=5,   range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hash='Meas 6$VDC')   #hash Meas 6$VDC:   5  ;40  ;0.1  ;False;3.000
VDC(value=6,   range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hash='Meas 7$VDC')   #hash Meas 7$VDC:   6  ;40  ;0.1  ;False;3.000
VDC(value=7,   range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hash='Meas 8$VDC')   #hash Meas 8$VDC:   7  ;40  ;0.1  ;False;3.000
VDC(value=8,   range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hash='Meas 9$VDC')   #hash Meas 9$VDC:   8  ;40  ;0.1  ;False;3.000
VDC(value=9,   range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hash='Meas 10$VDC')  #hash Meas 10$VDC:  9  ;40  ;0.1  ;False;3.000
VDC(value=10,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3, hash='Meas 11$VDC')  #hash Meas 11$VDC:  10 ;40  ;0.1  ;True ;3.000
VDC(value=11,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3, hash='Meas 12$VDC')  #hash Meas 12$VDC:  11 ;40  ;0.1  ;True ;3.000
VDC(value=12,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3, hash='Meas 13$VDC')  #hash Meas 13$VDC:  12 ;40  ;0.1  ;True ;3.000
VDC(value=13,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3, hash='Meas 14$VDC')  #hash Meas 14$VDC:  13 ;40  ;0.1  ;True ;3.000
VDC(value=14,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3, hash='Meas 15$VDC')  #hash Meas 15$VDC:  14 ;40  ;0.1  ;True ;3.000
VDC(value=15,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3, hash='Meas 16$VDC')  #hash Meas 16$VDC:  15 ;40  ;0.1  ;True ;3.000
VDC(value=16,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3, hash='Meas 17$VDC')  #hash Meas 17$VDC:  16 ;40  ;0.1  ;True ;3.000
VDC(value=17,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3, hash='Meas 18$VDC')  #hash Meas 18$VDC:  17 ;40  ;0.1  ;True ;3.000
VDC(value=18,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3, hash='Meas 19$VDC')  #hash Meas 19$VDC:  18 ;40  ;0.1  ;True ;3.000
VDC(value=19,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3, hash='Meas 20$VDC')  #hash Meas 20$VDC:  19 ;40  ;0.1  ;True ;3.000
VDC(value=20,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3, hash='Meas 21$VDC')  #hash Meas 21$VDC:  20 ;40  ;0.1  ;True ;3.000
VDC(value=21,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3, hash='Meas 22$VDC')  #hash Meas 22$VDC:  21 ;40  ;0.1  ;True ;3.000
VDC(value=22,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hash='Meas 23$VDC')  #hash Meas 23$VDC:  22 ;40  ;0.1  ;False;3.000
VDC(value=23,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hash='Meas 24$VDC')  #hash Meas 24$VDC:  23 ;40  ;0.1  ;False;3.000
VDC(value=24,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hash='Meas 25$VDC')  #hash Meas 25$VDC:  24 ;40  ;0.1  ;False;3.000
VDC(value=25,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hash='Meas 26$VDC')  #hash Meas 26$VDC:  25 ;40  ;0.1  ;False;3.000
VDC(value=26,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hash='Meas 27$VDC')  #hash Meas 27$VDC:  26 ;40  ;0.1  ;False;3.000
VDC(value=27,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hash='Meas 28$VDC')  #hash Meas 28$VDC:  27 ;40  ;0.1  ;False;3.000
VDC(value=28,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hash='Meas 29$VDC')  #hash Meas 29$VDC:  28 ;40  ;0.1  ;False;3.000
VDC(value=29,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hash='Meas 30$VDC')  #hash Meas 30$VDC:  29 ;40  ;0.1  ;False;3.000
VDC(value=30,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hash='Meas 31$VDC')  #hash Meas 31$VDC:  30 ;40  ;0.1  ;False;3.000
VDC(value=31,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hash='Meas 32$VDC')  #hash Meas 32$VDC:  31 ;40  ;0.1  ;False;3.000
VDC(value=32,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hash='Meas 33$VDC')  #hash Meas 33$VDC:  32 ;40  ;0.1  ;False;3.000
VDC(value=33,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hash='Meas 34$VDC')  #hash Meas 34$VDC:  33 ;40  ;0.1  ;False;3.000
VDC(value=34,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hash='Meas 35$VDC')  #hash Meas 35$VDC:  34 ;40  ;0.1  ;False;3.000
VDC(value=35,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hash='Meas 36$VDC')  #hash Meas 36$VDC:  35 ;40  ;0.1  ;False;3.000

Testing.GetScreenshot()
Testing.SET_OUTPUT_OFF()
#endregion Voltage measurement$VDC

#region Current measurement$IDC
#description: value \nmeasurement, A;range value, A;allowable\nstabilization\nfactor;is operating\nrange,\nTrue or False;delay time \nbefore \nmeasurement, s;
RFSE.Program('tree', 'set', 'select = Current measurement$IDC')

RFSE.Stage('Set NameGraph => IDC_GRAPH')
Testing.NameGraph = 'IDC_GRAPH'

IDC(value=0.01, range_value=5, allowable_stabilization_factor=0,   is_operating_range=False, time_delay=3,   hash='Meas 1$IDC')   #hash Meas 1$IDC:  0.01 ;5  ;0    ;False;3.000
IDC(value=0.1,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hash='Meas 2$IDC')   #hash Meas 2$IDC:  0.1  ;5  ;0.1  ;False;3.000
IDC(value=0.2,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hash='Meas 3$IDC')   #hash Meas 3$IDC:  0.2  ;5  ;0.1  ;False;3.000
IDC(value=0.3,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hash='Meas 4$IDC')   #hash Meas 4$IDC:  0.3  ;5  ;0.1  ;False;3.000
IDC(value=0.4,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hash='Meas 5$IDC')   #hash Meas 5$IDC:  0.4  ;5  ;0.1  ;False;3.000
IDC(value=0.5,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hash='Meas 6$IDC')   #hash Meas 6$IDC:  0.5  ;5  ;0.1  ;False;3.000
IDC(value=0.6,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hash='Meas 7$IDC')   #hash Meas 7$IDC:  0.6  ;5  ;0.1  ;False;3.000
IDC(value=0.7,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hash='Meas 8$IDC')   #hash Meas 8$IDC:  0.7  ;5  ;0.1  ;False;3.000
IDC(value=0.8,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hash='Meas 9$IDC')   #hash Meas 9$IDC:  0.8  ;5  ;0.1  ;False;3.000
IDC(value=0.9,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hash='Meas 10$IDC')  #hash Meas 10$IDC: 0.9  ;5  ;0.1  ;False;3.000
IDC(value=1.0,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3,   hash='Meas 11$IDC')  #hash Meas 11$IDC: 1.0  ;5  ;0.1  ;True ;3.000
IDC(value=1.1,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3,   hash='Meas 12$IDC')  #hash Meas 12$IDC: 1.1  ;5  ;0.1  ;True ;3.000
IDC(value=1.2,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3,   hash='Meas 13$IDC')  #hash Meas 13$IDC: 1.2  ;5  ;0.1  ;True ;3.000
IDC(value=1.3,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3,   hash='Meas 14$IDC')  #hash Meas 14$IDC: 1.3  ;5  ;0.1  ;True ;3.000
IDC(value=1.4,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3,   hash='Meas 15$IDC')  #hash Meas 15$IDC: 1.4  ;5  ;0.1  ;True ;3.000
IDC(value=1.5,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3,   hash='Meas 16$IDC')  #hash Meas 16$IDC: 1.5  ;5  ;0.1  ;True ;3.000
IDC(value=1.6,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3,   hash='Meas 17$IDC')  #hash Meas 17$IDC: 1.6  ;5  ;0.1  ;True ;3.000
IDC(value=1.7,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3,   hash='Meas 18$IDC')  #hash Meas 18$IDC: 1.7  ;5  ;0.1  ;True ;3.000
IDC(value=1.8,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3,   hash='Meas 19$IDC')  #hash Meas 19$IDC: 1.8  ;5  ;0.1  ;True ;3.000
IDC(value=1.9,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3,   hash='Meas 20$IDC')  #hash Meas 20$IDC: 1.9  ;5  ;0.1  ;True ;3.000
IDC(value=2.0,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3,   hash='Meas 21$IDC')  #hash Meas 21$IDC: 2.0  ;5  ;0.1  ;True ;3.000
IDC(value=2.1,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3,   hash='Meas 22$IDC')  #hash Meas 22$IDC: 2.1  ;5  ;0.1  ;True ;3.000
IDC(value=2.2,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hash='Meas 23$IDC')  #hash Meas 23$IDC: 2.2  ;5  ;0.1  ;False;3.000
IDC(value=2.3,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hash='Meas 24$IDC')  #hash Meas 24$IDC: 2.3  ;5  ;0.1  ;False;3.000
IDC(value=2.4,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hash='Meas 25$IDC')  #hash Meas 25$IDC: 2.4  ;5  ;0.1  ;False;3.000
IDC(value=2.5,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hash='Meas 26$IDC')  #hash Meas 26$IDC: 2.5  ;5  ;0.1  ;False;3.000
IDC(value=2.6,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hash='Meas 27$IDC')  #hash Meas 27$IDC: 2.6  ;5  ;0.1  ;False;3.000
IDC(value=2.7,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hash='Meas 28$IDC')  #hash Meas 28$IDC: 2.7  ;5  ;0.1  ;False;3.000
IDC(value=2.8,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hash='Meas 29$IDC')  #hash Meas 29$IDC: 2.8  ;5  ;0.1  ;False;3.000
IDC(value=2.9,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hash='Meas 30$IDC')  #hash Meas 30$IDC: 2.9  ;5  ;0.1  ;False;3.000
IDC(value=3.0,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hash='Meas 31$IDC')  #hash Meas 31$IDC: 3.0  ;5  ;0.1  ;False;3.000

Testing.GetScreenshot()
Testing.SET_OUTPUT_OFF()
#endregion Current measurement$IDC

RFSE.Stage(" ")
RFSE.Stage('name: Graph >> mode: close >> command: ', 'Plugin')
RFSE.Plugin("Graph", 'close', '')
RFSE.EndScript()
