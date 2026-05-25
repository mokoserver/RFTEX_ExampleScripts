import RFSE
import MOSC

RFSE.Stage("*********************************************************")
RFSE.Stage("********* Registration verification unit script *********")
RFSE.Stage("*********************************************************")

#region Equipment registration$Reg
MOSC.hashStatus("$Reg")
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

RFSE.Report("ProtocolNumber", "info", "string", "Measurement protocol number")
RFSE.Report("CurrentDate", "info", "string", "The current date")
RFSE.Report("ModelDevice", "info", "string", "Model of device under test")
RFSE.Report("SerialNumber", "info", "string", "Device serial number")
RFSE.Report("Owner", "info", "string", "Customer")
RFSE.Report("Request", "info", "string", "Request")
RFSE.Report("Verifier", "info", "string", "Verifier")
RFSE.Report("VerificationDate", "info", "string", "The verification date")
RFSE.Report("FormNumber", "info", "string", "Form number")
RFSE.Report("GosNumber", "info", "string", "Measurement number")

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

text_report_fluke = "U=(34mV-1000V), Error±(0,0012-0,005)%, 2nd category\\nI=(24uA-10A), Error±(0,011-0,1)%, " \
    "1 category\\nU~(25mV-1000V), 10Hz-500kHz, Error±(0,017-1)% 2nd category\\nI~=(2uA-10A), 20Hz-20kHz, " \
    "Error±(0,046-3,02)%, 2nd category\\nR=(0,50[[Ohm]]-50[Ohm]), (110M[Ohm]-1100M[Ohm]), Error ±(0,33-2)%, 3nd category"
text_report_voltmeter = "U=(0,001V-1000V), Error±(0,000315 – 0,0011)%  2-nd category\\nU~=(0.75mV-1000V), " \
                        "10Hz-50kHz, Error±(0,003 – 0,23)%, 2-nd category\\nI=(70nA-30A), Error±(0,00275 – 0,05)%, " \
                        "1 category\\nI~=(70nA-20A), 0,1Hz-10kHz, Error±(0,0165 – 0,55)%, 2-nd category"

RFSE.Report('VerificationTools', 'info', 'table', "Name, type, serial number#350;"
                                                  "Metrological characteristics#400;")

RFSE.Report("VerificationTools", "set", "table", f"Fluke 5522A Multifunctional Calibrator Serial №2182904; "
            f"{text_report_fluke}")
RFSE.Report("VerificationTools", "set", "table", f"Universal voltmeter calibrator H4-12 Serial №005211; "
            f"{text_report_voltmeter}")

MOSC.hash_passed()
#endregion Equipment registration$Reg

RFSE.EndScript()
