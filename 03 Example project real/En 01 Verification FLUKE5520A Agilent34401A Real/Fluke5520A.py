import RFSE
import MOSC


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

class Fluke5520A:

    def __init__(self):
        self.IsSimulation = False
        self.IsAutomatic = False

#######################################################################################################################
#########################################  Fluke5520A CHOICE CONNECTED  ###############################################
#######################################################################################################################

    def Choice_Connected(self) -> str:
        type_setting_Agilent34401A = RFSE.Report("TYPE_SETTING_AGILENT34401A", "get", "string", "", 'string')

        if type_setting_Agilent34401A != 'Simulation':

            type_connected = RFSE.Messenger("get", "Choose a way to connect Fluke5520A#@fluke5520a",
                                            "Please select an Fluke5520A instrument setup type\n"
                                            "Attention. By selecting simulation mode, "
                                            "you run all measurements in simulation mode!!!",
                                            "choice=Automatic;Manual;Simulation")
        else:
            type_connected = "Simulation"

        RFSE.Stage(" ")
        return type_connected

#######################################################################################################################
############################################  Fluke5520A Initialization  ##############################################
#######################################################################################################################

    def Initialization(self, init: bool = True) -> None:

        type_setting_fluke = self.Choice_Connected()

        RFSE.Report("TYPE_SETTING_FLUKE5520A", "info", "string", "Device setting type")

        match type_setting_fluke:
            case 'Simulation':
                self.IsSimulation = True
                RFSE.Report("TYPE_SETTING_FLUKE5520A", "set", 'string', 'Simulation')
            case 'Automatic':
                self.IsAutomatic = True
                RFSE.Report("TYPE_SETTING_FLUKE5520A", "set", 'string', 'Automatic')
            case "Manual":
                self.IsAutomatic = False
                RFSE.Report("TYPE_SETTING_FLUKE5520A", "set", 'string', 'Manual')

        status_connected = self.INIT_DEVICE()

        if status_connected != 'connected':
            is_manual_connected = self.NOT_SUCCESSFUL_INIT()
            if is_manual_connected:
                RFSE.Report("TYPE_SETTING_FLUKE5520A", "set", 'string', 'Manual')
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
############################################  Fluke5520A Init device   ################################################
#######################################################################################################################

    def INIT_DEVICE(self) -> str:
        if self.IsSimulation:
            RFSE.Stage('Driver: Fluke5000 >> mode: init >> command: ', 'driver')
            return "connected"
        elif self.IsAutomatic:
            return RFSE.Driver('Fluke5000', 'init', '')
        else:
            RFSE.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                           "Make settings:\nTurn on the device\nPress OK")

            return "connected"

#######################################################################################################################
######################################  Fluke5520A NOT SUCCESSFUL Init device   #######################################
#######################################################################################################################

    def NOT_SUCCESSFUL_INIT(self) -> bool:
        return RFSE.Messenger("get", "Fluke5520A initialization not successful#@fluke5520a",
                              "Failed to initialize Fluke5520A. Do you want to continue measuring in "
                              "Manual mode?", "boolean")

#######################################################################################################################
#############################################  Fluke5520A SET TIMEOUT  ################################################
#######################################################################################################################

    def SET_TIMEOUT(self) -> None:
        if self.IsSimulation:
            RFSE.Stage('Driver: Fluke5000 >> mode: set >> command: Timeout = 10000', 'driver')
        elif self.IsAutomatic:
            RFSE.Driver('Fluke5000', 'set', 'Timeout = 10000')
        else:
            RFSE.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                           "Make settings:\nSet Reset\nPress OK")

#######################################################################################################################
###############################################  Fluke5520A SET RESET  ################################################
#######################################################################################################################

    def SET_RESET(self) -> None:
        if self.IsSimulation:
            RFSE.Stage('Driver: Fluke5000 >> mode: set >> command: Reset', 'driver')
        elif self.IsAutomatic:
            RFSE.Driver('Fluke5000', 'set', 'Reset')
        else:
            RFSE.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                           "Make settings:\nSet Timeout = 10000\nPress OK")

#######################################################################################################################
############################################   Fluke5520 SET OUT = AUX   ##############################################
#######################################################################################################################

    def SET_OUT_AUX(self) -> None:
        if self.IsSimulation:
            RFSE.Stage('Driver: Fluke5000 >> mode: set >> command: OUT = AUX', 'driver')
        elif self.IsAutomatic:
            RFSE.Driver('Fluke5000', 'set', 'OUT = AUX')
        else:
            RFSE.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                           'Make settings:\nSet OUT = AUX\nPress OK')

#######################################################################################################################
############################################   Fluke5520 SET OUT = NORMAL   ###########################################
#######################################################################################################################

    def SET_OUT_NORMAL(self) -> None:
        if self.IsSimulation:
            RFSE.Stage('Driver: Fluke5000 >> mode: set >> command: OUT = NORMAL', 'driver')
        elif self.IsAutomatic:
            RFSE.Driver('Fluke5000', 'set', 'OUT = NORMAL')
        else:
            RFSE.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                           'Make settings:\nSet OUT = NORMAL\nPress OK')

#######################################################################################################################
############################################   Fluke5520 SET Conn = 4w  ###############################################
#######################################################################################################################

    def SET_CONN_4W(self) -> None:
        if self.IsSimulation:
            RFSE.Stage('Driver: Fluke5000 >> mode: set >> command: Conn = 4w', 'driver')
        elif self.IsAutomatic:
            RFSE.Driver('Fluke5000', 'set', 'Conn = 4w')
        else:
            RFSE.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                           'Make settings:\nSet Conn = 4w\nPress OK')

#######################################################################################################################
############################################   Fluke5520 SET Conn = NO  ###############################################
#######################################################################################################################

    def SET_CONN_NO(self) -> None:
        if self.IsSimulation:
            RFSE.Stage('Driver: Fluke5000 >> mode: set >> command: Conn = NO', 'driver')
        elif self.IsAutomatic:
            RFSE.Driver('Fluke5000', 'set', 'Conn = NO')
        else:
            RFSE.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                           'Make settings:\nSet Conn = NO\nPress OK')

#######################################################################################################################
###############################################   Fluke5520 SET VDC   #################################################
#######################################################################################################################
    def SET_VDC(self, verified: (str | float | int)) -> None:
        if self.IsSimulation:
            RFSE.Stage(f'Driver: Fluke5000 >> mode: set >> command: VDC = {verified}', 'driver')
        elif self.IsAutomatic:
            RFSE.Driver('Fluke5000', 'set', f'VDC = {verified}')
        else:
            RFSE.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                           f"Make settings:\nSet VDC = {verified}\nPress OK")

#######################################################################################################################
###############################################   Fluke5520 SET VAC   #################################################
#######################################################################################################################

    def SET_VAC(self, verified: (str | float | int), frequency: (str | float | int)) -> None:
        if self.IsSimulation:
            RFSE.Stage(f'DriverSet Fluke5000 >> mode: set >> command: VAC = {verified} {frequency}', 'driver')
        elif self.IsAutomatic:
            RFSE.Driver('Fluke5000', 'set', f'VAC = {verified} {frequency}')
        else:
            RFSE.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                           f"Make settings:\nSet VAC = {verified} {frequency}\nPress OK")

#######################################################################################################################
###############################################   Fluke5520 SET R   ###################################################
#######################################################################################################################
    def SET_R(self, verified: (str | float | int)) -> None:
        if self.IsSimulation:
            RFSE.Stage(f'Driver: Fluke5000 >> mode: set >> command: R = {verified}', 'driver')
        elif self.IsAutomatic:
            RFSE.Driver('Fluke5000', 'set', f'R = {verified}')
        else:
            RFSE.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                           f"Make settings:\nSet R = {verified}\nPress OK")

#######################################################################################################################
###############################################   Fluke5520 SET IDC   #################################################
#######################################################################################################################
    def SET_IDC(self, verified: (str | float | int)) -> None:
        if self.IsSimulation:
            RFSE.Stage(f'Driver: Fluke5000 >> mode: set >> command: IDC = {verified}', 'driver')
        elif self.IsAutomatic:
            RFSE.Driver('Fluke5000', 'set', f'IDC = {verified}')
        else:
            RFSE.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                           f"Make settings:\nSet IDC = {verified}\nPress OK")

#######################################################################################################################
###############################################   Fluke5520 SET IAC   #################################################
#######################################################################################################################
    def SET_IAC(self, verified: (str | float | int), frequency: (str | float | int)) -> None:
        if self.IsSimulation:
            RFSE.Stage(f'DriverSet Fluke5000 >> mode: set >> command: IAC = {verified} {frequency}', 'driver')
        elif self.IsAutomatic:
            RFSE.Driver('Fluke5000', 'set', f'IAC = {verified} {frequency}')
        else:
            RFSE.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                           f"Make settings:\nSet IAC = {verified} {frequency}\nPress OK")

#######################################################################################################################
#######################################   Fluke5520 SET SwitchOFF = Enable   ##########################################
#######################################################################################################################

    def SET_SwitchOFF_Enable(self) -> None:
        if self.IsSimulation:
            RFSE.Stage('Driver: Fluke5000 >> mode: set >> command: SwitchOFF = ENABLE', 'driver')
        elif self.IsAutomatic:
            RFSE.Driver('Fluke5000', 'set', 'SwitchOFF = ENABLE')
        else:
            RFSE.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                           'Make settings:\nSet Stop\nPress OK')

#######################################################################################################################
##########################################   Fluke5520 SET SwitchOFF = DIS   ##########################################
#######################################################################################################################

    def SET_SwitchOFF_DIS(self) -> None:
        if self.IsSimulation:
            RFSE.Stage('Driver: Fluke5000 >> mode: set >> command: SwitchOFF = DIS', 'driver')
        elif self.IsAutomatic:
            RFSE.Driver('Fluke5000', 'set', 'SwitchOFF = DISABLE')
        else:
            RFSE.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                           'Make settings:\nSet SwitchOFF = DISABLE\nPress OK')

#######################################################################################################################
##############################################   Fluke5520 SET STOP   #################################################
#######################################################################################################################

    def SET_STOP(self) -> None:
        if self.IsSimulation:
            RFSE.Stage('Driver: Fluke5000 >> mode: set >> command: Stop', 'driver')
        elif self.IsAutomatic:
            RFSE.Driver('Fluke5000', 'set', 'Stop')
        else:
            RFSE.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                           'Make settings:\nSet Stop\nPress OK')