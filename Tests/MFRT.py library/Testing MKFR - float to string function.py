import RFSE
import MFRT

RFSE.Messenger("set", "Testing MFRT function convert float to string#@notes",
               "This script demonstrates how to convert a float, int or string to a string of "
               "the given format. The format is specified using the reference number")

RFSE.Messenger("set", "Description#@info",
               "Value: translated value\n"
               "Reference number: a string number that will be the template to be converted\n"
               "Resolution: the number of zeros in the fractional part\n"
               "Delimiter: separator between number and fractional part\n"
               "Prefix: separator between number and fractional part")

test_list_reference_number = ["100.00000u", "100.0000u", "100.000u", "100.00u", "100.0u", "100u",
                              "100.00000m", "100.0000m", "100.000m", "100.00m", "100.0m", "100m",
                              "100.00000",  "100.0000",  "100.000",  "100.00",  "100.0",  "100",
                              "100.00000k", "100.0000k", "100.000k", "100.00k", "100.0k", "100k",
                              "100.00000M", "100.0000M", "100.000M", "100.00M", "100.0M", "100M"]

RFSE.Messenger("set", "Message#@notes",
               "Start translated value into:\n"
               "Value: str\n"
               "Reference number: str\n"
               "Resolution: None\n"
               "Prefix: None\n"
               "Delimiter: None")

RFSE.Report('StringConvertingRefNumber', 'info', 'table', 'Input value#130;'
                                                          'Reference number#130;'
                                                          'Resolution#75;'
                                                          'Prefix#50;'
                                                          'Delimiter#75;'
                                                          'Output value#130;')

resolution = prefix = delimiter = '-'

test_list_value = ["100m", "100", "100k"]

for input_value in test_list_value:
    for reference_number in test_list_reference_number:
        output_value = MFRT.ConvertFloatToString(input_value, reference_number)
        RFSE.Report('StringConvertingRefNumber', 'set', 'table', f'{input_value};'
                                                                 f'{reference_number};'
                                                                 f'{resolution};'
                                                                 f'{prefix};'
                                                                 f'{delimiter};'
                                                                 f'{output_value};')

RFSE.Messenger("set", "Message#@notes",
               "Start translated value into:\n"
               "Value: float\n"
               "Reference number: str\n"
               "Resolution: None\n"
               "Prefix: None\n"
               "Delimiter: None")


RFSE.Report('FloatConvertingRefNumber', 'info', 'table', 'Input value#130;'
                                                         'Reference number#130;'
                                                         'Resolution#75;'
                                                         'Prefix#50;'
                                                         'Delimiter#75;'
                                                         'Output value#130;')

test_list_value = [0.001, 100.001]

for input_value in test_list_value:
    for reference_number in test_list_reference_number:
        output_value = MFRT.ConvertFloatToString(input_value, reference_number)
        RFSE.Report('FloatConvertingRefNumber', 'set', 'table', f'{input_value};'
                                                                f'{reference_number};'
                                                                f'{resolution};'
                                                                f'{prefix};'
                                                                f'{delimiter};'
                                                                f'{output_value};')

RFSE.Messenger("set", "Message#@notes",
               "Start translated value into:\n"
               "Value: int\n"
               "Reference number: str\n"
               "Resolution: None\n"
               "Prefix: None\n"
               "Delimiter: None")

RFSE.Report('IntegerConvertingRefNumber', 'info', 'table', 'Input value#130;'
                                                           'Reference number#130;'
                                                           'Resolution#75;'
                                                           'Prefix#50;'
                                                           'Delimiter#75;'
                                                           'Output value#130;')

test_list_value = [0, 100]

for input_value in test_list_value:
    for reference_number in test_list_reference_number:
        output_value = MFRT.ConvertFloatToString(input_value, reference_number)
        RFSE.Report('IntegerConvertingRefNumber', 'set', 'table', f'{input_value};'
                                                                  f'{reference_number};'
                                                                  f'{resolution};'
                                                                  f'{prefix};'
                                                                  f'{delimiter};'
                                                                  f'{output_value};')


RFSE.Messenger("set", "Message#@notes",
               "Start translated value into:\n"
               "Value: int\n"
               "Reference number: str\n"
               "Resolution: int\n"
               "Prefix: None\n"
               "Delimiter: None")

RFSE.Report('ConvertingRefNumberRes', 'info', 'table', 'Input value#130;'
                                                       'Reference number#130;'
                                                       'Resolution#75;'
                                                       'Prefix#50;'
                                                       'Delimiter#75;'
                                                       'Output value#130;')


test_list_reference_number = ["100.00000u", "100.0000u", "100.000u", "100.00u", "100.0u", "100u",
                              "100.00000m", "100.0000m", "100.000m", "100.00m", "100.0m", "100m",
                              "100.00000", "100.0000", "100.000", "100.00", "100.0", "100",
                              "100.00000k", "100.0000k", "100.000k", "100.00k", "100.0k", "100k",
                              "100.00000M", "100.0000M", "100.000M", "100.00M", "100.0M", "100M"]

test_list_value = ["100m", "100", "100k"]

resolution = 10

for input_value in test_list_value:
    for reference_number in test_list_reference_number:
        output_value = MFRT.ConvertFloatToString(input_value, reference_number, resolution=resolution)
        RFSE.Report('ConvertingRefNumberRes', 'set', 'table', f'{input_value};'
                                                              f'{reference_number};'
                                                              f'{resolution};'
                                                              f'{prefix};'
                                                              f'{delimiter};'
                                                              f'{output_value};')


test_list_reference_number = ["100.00000u", "100.0000u", "100.000u", "100.00u", "100.0u", "100u",
                              "100.00000m", "100.0000m", "100.000m", "100.00m", "100.0m", "100m",
                              "100.00000", "100.0000", "100.000", "100.00", "100.0", "100",
                              "100.00000k", "100.0000k", "100.000k", "100.00k", "100.0k", "100k",
                              "100.00000M", "100.0000M", "100.000M", "100.00M", "100.0M", "100M"]

test_list_value = ["100m", "100", "100k"]

resolution = 2

for input_value in test_list_value:
    for reference_number in test_list_reference_number:
        output_value = MFRT.ConvertFloatToString(input_value, reference_number, resolution=resolution)
        RFSE.Report('ConvertingRefNumberRes', 'set', 'table', f'{input_value};'
                                                              f'{reference_number};'
                                                              f'{resolution};'
                                                              f'{prefix};'
                                                              f'{delimiter};'
                                                              f'{output_value};')

RFSE.Messenger("set", "Message#@notes",
               "Start translated value into:\n"
               "Value: int\n"
               "Reference number: str\n"
               "Resolution: int\n"
               "Prefix: None\n"
               "Delimiter: str")

RFSE.Report('ConvertingRefNumberResDel', 'info', 'table', 'Input value#130;'
                                                          'Reference number#130;'
                                                          'Resolution#75;'
                                                          'Prefix#50;'
                                                          'Delimiter#75;'
                                                          'Output value#130;')

test_list_reference_number = ["100.00000u", "100.0000u", "100.000u", "100.00u", "100.0u", "100u",
                              "100.00000m", "100.0000m", "100.000m", "100.00m", "100.0m", "100m",
                              "100.00000", "100.0000", "100.000", "100.00", "100.0", "100",
                              "100.00000k", "100.0000k", "100.000k", "100.00k", "100.0k", "100k",
                              "100.00000M", "100.0000M", "100.000M", "100.00M", "100.0M", "100M"]

test_list_value = ["100m", "100", "100k"]

delimiter = ','

resolution = 10

for input_value in test_list_value:
    for reference_number in test_list_reference_number:
        output_value = MFRT.ConvertFloatToString(input_value, reference_number, resolution=resolution,
                                                 delimiter=delimiter)
        RFSE.Report('ConvertingRefNumberResDel', 'set', 'table', f'{input_value};'
                                                                  f'{reference_number};'
                                                                  f'{resolution};'
                                                                  f'{prefix};'
                                                                  f'{delimiter};'
                                                                  f'{output_value};')


test_list_reference_number = ["100.00000u", "100.0000u", "100.000u", "100.00u", "100.0u", "100u",
                              "100.00000m", "100.0000m", "100.000m", "100.00m", "100.0m", "100m",
                              "100.00000", "100.0000", "100.000", "100.00", "100.0", "100",
                              "100.00000k", "100.0000k", "100.000k", "100.00k", "100.0k", "100k",
                              "100.00000M", "100.0000M", "100.000M", "100.00M", "100.0M", "100M"]

test_list_value = ["100m", "100", "100k"]

resolution = 2

delimiter = ','

for input_value in test_list_value:
    for reference_number in test_list_reference_number:
        output_value = MFRT.ConvertFloatToString(input_value, reference_number, resolution=resolution,
                                                 delimiter=delimiter)
        RFSE.Report('ConvertingRefNumberResDel', 'set', 'table', f'{input_value};'
                                                                 f'{reference_number};'
                                                                 f'{resolution};'
                                                                 f'{prefix};'
                                                                 f'{delimiter};'
                                                                 f'{output_value};')

RFSE.Messenger("set", "Message#@notes",
               "Start translated value into:\n"
               "Value: int\n"
               "Reference number: str\n"
               "Resolution: int\n"
               "Prefix: str\n"
               "Delimiter: str")

RFSE.Report('ConvertingRefNumberResDelPrefix', 'info', 'table', 'Input value#130;'
                                                                'Reference number#130;'
                                                                'Resolution#75;'
                                                                'Prefix#50;'
                                                                'Delimiter#75;'
                                                                'Output value#130;')

test_list_reference_number = ["100.00000u", "100.0000u", "100.000u", "100.00u", "100.0u", "100u",
                              "100.00000m", "100.0000m", "100.000m", "100.00m", "100.0m", "100m",
                              "100.00000", "100.0000", "100.000", "100.00", "100.0", "100",
                              "100.00000k", "100.0000k", "100.000k", "100.00k", "100.0k", "100k",
                              "100.00000M", "100.0000M", "100.000M", "100.00M", "100.0M", "100M"]

test_list_value = ["100m", "100", "100k"]

delimiter = ','

resolution = 10

prefix = 'm'

for input_value in test_list_value:
    for reference_number in test_list_reference_number:
        output_value = MFRT.ConvertFloatToString(input_value, reference_number, resolution=resolution,
                                                 delimiter=delimiter, prefix=prefix)
        RFSE.Report('ConvertingRefNumberResDelPrefix', 'set', 'table', f'{input_value};'
                                                                       f'{reference_number};'
                                                                       f'{resolution};'
                                                                       f'{prefix};'
                                                                       f'{delimiter};'
                                                                       f'{output_value};')


test_list_reference_number = ["100.00000u", "100.0000u", "100.000u", "100.00u", "100.0u", "100u",
                              "100.00000m", "100.0000m", "100.000m", "100.00m", "100.0m", "100m",
                              "100.00000", "100.0000", "100.000", "100.00", "100.0", "100",
                              "100.00000k", "100.0000k", "100.000k", "100.00k", "100.0k", "100k",
                              "100.00000M", "100.0000M", "100.000M", "100.00M", "100.0M", "100M"]

test_list_value = ["100m", "100", "100k"]

resolution = 2

prefix = 'm'

delimiter = ','

for input_value in test_list_value:
    for reference_number in test_list_reference_number:
        output_value = MFRT.ConvertFloatToString(input_value, reference_number, resolution=resolution,
                                                 delimiter=delimiter, prefix=prefix)
        RFSE.Report('ConvertingRefNumberResDelPrefix', 'set', 'table', f'{input_value};'
                                                                       f'{reference_number};'
                                                                       f'{resolution};'
                                                                       f'{prefix};'
                                                                       f'{delimiter};'
                                                                       f'{output_value};')

RFSE.Messenger("set", "Message#@notes",
               "Start translated value into:\n"
               "Value: int\n"
               "Reference number: None\n"
               "Resolution: int\n"
               "Prefix: str\n"
               "Delimiter: str")

RFSE.Report('ConvertingValueResDelPrefix', 'info', 'table', 'Input value#130;'
                                                            'Reference number#130;'
                                                            'Resolution#75;'
                                                            'Prefix#50;'
                                                            'Delimiter#75;'
                                                            'Output value#130;')

test_list_input_value = ["100.00000u", "100.0000u", "100.000u", "100.00u", "100.0u", "100u",
                         "100.00000m", "100.0000m", "100.000m", "100.00m", "100.0m", "100m",
                         "100.00000", "100.0000", "100.000", "100.00", "100.0", "100",
                         "100.00000k", "100.0000k", "100.000k", "100.00k", "100.0k", "100k",
                         "100.00000M", "100.0000M", "100.000M", "100.00M", "100.0M", "100M"]

resolution = 2

prefix = 'm'

delimiter = ','

reference_number = '-'

for input_value in test_list_input_value:
    output_value = MFRT.ConvertFloatToString(input_value, resolution=resolution, delimiter=delimiter, prefix=prefix)
    RFSE.Report('ConvertingValueResDelPrefix', 'set', 'table', f'{input_value};'
                                                               f'{reference_number};'
                                                               f'{resolution};'
                                                               f'{prefix};'
                                                               f'{delimiter};'
                                                               f'{output_value};')

test_list_input_value = ["100.00000u", "100.0000u", "100.000u", "100.00u", "100.0u", "100u",
                         "100.00000m", "100.0000m", "100.000m", "100.00m", "100.0m", "100m",
                         "100.00000", "100.0000", "100.000", "100.00", "100.0", "100",
                         "100.00000k", "100.0000k", "100.000k", "100.00k", "100.0k", "100k",
                         "100.00000M", "100.0000M", "100.000M", "100.00M", "100.0M", "100M"]

resolution = 10

prefix = 'k'

delimiter = ','

reference_number = '-'

for input_value in test_list_input_value:
    output_value = MFRT.ConvertFloatToString(input_value, resolution=resolution, delimiter=delimiter, prefix=prefix)
    RFSE.Report('ConvertingValueResDelPrefix', 'set', 'table', f'{input_value};'
                                                               f'{reference_number};'
                                                               f'{resolution};'
                                                               f'{prefix};'
                                                               f'{delimiter};'
                                                               f'{output_value};')
RFSE.Program('control', 'set', 'save word report')

RFSE.EndScript()
