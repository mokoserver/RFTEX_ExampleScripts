import RFSE
import MTLG
import MOSC

MTLG.TelegramProgram('alpha', 'Registration unit', 'set', 'registration', 'string')
RFSE.Stage("*********************************************************")
RFSE.Stage("*************** Registration unit script ****************")
RFSE.Stage("*********************************************************")
RFSE.Stage(" ")

#region Equipment registration$Reg
MOSC.hashstatus("$Reg")
RFSE.Program('tree', 'set', 'select = Equipment registration$Reg')

RFSE.Utility("IZRCSMinfo", "set", "Registration")

ProtocolNumber = RFSE.Utility("IZRCSMinfo", "get", "ProtocolNumber", "string")
CurrentDate = RFSE.Utility("IZRCSMinfo", "get", "CurrentDate", "string")
ModelDevice = RFSE.Utility("IZRCSMinfo", "get", "ModelDevice", "string")
SerialNumber = RFSE.Utility("IZRCSMinfo", "get", "SerialNumber", "string")
Owner = RFSE.Utility("IZRCSMinfo", "get", "owner", "string")
Request = RFSE.Utility("IZRCSMinfo", "get", "Request", "string")
Verifier = RFSE.Utility("IZRCSMinfo", "get", "Verifier", "string")
VerificationDate = RFSE.Utility("IZRCSMinfo", "get", "CurrentDate", "string")

RFSE.Report("REGISTRATION_ProtocolNumber", "info", "string", "Measurement protocol number")
RFSE.Report("REGISTRATION_CurrentDate", "info", "string", "The current date")
RFSE.Report("REGISTRATION_ModelDevice", "info", "string", "Model of device under test")
RFSE.Report("REGISTRATION_SerialNumber", "info", "string", "Device serial number")
RFSE.Report("REGISTRATION_Owner", "info", "string", "Customer")
RFSE.Report("REGISTRATION_Request", "info", "string", "Request")
RFSE.Report("REGISTRATION_Verifier", "info", "string", "Verifier")
RFSE.Report("REGISTRATION_VerificationDate", "info", "string", "The verification date")
RFSE.Report("REGISTRATION_FormNumber", "info", "string", "Form number")
RFSE.Report("REGISTRATION_GosNumber", "info", "string", "Measurement number")

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

RFSE.Report("VerificationConditions", "set", "table", f"Temperature; 20°C; {Temperature}")
RFSE.Report("VerificationConditions", "set", "table", f"Humidity; 60%; {Humidity}")
RFSE.Report("VerificationConditions", "set", "table", f"Pressure; 100kPa; {Pressure}")
RFSE.Stage(" ")

MOSC.hash_passed()
#endregion Equipment registration$Reg

RFSE.EndScript()
