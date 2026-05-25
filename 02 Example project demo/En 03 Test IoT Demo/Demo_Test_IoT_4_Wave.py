import time

import MGPH
import RFSE
import MFRT
import MOSC
import MTLG


class DemoTestIoTMeasurement:

    def __init__(self):
        self.FirstScriptStart, self.FirstResult, self.ContinueMeasurement = True, True, True
        self.WireConnection, self.NameGraph, self.Status = str(), str(), str()
        self.TimeDelay, self.Count_meas, self.RemeasurementNumber = 0, 0, 0
        self.OutCommand, self.GraphInit, self.FailedResult, self.Remeasurement = False, False, False, False
        self.AutomaticBK1697B, self.AutomaticFY6900, self.AutomaticAPPA207 = False, False, False
        self.ListResult, self.ListValue = [0], [0]
        self.MinError, self.MaxError = 0, 0
        self.__init_connected_and_type_connected()

########################################################################################################################
########################################################################################################################
########################################## Module measurement and report ###############################################
########################################################################################################################
########################################################################################################################

    def MeasurementAndReport(
            self,
            value: (str, float, int),
            value_limit: (str, float, int),
            percent_error: (float, int),
            wave: str,
            amplitude: (str, float, int),
            amplitude_limit: int,
            frequency: (str, float, int),
            hash: str,
            WireConnection: str,

    ) -> None:
        """
            Calculation and reporting function
        """
        name_table = hash.split('$')[1]

        self.MaxError = float((100 + percent_error) / 100)
        self.MinError = float((100 - percent_error) / 100)

        self.ContinueMeasurement = True

        f_value = MFRT.ConvertStringToFloat(value)

        self.ListValue.append(f_value)

        RFSE.Stage(f"{WireConnection} Measure -> value = {value}, value_limit = {value_limit}, wave = {wave}, "
                   f"amplitude = {amplitude}, amplitude_limit = {amplitude_limit}, frequency = {frequency}, "
                   f"percent_error = {percent_error}")

#######################################################################################################################
#####################################################  VDC  ###########################################################
#######################################################################################################################

        if WireConnection == 'VDC':

#######################################################################################################################
###################################################  VDC MEAS  ########################################################
#######################################################################################################################

            if self.AutomaticBK1697B:
                RFSE.Stage(f"name -> BK1697B; mode -> set; command -> VDC = {value}", 'driver')
            else:
                RFSE.Messenger("set", "Make settings BK1697B#TestIoT.png", "Make settings:\n"
                                                                           f"Set VDC = {value}\n"
                                                                           "Press OK")
            if self.AutomaticFY6900:
                RFSE.Stage(f"name -> FY6900; mode -> set; command -> WAVE = {wave}", 'driver')
                RFSE.Stage(f"name -> FY6900; mode -> set; command -> amplitude = {amplitude}", 'driver')
                RFSE.Stage(f"name -> FY6900; mode -> set; command -> frequency = {frequency}", 'driver')
            else:
                RFSE.Messenger("set", "Make settings FY1697B#TestIoT.png", "Make settings:\n"
                                                                           f"Set WAVE = {wave}\n"
                                                                           f"Set amplitude = {amplitude}\n"
                                                                           f"Set frequency = {frequency}\n"
                                                                           "Press OK")

            result = self.GetResultMeasurent(value=f_value)

#######################################################################################################################
##################################################  VDC REPORT  #######################################################
#######################################################################################################################

            RFSE.Report(name_table, "set", "table", f"{value};"
                                                    f"{value_limit};"
                                                    f"{percent_error};"
                                                    f"{MFRT.ConvertFloatToString(value * (percent_error / 100), resolution=3)};"
                                                    f"{wave};"
                                                    f"{amplitude};"
                                                    f"{amplitude_limit};"
                                                    f"{frequency};"
                                                    f"{result};")
            RFSE.Stage(" ")

#######################################################################################################################
####################################################  IDC  ############################################################
#######################################################################################################################

        elif WireConnection == 'IDC':

#######################################################################################################################
#################################################  IDC MEAS  ##########################################################`
#######################################################################################################################

            if self.AutomaticBK1697B:
                RFSE.Stage(f"name -> BK1697B; mode -> set; command -> IDC = {value}", 'driver')
            else:
                RFSE.Messenger("set", "Make settings BK1697B#TestIoT.png", "Make settings:\n"
                                                                           f"Set IDC = {value}\n"
                                                                           "Press OK")
            if self.AutomaticFY6900:
                RFSE.Stage(f"name -> FY6900; mode -> set; command -> WAVE = {wave}", 'driver')
                RFSE.Stage(f"name -> FY6900; mode -> set; command -> amplitude = {amplitude}", 'driver')
                RFSE.Stage(f"name -> FY6900; mode -> set; command -> frequency = {frequency}", 'driver')
            else:
                RFSE.Messenger("set", "Make settings FY6900#TestIoT.png", "Make settings:\n"
                                                                           f"Set WAVE = {wave}\n"
                                                                           f"Set amplitude = {amplitude}\n"
                                                                           f"Set frequency = {frequency}\n"
                                                                           "Press OK")

            result = self.GetResultMeasurent(value=f_value)

#######################################################################################################################
####################################################  IDC REPORT  #####################################################
#######################################################################################################################

            RFSE.Report(name_table, "set", "table", f"{value};"
                                                    f"{value_limit};"
                                                    f"{percent_error};"
                                                    f"{MFRT.ConvertFloatToString(f_value * (percent_error / 100), resolution=3)};"
                                                    f"{wave};"
                                                    f"{amplitude};"
                                                    f"{amplitude_limit};"
                                                    f"{frequency};"
                                                    f"{result};")

            RFSE.Stage(" ")

########################################################################################################################
########################################################################################################################
########################################  Module return result measurement  ############################################
########################################################################################################################
########################################################################################################################
    def GetResultMeasurent(self, value):

        f_result, result = 0, 0

        while self.ContinueMeasurement:
            time.sleep(self.TimeDelay)
            if self.AutomaticAPPA207:
                RFSE.Stage(f"name -> APPA207; mode -> get; command -> read", 'driver')
                result = value
            else:
                result = RFSE.Messenger("get", "Input result#@notes",
                                        "Enter the measured result from APPA207\nPress OK", "string")
            RFSE.Stage(" ")
            f_result = MFRT.ConvertStringToFloat(result)
            if isinstance(f_result, str):
                continue
            if value * self.MaxError < f_result or value * self.MinError > f_result:
                if self.Count_meas >= self.RemeasurementNumber - 1:
                    choices = self.CallMessengerChoices(result=f_result, value=value)
                    if choices:
                        continue
                else:
                    self.CallMessengerErrorPoint(result=f_result, value=value)
                    continue
            else:
                if value * self.MaxError < f_result or value * self.MinError > f_result:
                    self.Status = 'Failed'
                else:
                    self.Status = 'OK'
                self.Count_meas = 0
            self.ContinueMeasurement = False
        self.ListResult.append(f_result)
        return result

########################################################################################################################
########################################################################################################################
##################################### Module check wire connection devices #############################################
########################################################################################################################
########################################################################################################################

    def CheckWireConnection(self, WireConnection: str):
        """
            Function check type wire connection
            :param WireConnection: type wire connection
            :return: None
        """
        if self.WireConnection != 'VDC':
            if WireConnection == 'VDC':
                MTLG.TelegramMessenger('beta', 'set', 'Testing VDC', 'Connect a BK1697 to the APPA207 to check '
                                                                     'VDC voltage.\nCalibrator output OUT', 'string')
                RFSE.Messenger('set', 'Testing VDC#TestIoT_VDC.png',
                               'Connect a BK1697 to the APPA207 to check VDC voltage.\n'
                               'Calibrator output OUT')
        if self.WireConnection != "IDC":
            if WireConnection == 'IDC':
                MTLG.TelegramMessenger('beta', 'set', 'Testing IDC', 'Connect a BK1697 to the APPA207 to check '
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

    def CheckConnectDevices(self):
        if self.FirstScriptStart:
            self.InitializationBK1697B(init=False)
            self.InitializationFY6900(init=False)
            self.InitializationAPPA207(init=False)
            self.FirstScriptStart = False

########################################################################################################################
########################################################################################################################
########################################################################################################################

    def InitializationBK1697B(self, init=True):

        RFSE.Stage("*********************************************************")
        RFSE.Stage("***************** Init device BK1697B *******************")
        RFSE.Stage("*********************************************************")
        RFSE.Stage(" ")

        type_setting_BK1697B = RFSE.Messenger("get", "Choose a way to connect BK1697B#TestIoT.png",
                                                     "Please select an BK1697B instrument setup type",
                                                     "choice=Automatic;Manual")

        RFSE.Report("TYPE_SETTING_BK1697B", "info", "string", "Device setting type")
        RFSE.Stage(" ")

        if type_setting_BK1697B == 'Automatic':
            choices = None
            RFSE.Stage('Driver: BK1697B >> mode: init >> command: ', 'driver')
            BK1697B_INIT = 'connected'
            if BK1697B_INIT != 'connected':
                choices = RFSE.Messenger("get", "BK1697B initialization not successful#@attention",
                                         "Failed to initialize BK1697B. Do you want to continue measuring in "
                                         "Manual mode?", "boolean")
            if not choices:
                RFSE.Report("TYPE_SETTING_BK1697B", "set", "string", "Automatic")
                self.AutomaticBK1697B = True
            else:
                type_setting_BK1697B = 'Manual'

        if type_setting_BK1697B == 'Manual':
            self.AutomaticBK1697B = False
            RFSE.Report("TYPE_SETTING_BK1697B", "set", 'string', 'Manual')
            RFSE.Messenger("set", "Make settings BK1697B#TestIoT.png", "Make settings:\n"
                                                                       "Turn on the device\n"
                                                                       "Press OK")

########################################################################################################################
        
        if init:
            if self.AutomaticBK1697B:
                RFSE.Report('DevicesUsed', 'set', 'table', 'BK1697B;Connected;')
                MOSC.hash_passed()
            else:
                RFSE.Report('DevicesUsed', 'set', 'table', 'BK1697B;Disconnected;')
                MOSC.hash_failed()

########################################################################################################################
########################################################################################################################
########################################################################################################################
    def InitializationFY6900(self, init=True):

        RFSE.Stage("*********************************************************")
        RFSE.Stage("***************** Init device FY6900 ********************")
        RFSE.Stage("*********************************************************")
        RFSE.Stage(" ")

        type_setting_FY6900 = RFSE.Messenger("get", "Choose a way to connect FY6900#TestIoT.png",
                                                    "Please select an FY6900 instrument setup type",
                                                    "choice=Automatic;Manual")

        RFSE.Report("TYPE_SETTING_FY6900", "info", "string", "Device setting type")
        RFSE.Stage(" ")

        if type_setting_FY6900 == 'Automatic':
            choices = None
            RFSE.Stage('Driver: FY6900 >> mode: init >> command: ', 'driver')
            FY6900_INIT = 'connected'
            if FY6900_INIT != 'connected':
                choices = RFSE.Messenger("get", "FY6900 initialization not successful#@attention",
                                         "Failed to initialize FY6900. Do you want to continue measuring in "
                                         "Manual mode?", "boolean")
            if not choices:
                RFSE.Report("TYPE_SETTING_FY6900", "set", "string", "Automatic")
                self.AutomaticFY6900 = True
            else:
                type_setting_FY6900 = 'Manual'

        if type_setting_FY6900 == 'Manual':
            RFSE.Report("TYPE_SETTING_FY6900", "set", "string", "Manual")
            RFSE.Messenger("set", "Make settings FY6900#TestIoT.png", "Make settings:\n"
                                                                      "Turn on the device\n"
                                                                      "Press OK")

########################################################################################################################

        if init:
            if self.AutomaticFY6900:
                RFSE.Report('DevicesUsed', 'set', 'table', 'FY6900;Connected;')
                MOSC.hash_passed()
            else:
                RFSE.Report('DevicesUsed', 'set', 'table', 'FY6900;Disconnected;')
                MOSC.hash_failed()

########################################################################################################################
########################################################################################################################
########################################################################################################################

    def InitializationAPPA207(self, init=True):

        RFSE.Stage("*********************************************************")
        RFSE.Stage("**************** Init device APPA207 ********************")
        RFSE.Stage("*********************************************************")
        RFSE.Stage(" ")

        type_setting_APPA207 = RFSE.Messenger("get", "Choose a way to connect APPA207#TestIoT.png",
                                                     "Please select an APPA207 instrument setup type",
                                                     "choice=Automatic;Manual")

        RFSE.Report("TYPE_SETTING_APPA207", "info", "string", "Device setting type")
        RFSE.Stage(" ")

        if type_setting_APPA207 == 'Automatic':

            choices = None
            RFSE.Stage('Driver: APPA207 >> mode: init >> command: ', 'driver')
            APPA207_INIT = 'connected'
            if APPA207_INIT != 'connected':
                choices = RFSE.Messenger("get", "APPA207 initialization not successful#@attention",
                                         "Failed to initialize APPA207. Do you want to continue measuring in "
                                         "Manual mode?", "boolean")
            if not choices:
                RFSE.Report("TYPE_SETTING_APPA207", "set", "string", "Automatic")
                self.AutomaticAPPA207 = True
            else:
                type_setting_APPA207 = 'Manual'

        if type_setting_APPA207 == 'Manual':
            self.AutomaticAPPA207 = False
            RFSE.Report("TYPE_SETTING_APPA207", "set", "string", "Manual")
            RFSE.Messenger("set", "Make settings APPA207#TestIoT.png", "Make settings:\n"
                                                                       "Turn on the device\n"
                                                                       "Press OK")

########################################################################################################################
        
        if init:
            if self.AutomaticAPPA207:
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

    def CheckGraphInit(self):
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

    def CreateGraph(self):
        """
            Function initialization functions create a Graph
            :return: None
        """
        self.CreateGraphValue()
        self.CreateGraphResult()
        self.FirstResult = False

########################################################################################################################
########################################################################################################################
########################################################################################################################

    def CreateGraphMask(self, value_limit):
        """
            Create mask Graph
            :param value_limit: coordinate value Ox
            :return: None
        """
        if self.FirstResult:
            RFSE.Stage("*********************************************************")
            RFSE.Stage("***************** Create Graph mask  ********************")
            RFSE.Stage("*********************************************************")
            RFSE.Stage(" ")
            MGPH.ClearGraph()
            Value_OyOx = [0, value_limit, 0, 20]
            Name_Oy = "Amplitude"
            Name_Ox = " Iteration"
            Autoscale = "No"
            MGPH.AddGraphSett(Value_OyOx, Name_Oy, Name_Ox, Autoscale)
            RFSE.Stage(" ")

########################################################################################################################
########################################################################################################################
########################################################################################################################

    def CreateGraphValue(self):
        """
            Function to create a Graph by value
            :return: None
        """
        RFSE.Stage("*********************************************************")
        RFSE.Stage("************* Create Graph a input value ****************")
        RFSE.Stage("*********************************************************")
        RFSE.Stage(" ")
        name_graph_plus = f'{self.NameGraph}_value_plus'
        name_graph_minus = f'{self.NameGraph}_value_minus'
        ArrOy_plus = [float(f'{x * self.MaxError:.14f}') for x in self.ListValue]
        ArrOy_minus = [float(f'{x * self.MinError:14f}') for x in self.ListValue]
        numLine_plus = name_graph_plus
        numLine_minus = name_graph_minus
        ArrOx = [x for x in range(len(self.ListValue))]
        LineWidth = "3"
        Color = "FF0000"
        Visible = "Yes"
        if self.FirstResult:
            MGPH.AddLine(name_graph_plus, ArrOy_plus, ArrOx, LineWidth, Color, Visible)
            MGPH.AddLine(name_graph_minus, ArrOy_minus, ArrOx, LineWidth, Color, Visible)
        else:
            MGPH.ChangeLine(numLine_plus, name_graph_plus, ArrOy_plus, ArrOx, LineWidth, Color, Visible)
            MGPH.ChangeLine(numLine_minus, name_graph_minus, ArrOy_minus, ArrOx, LineWidth, Color, Visible)
        RFSE.Stage(" ")

########################################################################################################################
########################################################################################################################
#######################################################################################################################

    def CreateGraphResult(self):
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

    def GetScreenshot(self):
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
        self.ListValue, self.ListResult = [0], [0]
        RFSE.Stage(" ")

########################################################################################################################
########################################################################################################################
################################### Module driver BK1697B set output ON or OFF #########################################
########################################################################################################################
########################################################################################################################

    def OutONNCommand(self):
        """
            BK1697B output check function ON
            :return: None
        """
        if not self.OutCommand:
            self.OutCommand = True
            if self.AutomaticBK1697B:
                RFSE.Stage('name -> BK1697B; mode -> set; command -> OUTPUT = ON', 'set')
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
        if self.AutomaticBK1697B:
            RFSE.Stage('name -> BK1697B; mode -> set; command -> OUTPUT = OFF', 'set')
        else:
            RFSE.Messenger("set", "Make settings BK1697B#TestIoT.png", "Make settings:\n"
                                                                       "Set OUTPUT = OFF\n"
                                                                       "Press OK")

########################################################################################################################
########################################################################################################################
###################################### Module repeat or error report ###################################################
########################################################################################################################
########################################################################################################################

    def CallMessengerChoices(self, result, value) -> str:

        limit_type = "upper" if self.MaxError * value < result else "lower"
        limit_value = result - (self.MaxError * value) if limit_type == "upper" else self.MinError * value - result

        error_message = 'Do you want to repeat measuring this point?\n'
        error_message += f'Lower limit < Result < Upper limit\n'
        error_message += f'{MFRT.ConvertFloatToString(self.MinError * value, resolution=3) if self.MinError * value > 0 else MFRT.ConvertFloatToString(0, resolution=3)} < '
        error_message += f'{MFRT.ConvertFloatToString(result, resolution=3)} < '
        error_message += f'{MFRT.ConvertFloatToString(self.MaxError * value, resolution=3)}\n'
        error_message += f'The measurement does not meet the {limit_type} limit ' \
                         f'on {MFRT.ConvertFloatToString(limit_value, resolution=3)}'

        choices = RFSE.Messenger('get', 'The measurement result did not pass the specified limit#@repeat',
                                 error_message, 'boolean')

        self.FailedResult = True
        self.Count_meas = 0
        return choices

########################################################################################################################
########################################################################################################################
########################################################################################################################

    def CallMessengerErrorPoint(self, result, value) -> None:

        limit_type = "upper" if self.MaxError * value < result else "lower"
        limit_value = result - (self.MaxError * value) if limit_type == "upper" else self.MinError * value - result

        error_message = 'The measurement result did not pass the specified limit\n'
        error_message += 'The value is being remeasured\n'
        error_message += f'Lower limit <  Result < Upper limit\n'
        error_message += f'{MFRT.ConvertFloatToString(self.MinError * value, resolution=3) if self.MinError * value > 0 else MFRT.ConvertFloatToString(0, resolution=3)} < '
        error_message += f'{MFRT.ConvertFloatToString(result, resolution=3)} < '
        error_message += f'{MFRT.ConvertFloatToString(self.MaxError * value, resolution=3)}\n'
        error_message += f'The measurement does not meet the {limit_type} limit ' \
                         f'on {MFRT.ConvertFloatToString(limit_value, resolution=3)}'

        RFSE.Messenger('set', 'Measurement failed#@failed', error_message, delaytime='5')
        self.Count_meas += 1

########################################################################################################################
########################################################################################################################
######################################## Module load tables in RFSE.Reports ############################################
########################################################################################################################
########################################################################################################################

    @staticmethod
    def LoadTablesHeadInfo():
        RFSE.Report('VDC_SIN', 'info', 'table', "Value#100;"
                                                "ValueLimit#100;"
                                                "PercentError#100;"
                                                "PermissibleVariation#150;"
                                                "Wave#100;"
                                                "Amplitude#100;"
                                                "AmplitudeLimit#100;"
                                                "Frequency#100;"
                                                "Result#100;")

        RFSE.Report('VDC_SQUARE', 'info', 'table', "Value#100;"
                                                   "ValueLimit#100;"
                                                   "PercentError#100;"
                                                   "PermissibleVariation#150;"
                                                   "Wave#100;"
                                                   "Amplitude#100;"
                                                   "AmplitudeLimit#100;"
                                                   "Frequency#100;"
                                                   "Result#100;")

        RFSE.Report('IDC_RAMP', 'info', 'table', "Value#100;"
                                                 "ValueLimit#100;"
                                                 "PercentError#100;"
                                                 "PermissibleVariation#150;"
                                                 "Wave#100;"
                                                 "Amplitude#100;"
                                                 "AmplitudeLimit#100;"
                                                 "Frequency#100;"
                                                 "Result#100;")

        RFSE.Report('IDC_NEGRAMP', 'info', 'table', "Value#100;"
                                                    "ValueLimit#100;"
                                                    "PercentError#100;"
                                                    "PermissibleVariation#150;"
                                                    "Wave#100;"
                                                    "Amplitude#100;"
                                                    "AmplitudeLimit#100;"
                                                    "Frequency#100;"
                                                    "Result#100;")
        RFSE.Stage(" ")

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################

    def __init_connected_and_type_connected(self):
        type_setting_BK1697B = RFSE.Report("TYPE_SETTING_BK1697B", "get", "string", "", 'string')
        type_setting_FY6900 = RFSE.Report("TYPE_SETTING_FY6900", "get", "string", "", 'string')
        type_setting_APPA207 = RFSE.Report("TYPE_SETTING_APPA207", "get", "string", "", 'string')

        if len(type_setting_BK1697B) == 0 or len(type_setting_FY6900) == 0 or len(type_setting_APPA207) == 0:
            self.FirstScriptStart = True
            return
        else:
            self.FirstScriptStart = False

        if type_setting_BK1697B == 'Automatic':
            self.AutomaticBK1697B = True
        else:
            self.AutomaticBK1697B = False

        if type_setting_FY6900 == 'Automatic':
            self.AutomaticFY6900 = True
        else:
            self.AutomaticFY6900 = False

        if type_setting_APPA207 == 'Automatic':
            self.AutomaticAPPA207 = True
        else:
            self.AutomaticAPPA207 = False


Testing = DemoTestIoTMeasurement()
