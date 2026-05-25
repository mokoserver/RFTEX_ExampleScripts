import RFSE
import MOSC


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################


class Agilent34401A:

    def __init__(self):
        self.IsSimulation = False
        self.IsAutomatic = False

#######################################################################################################################
#######################################  Agilent34401A CHOICE CONNECTED  ##############################################
#######################################################################################################################
    def Choice_Connected(self) -> str:

        type_setting_Fluke5520A = RFSE.Report("TYPE_SETTING_FLUKE5520A", "get", "string", "", 'string')

        if type_setting_Fluke5520A != 'Simulation':
            type_connected = RFSE.Messenger("get", "Choose a way to connect AGILENT34401A#@agilent34401a",
                                            "Please select an Agilent34401A instrument setup type\n"
                                            "Attention. By selecting simulation mode, "
                                            "you run all measurements in simulation mode!!!",
                                            "choice=Automatic;Manual;Simulation")
        else:
            type_connected = "Simulation"

        RFSE.Stage(" ")
        return type_connected

#######################################################################################################################
#########################################  Agilent34401A Initialization  ##############################################
#######################################################################################################################

    def Initialization(self, init: bool = True) -> None:

        type_setting_agilent = self.Choice_Connected()

        RFSE.Report("TYPE_SETTING_AGILENT34401A", "info", "string", "Device setting type")

        match type_setting_agilent:
            case 'Simulation':
                self.IsSimulation = True
                RFSE.Report("TYPE_SETTING_AGILENT34401A", "set", 'string', 'Simulation')
            case 'Automatic':
                self.IsAutomatic = True
                RFSE.Report("TYPE_SETTING_AGILENT34401A", "set", 'string', 'Automatic')
            case "Manual":
                self.IsAutomatic = False
                RFSE.Report("TYPE_SETTING_AGILENT34401A", "set", 'string', 'Manual')

        status_connected = self.INIT_DEVICE()

        if status_connected != 'connected':
            is_manual_connected = self.NOT_SUCCESSFUL_INIT()
            if is_manual_connected:
                RFSE.Report("TYPE_SETTING_AGILENT34401A", "set", 'string', 'Manual')
                self.IsAutomatic = False
            self.INIT_DEVICE()

        self.SET_TIMEOUT()
        self.SET_RESET()

#######################################################################################################################

        if init:
            if self.IsAutomatic or self.IsSimulation:
                MOSC.hash_passed()
            else:
                MOSC.hash_failed()

#######################################################################################################################
##########################################  Agilent34401A Init device  ################################################
#######################################################################################################################

    def INIT_DEVICE(self) -> str:
        if self.IsSimulation:
            RFSE.Stage('Driver: AgilentDMM >> mode: init >> command: ', 'driver')
            return "connected"
        elif self.IsAutomatic:
            return RFSE.Driver('AgilentDMM', 'init', '')
        else:
            RFSE.Messenger("set", "Make settings Agilent34401A#@agilent34401a",
                           "Make settings:\nTurn on the device\nPress OK")

            return "connected"

#######################################################################################################################
###################################  Agilent34401A NOT SUCCESSFUL Init device   #######################################
#######################################################################################################################
    def NOT_SUCCESSFUL_INIT(self) -> bool:
        return RFSE.Messenger("get", "AGILENT34401A initialization not successful#@agilent34401a",
                              "Failed to initialize AGILENT34401A. Do you want to continue measuring in "
                              "Manual mode?", "boolean")

#######################################################################################################################
##########################################  Agilent34401A SET TIMEOUT  ################################################
#######################################################################################################################

    def SET_TIMEOUT(self) -> None:
        if self.IsSimulation:
            RFSE.Stage('Driver: AgilentDMM >> mode: set >> command: Timeout = 10000', 'driver')
        elif self.IsAutomatic:
            RFSE.Driver('AgilentDMM', 'set', 'Timeout = 10000')
        else:
            RFSE.Messenger("set", "Make settings Agilent34401A#@agilent34401a",
                           "Make settings:\nSet Reset\nPress OK")

#######################################################################################################################
############################################  Agilent34401A SET RESET  ################################################
#######################################################################################################################

    def SET_RESET(self) -> None:
        if self.IsSimulation:
            RFSE.Stage('Driver: AgilentDMM >> mode: set >> command: Reset', 'driver')
        elif self.IsAutomatic:
            RFSE.Driver('AgilentDMM', 'set', 'Reset')
        else:
            RFSE.Messenger("set", "Make settings Agilent34401A#@agilent34401a",
                           "Make settings:\nSet Timeout = 10000\nPress OK")

#######################################################################################################################
#############################################  Agilent34401A SET FUNC  ################################################
#######################################################################################################################

    def SET_FUNC(self, WireConnection: str) -> None:
        if self.IsSimulation:
            RFSE.Stage(f'Driver: AgilentDMM >> mode: set >> command: func = {WireConnection} ', 'driver')
        elif self.IsAutomatic:
            RFSE.Driver('AgilentDMM', 'set', f'func = {WireConnection}')
        else:
            RFSE.Messenger('set', 'Make settings on Agilent34401A#@agilent34401a',
                           f'Make settings:\nSet func = {WireConnection}\nPress OK')

#######################################################################################################################
#############################################  Agilent34401A SET NPLC  ################################################
#######################################################################################################################

    def SET_NPLC_100(self) -> None:
        if self.IsSimulation:
            RFSE.Stage('Driver: AgilentDMM >> mode: set >> command: NPLC = 100 ', 'driver')
        elif self.IsAutomatic:
            RFSE.Driver('AgilentDMM', 'set', 'NPLC = 100')
        else:
            RFSE.Messenger('set', 'Make settings on Agilent34401A#@agilent34401a',
                           f'Make settings:\nSet NPLC = 100\nPress OK')

#######################################################################################################################
#############################################  Agilent34401A SET RES  #################################################
#######################################################################################################################

    def SET_RES_MIN(self) -> None:
        if self.IsSimulation:
            RFSE.Stage('Driver: AgilentDMM >> mode: set >> command: RES = MIN ', 'driver')
        elif self.IsAutomatic:
            RFSE.Driver('AgilentDMM', 'set', 'RES = MIN')
        else:
            RFSE.Messenger('set', 'Make settings on Agilent34401A#@agilent34401a',
                           'Set Resolution = MIN;\nPress OK')

#######################################################################################################################
############################################  Agilent34401A SET BAND  #################################################
#######################################################################################################################

    def SET_BAND_MIN(self) -> None:

        if self.IsSimulation:
            RFSE.Stage('Driver: AgilentDMM >> mode: set >> command: BAND = 3 ', 'driver')
        elif self.IsAutomatic:
            RFSE.Driver('AgilentDMM', 'set', 'BAND = 3')
        else:
            RFSE.Messenger('set', 'Make settings on Agilent34401A#@agilent34401a',
                           'Set the filter to 3 Hz;\nPress OK')

#######################################################################################################################
###########################################  Agilent34401A SET RANGE  #################################################
#######################################################################################################################
    def SET_RANGE(self, range: (str | float | int)) -> None:
        if self.IsSimulation:
            RFSE.Stage('Driver: AgilentDMM >> mode: set >> command: range = {range}', 'driver')
        elif self.IsAutomatic:
            RFSE.Driver('AgilentDMM', 'set', f'range = {range}')
        else:
            RFSE.Messenger("set", "Make settings on Agilent34401A#@agilent34401a",
                           f"Make settings:\nSet range = {range}\nPress OK")

#######################################################################################################################
##########################################  Agilent34401A SET AUTOZERO  ###############################################
#######################################################################################################################
    def SET_AUTOZERO_ONCE(self) -> None:
        if self.IsSimulation:
            RFSE.Stage('Driver: AgilentDMM >> mode: set >> command: AUTOZERO = ONCE', 'driver')
        elif self.IsAutomatic:
            RFSE.Driver('AgilentDMM', 'set', 'AUTOZERO = ONCE')
        else:
            RFSE.Messenger('set', 'Make settings on Agilent34401A#@agilent34401a',
                           'Set the resolution to 4th decimal places;\nClick OK')

#######################################################################################################################
##########################################  Agilent34401A READ RESULT  ################################################
#######################################################################################################################
    def Read_Result(self, verified: (int, float)) -> (str, int, float):
        if self.IsSimulation:
            RFSE.Stage('DriverSet AgilentDMM >> mode: get >> command: result = read', 'driver')
            result = verified
        elif self.IsAutomatic:
            result = RFSE.Driver('AgilentDMM', 'get', 'read')
        else:
            result = RFSE.Messenger("get", "Input result#@notes",
                                    "Enter the measured result from Agilent34401A\nPress OK", "string")
        RFSE.Stage(" ")
        return result
