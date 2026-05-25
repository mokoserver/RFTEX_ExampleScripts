import RFSE
import MTLG
import MOSC

MTLG.TelegramProgram('alpha', 'Проверка регистрации', 'set', 'Регистрация', 'string')
RFSE.Stage("*********************************************************")
RFSE.Stage("*************** Проверка регистрации ****************")
RFSE.Stage("*********************************************************")
RFSE.Stage(" ")

#region Регистрация оборудования$Reg
MOSC.hashStatus("$Reg")
RFSE.Program('tree', 'set', 'select = Регистрация оборудования$Reg')

RFSE.Utility("IZRCSMinfo", "set", "Registration")

ProtocolNumber = RFSE.Utility("IZRCSMinfo", "get", "ProtocolNumber", "string")
CurrentDate = RFSE.Utility("IZRCSMinfo", "get", "CurrentDate", "string")
ModelDevice = RFSE.Utility("IZRCSMinfo", "get", "ModelDevice", "string")
SerialNumber = RFSE.Utility("IZRCSMinfo", "get", "SerialNumber", "string")
Owner = RFSE.Utility("IZRCSMinfo", "get", "owner", "string")
Request = RFSE.Utility("IZRCSMinfo", "get", "Request", "string")
Verifier = RFSE.Utility("IZRCSMinfo", "get", "Verifier", "string")
VerificationDate = RFSE.Utility("IZRCSMinfo", "get", "CurrentDate", "string")

RFSE.Report("REGISTRATION_ProtocolNumber", "info", "string", "Номер протокола измерения")
RFSE.Report("REGISTRATION_CurrentDate", "info", "string", "Текущая дата")
RFSE.Report("REGISTRATION_ModelDevice", "info", "string", "Модель тестируемого устройства")
RFSE.Report("REGISTRATION_SerialNumber", "info", "string", "Серийный номер устройства")
RFSE.Report("REGISTRATION_Owner", "info", "string", "Владелец")
RFSE.Report("REGISTRATION_Request", "info", "string", "Запрос")
RFSE.Report("REGISTRATION_Verifier", "info", "string", "Поверяющий")
RFSE.Report("REGISTRATION_VerificationDate", "info", "string", "Дата поверки")
RFSE.Report("REGISTRATION_FormNumber", "info", "string", "Номер формы")
RFSE.Report("REGISTRATION_GosNumber", "info", "string", "Номер измерения")

RFSE.Report("REGISTRATION_ProtocolNumber", "set", "string", ProtocolNumber)
RFSE.Report("REGISTRATION_CurrentDate", "set", "string", CurrentDate)
RFSE.Report("REGISTRATION_ModelDevice", "set", "string", ModelDevice)
RFSE.Report("REGISTRATION_SerialNumber", "set", "string", SerialNumber)
RFSE.Report("REGISTRATION_Owner", "set", "string", Owner)
RFSE.Report("REGISTRATION_Request", "set", "string", Request)
RFSE.Report("REGISTRATION_Verifier", "set", "string", Verifier)
RFSE.Report("REGISTRATION_VerificationDate", "set", "string", VerificationDate)
RFSE.Report("REGISTRATION_FormNumber", "set", "string", "432-164")
RFSE.Report("REGISTRATION_GosNumber", "set", "string", "52147-12")

RFSE.Utility("IZRCSMinfo", "set", "Conditions")

Temperature = RFSE.Utility("IZRCSMinfo", "get", "Temperature", "string")
Humidity = RFSE.Utility("IZRCSMinfo", "get", "Humidity", "string")
Pressure = RFSE.Utility("IZRCSMinfo", "get", "Pressure", "string")

RFSE.Report('VerificationConditions', 'info', 'table', "Controlled parameters#150;"
                                                       "ND requirements#100;"
                                                       "Measured values#100;")

RFSE.Report("VerificationConditions", "set", "table", f"Температура; 20°C; {Temperature}")
RFSE.Report("VerificationConditions", "set", "table", f"Влажность; 60%; {Humidity}")
RFSE.Report("VerificationConditions", "set", "table", f"Давление; 100kPa; {Pressure}")
RFSE.Stage(" ")

MOSC.hash_passed()
#endregion Регистрация оборудования$Reg

RFSE.EndScript()
