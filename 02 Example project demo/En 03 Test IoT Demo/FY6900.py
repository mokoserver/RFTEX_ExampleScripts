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

#######################################################################################################################
##########################################  FY6900 CHOICE CONNECTED  ##################################################
#######################################################################################################################

    def Choice_Connected(self) -> str:

        type_connected = RFSE.Messenger("get", "Choose a way to connect FY6900#TestIoT.png",
                                            "Please select an FY6900 instrument setup type\n"
                                            "Attention. By selecting simulation mode, "
                                            "you run all measurements in simulation mode!!!",
                                            "choice=Automatic;Manual;Simulation")

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
            case 'Automatic':
                self.IsAutomatic = True
                RFSE.Report("TYPE_SETTING_FY6900", "set", 'string', 'Automatic')
            case "Manual":
                self.IsAutomatic = False
                RFSE.Report("TYPE_SETTING_FY6900", "set", 'string', 'Manual')

########################################################################################################################

        if init:
            if self.IsAutomatic:
                RFSE.Report('DevicesUsed', 'set', 'table', 'FY6900;Connected;')
                MOSC.hash_passed()
            else:
                RFSE.Report('DevicesUsed', 'set', 'table', 'FY6900;Disconnected;')
                MOSC.hash_failed()

#######################################################################################################################
############################################  FY6900 Init device  #####################################################
#######################################################################################################################

    def INIT_DEVICE(self) -> str:
        if self.IsAutomatic:
            RFSE.Stage('Driver: FY6900 >> mode: init >> command: ', 'driver')
            return "connected"
        else:
            RFSE.Messenger("set", "Make settings FY6900#@attention",
                           "Make settings:\nTurn on the device\nPress OK")

            return "connected"

#######################################################################################################################
###############################################  FY6900 SET WAVE  #####################################################
#######################################################################################################################

    def SET_WAVE(self, wave: str) -> None:
        if self.IsAutomatic:
            RFSE.Stage(f"name -> FY6900; mode -> set; command -> WAVE = {wave}", 'driver')
        else:
            RFSE.Messenger("set", "Make settings FY6900#TestIoT.png", "Make settings:\n"
                                                                      f"Set WAVE = {wave}\n"
                                                                      "Press OK")

#######################################################################################################################
#############################################  FY6900 SET AMPLITUDE  ##################################################
#######################################################################################################################

    def SET_AMPLITUDE(self, amplitude: str) -> None:
        if self.IsAutomatic:
            RFSE.Stage(f"name -> FY6900; mode -> set; command -> amplitude = {amplitude}", 'driver')
        else:
            RFSE.Messenger("set", "Make settings FY6900#TestIoT.png", "Make settings:\n"
                                                                      f"Set amplitude = {amplitude}\n"
                                                                      "Press OK")

#######################################################################################################################
#############################################  FY6900 SET FREQUENCY  ##################################################
#######################################################################################################################

    def SET_FREQUENCY(self, frequency: (int | float | str)) -> None:
        if self.IsAutomatic:
            RFSE.Stage(f"name -> FY6900; mode -> set; command -> frequency = {frequency}", 'driver')
        else:
            RFSE.Messenger("set", "Make settings FY6900#TestIoT.png", "Make settings:\n"
                                                                      f"Set frequency = {frequency}\n"
                                                                      "Press OK")
