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
############################################ Модуль измерения и отчета #################################################
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

        name_table = hash.split('$')[1]

        self.MaxError = float((100 + percent_error) / 100)
        self.MinError = float((100 - percent_error) / 100)

        self.ContinueMeasurement = True

        f_value = MFRT.ConvertStringToFloat(value)

        self.ListValue.append(f_value)

        RFSE.Stage(f"Измерение {WireConnection} -> значение = {value}, значение лимита = {value_limit},"
                   f" сигнал генератора = {wave}, амплитуда = {amplitude}, лимит амплитуды = {amplitude_limit}, "
                   f"частота = {frequency}, процент допустимой ошибки = {percent_error}")

#######################################################################################################################
#####################################################  VDC  ###########################################################
#######################################################################################################################

        if WireConnection == 'VDC':

#######################################################################################################################
#################################################  Измерение VDC  #####################################################
#######################################################################################################################

            if self.AutomaticBK1697B:
                RFSE.Stage(f"name -> BK1697B; mode -> set; command -> VDC = {value}", 'driver')
            else:
                RFSE.Messenger("set", "Произведите настройки BK1697B#TestIoT.png", "Произведите настройки:\n"
                                                                                   f"Установите VDC = {value}\n"
                                                                                   "Нажмите ОК")
            if self.AutomaticFY6900:
                RFSE.Stage(f"name -> FY6900; mode -> set; command -> WAVE = {wave}", 'driver')
                RFSE.Stage(f"name -> FY6900; mode -> set; command -> amplitude = {amplitude}", 'driver')
                RFSE.Stage(f"name -> FY6900; mode -> set; command -> frequency = {frequency}", 'driver')
            else:
                RFSE.Messenger("set", "Произведите настройки BK1697B#TestIoT.png", "Произведите настройки:\n"
                                                                                   f"Установите WAVE = {wave}\n"
                                                                                   f"Установите amplitude = {amplitude}\n"
                                                                                   f"Установите frequency = {frequency}\n"
                                                                                   "Нажмите ОК")

            result = self.GetResultMeasurent(value=f_value)

#######################################################################################################################
###################################################  Отчет VDC  #######################################################
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
###############################################  Измерение IDC ########################################################`
#######################################################################################################################

            if self.AutomaticBK1697B:
                RFSE.Stage(f"name -> BK1697B; mode -> set; command -> IDC = {value}", 'driver')
            else:
                RFSE.Messenger("set", "Произведите настройки BK1697B#TestIoT.png", "Произведите настройки:\n"
                                                                                   f"Установите IDC = {value}\n"
                                                                                   "Нажмите ОК")
            if self.AutomaticFY6900:
                RFSE.Stage(f"name -> FY6900; mode -> set; command -> WAVE = {wave}", 'driver')
                RFSE.Stage(f"name -> FY6900; mode -> set; command -> amplitude = {amplitude}", 'driver')
                RFSE.Stage(f"name -> FY6900; mode -> set; command -> frequency = {frequency}", 'driver')
            else:
                RFSE.Messenger("set", "Произведите настройки BK1697B#TestIoT.png", "Произведите настройки:\n"
                                                                                   f"Установите WAVE = {wave}\n"
                                                                                   f"Установите amplitude = {amplitude}\n"
                                                                                   f"Установите frequency = {frequency}\n"
                                                                                   "Нажмите ОК")

            result = self.GetResultMeasurent(value=f_value)

#######################################################################################################################
#####################################################  Отчет IDC  #####################################################
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
####################################  Модуль возвращения результата измерения  #########################################
########################################################################################################################
########################################################################################################################
    def GetResultMeasurent(
            self,
            value: (float, int),

    ) -> float:

        f_result, result = 0, 0
        while self.ContinueMeasurement:
            time.sleep(self.TimeDelay)
            if self.AutomaticAPPA207:
                RFSE.Stage(f"name -> APPA207; mode -> get; command -> read", 'driver')
                result = value
            else:
                result = RFSE.Messenger("get", "Результат измерения#@notes",
                                        "Запишите значение измереня с прибора APPA207\nНажмите ОК", "string")
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
                    self.Status = 'Неуспешно'
                else:
                    self.Status = 'ОК'
                self.Count_meas = 0
            self.ContinueMeasurement = False
        self.ListResult.append(f_result)
        return result

########################################################################################################################
########################################################################################################################
##################################### Модуль проверки подключения устройств ############################################
########################################################################################################################
########################################################################################################################

    def CheckWireConnection(self, WireConnection: str) -> None:

        if self.WireConnection != 'VDC':
            if WireConnection == 'VDC':
                MTLG.TelegramMessenger('beta', 'set', 'Тестирование VDC',
                                       'Подключите BK1697 к APPA207 чтобы проверить VDC.\n'
                                       'Выход калибратора OUT', 'string')

                RFSE.Messenger('set', 'Тестирование VDC#TestIoT_VDC.png',
                               'Подключите BK1697 к APPA207 чтобы проверить VDC.\n'
                               'Выход калибратора OUT')

        if self.WireConnection != "IDC":
            if WireConnection == 'IDC':
                MTLG.TelegramMessenger('beta', 'set', 'Тестирование IDC',
                                       'Подключите BK1697 к APPA207, чтобы проверить ток IDC.\n'
                                       'Выход калибратора OUT', 'string')

                RFSE.Messenger('set', 'Тестирование IDC#TestIoT_IDC.png',
                               'Подключите BK1697 к APPA207, чтобы проверить ток IDC.\n'
                               'Выход калибратора OUT')

        self.WireConnection = WireConnection
        RFSE.Stage(' ')

########################################################################################################################
########################################################################################################################
##################################### Модуль проверки инициализации приборов ###########################################
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

        RFSE.Stage("***********************************************************")
        RFSE.Stage("***************** Инициализация BK1697B *******************")
        RFSE.Stage("***********************************************************")
        RFSE.Stage(" ")

        type_setting_BK1697B = RFSE.Messenger("get", "Выберите способ подключения BK1697B#TestIoT.png",
                                              "Пожалуйста, выберите тип настройки прибора BK1697B\n",
                                              "choice=Автоматический;Вручную")

        RFSE.Report("ТИП_НАСТРОЙКИ_BK1697B", "info", "string", "Тип настройки устройства")
        RFSE.Stage(" ")

        if type_setting_BK1697B == 'Автоматический':
            choices = None
            RFSE.Stage('Driver: BK1697B >> mode: init >> command: ', 'driver')
            BK1697B_INIT = 'connected'

            if BK1697B_INIT != 'connected':
                choices = RFSE.Messenger("get", "Инициализация BK1697B не удалась#@attention",
                                         "Не удалось инициализировать BK1697B. Продолжить измерения в "
                                         "ручном режиме?", "boolean")
            if not choices:
                self.AutomaticBK1697B = True
                RFSE.Report("ТИП_НАСТРОЙКИ_BK1697B", "set", 'string', 'Автоматический')
            else:
                type_setting_BK1697B = 'Вручную'

        if type_setting_BK1697B == 'Вручную':
            self.AutomaticBK1697B = False
            RFSE.Report("ТИП_НАСТРОЙКИ_BK1697B", "set", 'string', 'Вручную')
            RFSE.Messenger("set", "Произведите настройки BK1697B#TestIoT.png", "Произведите настройки:\n"
                                                                               "Подключите устройство\n"
                                                                               "Нажмите ОК")

########################################################################################################################

        if init:
            if self.AutomaticBK1697B:
                RFSE.Report('DevicesUsed', 'set', 'table', 'BK1697B;Подключен;')
                MOSC.hash_passed()
            else:
                RFSE.Report('DevicesUsed', 'set', 'table', 'BK1697B;Отключен;')
                MOSC.hash_failed()

########################################################################################################################
########################################################################################################################
########################################################################################################################
    def InitializationFY6900(self, init=True):

        RFSE.Stage("***********************************************************")
        RFSE.Stage("***************** Инициализация FY6900 ********************")
        RFSE.Stage("***********************************************************")
        RFSE.Stage(" ")

        type_setting_FY6900 = RFSE.Messenger("get", "Выберите способ подключения FY6900#TestIoT.png",
                                             "Пожалуйста, выберите тип настройки прибора FY6900\n",
                                             "choice=Автоматический;Вручную")

        RFSE.Report("ТИП_НАСТРОЙКИ_FY6900", "info", "string", "Тип настройки устройства")
        RFSE.Stage(" ")

        if type_setting_FY6900 == 'Автоматический':
            choices = None
            RFSE.Stage('Driver: FY6900 >> mode: init >> command: ', 'driver')
            FY6900_INIT = 'connected'

            if FY6900_INIT != 'connected':
                self.AutomaticFY6900 = True
                RFSE.Report("ТИП_НАСТРОЙКИ_FY6900", "set", "string", "Автоматический")
                choices = RFSE.Messenger("get", "Инициализация FY6900 не удалась#@attention",
                                         "Не удалось инициализировать FY6900. Продолжить измерения в "
                                         "ручном режиме?", "boolean")
            if not choices:
                self.AutomaticFY6900 = True
                RFSE.Report("ТИП_НАСТРОЙКИ_FY6900", "set", 'string', 'Автоматический')
            else:
                type_setting_FY6900 = 'Вручную'

        if type_setting_FY6900 == 'Вручную':
            RFSE.Report("ТИП_НАСТРОЙКИ_FY6900", "set", "string", "Вручную")
            RFSE.Messenger("set", "Произведите настройки FY6900#TestIoT.png", "Произведите настройки:\n"
                                                                              "Подключите устройство\n"
                                                                              "Нажмите ОК")

########################################################################################################################

        if init:
            if self.AutomaticFY6900:
                RFSE.Report('DevicesUsed', 'set', 'table', 'FY6900;Подключен;')
                MOSC.hash_passed()
            else:
                RFSE.Report('DevicesUsed', 'set', 'table', 'FY6900;Отключен;')
                MOSC.hash_failed()

########################################################################################################################
########################################################################################################################
########################################################################################################################

    def InitializationAPPA207(self, init=True):

        RFSE.Stage("***********************************************************")
        RFSE.Stage("**************** Инициализация APPA207 ********************")
        RFSE.Stage("***********************************************************")
        RFSE.Stage(" ")

        type_setting_APPA207 = RFSE.Messenger("get", "Выберите способ подключения APPA207#TestIoT.png",
                                              "Пожалуйста, выберите тип настройки прибора APPA207\n",
                                              "choice=Автоматический;Вручную")

        RFSE.Report("ТИП_НАСТРОЙКИ_APPA207", "info", "string", "Тип настройки устройства")
        RFSE.Stage(" ")

        if type_setting_APPA207 == 'Автоматический':

            choices = None
            RFSE.Stage('Driver: APPA207 >> mode: init >> command: ', 'driver')
            APPA207_INIT = 'connected'

            if APPA207_INIT != 'connected':
                self.AutomaticAPPA207 = True
                RFSE.Report("ТИП_НАСТРОЙКИ_APPA207", "set", "string", "Автоматический")
                choices = RFSE.Messenger("get", "Инициализация APPA207 не удалась#@attention",
                                         "Не удалось инициализировать APPA207. Продолжить измерения в "
                                         "ручном режиме?", "boolean")
            if not choices:
                self.AutomaticAPPA207 = True
                RFSE.Report("ТИП_НАСТРОЙКИ_APPA207", "set", 'string', 'Автоматический')
            else:
                type_setting_APPA207 = 'Вручную'

        if type_setting_APPA207 == 'Вручную':
            self.AutomaticAPPA207 = False
            RFSE.Report("ТИП_НАСТРОЙКИ_APPA207", "set", "string", "Вручную")
            RFSE.Messenger("set", "Произведите настройки APPA207#TestIoT.png", "Произведите настройки:\n"
                                                                               "Подключите устройство\n"
                                                                               "Нажмите ОК")

########################################################################################################################

        if init:
            if self.AutomaticAPPA207:
                RFSE.Report('DevicesUsed', 'set', 'table', 'APPA207;Подключен;')
                MOSC.hash_passed()
            else:
                RFSE.Report('DevicesUsed', 'set', 'table', 'APPA207;Отключен;')
                MOSC.hash_failed()

########################################################################################################################
########################################################################################################################
############################################### Модуль работы с Graph ##################################################
########################################################################################################################
########################################################################################################################

    def CheckGraphInit(self) -> None:
        """
            Функция проверки инициализации Graph
            :return: None
        """
        if not self.GraphInit:
            RFSE.Stage("***********************************************************")
            RFSE.Stage("******************* Инициализация Graph   *****************")
            RFSE.Stage("***********************************************************")
            RFSE.Stage(" ")
            MGPH.GraphInit()
            self.GraphInit = True
            time.sleep(5)
            RFSE.Stage(" ")

########################################################################################################################
########################################################################################################################
########################################################################################################################

    def CreateGraph(self) -> None:
        """
            Функция создания Graph
            :return: None
        """
        self.CreateGraphValue()
        self.CreateGraphResult()
        self.FirstResult = False

########################################################################################################################
########################################################################################################################
########################################################################################################################

    def CreateGraphMask(self, value_limit: int) -> None:
        """
            Создание маски Graph
            :param value_limit: координата Ox
            :return: None
        """
        if self.FirstResult:
            RFSE.Stage("************************************************************")
            RFSE.Stage("***************** Создание маски Graph  ********************")
            RFSE.Stage("************************************************************")
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

    def CreateGraphValue(self) -> None:
        """
            Функция создания Graph значений
            :return: None
        """
        RFSE.Stage("***************************************************************")
        RFSE.Stage("************* Создание Graph вводимых значений ****************")
        RFSE.Stage("***************************************************************")
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

    def CreateGraphResult(self) -> None:
        """
            Функция создания Graph результата
            :return: None
        """
        RFSE.Stage("*****************************************************************")
        RFSE.Stage("*************** Создание Graph вводимых полученных **************")
        RFSE.Stage("*****************************************************************")
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

    def GetScreenshot(self) -> None:
        """
            Функция создания скриншота Graph, сохранения скриншота в Word и очистки Graph
            :return: None
        """
        RFSE.Stage("********************************************************")
        RFSE.Stage("************** Создание скриншота Graph ****************")
        RFSE.Stage("********************************************************")
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
################################# Модуль подключения и отключения выхода BK1697B #######################################
########################################################################################################################
########################################################################################################################

    def OutONNCommand(self) -> None:
        """
            Функция проверки выхода BK1697B на включение
            :return: None
        """
        if not self.OutCommand:
            self.OutCommand = True
            if self.AutomaticBK1697B:
                RFSE.Stage('name -> BK1697B; mode -> set; command -> OUTPUT = ON', 'set')
            else:
                RFSE.Messenger("set", "Произведите настройки BK1697B#TestIoT.png", "Произведите настройки:\n"
                                                                                   "Установите OUTPUT = ON\n"
                                                                                   "Нажмите ОК")
            RFSE.Stage(" ")

########################################################################################################################
########################################################################################################################
########################################################################################################################

    def SET_OUTPUT_OFF(self):
        """
             Функция проверки выхода BK1697B на отключение
            :return: None
        """
        self.OutCommand = False
        self.FirstResult = True
        if self.AutomaticBK1697B:
            RFSE.Stage('name -> BK1697B; mode -> set; command -> OUTPUT = OFF', 'set')
        else:
            RFSE.Messenger("set", "Произведите настройки BK1697B#TestIoT.png", "Произведите настройки:\n"
                                                                               "Установите OUTPUT = OFF\n"
                                                                               "Нажмите ОК")

########################################################################################################################
########################################################################################################################
################################# Модуль повторения или ошибок измерения ###############################################
########################################################################################################################
########################################################################################################################

    def CallMessengerChoices(self, result: (float, int), value: (float, int)) -> str:

        limit_type = "верхнему" if self.MaxError * value < result else "нижнему"
        limit_value = result - (self.MaxError * value) if limit_type == "верхнему" else self.MinError * value - result

        error_message = 'Хотите ли вы повторить переизмерение данной точки?\n'
        error_message += f'Нижний порог измерения <  Результат < Верхний порог измерения\n'
        error_message += f'{MFRT.ConvertFloatToString(self.MinError * value, resolution=3) if self.MinError * value > 0 else MFRT.ConvertFloatToString(0, resolution=3)} < '
        error_message += f'{MFRT.ConvertFloatToString(result, resolution=3)} < '
        error_message += f'{MFRT.ConvertFloatToString(self.MaxError * value, resolution=3)}\n'
        error_message += f'Измерение не соответствует {limit_type} пределу ' \
                         f'на {MFRT.ConvertFloatToString(limit_value, resolution=3)}'

        choices = RFSE.Messenger('get', 'Результат измерения не вошел в указанный предел#@repeat',
                                 error_message, 'boolean')

        self.FailedResult = True
        self.Count_meas = 0
        return choices

########################################################################################################################
########################################################################################################################
########################################################################################################################

    def CallMessengerErrorPoint(self, result: (float, int), value: (float, int)) -> None:

        limit_type = "верхнему" if self.MaxError * value < result else "нижнему"
        limit_value = result - (self.MaxError * value) if limit_type == "верхнему" else self.MinError * value - result
        error_message = 'Результат измерения не вошел в указанный предел\n'
        error_message += 'Значение переизмеряется\n'
        error_message += f'Нижний порог измерения <  Результат < Верхний порог измерения\n'
        error_message += f'{MFRT.ConvertFloatToString(self.MinError * value, resolution=3) if self.MinError * value > 0 else MFRT.ConvertFloatToString(0, resolution=3)} < '
        error_message += f'{MFRT.ConvertFloatToString(result, resolution=3)} < '
        error_message += f'{MFRT.ConvertFloatToString(self.MaxError * value, resolution=3)}\n'
        error_message += f'Измерение не соответствует {limit_type} пределу ' \
                         f'на {MFRT.ConvertFloatToString(limit_value, resolution=3)}'

        RFSE.Messenger('set', 'Измерение неуспешно#@failed', error_message, delaytime='5')
        self.Count_meas += 1

########################################################################################################################
########################################################################################################################
####################################### Модуль загрузки таблиц в RFSE.Report ###########################################
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

        RFSE.Report('VDC_RECTANGLE', 'info', 'table', "Value#100;"
                                                      "ValueLimit#100;"
                                                      "PercentError#100;"
                                                      "PermissibleVariation#150;"
                                                      "Wave#100;"
                                                      "Amplitude#100;"
                                                      "AmplitudeLimit#100;"
                                                      "Frequency#100;"
                                                      "Result#100;")

        RFSE.Report('VDC_TRAPEZOID', 'info', 'table', "Value#100;"
                                                      "ValueLimit#100;"
                                                      "PercentError#100;"
                                                      "PermissibleVariation#150;"
                                                      "Wave#100;"
                                                      "Amplitude#100;"
                                                      "AmplitudeLimit#100;"
                                                      "Frequency#100;"
                                                      "Result#100;")

        RFSE.Report('IDC_CMOS', 'info', 'table', "Value#100;"
                                                 "ValueLimit#100;"
                                                 "PercentError#100;"
                                                 "PermissibleVariation#150;"
                                                 "Wave#100;"
                                                 "Amplitude#100;"
                                                 "AmplitudeLimit#100;"
                                                 "Frequency#100;"
                                                 "Result#100;")

        RFSE.Report('IDC_PULSE', 'info', 'table', "Value#100;"
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
        type_setting_BK1697B = RFSE.Report("ТИП_НАСТРОЙКИ_BK1697B", "get", "string", "", 'string')
        type_setting_FY6900 = RFSE.Report("ТИП_НАСТРОЙКИ_FY6900", "get", "string", "", 'string')
        type_setting_APPA207 = RFSE.Report("ТИП_НАСТРОЙКИ_APPA207", "get", "string", "", 'string')

        if len(type_setting_BK1697B) == 0 or len(type_setting_FY6900) == 0 or len(type_setting_APPA207) == 0:
            self.FirstScriptStart = True
            return
        else:
            self.FirstScriptStart = False

        if type_setting_BK1697B == 'Автоматический':
            self.AutomaticBK1697B = True
        else:
            self.AutomaticBK1697B = False

        if type_setting_FY6900 == 'Автоматический':
            self.AutomaticFY6900 = True
        else:
            self.AutomaticFY6900 = False

        if type_setting_APPA207 == 'Автоматический':
            self.AutomaticAPPA207 = True
        else:
            self.AutomaticAPPA207 = False


Testing = DemoTestIoTMeasurement()


