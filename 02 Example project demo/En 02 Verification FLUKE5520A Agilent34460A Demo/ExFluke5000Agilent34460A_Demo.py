import time

import RFSE
import MFRT
import MOSC


class ExFluke5000Agilent34460A:
    def __init__(self) -> None:
        self.FirstScriptStart, self.ContinueMeasurement = True, True
        self.RemeasurementNumber, self.TimeDelay, self.Count_meas = 0, 0, 0
        self.WireConnection = str()
        self.Remeasurement, self.Driver_start = False, False
        self.LowerLimitResult, self.UpperLimitResult, self.Status = None, None, None
        self.AutomaticFluke5520A, self.AutomaticAgilent34460A = False, False
        self.__init_connected_and_type_connected()

    def MeasurementAndReport(self, range, verified, error, WireConnection, frequency=None, filter=None) -> None:
        """
            Calculation and reporting function
        """
        f_verified = MFRT.ConvertStringToFloat(verified)
        f_error = MFRT.ConvertStringToFloat(error)

#######################################################################################################################
#######################################################  VDC  #########################################################
#######################################################################################################################

        if WireConnection == 'VDC':

#######################################################################################################################
#####################################################  VDC MEAS  ######################################################
#######################################################################################################################

            RFSE.Stage(f'VDC Measure -> range = {range}, verified = {verified}, error = {error}')

############################################   Agilent34460A SET RANGE   ##############################################
            if self.AutomaticAgilent34460A:
                RFSE.Stage(f'Driver: AgilentDMM >> mode: set >> command: range = {range}', 'driver')
            else:
                RFSE.Messenger("set", "Make settings on Agilent34460A#@agilent34460a",
                               f"Make settings:\nSet range = {range}\nPress OK")
#######################################################################################################################

#############################################   Fluke5520A SET VDC   ##################################################
            if self.AutomaticFluke5520A:
                RFSE.Stage(f'Driver: Fluke5000 >> mode: set >> command: VDC = {verified}', 'driver')
            else:
                RFSE.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                               f"Make settings:\nSet VDC = {verified}\nPress OK")
#######################################################################################################################

            f_result, accuracy = self.GetResultMeasurement(verified=f_verified, error=f_error)

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

        elif WireConnection == 'VAC':

#######################################################################################################################
####################################################  VAC MEAS  #######################################################
#######################################################################################################################

            RFSE.Stage(f'VAC Measure -> range = {range}, verified = {verified}, filter = {filter}, '
                       f'frequency = {frequency}, error = {error}')

#############################################   Agilent34460A SET RANGE   #############################################
############################################   Agilent34460A SET ACBand   #############################################
            if self.AutomaticAgilent34460A:
                RFSE.Stage(f'DriverSet AgilentDMM >> mode: set >> command: range = {range}', 'driver')
                RFSE.Stage(f'DriverSet AgilentDMM >> mode: set >> command: ACBand = {filter}', 'driver')
            else:
                RFSE.Messenger("set", "Make settings on Agilent34460A#@agilent34460a",
                               f"Make settings:\nSet range = {range}\nSet ACBand = {filter}\nPress OK")

#######################################################################################################################

#############################################   Fluke5520A SET VAC   ##################################################
            if self.AutomaticFluke5520A:
                RFSE.Stage(f'DriverSet Fluke5000 >> mode: set >> command: VAC = {verified} {frequency}', 'driver')
            else:
                RFSE.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                               f"Make settings:\nSet VAC = {verified} {frequency}\nPress OK")
#######################################################################################################################

            f_result, accuracy = self.GetResultMeasurement(verified=f_verified, error=f_error)

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

        elif WireConnection == 'R2':

#######################################################################################################################
####################################################  R2 MEAS  ########################################################
#######################################################################################################################

            RFSE.Stage(f'R2 Measure -> range = {range}, verified = {verified}, error = {error}')

############################################   Agilent34460A SET RANGE   ##############################################
            if self.AutomaticAgilent34460A:
                RFSE.Stage(f'Driver: AgilentDMM >> mode: set >> command: range = {range}', 'driver')
            else:
                RFSE.Messenger("set", "Make settings on Agilent34460A#@agilent34460a",
                               f"Make settings:\nSet range = {range}\nPress OK")
#######################################################################################################################

#############################################   Fluke5520A SET R2   ###################################################
            if self.AutomaticFluke5520A:
                RFSE.Stage(f'Driver: Fluke5000 >> mode: set >> command: R2 = {verified}', 'driver')
            else:
                RFSE.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                               f"Make settings:\nSet R2 = {verified}\nPress OK")
#######################################################################################################################

            f_result, accuracy = self.GetResultMeasurement(verified=f_verified, error=f_error)

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

        elif WireConnection == 'R4':

#######################################################################################################################
#####################################################  R4 MEAS  #######################################################
#######################################################################################################################

            RFSE.Stage(f'R4 Measure -> range = {range}, verified = {verified}, error = {error}')

############################################   Agilent34460A SET RANGE   ##############################################
            if self.AutomaticAgilent34460A:
                RFSE.Stage(f'Driver: AgilentDMM >> mode: set >> command: range = {range}', 'driver')
            else:
                RFSE.Messenger("set", "Make settings on Agilent34460A#@agilent34460a",
                               f"Make settings:\nSet range = {range}\nPress OK")
#######################################################################################################################

#############################################   Fluke5520A SET R4  ###################################################

            if self.AutomaticFluke5520A:
                RFSE.Stage(f'Driver: Fluke5000 >> mode: set >> command: R4 = {verified}', 'driver')
            else:
                RFSE.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                               f"Make settings:\nSet R4 = {verified}\nPress OK")
#######################################################################################################################

            f_result, accuracy = self.GetResultMeasurement(verified=f_verified, error=f_error)

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

        elif WireConnection == 'IDC':

#######################################################################################################################
#####################################################  IDC MEAS  ######################################################
#######################################################################################################################

            RFSE.Stage(f'IDC Measure -> range = {range}, verified = {verified}, error = {error}')

############################################   Agilent34460A SET RANGE   ##############################################
            if self.AutomaticAgilent34460A:
                RFSE.Stage(f'Driver: AgilentDMM >> mode: set >> command: range = {range}', 'driver')
            else:
                RFSE.Messenger("set", "Make settings on Agilent34460A#@agilent34460a",
                               f"Make settings:\nSet range = {range}\nPress OK")
#######################################################################################################################

#############################################   Fluke5520A SET IDC   ##################################################

            if self.AutomaticFluke5520A:
                RFSE.Stage(f'Driver: Fluke5000 >> mode: set >> command: IDC = {verified}', 'driver')
            else:
                RFSE.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                               f"Make settings:\nSet IDC = {verified}\nPress OK")
#######################################################################################################################

            f_result, accuracy = self.GetResultMeasurement(verified=f_verified, error=f_error)

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

        elif WireConnection == 'IAC':

#######################################################################################################################
#####################################################  IAC MEAS  ######################################################
#######################################################################################################################

            RFSE.Stage(f'IAC Measure -> range = {range}, verified = {verified}, filter = {filter}, '
                       f'frequency = {frequency}, error = {error}')

############################################   Agilent34460A SET RANGE   ##############################################
############################################   Agilent34460A SET ACBand   #############################################
            if self.AutomaticAgilent34460A:
                RFSE.Stage(f'DriverSet AgilentDMM >> mode: set >> command: range = {range}', 'driver')
                RFSE.Stage(f'DriverSet AgilentDMM >> mode: set >> command: ACBand = {filter}', 'driver')
            else:
                RFSE.Messenger("set", "Make settings on Agilent34460A#@agilent34460a",
                               f"Make settings:\nSet range = {range}\nSet ACBand = {filter}\nPress OK")
#######################################################################################################################

#############################################   Fluke5520A SET IAC   ##################################################

            if self.AutomaticFluke5520A:
                RFSE.Stage(f'DriverSet Fluke5000 >> mode: set >> command: IAC = {verified} {frequency}', 'driver')
            else:
                RFSE.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                               f"Make settings:\nSet IAC = {verified} {frequency}\nPress OK")
#######################################################################################################################

            f_result, accuracy = self.GetResultMeasurement(verified=f_verified, error=f_error)

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

    def GetResultMeasurement(self, verified, error) -> (float, float):
        f_result, accuracy = 0, 0
        while self.ContinueMeasurement:

            time.sleep(self.TimeDelay)
############################################   Agilent34460A READ RESULT    ###########################################
            if self.AutomaticAgilent34460A:
                RFSE.Stage(f'DriverSet AgilentDMM >> mode: get >> command: result = read', 'driver')
                result = verified
            else:
                result = RFSE.Messenger("get", "Input result#@notes",
                                        "Enter the measured result from Agilent34460A\nPress OK", "string")
            RFSE.Stage(" ")
#######################################################################################################################

            f_result = MFRT.ConvertStringToFloat(result)
            if isinstance(f_result, str):
                continue
            accuracy = abs(verified - f_result)
            if accuracy > error and self.Remeasurement:
                if self.Count_meas >= self.RemeasurementNumber - 1:
                    choices = self.CallMessengerChoices(
                        verified=verified, error=error, result=f_result, reference_number=verified)
                    if choices:
                        continue
                else:
                    self.CallMessengerErrorPoint(
                        verified=verified, error=error, result=f_result, reference_number=verified)
                    continue
            else:
                if accuracy > error:
                    self.Status = 'Failed'
                else:
                    self.Status = 'OK'
                self.Count_meas = 0

            self.ContinueMeasurement = False
        return f_result, accuracy

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def MeasurementStartCommand(self, WireConnection: str) -> None:
        if not self.Driver_start:

############################################   Agilent34460A SET FUNC   ###############################################
            if self.AutomaticAgilent34460A:
                RFSE.Stage(f'Driver: AgilentDMM >> mode: set >> command: func = {WireConnection} ', 'driver')
            else:
                RFSE.Messenger('set', 'Make settings on Agilent34460A#@agilent34460a',
                               f'Make settings:\nSet func = {WireConnection}\nPress OK')
#######################################################################################################################

############################################   Fluke5520 SET OUT = AUX   ##############################################
            if WireConnection in ['IDC', 'IAC']:
                if self.AutomaticFluke5520A:
                    RFSE.Stage('Driver: Fluke5000 >> mode: set >> command: OUT = AUX', 'driver')
                else:
                    RFSE.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                                   f'Make settings:\nSet OUT = AUX\nPress OK')
#######################################################################################################################

###########################################   Fluke5520 SET OUT = NORMAL  #############################################
            elif WireConnection != 'R2':
                if self.AutomaticFluke5520A:
                    RFSE.Stage('Driver: Fluke5000 >> mode: set >> command: OUT = NORMAL', 'driver')
                else:
                    RFSE.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                                   f'Make settings:\nSet OUT = NORMAL\nPress OK')
#######################################################################################################################

############################################   Fluke5520 SET Conn = 4w  ###############################################
            if WireConnection == 'R4':
                if self.AutomaticFluke5520A:
                    RFSE.Stage('Driver: Fluke5000 >> mode: set >> command: Conn = 4w', 'driver')
                else:
                    RFSE.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                                   f'Make settings:\nSet Conn = 4w\nPress OK')
#######################################################################################################################

############################################   Fluke5520 SET Conn = NO  ###############################################
            elif WireConnection == 'R2':
                if self.AutomaticFluke5520A:
                    RFSE.Stage('Driver: Fluke5000 >> mode: set >> command: Conn = NO', 'driver')
                else:
                    RFSE.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                                   f'Make settings:\nSet Conn = NO\nPress OK')
#######################################################################################################################

##########################################   Fluke5520 SET SwitchOFF = DIS   ##########################################
            if self.AutomaticFluke5520A:
                RFSE.Stage('Driver: Fluke5000 >> mode: set >> command: SwitchOFF = DIS', 'driver')
            else:
                RFSE.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                               f'Make settings:\nSet SwitchOFF = DISABLE\nPress OK')
#######################################################################################################################

            RFSE.Stage(" ")
            self.Driver_start = True

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def MeasurementStopCommand(self) -> None:

########################################   Fluke5520 SET SwitchOFF = ENABLE   #########################################
###############################################   Fluke5520 SET Stop  #################################################
        if self.AutomaticFluke5520A:
            RFSE.Stage('Driver: Fluke5000 >> mode: set >> command: SwitchOFF = ENABLE', 'driver')
            RFSE.Stage('Driver: Fluke5000 >> mode: set >> command: Stop', 'driver')
        else:
            RFSE.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                           f'Make settings:\nSet SwitchOFF = ENABLE\nSet Stop\nPress OK')
#######################################################################################################################

        self.Driver_start = False

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def CheckWireConnection(self, WireConnection: str) -> None:
        self.ContinueMeasurement = True
        if self.WireConnection not in ['VDC', 'VAC', 'R2']:
            if WireConnection == 'VDC':
                RFSE.Messenger('set',
                               'Connecting wires#FLUKE5520A_AGILENT34460A_V_R2.jpg',
                               'Connect a multimeter to the calibrator to check VDC voltage.\n'
                               'Calibrator output NORMAL')
            elif WireConnection == 'VAC':
                RFSE.Messenger('set',
                               'Connecting wires#FLUKE5520A_AGILENT34460A_V_R2.jpg',
                               'Connect a multimeter to the calibrator to check VAC voltage.\n'
                               'Calibrator output NORMAL')
            elif WireConnection == 'R2':
                RFSE.Messenger('set',
                               'Connecting wires#FLUKE5520A_AGILENT34460A_V_R2.jpg',
                               'Connect a multimeter to the calibrator to check R2 resistance.\n'
                               'Calibrator output NORMAL')
        if self.WireConnection not in ['IDC', 'IAC']:
            if WireConnection == 'IDC':
                RFSE.Messenger("set",
                               'Connecting wires#FLUKE5520A_AGILENT34460A_I3_2.jpg',
                               'Connect a multimeter to the calibrator to test.\n'
                               'DC current IDC up to 3 A.\n'
                               'Calibrator output AUX up to 2 A.')
            elif WireConnection == 'IAC':
                RFSE.Messenger("set",
                               'Connecting wires#FLUKE5520A_AGILENT34460A_I3_2.jpg',
                               'Connect a multimeter to the calibrator to test.\n'
                               'AC current IAC up to 3 A.\n'
                               'Calibrator output AUX up to 2 A.')

        if self.WireConnection not in ['R4']:
            if WireConnection == 'R4':     RFSE.Messenger('set',
                                                          'Connecting wires#FLUKE5520A_AGILENT34460A_R4.jpg',
                                                          'Connect a multimeter to the calibrator to check.\n'
                                                          'RES resistance in 4-wire circuit.')

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

            self.InitializationAGILENT34460A(init=False)
            self.InitializationFluke5520A(init=False)

            self.FirstScriptStart = False

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def InitializationAGILENT34460A(self, init=True) -> None:

        type_setting_agilent = RFSE.Messenger("get", "Choose a way to connect AGILENT34460A#@agilent34460a",
                                                     "Please select an Agilent34460A instrument setup type",
                                                     "choice=Automatic;Manual")

        RFSE.Stage(" ")

        RFSE.Report("TYPE_SETTING_AGILENT34460A", "info", "string", "Device setting type")

############################################   AGILENT34460A Init   ###################################################
#########################################   AGILENT34460A SET Timeout  ################################################
##########################################   AGILENT34460A SET Reset  #################################################

        if type_setting_agilent == 'Automatic':

            choices = None

            RFSE.Stage('Driver: AgilentDMM >> mode: init >> command: ', 'driver')
            agilent3401a_status = 'connected'

            if agilent3401a_status != 'connected':
                choices = RFSE.Messenger("get", "AGILENT34460A initialization not successful#@agilent34460a",
                                         "Failed to initialize AGILENT34460A. Do you want to continue measuring in "
                                         "Manual mode?", "boolean")

            if not choices or agilent3401a_status == 'connected':
                self.AutomaticAgilent34460A = True
                RFSE.Report("TYPE_SETTING_AGILENT34460A", "set", 'string', 'Automatic')
                RFSE.Stage('Driver: AgilentDMM >> mode: set >> command: Timeout = 10000', 'driver')
                RFSE.Stage('Driver: AgilentDMM >> mode: set >> command: Reset', 'driver')
            else:
                type_setting_agilent = 'Manual'

        if type_setting_agilent == 'Manual':
            RFSE.Report("TYPE_SETTING_AGILENT34460A", "set", 'string', 'Manual')
            self.AutomaticAgilent34460A = False
            RFSE.Messenger("set", "Make settings Agilent34460A#@agilent34460a", "Make settings:\n"
                                                                                "Turn on the device\n"
                                                                                "Set Timeout = 10000\n"
                                                                                "Set Reset\n"
                                                                                "Press OK")

#######################################################################################################################

        if init:
            if self.AutomaticAgilent34460A:
                MOSC.hash_passed()
            else:
                MOSC.hash_failed()

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def InitializationFluke5520A(self, init=True) -> None:
        type_setting_fluke = RFSE.Messenger("get", "Choose a way to connect FLUKE5520A#@fluke5520a",
                                                   "Please select an FLUKE5520 instrument setup type",
                                                   "choice=Automatic;Manual")

        RFSE.Stage(" ")

        RFSE.Report("TYPE_SETTING_FLUKE5520A", "info", "string", "Device setting type")

###################################################   Fluke5520 Init   ################################################
###############################################   Fluke5520 SET Timeout  ##############################################
################################################   Fluke5520 SET Reset  ###############################################

        if type_setting_fluke == 'Automatic':

            choices = None

            RFSE.Stage('Driver: Fluke5000 >> mode: init >> command: ', 'driver')
            fluke_5520a_status = 'connected'

            if fluke_5520a_status != 'connected':
                choices = RFSE.Messenger("get", "Fluke5520A initialization not successful#@fluke5520a",
                                         "Failed to initialize Fluke5520A. Do you want to continue measuring in "
                                         "Manual mode?", "boolean")
            if not choices or fluke_5520a_status == 'connected':

                self.AutomaticFluke5520A = True

                RFSE.Report("TYPE_SETTING_FLUKE5520A", "set", "string", "Automatic")
                RFSE.Stage('Driver: Fluke5000 >> mode: set >> command: Timeout = 10000', 'driver')
                RFSE.Stage('Driver: Fluke5000 >> mode: set >> command: Reset', 'driver')
            else:
                type_setting_fluke = 'Manual'

        if type_setting_fluke == 'Manual':
            RFSE.Report("TYPE_SETTING_FLUKE5520A", "set", "string", "Manual")
            self.AutomaticFluke5520A = False
            RFSE.Messenger("set", "Make settings on Fluke5520A#@fluke5520a", "Make settings:\n"
                                                                             "Turn on the device\n"
                                                                             "Set Timeout = 10000\n"
                                                                             "Set Reset\n"
                                                                             "Press OK")

#######################################################################################################################
        if init:
            if self.AutomaticFluke5520A:
                MOSC.hash_passed()
            else:
                MOSC.hash_failed()

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
####################################################################################################################

    def SettingMeasurementLimits(self, verified, error) -> None:
        self.LowerLimitResult = verified - error
        self.UpperLimitResult = verified + error

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def CallMessengerChoices(self, verified, error, result, reference_number) -> str:
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

    def CallMessengerErrorPoint(self, verified, error, result, reference_number) -> None:
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

    @staticmethod
    def LoadTablesHeadInfo() -> None:
        RFSE.Report('VDC', 'info', 'table', "Range#100;"
                                            "Point#100;"
                                            "Result#100;"
                                            "Accuracy#100;"
                                            "Permissible error#100;"
                                            "Conclusion#100;")

        RFSE.Report('VAC', 'info', 'table', "Range#100;"
                                            "Point#100;"
                                            "Frequency#100;"
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

        RFSE.Report('IDC', 'info', 'table', "Range#100;"
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
        RFSE.Stage(" ")

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def __init_connected_and_type_connected(self):
        type_setting_Fluke5520A = RFSE.Report("TYPE_SETTING_FLUKE5520A", "get", "string", "", 'string')
        type_setting_Agilent34460A = RFSE.Report("TYPE_SETTING_AGILENT34460A", "get", "string", "", 'string')

        if len(type_setting_Agilent34460A) == 0 or len(type_setting_Fluke5520A) == 0:
            self.FirstScriptStart = True
            return
        else:
            self.FirstScriptStart = False

        if type_setting_Fluke5520A.lower() == 'automatic':
            self.AutomaticFluke5520A = True
        else:
            self.AutomaticFluke5520A = False

        if type_setting_Agilent34460A.lower() == 'automatic':
            self.AutomaticAgilent34460A = True
        else:
            self.AutomaticAgilent34460A = False


Poverka = ExFluke5000Agilent34460A()
