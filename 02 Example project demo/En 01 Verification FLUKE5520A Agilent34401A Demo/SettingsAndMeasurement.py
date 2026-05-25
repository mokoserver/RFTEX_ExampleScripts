import time

import RFSE
import MFRT
import MOSC
from Fluke5520A import Fluke5520A
from Agilent34401A import Agilent34401A


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

class SettingsAndMeasurement:
    def __init__(self) -> None:
        self.FirstScriptStart, self.ContinueMeasurement = True, True
        self.RemeasurementNumber, self.TimeDelay, self.Count_meas = 0, 0, 0
        self.WireConnection = str()
        self.Remeasurement, self.Driver_start = False, False
        self.Agilent34401A = Agilent34401A()
        self.Fluke5520A = Fluke5520A()
        self.R4FirstResult = True
        self.LowerLimitResult, self.UpperLimitResult, self.Status = None, None, None
        self.__init_connected_and_type_connected()
        
        
#######################################################################################################################
#######################################################  VDC  #########################################################
#######################################################################################################################

    def VDC_Measurement(self, range: (str | float | int), verified: (str | float | int), error: (str | float | int)) -> None:

        f_verified = MFRT.ConvertStringToFloat(verified)
        f_error = MFRT.ConvertStringToFloat(error)
        
#######################################################################################################################
#####################################################  VDC MEAS  ######################################################
#######################################################################################################################

        RFSE.Stage(f'VDC Measure -> range = {range}, verified = {verified}, error = {error}')

        self.Agilent34401A.SET_RANGE(range=range)

        self.Fluke5520A.SET_VDC(verified=verified)

        f_result, accuracy = self.GetResultMeasurement(f_verified=f_verified, error=f_error, verified=verified)

#######################################################################################################################
####################################################  VDC REPORT  #####################################################
#######################################################################################################################

        RFSE.Report("VDC", "set", "table", f"{range};"
                                           f"{verified};"
                                           f"{MFRT.ConvertFloatToString(f_result, verified)};"
                                           f"{MFRT.ConvertFloatToString(accuracy, verified)};"
                                           f"{MFRT.ConvertFloatToString(error)};"
                                           f"{self.Status}")

#######################################################################################################################
#######################################################  VAC  #########################################################
#######################################################################################################################

    def VAC_Measurement(self, range: (str | float | int), verified: (str | float | int), frequency: (str | float | int),
                        error: (str | float | int)) -> None:
        
        f_verified = MFRT.ConvertStringToFloat(verified)
        f_error = MFRT.ConvertStringToFloat(error)

#######################################################################################################################
####################################################  VAC MEAS  #######################################################
#######################################################################################################################

        RFSE.Stage(f'VAC Measure -> range = {range}, verified = {verified}, frequency = {frequency}, error = {error}')

        self.Agilent34401A.SET_RANGE(range=range)

        self.Fluke5520A.SET_VAC(verified=verified, frequency=frequency)

        f_result, accuracy = self.GetResultMeasurement(f_verified=f_verified, error=f_error, verified=verified)

#######################################################################################################################
###################################################  VAC REPORT  ######################################################
#######################################################################################################################

        RFSE.Report("VAC", "set", "table", f"{range};"
                                           f"{verified};"
                                           f"{frequency};"
                                           f"{MFRT.ConvertFloatToString(f_result, verified)};"
                                           f"{MFRT.ConvertFloatToString(accuracy, verified)};"
                                           f"{error};"
                                           f"{self.Status}")

#######################################################################################################################
#####################################################   R2  ###########################################################
#######################################################################################################################

    def R2_Measurement(self, range: (str | float | int), verified: (str | float | int),error: (str | float | int)) -> None:

        f_verified = MFRT.ConvertStringToFloat(verified)
        f_error = MFRT.ConvertStringToFloat(error)
        
#######################################################################################################################
####################################################  R2 MEAS  ########################################################
#######################################################################################################################

        RFSE.Stage(f'R2 Measure -> range = {range}, verified = {verified}, error = {error}')

        self.Agilent34401A.SET_RANGE(range=range)

        self.Fluke5520A.SET_R(verified=verified)

        f_result, accuracy = self.GetResultMeasurement(f_verified=f_verified, error=f_error, verified=verified)

#######################################################################################################################
###################################################  R2 REPORT  #######################################################
#######################################################################################################################

        RFSE.Report("RES", "set", "table", f"{range};"
                                           f"{verified};"
                                           f"{MFRT.ConvertFloatToString(f_result, verified)};"
                                           f"{MFRT.ConvertFloatToString(accuracy, verified)};"
                                           f"{error};"
                                           f"{self.Status}")

#######################################################################################################################
#####################################################   R4  ###########################################################
#######################################################################################################################

    def R4_Measurement(self, range: (str | float | int), verified: (str | float | int), error: (str | float | int)) -> None:

        f_verified = MFRT.ConvertStringToFloat(verified)
        f_error = MFRT.ConvertStringToFloat(error)

#######################################################################################################################
#####################################################  R4 MEAS  #######################################################
#######################################################################################################################

        RFSE.Stage(f'R4 Measure -> range = {range}, verified = {verified}, error = {error}')

        if self.R4FirstResult:
            
            self.Fluke5520A.SET_R(verified=0)
            time.sleep(3)
            self.Agilent34401A.SET_AUTOZERO_ONCE()
            
            self.R4FirstResult = False

        self.Agilent34401A.SET_RANGE(range=range)

        self.Fluke5520A.SET_R(verified=verified)

        f_result, accuracy = self.GetResultMeasurement(f_verified=f_verified, error=f_error, verified=verified)

#######################################################################################################################
##############################################  R4 REPORT  ############################################################
#######################################################################################################################

        RFSE.Report("RES", "set", "table", f"{range};"
                                           f"{verified};"
                                           f"{MFRT.ConvertFloatToString(f_result, verified)};"
                                           f"{MFRT.ConvertFloatToString(accuracy, verified)};"
                                           f"{error};"
                                           f"{self.Status}")

#######################################################################################################################
#######################################################  IDC  #########################################################
#######################################################################################################################

    def IDC_Measurement(self, range: (str | float | int), verified: (str | float | int), error: (str | float | int)) -> None:

        f_verified = MFRT.ConvertStringToFloat(verified)
        f_error = MFRT.ConvertStringToFloat(error)

#######################################################################################################################
#####################################################  IDC MEAS  ######################################################
#######################################################################################################################

        RFSE.Stage(f'IDC Measure -> range = {range}, verified = {verified}, error = {error}')

        self.Agilent34401A.SET_RANGE(range=range)

        self.Fluke5520A.SET_IDC(verified=verified)

        f_result, accuracy = self.GetResultMeasurement(f_verified=f_verified, error=f_error, verified=verified)

#######################################################################################################################
####################################################  IDC REPORT  #####################################################
#######################################################################################################################

        RFSE.Report("IDC", "set", "table", f"{range};"
                                           f"{verified};"
                                           f"{MFRT.ConvertFloatToString(f_result, verified)};"
                                           f"{MFRT.ConvertFloatToString(accuracy, verified)};"
                                           f"{error};"
                                           f"{self.Status}")

#######################################################################################################################
#######################################################  IAC  #########################################################
#######################################################################################################################

    def IAC_Measurement(self, range: (str | float | int), verified: (str | float | int), frequency: (str | float | int),
                        error: (str | float | int)) -> None:

        f_verified = MFRT.ConvertStringToFloat(verified)
        f_error = MFRT.ConvertStringToFloat(error)

#######################################################################################################################
#####################################################  IAC MEAS  ######################################################
#######################################################################################################################

        RFSE.Stage(f'IAC Measure -> range = {range}, verified = {verified}, frequency = {frequency}, '
                   f'error = {error}')

        self.Agilent34401A.SET_RANGE(range=range)

        self.Fluke5520A.SET_IAC(verified=verified, frequency=frequency)

        f_result, accuracy = self.GetResultMeasurement(f_verified=f_verified, error=f_error, verified=verified)

#######################################################################################################################
###################################################  IAC REPORT  ######################################################
#######################################################################################################################

        RFSE.Report("IAC", "set", "table", f"{range};"
                                           f"{verified};"
                                           f"{frequency};"
                                           f"{MFRT.ConvertFloatToString(f_result, verified)};"
                                           f"{MFRT.ConvertFloatToString(accuracy, verified)};"
                                           f"{error};"
                                           f"{self.Status}")

#######################################################################################################################
#######################################################################################################################
########################################  Function get result measuare   ##############################################
#######################################################################################################################
#######################################################################################################################

    def GetResultMeasurement(self, f_verified: (float | int), error: (float | int), verified: str) -> (float, float):
        
        f_result, accuracy = 0, 0
        while self.ContinueMeasurement:

            time.sleep(0.1)
            
            result = self.Agilent34401A.Read_Result(verified=f_verified)
            
            f_result = MFRT.ConvertStringToFloat(result)
            
            if isinstance(f_result, str):
                continue

            accuracy = abs(f_verified - f_result)
            if accuracy > error and self.Remeasurement:
                if self.Count_meas >= self.RemeasurementNumber - 1:
                    choices = self.CallMessengerChoices(
                        verified=f_verified, error=error, result=f_result, reference_number=verified)
                    if choices:
                        continue
                else:
                    self.CallMessengerErrorPoint(
                        verified=f_verified, error=error, result=f_result, reference_number=verified)
                    continue

            if accuracy > error:
                self.Status = 'Failed'
                MOSC.hash_failed()
            else:
                self.Status = 'OK'
                MOSC.hash_passed()

            self.Count_meas = 0
            self.ContinueMeasurement = False
        self.ContinueMeasurement = True
        return f_result, accuracy

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def MeasurementStartCommand(self, WireConnection: str) -> None:

        if not self.Driver_start:

            self.Agilent34401A.SET_FUNC(WireConnection=WireConnection)
            self.Agilent34401A.SET_RES_MIN()

            match WireConnection:
                case "VDC":
                    self.Agilent34401A.SET_NPLC_100()
                    self.Fluke5520A.SET_OUT_NORMAL()

                case "VAC":
                    self.Agilent34401A.SET_BAND_MIN()
                    self.Fluke5520A.SET_OUT_NORMAL()

                case "R2":
                    self.Agilent34401A.SET_NPLC_100()
                    self.Fluke5520A.SET_CONN_NO()

                case "R4":
                    self.Agilent34401A.SET_NPLC_100()
                    self.Fluke5520A.SET_OUT_NORMAL()
                    self.Fluke5520A.SET_CONN_4W()

                case "IDC":
                    self.Agilent34401A.SET_NPLC_100()
                    self.Fluke5520A.SET_OUT_AUX()

                case "IAC":
                    self.Agilent34401A.SET_BAND_MIN()
                    self.Fluke5520A.SET_OUT_AUX()

            self.Fluke5520A.SET_SwitchOFF_DIS()

            RFSE.Stage(" ")
            self.Driver_start = True

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def MeasurementStopCommand(self) -> None:

        self.Fluke5520A.SET_SwitchOFF_Enable()
        self.Fluke5520A.SET_STOP()

        self.Driver_start = False
        self.ContinueMeasurement = True

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################


    def CheckWireConnection(self, WireConnection: str) -> None:
        
        if self.WireConnection != WireConnection:
            match WireConnection:
                case "VDC":
                    RFSE.Messenger('set',
                                   'Connecting wires#FLUKE5520A_AGILENT34401A_V_R2.png',
                                   'Connect a multimeter to the calibrator to check VDC voltage.\n'
                                   'Calibrator output NORMAL')
                case "VAC":
                    RFSE.Messenger('set',
                                   'Connecting wires#FLUKE5520A_AGILENT34401A_V_R2.png',
                                   'Connect a multimeter to the calibrator to check VAC voltage.\n'
                                   'Calibrator output NORMAL')
                case "R2":
                    RFSE.Messenger('set',
                                   'Connecting wires#FLUKE5520A_AGILENT34401A_V_R2.png',
                                   'Connect a multimeter to the calibrator to check R2 resistance.\n'
                                   'Calibrator output NORMAL')
                case "R4":
                    RFSE.Messenger('set',
                                   'Connecting wires#FLUKE5520A_AGILENT34401A_R4.png',
                                   'Connect a multimeter to the calibrator to check.\n'
                                   'RES resistance in 4-wire circuit.')
                case "IDC":
                    RFSE.Messenger("set",
                                   'Connecting wires#FLUKE5520A_AGILENT34401A_I.png',
                                   'Connect a multimeter to the calibrator to test.\n'
                                   'DC current IDC up to 3 A.\n'
                                   'Calibrator output AUX up to 2 A.')
                case "IAC":
                    RFSE.Messenger("set",
                                   'Connecting wires#FLUKE5520A_AGILENT34401A_I.png',
                                   'Connect a multimeter to the calibrator to test.\n'
                                   'AC current IAC up to 3 A.\n'
                                   'Calibrator output AUX up to 2 A.')

            self.WireConnection = WireConnection
            RFSE.Stage(' ')

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def CheckConnectDevices(self) -> None:
        if self.FirstScriptStart:
            RFSE.Stage('*****************************************************')
            RFSE.Stage('***************** Connect Devices *******************')
            RFSE.Stage('*****************************************************')

            self.Agilent34401A.Initialization(init=False)
            self.Fluke5520A.Initialization(init=False)

            self.FirstScriptStart = False



#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def SettingMeasurementLimits(self, verified: (float | int), error: (float | int)) -> None:
        self.LowerLimitResult = verified - error
        self.UpperLimitResult = verified + error

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def CallMessengerChoices(self, verified: (float | int), error: (float | int), result: (float | int),
                             reference_number: str) -> str:

        self.SettingMeasurementLimits(verified=verified, error=error)

        limit_type = "lower" if self.LowerLimitResult > result else "upper"
        limit_value = self.LowerLimitResult - result if limit_type == "lower" else result - self.UpperLimitResult

        error_message = 'Do you want to repeat measuring this point?\n'
        error_message += f'Lower limit < Result < Upper limit\n'
        error_message += f'{MFRT.ConvertFloatToString(self.LowerLimitResult, reference_number)} < '
        error_message += f'{MFRT.ConvertFloatToString(result, reference_number)} < '
        error_message += f'{MFRT.ConvertFloatToString(self.UpperLimitResult, reference_number)}\n'
        error_message += f'The measurement does not meet the {limit_type} limit ' \
                         f'on {MFRT.ConvertFloatToString(limit_value, reference_number)}'

        choices = RFSE.Messenger('get', 'The measurement result did not pass the specified limit#@repeat',
                                 error_message, 'boolean')

        self.Status = "Failed"
        self.Count_meas = 0
        return choices

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def CallMessengerErrorPoint(self, verified: (float | int), error: (float | int), result: (float | int),
                                reference_number: str) -> None:

        self.SettingMeasurementLimits(verified=verified, error=error)

        limit_type = "lower" if self.LowerLimitResult > result else "upper"
        limit_value = self.LowerLimitResult - result if limit_type == "lower" else result - self.UpperLimitResult

        error_message = 'The measurement result did not pass the specified limit\n'
        error_message += 'The value is being remeasured\n'
        error_message += f'Lower limit <  Result < Upper limit\n'
        error_message += f'{MFRT.ConvertFloatToString(self.LowerLimitResult, reference_number)} < '
        error_message += f'{MFRT.ConvertFloatToString(result, reference_number)} < '
        error_message += f'{MFRT.ConvertFloatToString(self.UpperLimitResult, reference_number)}\n'
        error_message += f'The measurement does not meet the {limit_type} limit ' \
                         f'on {MFRT.ConvertFloatToString(limit_value, reference_number)}'

        RFSE.Messenger('set', 'Measurement failed#@failed', error_message, delaytime='5')
        self.Count_meas += 1

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    @staticmethod
    def LoadTablesHeadInfo() -> None:
        RFSE.Report('VAC', 'info', 'table', "Range#100;"
                                            "Point#100;"
                                            "Frequency#100;"
                                            "Result#100;"
                                            "Accuracy#100;"
                                            "Permissible error#100;"
                                            "Conclusion#100;")

        RFSE.Report('VDC', 'info', 'table', "Range#100;"
                                            "Point#100;"
                                            "Result#100;"
                                            "Accuracy#100;"
                                            "Permissible error#100;"
                                            "Conclusion#100;")

        RFSE.Report('RES', 'info', 'table', "Range#100;"
                                            "Point#100;"
                                            "Result#100;"
                                            "Accuracy#100;"
                                            "Permissible error#100;"
                                            "Conclusion#100;")

        RFSE.Report('IAC', 'info', 'table', "Range#100;"
                                            "Point#100;"
                                            "Frequency#100;"
                                            "Result#100;"
                                            "Accuracy#100;"
                                            "Permissible error#100;"
                                            "Conclusion#100;")

        RFSE.Report('IDC', 'info', 'table', "Range#100;"
                                            "Point#100;"
                                            "Result#100;"
                                            "Accuracy#100;"
                                            "Permissible error#100;"
                                            "Conclusion#100;")

        RFSE.Stage(" ")

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def __init_connected_and_type_connected(self) -> None:
        type_setting_Fluke5520A = RFSE.Report("TYPE_SETTING_FLUKE5520A", "get", "string", "", 'string')
        type_setting_Agilent34401A = RFSE.Report("TYPE_SETTING_AGILENT34401A", "get", "string", "", 'string')

        if not type_setting_Agilent34401A or not type_setting_Fluke5520A:
            self.FirstScriptStart = True
            self.Agilent34401A.IsSimulation = False
            self.Fluke5520A.IsSimulation = False
            return
        else:
            self.FirstScriptStart = False

        if 'simulation' in [type_setting_Fluke5520A.lower(), type_setting_Agilent34401A.lower()]:
            self.Agilent34401A.IsSimulation = True
            self.Fluke5520A.IsSimulation = True
            return
        else:
            self.Agilent34401A.IsSimulation = False
            self.Fluke5520A.IsSimulation = False

        if type_setting_Fluke5520A.lower() == 'automatic':
            self.Fluke5520A.IsAutomatic = True
        else:
            self.Fluke5520A.IsAutomatic = False

        if type_setting_Agilent34401A.lower() == 'automatic':
            self.Agilent34401A.IsAutomatic = True
        else:
            self.Agilent34401A.IsAutomatic = False

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def check_simulation_mode(self) -> None:
        hash_list = ['Initialization AGILENT34401A$Init', 'Initialization FLUKE5520A$Init']
        if self.Agilent34401A.IsSimulation or self.Fluke5520A.IsSimulation:

            self.Agilent34401A.IsSimulation = True
            self.Fluke5520A.IsSimulation = True

            for count, one_hash in enumerate(hash_list):
                status = MOSC.get_hashes_status(hash=one_hash)
                if status not in "passed":
                    RFSE.Program('tree', 'set', f'select = {one_hash}')
                    MOSC.hash_passed()

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################


Poverka = SettingsAndMeasurement()
