import RFSE
import MOSC

RFSE.Stage("*********************************************************")
RFSE.Stage("********* Скрипт проверки регистрации модуля *********")
RFSE.Stage("*********************************************************")
UtilityInfo = "RFTEX_example_info"
#region Регистрация оборудования$Reg
MOSC.hashStatus("$Reg")
RFSE.Program('tree', 'set', 'select = Регистрация оборудования$Reg')

RFSE.Utility(UtilityInfo, "set", "Registration")
RFSE.Utility(UtilityInfo, "set", "Conditions")

ProtocolNumber = RFSE.Utility(UtilityInfo, "get", "ProtocolNumber", "string")
CurrentDate = RFSE.Utility(UtilityInfo, "get", "CurrentDate", "string")
ModelDevice = RFSE.Utility(UtilityInfo, "get", "ModelDevice", "string")
SerialNumber = RFSE.Utility(UtilityInfo, "get", "SerialNumber", "string")
Owner = RFSE.Utility(UtilityInfo, "get", "owner", "string")
Request = RFSE.Utility(UtilityInfo, "get", "Request", "string")
Verifier = RFSE.Utility(UtilityInfo, "get", "Verifier", "string")
VerificationDate = RFSE.Utility(UtilityInfo, "get", "CurrentDate", "string")

RFSE.Report("ProtocolNumber", "info", "string", "Номер протокола измерений")
RFSE.Report("CurrentDate", "info", "string", "Текущая дата")
RFSE.Report("ModelDevice", "info", "string", "Модель поверяемого прибора")
RFSE.Report("SerialNumber", "info", "string", "Заводской номер прибора")
RFSE.Report("Owner", "info", "string", "Заказчик")
RFSE.Report("Request", "info", "string", "Заявка")
RFSE.Report("Verifier", "info", "string", "Поверитель")
RFSE.Report("VerificationDate", "info", "string", "Дата поверки")
RFSE.Report("FormNumber", "info", "string", "Номер формы")
RFSE.Report("GosNumber", "info", "string", "Номер госреестра")

RFSE.Report("ProtocolNumber", "set", "string", ProtocolNumber)
RFSE.Report("CurrentDate", "set", "string", CurrentDate)
RFSE.Report("ModelDevice", "set", "string", ModelDevice)
RFSE.Report("SerialNumber", "set", "string", SerialNumber)
RFSE.Report("Owner", "set", "string", Owner)
RFSE.Report("Request", "set", "string", Request)
RFSE.Report("Verifier", "set", "string", Verifier)
RFSE.Report("VerificationDate", "set", "string", VerificationDate)
RFSE.Report("FormNumber", "set", "string", "432-164")
RFSE.Report("GosNumber", "set", "string", "52147-12")

RFSE.Utility(UtilityInfo, "set", "Conditions")

Temperature = RFSE.Utility(UtilityInfo, "get", "Temperature", "string")
Humidity = RFSE.Utility(UtilityInfo, "get", "Humidity", "string")
Pressure = RFSE.Utility(UtilityInfo, "get", "Pressure", "string")

RFSE.Report('VerificationConditions', 'info', 'table', "Контролируемые параметры#150;"
                                                       "Требования НД#100;"
                                                       "Измеренные значения#100;")

RFSE.Report("VerificationConditions", "set", "table", f"Температура; 20°C; {Temperature}")
RFSE.Report("VerificationConditions", "set", "table", f"Влажность; 60%; {Humidity}")
RFSE.Report("VerificationConditions", "set", "table", f"Давление; 100кПа; {Pressure}")

text_report_fluke = "U=(34мВ-1000В), Погр.±(0,0012-0,005)%, 2 разряд\\nI=(24мкА-10А), Погр.±(0,011-0,1)%, " \
    "1 разряд\\nU~=(25мВ-1000В), 10Гц-500кГц, Погр.±(0,017-1)% 2 разряд\\nI~=(2мкА-10А), 20Гц-20кГц, " \
    "Погр.±(0,046-3,02)%, 2 разряд\\nR=(0,50[Ом]-50[Ом]), (110М[Ом]-1100М[Ом]), Погр. ±(0,33-2)%, 3 разряд"
text_report_voltmeter = "U=(0,001В-1000В), Погр.±(0,000315 – 0,0011)% 2-й разряд\\nU~=(0.75мВ-1000В), " \
                        "10Гц-50кГц, Погр.±(0,003 – 0,23)%, 2-й разряд\\nI=(70нА-30А), Погр.±(0,00275 – 0,05)%, " \
                        "1 разряд\\nI~=(70нА-20А), 0,1Гц-10кГц, Погр.±(0,0165 – 0,55)%, 2-й разряд"

RFSE.Report('VerificationTools', 'info', 'table', "Наименование, тип, заводской номер#350;"
                                                  "Метрологические характеристики#400;")

RFSE.Report("VerificationTools", "set", "table", f"Калибратор многофункциональный Fluke 5522A Зав.№2182904; "
            f"{text_report_fluke}")
RFSE.Report("VerificationTools", "set", "table", f"Вольтметр универсальный калибратор Н4-12 Зав.№005211; "
            f"{text_report_voltmeter}")

MOSC.hash_passed()
#endregion Регистрация оборудования$Reg

RFSE.EndScript()
