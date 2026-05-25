import MOSC
import RFSE


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

class APPA207:

    def __init__(self):
        self.IsAutomatic = False
        self.IsSimulation = False

#######################################################################################################################
##########################################  APPA207 CHOICE CONNECTED  #################################################
#######################################################################################################################

    def Choice_Connected(self) -> str:

        type_setting_FY6900 = RFSE.Report("TYPE_SETTING_FY6900", "get", "string", "", 'string')
        type_setting_BK1697B = RFSE.Report("TYPE_SETTING_BK1697B", "get", "string", "", 'string')

        if "Simulation" not in [type_setting_FY6900, type_setting_BK1697B]:
            type_connected = RFSE.Messenger("get", "Choose a way to connect APPA207#TestIoT.png",
                                            "Please select an APPA207 instrument setup type\n"
                                            "Attention. By selecting simulation mode, "
                                            "you run all measurements in simulation mode!!!",
                                            "choice=Automatic;Manual;Simulation")
        else:
            type_connected = 'Simulation'

        RFSE.Stage(" ")
        return type_connected

#######################################################################################################################
###########################################  APPA207 Initialization  ##################################################
#######################################################################################################################

    def Initialization(self, init: bool = True) -> None:

        RFSE.Stage("*********************************************************")
        RFSE.Stage("**************** Init device APPA207 ********************")
        RFSE.Stage("*********************************************************")
        RFSE.Stage(" ")

        type_setting_appa = self.Choice_Connected()

        RFSE.Report("TYPE_SETTING_APPA207", "info", "string", "Device setting type")
        RFSE.Stage(" ")

        match type_setting_appa:
            case 'Simulation':
                self.IsSimulation = True
                RFSE.Report("TYPE_SETTING_APPA207", "set", 'string', 'Simulation')
            case 'Automatic':
                self.IsAutomatic = True
                RFSE.Report("TYPE_SETTING_APPA207", "set", 'string', 'Automatic')
            case "Manual":
                self.IsAutomatic = False
                RFSE.Report("TYPE_SETTING_APPA207", "set", 'string', 'Manual')

        status_connected = self.INIT_DEVICE()

        if status_connected != 'connected':
            is_manual_connected = self.NOT_SUCCESSFUL_INIT()
            if is_manual_connected:
                RFSE.Report("TYPE_SETTING_APPA207", "set", 'string', 'Manual')
                self.IsAutomatic = False
            self.INIT_DEVICE()

########################################################################################################################

        if init:
            if self.IsAutomatic or self.IsSimulation:
                RFSE.Report('DevicesUsed', 'set', 'table', 'APPA207;Connected;')
                MOSC.hash_passed()
            else:
                RFSE.Report('DevicesUsed', 'set', 'table', 'APPA207;Disconnected;')
                MOSC.hash_failed()

#######################################################################################################################
#############################################  APPA207 Init device  ###################################################
#######################################################################################################################

    def INIT_DEVICE(self) -> str:
        if self.IsSimulation:
            RFSE.Stage('Driver: APPA207 >> mode: init >> command: ', 'driver')
            return "connected"
        elif self.IsAutomatic:
            return RFSE.Driver('APPA207', 'init', '')
        else:
            RFSE.Messenger("set", "Make settings APPA207#@attention",
                           "Make settings:\nTurn on the device\nPress OK")

            return "connected"

#######################################################################################################################
#####################################  APPA207 NOT SUCCESFUL Init device  #############################################
#######################################################################################################################

    @staticmethod
    def NOT_SUCCESSFUL_INIT() -> bool:
        return RFSE.Messenger("get", "APPA207 initialization not successful#@attention",
                              "Failed to initialize APPA207. Do you want to continue measuring in "
                              "Manual mode?", "boolean")

#######################################################################################################################
###########################################  APPA207 READ RESULT  #####################################################
#######################################################################################################################

    def READ_RESULT(self, value: (float | int)) -> str:
        if self.IsSimulation:
            RFSE.Stage(f"name -> APPA207; mode -> get; command -> read", 'driver')
            result = str(value)
        elif self.IsAutomatic:
            result = RFSE.Driver('APPA207', 'get', 'read')
        else:
            result = RFSE.Messenger("get", "Input result#@notes",
                                    "Enter the measured result from APPA207\nPress OK", "string")
        RFSE.Stage(" ")
        return result
