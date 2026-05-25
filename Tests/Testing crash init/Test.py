import time

from BK1697B import BK1697B
import RFSE

testing_devices = BK1697B()

testing_devices.Initialization()

testing_devices.SET_OUTPUT_ON()
num_testing = 1

while True:
    value = 5 if num_testing % 2 == 1 else 10
    RFSE.Stage(f'Number iteration: {num_testing}')
    testing_devices.SET_VALUE(value=value)
    RFSE.Stage(" ")
    if num_testing % 10 == 0:
        choices = testing_devices.CHOICES()
        RFSE.Stage(' ')
        if not choices:
            break
    num_testing += 1
    time.sleep(2)

testing_devices.SET_OUTPUT_OFF()
RFSE.EndScript()
