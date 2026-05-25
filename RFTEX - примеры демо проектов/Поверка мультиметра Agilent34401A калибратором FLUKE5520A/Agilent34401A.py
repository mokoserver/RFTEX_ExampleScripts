import RFSE
import MOSC


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

class Agilent34401A:

    def __init__(self):
        self.IsAutomatic = False

#######################################################################################################################
#######################################  Agilent34401A CHOICE CONNECTED  ##############################################
#######################################################################################################################
    def Choice_Connected(self) -> str:

        type_connected = RFSE.Messenger("get", "Choose a way to connect AGILENT34401A#@agilent34401a",
                                            "Please select an Agilent34401A instrument setup type\n"
                                            "Attention. By selecting simulation mode, "
                                            "you run all measurements in simulation mode!!!",
                                            "choice=Automatic;Manual")

        RFSE.Stage(" ")
        return type_connected

#######################################################################################################################
#########################################  Agilent34401A Initialization  ##############################################
#######################################################################################################################

    def Initialization(self, init: bool = True):

        type_setting_agilent = self.Choice_Connected()

        RFSE.Report("TYPE_SETTING_AGILENT34401A", "info", "string", "Device setting type")

        match type_setting_agilent:
            case 'Automatic':
                self.IsAutomatic = True
                RFSE.Report("TYPE_SETTING_AGILENT34401A", "set", 'string', 'Automatic')
            case "Manual":
                self.IsAutomatic = False
                RFSE.Report("TYPE_SETTING_AGILENT34401A", "set", 'string', 'Manual')

        self.SET_TIMEOUT()
        self.SET_RESET()

#######################################################################################################################

        if init:
            if self.IsAutomatic:
                MOSC.hash_passed()
            else:
                MOSC.hash_failed()

#######################################################################################################################
##########################################  Agilent34401A Init device  ################################################
#######################################################################################################################

    def INIT_DEVICE(self) -> str:
        if self.IsAutomatic:
            RFSE.Stage('Driver: AgilentDMM >> mode: init >> command: ', 'driver')
            return "connected"
        else:
            RFSE.Messenger("set", "Make settings Agilent34401A#@agilent34401a",
                           "Make settings:\nTurn on the device\nPress OK")

            return "connected"

#######################################################################################################################
##########################################  Agilent34401A SET TIMEOUT  ################################################
#######################################################################################################################

    def SET_TIMEOUT(self) -> None:
        if self.IsAutomatic:
            RFSE.Stage('Driver: AgilentDMM >> mode: set >> command: Timeout = 10000', 'driver')
        else:
            RFSE.Messenger("set", "Make settings Agilent34401A#@agilent34401a",
                           "Make settings:\nSet Reset\nPress OK")

#######################################################################################################################
############################################  Agilent34401A SET RESET  ################################################
#######################################################################################################################

    def SET_RESET(self) -> None:
        if self.IsAutomatic:
            RFSE.Stage('Driver: AgilentDMM >> mode: set >> command: Reset', 'driver')
        else:
            RFSE.Messenger("set", "Make settings Agilent34401A#@agilent34401a",
                           "Make settings:\nSet Timeout = 10000\nPress OK")

#######################################################################################################################
#############################################  Agilent34401A SET FUNC  ################################################
#######################################################################################################################

    def SET_FUNC(self, WireConnection: str) -> None:
        if self.IsAutomatic:
            RFSE.Stage(f'Driver: AgilentDMM >> mode: set >> command: func = {WireConnection} ', 'driver')
        else:
            RFSE.Messenger('set', 'Make settings on Agilent34401A#@agilent34401a',
                           f'Make settings:\nSet func = {WireConnection}\nPress OK')

#######################################################################################################################
#############################################  Agilent34401A SET NPLC  ################################################
#######################################################################################################################

    def SET_NPLC_100(self) -> None:
        if self.IsAutomatic:
            RFSE.Stage('Driver: AgilentDMM >> mode: set >> command: NPLC = 100 ', 'driver')
        else:
            RFSE.Messenger('set', 'Make settings on Agilent34401A#@agilent34401a',
                           f'Make settings:\nSet NPLC = 100\nPress OK')

#######################################################################################################################
#############################################  Agilent34401A SET RES  #################################################
#######################################################################################################################

    def SET_RES_MIN(self) -> None:
        if self.IsAutomatic:
            RFSE.Stage('Driver: AgilentDMM >> mode: set >> command: RES = MIN ', 'driver')
        else:
            RFSE.Messenger('set', 'Make settings on Agilent34401A#@agilent34401a',
                           'Set Resolution = MIN;\nPress OK')

#######################################################################################################################
############################################  Agilent34401A SET BAND  #################################################
#######################################################################################################################

    def SET_BAND_MIN(self) -> None:

        if self.IsAutomatic:
            RFSE.Stage('Driver: AgilentDMM >> mode: set >> command: BAND = 3 ', 'driver')
        else:
            RFSE.Messenger('set', 'Make settings on Agilent34401A#@agilent34401a',
                           'Set the filter to 3 Hz;\nPress OK')

#######################################################################################################################
###########################################  Agilent34401A SET RANGE  #################################################
#######################################################################################################################
    def SET_RANGE(self, range: (str | float | int)) -> None:

        if self.IsAutomatic:
            RFSE.Stage('Driver: AgilentDMM >> mode: set >> command: range = {range}', 'driver')
        else:
            RFSE.Messenger("set", "Make settings on Agilent34401A#@agilent34401a",
                           f"Make settings:\nSet range = {range}\nPress OK")

#######################################################################################################################
##########################################  Agilent34401A SET AUTOZERO  ###############################################
#######################################################################################################################
    def SET_AUTOZERO_ONCE(self) -> None:

        if self.IsAutomatic:
            RFSE.Stage('Driver: AgilentDMM >> mode: set >> command: AUTOZERO = ONCE', 'driver')
        else:
            RFSE.Messenger('set', 'Make settings on Agilent34401A#@agilent34401a',
                           'Set the resolution to 4th decimal places;\nClick OK')

#######################################################################################################################
##########################################  Agilent34401A READ RESULT  ################################################
#######################################################################################################################
    def Read_Result(self, verified: (int, float)) -> (str, int, float):

        if self.IsAutomatic:
            RFSE.Stage('DriverSet AgilentDMM >> mode: get >> command: result = read', 'driver')
            result = verified
        else:
            result = RFSE.Messenger("get", "Input result#@notes",
                                    "Enter the measured result from Agilent34401A\nPress OK", "string")
        RFSE.Stage(" ")
        return result
