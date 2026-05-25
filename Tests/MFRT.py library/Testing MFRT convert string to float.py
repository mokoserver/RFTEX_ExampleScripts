import RFSE
import MFRT

RFSE.Messenger("set", "Testing MFRT function convert string to float#@notes",
               "This script will demonstrate the function of converting a number from a string to a number")

RFSE.Report('StringToFloat', 'info', 'table', 'Input number#150;'
                                              'Output number#150;')

test_list_input_value = ["100.00000u", "100.0000u", "100.000u", "100.00u", "100.0u", "100u",
                         "100.00000m", "100.0000m", "100.000m", "100.00m", "100.0m", "100m",
                         "100.00000",  "100.0000",  "100.000",  "100.00",  "100.0",  "100",
                         "100.00000k", "100.0000k", "100.000k", "100.00k", "100.0k", "100k",
                         "100.00000M", "100.0000M", "100.000M", "100.00M", "100.0M", "100M"]

for input_value in test_list_input_value:
    output_value = MFRT.ConvertStringToFloat(input_value)
    RFSE.Report('StringToFloat', 'set', 'table', f'{input_value};'
                                                 f'{output_value}')

RFSE.Messenger("set", "Testing MFRT failed delimiter value function convert string to float#@failed",
               "This script will demonstrate failed delimiter value the function of converting a "
               "number from a string to a number")

RFSE.Report('StringToFloatFailedDelimiter', 'info', 'table', 'Input number#150;'
                                                             'Output number#150;')

test_list_input_value_error_delimiter = ["100/00000u", "100#0000u", "100*000u", "100)00u", "100(0u", "100u.",
                                         "100/00000m", "100#0000m", "100*000m", "100)00m", "100(0m", "100m.",
                                         "100/00000",  "100#0000",  "100*000",  "100)00",  "100(0",  "100.",
                                         "100/00000k", "100#0000k", "100*000k", "100)00k", "100(0k", "100k.",
                                         "100/00000M", "100#0000M", "100*000M", "100)00M", "100(0M", "100M."]

for input_value in test_list_input_value_error_delimiter:
    output_value = MFRT.ConvertStringToFloat(input_value)
    RFSE.Report('StringToFloatFailedDelimiter', 'set', 'table', f'{input_value};'
                                                                f'{output_value}')

RFSE.Messenger("set", "Testing MFRT failed function convert string to float#@failed",
               "This script will demonstrate failed the function of converting a number from a string to a number")

RFSE.Report('StringToFloatFailedPrefixOrValue', 'info', 'table', 'Input number#150;'
                                                                 'Output number#150;')

test_list_error_input = [100, 100.001, '100s', '100rh', '0.0001rh', '1212||m']

for input_value in test_list_error_input:
    output_value = MFRT.ConvertStringToFloat(input_value)
    RFSE.Report('StringToFloatFailedPrefixOrValue', 'set', 'table', f'{input_value};'
                                                                    f'{output_value}')

RFSE.EndScript()
