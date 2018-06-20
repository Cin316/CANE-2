import time
import commands

def headphonesConnected():
    address = "AA:00:A7:00:D8:54"
    command = 'echo "info ' + address + '" | bluetoothctl'
    output = "Connected: yes" in commands.getstatusoutput(command)[1]
    return output

while not headphonesConnected():
    time.sleep(5)

time.sleep(10)

