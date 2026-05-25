import RFSE
import MTLG
import MOSC

MTLG.TelegramProgram('alpha', 'Registration unit', 'set', 'registration')
RFSE.Stage("*********************************************************")
RFSE.Stage("*************** Registration unit script ****************")
RFSE.Stage("*********************************************************")
RFSE.Stage(" ")

#region Equipment registration$Reg
MOSC.hashStatus("$Reg")
RFSE.Program('tree', 'set', 'select = Equipment registration$Reg')

RFSE.Utility("CSMinfo", "set", "Registration")

ProtocolNumber = RFSE.Utility("CSMinfo", "get", "ProtocolNumber", "string")
CurrentDate = RFSE.Utility("CSMinfo", "get", "CurrentDate", "string")
ModelDevice = RFSE.Utility("CSMinfo", "get", "ModelDevice", "string")
SerialNumber = RFSE.Utility("CSMinfo", "get", "SerialNumber", "string")
Owner = RFSE.Utility("CSMinfo", "get", "owner", "string")
Request = RFSE.Utility("CSMinfo", "get", "Request", "string")
Verifier = RFSE.Utility("CSMinfo", "get", "Verifier", "string")
VerificationDate = RFSE.Utility("CSMinfo", "get", "CurrentDate", "string")

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

RFSE.Utility("CSMinfo", "set", "Conditions")

Temperature = RFSE.Utility("CSMinfo", "get", "Temperature", "string")
Humidity = RFSE.Utility("CSMinfo", "get", "Humidity", "string")
Pressure = RFSE.Utility("CSMinfo", "get", "Pressure", "string")

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
