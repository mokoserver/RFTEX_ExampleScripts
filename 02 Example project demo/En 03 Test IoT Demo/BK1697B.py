import MOSC
import RFSE


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

class BK1697B:

    def __init__(self):
        self.IsAutomatic = False
        self.IsOutputON = False

#######################################################################################################################
##########################################  BK1697B CHOICE CONNECTED  #################################################
#######################################################################################################################

    def Choice_Connected(self) -> str:

        type_connected = RFSE.Messenger("get", "Choose a way to connect BK1697B#TestIoT.png",
                                                   "Please select an BK1697B instrument setup type\n"
                                                   "Attention. By selecting simulation mode, "
                                                   "you run all measurements in simulation mode!!!",
                                                   "choice=Automatic;Manual")

        RFSE.Stage(" ")
        return type_connected

#######################################################################################################################
###########################################  BK1697B Initialization  ##################################################
#######################################################################################################################

    def Initialization(self, init: bool = True) -> None:

        RFSE.Stage("*********************************************************")
        RFSE.Stage("***************** Init device BK1697B *******************")
        RFSE.Stage("*********************************************************")
        RFSE.Stage(" ")

        type_setting_bk = self.Choice_Connected()

        RFSE.Report("TYPE_SETTING_BK1697B", "info", "string", "Device setting type")
        RFSE.Stage(" ")

        match type_setting_bk:
            case 'Automatic':
                self.IsAutomatic = True
                RFSE.Report("TYPE_SETTING_BK1697B", "set", 'string', 'Automatic')
            case "Manual":
                self.IsAutomatic = False
                RFSE.Report("TYPE_SETTING_BK1697B", "set", 'string', 'Manual')


########################################################################################################################

        if init:
            if self.IsAutomatic:
                RFSE.Report('DevicesUsed', 'set', 'table', 'BK1697B;Connected;')
                MOSC.hash_passed()
            else:
                RFSE.Report('DevicesUsed', 'set', 'table', 'BK1697B;Disconnected;')
                MOSC.hash_failed()

#######################################################################################################################
#############################################  BK1697B Init device  ###################################################
#######################################################################################################################

    def INIT_DEVICE(self) -> str:
        if self.IsAutomatic:
            RFSE.Stage('Driver: BK1697B >> mode: init >> command: ', 'driver')
            return "connected"
        else:
            RFSE.Messenger("set", "Make settings BK1697B#@attention",
                           "Make settings:\nTurn on the device\nPress OK")

            return "connected"


#######################################################################################################################
###############################################  BK1697B SET VALUE  ###################################################
#######################################################################################################################

    def SET_VALUE(self, value: (float | int | str), Wireconnection: str) -> None:
        if self.IsAutomatic:
            RFSE.Stage(f"name -> BK1697B; mode -> set; command -> {Wireconnection} = {value}", 'driver')
        else:
            RFSE.Messenger("set", "Make settings BK1697B#TestIoT.png", "Make settings:\n"
                                                                       f"Set {Wireconnection} = {value}\n"
                                                                       "Press OK")

#######################################################################################################################
#############################################  BK1697B SET OUTPUT ON  #################################################
#######################################################################################################################

    def SET_OUTPUT_ON(self) -> None:
        if not self.IsOutputON:
            self.IsOutputON = True
            if self.IsAutomatic:
                RFSE.Stage('name -> BK1697B; mode -> set; command -> OUTPUT = ON', 'set')
            else:
                RFSE.Messenger("set", "Make settings BK1697B#TestIoT.png", "Make settings:\n"
                                                                           "Set OUTPUT = ON\n"
                                                                           "Press OK")
            RFSE.Stage(" ")

#######################################################################################################################
############################################  BK1697B SET OUTPUT OFF  #################################################
#######################################################################################################################

    def SET_OUTPUT_OFF(self) -> None:
        self.IsOutputON = False
        if self.IsAutomatic:
            RFSE.Stage('name -> BK1697B; mode -> set; command -> OUTPUT = OFF', 'set')
        else:
            RFSE.Messenger("set", "Make settings BK1697B#TestIoT.png", "Make settings:\n"
                                                                       "Set OUTPUT = OFF\n"
                                                                       "Press OK")
