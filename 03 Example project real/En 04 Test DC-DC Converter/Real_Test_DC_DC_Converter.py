import time

import MGPH
import RFSE
import MFRT
import MOSC
import MTLG


class DemoTestIoTMeasurement:

    def __init__(self):
        self.FirstScriptStart, self.FirstResult, self.ContinueMeasurement = True, True, True
        self.WireConnection, self.NameGraph, self.status = str(), str(), str()
        self.TimeDelay = 0
        self.OutCommand, self.GraphInit, self.FailedResult = False, False, False
        self.AutomaticBK1697B, self.AutomaticAPPA207, self.Simulation = False, False, False
        self.ListResult, self.ListStabilization, self.ListOperatingRange = list(), list(), list()
        self.ChangeOperatingRange = False
        self.Error = 0
        self.__init_connected_and_type_connected()

########################################################################################################################
########################################################################################################################
########################################## Module measurement and report ###############################################
########################################################################################################################
########################################################################################################################

    def MeasurementAndReport(
            self,
            value: (str | float | int),
            range_value: (str | float | int),
            allowable_stabilization_factor: (float | int),
            is_operating_range: bool,
            hash: str,
            WireConnection :str,

    ) -> None:

        """
            Calculation and reporting function
        """
        name_table = hash.split('$')[1]
        number_measurement = hash.split('$')[0][5:]

        self.Error = float((100 + allowable_stabilization_factor) / 100)
        
        self.ContinueMeasurement = True

        self.AddOperationValueGraph(is_operating_range=is_operating_range, WireConnection=WireConnection)

        f_value = MFRT.ConvertStringToFloat(value)

        RFSE.Stage(f"{WireConnection} Measure -> value = {value}, range_value = {range_value}, "
                   f"allowable_stabilization_factor = {allowable_stabilization_factor}")

#######################################################################################################################
#####################################################  VDC  ###########################################################
#######################################################################################################################

        if WireConnection == 'VDC':

#######################################################################################################################
###################################################  VDC MEAS  ########################################################
#######################################################################################################################

            if self.Simulation:
                RFSE.Stage(f"name -> BK1697B; mode -> set; command -> VDC = {value}", 'driver')
            elif self.AutomaticBK1697B:
                RFSE.Driver('BK1697B', 'set', f'VDC = {value}')
            else:
                RFSE.Messenger("set", "Make settings BK1697B#TestIoT.png", "Make settings:\n"
                                                                           f"Set VDC = {value}\n"
                                                                           "Press OK")

            result, stabilization_factor = self.GetResultMeasurent(
                value=f_value,
                allowable_stabilization_factor=allowable_stabilization_factor)

#######################################################################################################################
##################################################  VDC REPORT  #######################################################
#######################################################################################################################

            RFSE.Report(name_table, "set", "table", 
                        f"{number_measurement};"
                        f"{value};"
                        f"{result};"
                        f"{allowable_stabilization_factor};"
                        f"{is_operating_range};"
                        f"{stabilization_factor};"
                        f"{self.status};")

            RFSE.Stage(" ")

#######################################################################################################################
####################################################  IDC  ############################################################
#######################################################################################################################

        elif WireConnection == 'IDC':

#######################################################################################################################
#################################################  IDC MEAS  ##########################################################`
#######################################################################################################################

            if self.Simulation:
                RFSE.Stage(f"name -> BK1697B; mode -> set; command -> IDC = {value}", 'driver')
            elif self.AutomaticBK1697B:
                RFSE.Driver('BK1697B', 'set', f'IDC = {value}')
            else:
                RFSE.Messenger("set", "Make settings BK1697B#TestIoT.png", "Make settings:\n"
                                                                           f"Set IDC = {value}\n"
                                                                           "Press OK")

            result, stabilization_factor = self.GetResultMeasurent(
                value=f_value,
                allowable_stabilization_factor=allowable_stabilization_factor)

#######################################################################################################################
####################################################  IDC REPORT  #####################################################
#######################################################################################################################

            RFSE.Report(name_table, "set", "table",
                        f"{number_measurement};"
                        f"{value};"
                        f"{result};"
                        f"{allowable_stabilization_factor};"
                        f"{is_operating_range};"
                        f"{stabilization_factor};"
                        f"{self.status};")
            
            RFSE.Stage(" ")

########################################################################################################################
########################################################################################################################
########################################  Module return result measurement  ############################################
########################################################################################################################
########################################################################################################################
    def GetResultMeasurent(
            self,
            value: (float | int),
            allowable_stabilization_factor: (float | int),

    ) -> tuple:

        f_result, result, stabilization_factor = 0, 0, 0
        while self.ContinueMeasurement:
            time.sleep(self.TimeDelay)
            if self.Simulation:
                RFSE.Stage(f"name -> APPA207; mode -> get; command -> read", 'driver')
                result = value
            elif self.AutomaticAPPA207:
                result = RFSE.Driver('APPA207', 'get', 'read')
            else:
                result = RFSE.Messenger("get", "Input result#@notes",
                                        "Enter the measured result from APPA207\nPress OK", "string")
            RFSE.Stage(" ")
            f_result = MFRT.ConvertStringToFloat(result)
            
            if isinstance(f_result, str):
                continue
                
            stabilization_factor = round((value - f_result) / value, 3) if value != 0 and f_result != 0 else 0
            self.ListStabilization.append(stabilization_factor + 1)
            
            if stabilization_factor > allowable_stabilization_factor:
                self.status = 'Failed'
            else:
                self.status = 'OK'
            self.ContinueMeasurement = False

        self.ListResult.append(f_result)
        return result, stabilization_factor

########################################################################################################################
########################################################################################################################
##################################### Module check wire connection devices #############################################
########################################################################################################################
########################################################################################################################

    def CheckWireConnection(self, WireConnection: str) -> None:

        """
            Function check type wire connection
            :param WireConnection: type wire connection
            :return: None
        """
        if self.WireConnection != 'VDC':
            if WireConnection == 'VDC':
                MTLG.TelegramMessenger('beta', 'set', 'Testing VDC',
                                       'Connect a BK1697 to the APPA207 to check VDC voltage.\n'
                                       'Calibrator output OUT', 'string')
                RFSE.Messenger('set', 'Testing VDC#TestIoT_VDC.png',
                               'Connect a BK1697 to the APPA207 to check VDC voltage.\n'
                               'Calibrator output OUT')
        if self.WireConnection != "IDC":
            if WireConnection == 'IDC':
                MTLG.TelegramMessenger('beta', 'set', 'Testing IDC',
                                       'Connect a BK1697 to the APPA207 to check '
                                       'IDC currenty.\nCalibrator output OUT', 'string')

                RFSE.Messenger('set', 'Testing IDC#TestIoT_IDC.png',
                               'Connect a BK1697 to the APPA207 to check IDC currenty.\n'
                               'Calibrator output OUT')

        self.WireConnection = WireConnection
        RFSE.Stage(' ')

########################################################################################################################
########################################################################################################################
############################################# Module connected devices #################################################
########################################################################################################################
########################################################################################################################

    def CheckConnectDevices(self) -> None:

        if self.FirstScriptStart:
            self.InitializationBK1697B(init=False)
            self.InitializationAPPA207(init=False)
            self.FirstScriptStart = False

########################################################################################################################
########################################################################################################################
########################################################################################################################

    def InitializationBK1697B(self, init: bool = True) -> None:

        RFSE.Stage("*********************************************************")
        RFSE.Stage("***************** Init device BK1697B *******************")
        RFSE.Stage("*********************************************************")
        RFSE.Stage(" ")

        if not self.Simulation:
            type_setting_BK1697B = RFSE.Messenger("get", "Choose a way to connect BK1697B#TestIoT.png",
                                                  "Please select an BK1697B instrument setup type\n"
                                                  "Attention. By selecting simulation mode, "
                                                  "you run all measurements in simulation mode!!!",
                                                  "choice=Automatic;Manual;Simulation")
        else:
            type_setting_BK1697B = 'Simulation'

        RFSE.Report("TYPE_SETTING_BK1697B", "info", "string", "Device setting type")
        RFSE.Stage(" ")

        if type_setting_BK1697B == 'Automatic':
            choices = None
            BK1697B_INIT = RFSE.Driver('BK1697B', 'init', '')
            if BK1697B_INIT != 'connected':
                choices = RFSE.Messenger("get", "BK1697B initialization not successful#@attention",
                                         "Failed to initialize BK1697B. Do you want to continue measuring in "
                                         "Manual mode?", "boolean")
            if not choices:
                self.AutomaticBK1697B = True
                RFSE.Report("TYPE_SETTING_BK1697B", "set", 'string', 'Automatic')
            else:
                type_setting_BK1697B = 'Manual'

        if type_setting_BK1697B == 'Manual':
            self.AutomaticBK1697B = False
            RFSE.Report("TYPE_SETTING_BK1697B", "set", 'string', 'Manual')
            RFSE.Messenger("set", "Make settings BK1697B#TestIoT.png", "Make settings:\n"
                                                                       "Turn on the device\n"
                                                                       "Press OK")

        elif type_setting_BK1697B == 'Simulation':
            self.Simulation = True
            RFSE.Report("TYPE_SETTING_BK1697B", "set", 'string', 'Simulation')
            RFSE.Stage('Driver: BK1697B >> mode: init >> command: ', 'driver')
            
########################################################################################################################
        
        if init:
            if self.AutomaticBK1697B or self.Simulation:
                RFSE.Report('DevicesUsed', 'set', 'table', 'BK1697B;Connected;')
                MOSC.hash_passed()
            else:
                RFSE.Report('DevicesUsed', 'set', 'table', 'BK1697B;Disconnected;')
                MOSC.hash_failed()

########################################################################################################################
########################################################################################################################
########################################################################################################################

    def InitializationAPPA207(self, init: bool = True) -> None:

        RFSE.Stage("*********************************************************")
        RFSE.Stage("**************** Init device APPA207 ********************")
        RFSE.Stage("*********************************************************")
        RFSE.Stage(" ")

        if not self.Simulation:
            type_setting_APPA207 = RFSE.Messenger("get", "Choose a way to connect APPA207#TestIoT.png",
                                                         "Please select an APPA207 instrument setup type\n"
                                                         "Attention. By selecting simulation mode, "
                                                         "you run all measurements in simulation mode!!!",
                                                         "choice=Automatic;Manual;Simulation")
        else:
            type_setting_APPA207 = 'Simulation'

        RFSE.Report("TYPE_SETTING_APPA207", "info", "string", "Device setting type")
        RFSE.Stage(" ")

        if type_setting_APPA207 == 'Automatic':

            choices = None
            APPA207_INIT = RFSE.Driver('APPA207', 'init', '')
            if APPA207_INIT != 'connected':
                self.AutomaticAPPA207 = True
                RFSE.Report("TYPE_SETTING_APPA207", "set", "string", "Automatic")
                choices = RFSE.Messenger("get", "APPA207 initialization not successful#@attention",
                                         "Failed to initialize APPA207. Do you want to continue measuring in "
                                         "Manual mode?", "boolean")
            if not choices:
                self.AutomaticAPPA207 = True
                RFSE.Report("TYPE_SETTING_APPA207", "set", 'string', 'Automatic')
            else:
                type_setting_APPA207 = 'Manual'

        if type_setting_APPA207 == 'Manual':
            self.AutomaticAPPA207 = False
            RFSE.Report("TYPE_SETTING_APPA207", "set", "string", "Manual")
            RFSE.Messenger("set", "Make settings APPA207#TestIoT.png", "Make settings:\n"
                                                                       "Turn on the device\n"
                                                                       "Press OK")
        elif type_setting_APPA207 == 'Simulation':
            self.Simulation = True
            RFSE.Report("TYPE_SETTING_APPA207", "set", "string", "Simulation")
            RFSE.Stage('Driver: APPA207 >> mode: init >> command: ', 'driver')
            
########################################################################################################################
        
        if init:
            if self.AutomaticAPPA207 or self.Simulation:
                RFSE.Report('DevicesUsed', 'set', 'table', 'APPA207;Connected;')
                MOSC.hash_passed()
            else:
                RFSE.Report('DevicesUsed', 'set', 'table', 'APPA207;Disconnected;')
                MOSC.hash_failed()

########################################################################################################################
########################################################################################################################
########################################### Module for working with Graph ##############################################
########################################################################################################################
########################################################################################################################

    def CheckGraphInit(self) -> None:
        """
            Function check initialization Graph
            :return: None
        """
        if not self.GraphInit:
            RFSE.Stage("*********************************************************")
            RFSE.Stage("***************** Init module Graph   *******************")
            RFSE.Stage("*********************************************************")
            RFSE.Stage(" ")
            MGPH.GraphInit()
            self.GraphInit = True
            time.sleep(5)
            RFSE.Stage(" ")

########################################################################################################################
########################################################################################################################
########################################################################################################################

    def CreateGraph(self, WireConnection: str) -> None:
        """
            Function initialization functions create a Graph
            :return: None
        """
        self.CreateGraphOperationRange()
        self.CreateGraphStabilization(WireConnection=WireConnection)
        self.CreateGraphResult()
        self.FirstResult = False

########################################################################################################################
########################################################################################################################
########################################################################################################################

    def CreateGraphMask(self, range_value: int) -> None:
        """
            Create mask Graph
            :param range_value: coordinate value Ox
            :return: None
        """
        if self.FirstResult:
            RFSE.Stage("*********************************************************")
            RFSE.Stage("***************** Create Graph mask  ********************")
            RFSE.Stage("*********************************************************")
            RFSE.Stage(" ")
            MGPH.ClearGraph()
            Value_OyOx = [0, range_value, 0, 40]
            Name_Oy = "Amplitude"
            Name_Ox = " Iteration"
            Autoscale = "No"
            MGPH.AddGraphSett(Value_OyOx, Name_Oy, Name_Ox, Autoscale)
            RFSE.Stage(" ")

########################################################################################################################
########################################################################################################################
########################################################################################################################

    def CreateGraphOperationRange(self) -> None:
        """
            Function to create a Graph by operation range
            :return: None
        """
        RFSE.Stage("*********************************************************")
        RFSE.Stage("************ Create Graph a operation range *************")
        RFSE.Stage("*********************************************************")
        RFSE.Stage(" ")
        name_graph_plus = f'Operation range {self.NameGraph}'
        ArrOy_plus = [self.ListOperatingRange[x][0] for x in range(len(self.ListOperatingRange))]
        numLine_plus = name_graph_plus
        ArrOx = [self.ListOperatingRange[x][1] for x in range(len(self.ListOperatingRange))]
        LineWidth = "3"
        Color = "1A76D9"
        Visible = "Yes"
        if self.FirstResult:
            MGPH.AddLine(name_graph_plus, ArrOy_plus, ArrOx, LineWidth, Color, Visible)
        else:
            MGPH.ChangeLine(numLine_plus, name_graph_plus, ArrOy_plus, ArrOx, LineWidth, Color, Visible)
        RFSE.Stage(" ")

########################################################################################################################
########################################################################################################################
########################################################################################################################

    def CreateGraphStabilization(self, WireConnection: str) -> None:
        """
            Function to create a Graph by stabilization coefficient
            :return: None
        """
        RFSE.Stage("*********************************************************")
        RFSE.Stage("******** Create Graph a stabilization coefficient *******")
        RFSE.Stage("*********************************************************")
        RFSE.Stage(" ")
        name_graph_plus = f'Stabilization {self.NameGraph}'
        ArrOy_plus = [x * 20 if WireConnection == "VDC" else x * 2.5 for x in self.ListStabilization]
        numLine_plus = name_graph_plus
        ArrOx = [x for x in range(len(self.ListStabilization))]
        LineWidth = "3"
        Color = "FF0000"
        Visible = "Yes"
        if self.FirstResult:
            MGPH.AddLine(name_graph_plus, ArrOy_plus, ArrOx, LineWidth, Color, Visible)
        else:
            MGPH.ChangeLine(numLine_plus, name_graph_plus, ArrOy_plus, ArrOx, LineWidth, Color, Visible)
        RFSE.Stage(" ")

########################################################################################################################
########################################################################################################################
########################################################################################################################

    def CreateGraphResult(self) -> None:
        """
            Function to create a Graph by result
            :return: None
        """
        RFSE.Stage("*********************************************************")
        RFSE.Stage("************* Create Graph a result value ***************")
        RFSE.Stage("*********************************************************")
        RFSE.Stage(" ")
        name = f'{self.NameGraph}_result'
        numLine = name
        ArrOy = self.ListResult
        ArrOx = [x for x in range(len(self.ListResult))]
        LineWidth = "3"
        Color = "0"
        Visible = "Yes"
        if self.FirstResult:
            MGPH.AddLine(name, ArrOy, ArrOx, LineWidth, Color, Visible)
        else:
            MGPH.ChangeLine(numLine, name, ArrOy, ArrOx, LineWidth, Color, Visible)

########################################################################################################################
########################################################################################################################
########################################################################################################################

    def GetScreenshot(self) -> None:
        """
            Function create screenshot Graph, save screenshot in Word and clear Graph
            :return: None
        """
        RFSE.Stage("*********************************************************")
        RFSE.Stage("************* Getting a screenshot Graph ****************")
        RFSE.Stage("*********************************************************")
        RFSE.Stage(" ")
        screen = MGPH.GetScreenshotGraph()
        RFSE.Stage(f"name: {self.NameGraph} >> mode: set >> kind: picture >> data: screen", "Report")
        RFSE.Stage(" ")
        RFSE.Report(self.NameGraph, 'set', 'picture', screen)
        self.NameGraph = None
        MGPH.ClearGraph()
        self.ListStabilization, self.ListResult, self.ListOperatingRange = list(), list(), list()
        RFSE.Stage(" ")

########################################################################################################################
########################################################################################################################
################################### Module driver BK1697B set output ON or OFF #########################################
########################################################################################################################
########################################################################################################################

    def OutONNCommand(self) -> None:
        """
            BK1697B output check function ON
            :return: None
        """
        if not self.OutCommand:
            self.OutCommand = True
            if self.Simulation:
                RFSE.Stage('name -> BK1697B; mode -> set; command -> OUTPUT = ON', 'set')
            elif self.AutomaticBK1697B:
                RFSE.Driver('BK1697B', 'set', 'OUTPUT = ON')
            else:
                RFSE.Messenger("set", "Make settings BK1697B#TestIoT.png", "Make settings:\n"
                                                                           "Set OUTPUT = ON\n"
                                                                           "Press OK")
            RFSE.Stage(" ")

########################################################################################################################
########################################################################################################################
########################################################################################################################

    def SET_OUTPUT_OFF(self):
        """
            BK1697B output set function OUT
            :return: None
        """
        self.OutCommand = False
        self.FirstResult = True
        self.ChangeOperatingRange = False
        if self.Simulation:
            RFSE.Stage('name -> BK1697B; mode -> set; command -> OUTPUT = OFF', 'set')
        elif self.AutomaticBK1697B:
            RFSE.Driver('BK1697B', 'set', 'OUTPUT = OFF')
        else:
            RFSE.Messenger("set", "Make settings BK1697B#TestIoT.png", "Make settings:\n"
                                                                       "Set OUTPUT = OFF\n"
                                                                       "Press OK")


########################################################################################################################
########################################################################################################################
######################################## Module load tables in RFSE.Reports ############################################
########################################################################################################################
########################################################################################################################

    @staticmethod
    def LoadTablesHeadInfo() -> None:

        RFSE.Report(name='VDC', mode='info', kind='table', data="NumberMeasurement#150;"
                                                                "InputValue#75;"
                                                                "OutputValue#75;"
                                                                "AllowableStabilizationFactor#170;"
                                                                "IsOperatingRange#120;"
                                                                "StabilizationFactor#110;"
                                                                "Status#75;")

        RFSE.Report(name='IDC', mode='info', kind='table', data="NumberMeasurement#150;"
                                                                "InputValue#75;"
                                                                "OutputValue#75;"
                                                                "AllowableStabilizationFactor#170;"
                                                                "IsOperatingRange#120;"
                                                                "StabilizationFactor#110;"
                                                                "Status#75;")
        RFSE.Stage(" ")

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################

    def AddOperationValueGraph(self, is_operating_range: bool, WireConnection: str) -> None:

        max_value_graph_operating = 40 if WireConnection == 'VDC' else 5

        if self.ChangeOperatingRange != is_operating_range:
            self.ChangeOperatingRange = is_operating_range
            if is_operating_range is True:
                self.ListOperatingRange.append((0, len(self.ListResult)))
                self.ListOperatingRange.append((max_value_graph_operating, len(self.ListResult)))
            else:
                self.ListOperatingRange.append((max_value_graph_operating, len(self.ListResult)))
                self.ListOperatingRange.append((0, len(self.ListResult)))
        else:
            self.ListOperatingRange.append(
                (0 if not self.ChangeOperatingRange else max_value_graph_operating, len(self.ListResult)))


########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################

    def __init_connected_and_type_connected(self) -> None:
        type_setting_BK1697B = RFSE.Report("TYPE_SETTING_BK1697B", "get", "string", "", 'string')
        type_setting_APPA207 = RFSE.Report("TYPE_SETTING_APPA207", "get", "string", "", 'string')

        if len(type_setting_BK1697B) == 0 or len(type_setting_APPA207) == 0:
            self.FirstScriptStart = True
            self.Simulation = False
            return
        else:
            self.FirstScriptStart = False

        if 'Simulation' in [type_setting_BK1697B, type_setting_APPA207]:
            self.Simulation = True
            return
        else:
            self.Simulation = False

        if type_setting_BK1697B == 'Automatic':
            self.AutomaticBK1697B = True
        else:
            self.AutomaticBK1697B = False

        if type_setting_APPA207 == 'Automatic':
            self.AutomaticAPPA207 = True
        else:
            self.AutomaticAPPA207 = False


Testing = DemoTestIoTMeasurement()
