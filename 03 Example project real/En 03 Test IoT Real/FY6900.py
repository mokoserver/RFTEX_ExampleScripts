import MOSC
import RFSE


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

class FY6900:

    def __init__(self):
        self.IsAutomatic = False
        self.IsSimulation = False

#######################################################################################################################
##########################################  FY6900 CHOICE CONNECTED  ##################################################
#######################################################################################################################

    def Choice_Connected(self) -> str:

        type_setting_BK1697B = RFSE.Report("TYPE_SETTING_BK1697B", "get", "string", "", 'string')
        type_setting_APPA207 = RFSE.Report("TYPE_SETTING_APPA207", "get", "string", "", 'string')

        if "Simulation" not in [type_setting_BK1697B, type_setting_APPA207]:
            type_connected = RFSE.Messenger("get", "Choose a way to connect FY6900#TestIoT.png",
                                            "Please select an FY6900 instrument setup type\n"
                                            "Attention. By selecting simulation mode, "
                                            "you run all measurements in simulation mode!!!",
                                            "choice=Automatic;Manual;Simulation")
        else:
            type_connected = 'Simulation'

        RFSE.Stage(" ")

        return type_connected

#######################################################################################################################
###########################################  FY6900 Initialization  ###################################################
#######################################################################################################################

    def Initialization(self, init: bool = True) -> None:

        RFSE.Stage("*********************************************************")
        RFSE.Stage("***************** Init device BK1697B *******************")
        RFSE.Stage("*********************************************************")
        RFSE.Stage(" ")

        type_setting_fy = self.Choice_Connected()

        RFSE.Report("TYPE_SETTING_FY6900", "info", "string", "Device setting type")
        RFSE.Stage(" ")

        match type_setting_fy:
            case 'Simulation':
                self.IsSimulation = True
                RFSE.Report("TYPE_SETTING_FY6900", "set", 'string', 'Simulation')
            case 'Automatic':
                self.IsAutomatic = True
                RFSE.Report("TYPE_SETTING_FY6900", "set", 'string', 'Automatic')
            case "Manual":
                self.IsAutomatic = False
                RFSE.Report("TYPE_SETTING_FY6900", "set", 'string', 'Manual')

        status_connected = self.INIT_DEVICE()

        if status_connected != 'connected':
            is_manual_connected = self.NOT_SUCCESSFUL_INIT()
            if is_manual_connected:
                RFSE.Report("TYPE_SETTING_FY6900", "set", 'string', 'Manual')
                self.IsAutomatic = False
            self.INIT_DEVICE()

########################################################################################################################

        if init:
            if self.IsAutomatic or self.IsSimulation:
                RFSE.Report('DevicesUsed', 'set', 'table', 'FY6900;Connected;')
                MOSC.hash_passed()
            else:
                RFSE.Report('DevicesUsed', 'set', 'table', 'FY6900;Disconnected;')
                MOSC.hash_failed()

#######################################################################################################################
############################################  FY6900 Init device  #####################################################
#######################################################################################################################

    def INIT_DEVICE(self) -> str:
        if self.IsSimulation:
            RFSE.Stage('Driver: FY6900 >> mode: init >> command: ', 'driver')
            return "connected"
        elif self.IsAutomatic:
            return RFSE.Driver('FY6900', 'init', '')
        else:
            RFSE.Messenger("set", "Make settings FY6900#@attention",
                           "Make settings:\nTurn on the device\nPress OK")

            return "connected"

#######################################################################################################################
######################################  FY6900 NOT SUCCESFUL Init device  #############################################
#######################################################################################################################

    @staticmethod
    def NOT_SUCCESSFUL_INIT() -> bool:
        return RFSE.Messenger("get", "FY6900 initialization not successful#@attention",
                              "Failed to initialize FY6900. Do you want to continue measuring in "
                              "Manual mode?", "boolean")

#######################################################################################################################
###############################################  FY6900 SET WAVE  #####################################################
#######################################################################################################################

    def SET_WAVE(self, wave: str) -> None:
        if self.IsSimulation:
            RFSE.Stage(f"name -> FY6900; mode -> set; command -> WAVE = {wave}", 'driver')
        elif self.IsAutomatic:
            RFSE.Driver('FY6900', 'set', f'WAVE = {wave}')
        else:
            RFSE.Messenger("set", "Make settings FY6900#TestIoT.png", "Make settings:\n"
                                                                      f"Set WAVE = {wave}\n"
                                                                      "Press OK")

#######################################################################################################################
#############################################  FY6900 SET AMPLITUDE  ##################################################
#######################################################################################################################

    def SET_AMPLITUDE(self, amplitude: str) -> None:
        if self.IsSimulation:
            RFSE.Stage(f"name -> FY6900; mode -> set; command -> amplitude = {amplitude}", 'driver')
        elif self.IsAutomatic:
            RFSE.Driver('FY6900', 'set', f'amplitude = {amplitude}')
        else:
            RFSE.Messenger("set", "Make settings FY6900#TestIoT.png", "Make settings:\n"
                                                                      f"Set amplitude = {amplitude}\n"
                                                                      "Press OK")

#######################################################################################################################
#############################################  FY6900 SET FREQUENCY  ##################################################
#######################################################################################################################

    def SET_FREQUENCY(self, frequency: (str | float | int)) -> None:
        if self.IsSimulation:
            RFSE.Stage(f"name -> FY6900; mode -> set; command -> frequency = {frequency}", 'driver')
        elif self.IsAutomatic:
            RFSE.Driver('FY6900', 'set', f'frequency = {frequency}')
        else:
            RFSE.Messenger("set", "Make settings FY6900#TestIoT.png", "Make settings:\n"
                                                                      f"Set frequency = {frequency}\n"
                                                                      "Press OK")
