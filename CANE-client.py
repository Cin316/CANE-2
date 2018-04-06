from bluetooth import *
import sys
import random
from src.newUltrasonic import *
from src.dummySound import *

#host_address = "B8:27:EB:6E:D4:DF"
host_address = "B8:27:EB:D4:16:2E"
port = 1

sideOpt = DistanceOptions()
sideOpt.minDistance = 0.02
sideOpt.maxDistance = 1.0
sideOpt.inverseConstant = 0.7
frontOpt = DistanceOptions()
frontOpt.minDistance = 0.10
frontOpt.maxDistance = 3.5
frontOpt.inverseConstant = 1
frontOpt.frontSensor = True

sound = DummySoundThread(2)

thread = UltrasonicThread([24,             24            ],
                          [12,             5             ],
                          [sideOpt,        frontOpt      ],
                          [sound,         sound         ])

def main():
    global sock

    thread.start()
    
    # Create the client socket
    sock = BluetoothSocket( RFCOMM )
    sock.connect((host_address, port))
    
    print("Connected")
    while True:
        processCommand(sock.recv(1024))
    sock.close()

def processCommand(command):
    global sock
    print("received command: " + str(command))
    if command == "getDropOff":
        sock.send(getDropOffStatus())
    elif command == "getSideUltrasonic":
        sock.send(getSideUltrasonicStatus())
    elif command == "getFrontUltrasonic":
        sock.send(getFrontUltrasonicStatus())
    return;

def getDropOffStatus():
    return "NO" 

def getSideUltrasonicStatus():
    return str(sound.frequencies[0])

def getFrontUltrasonicStatus():
    return str(sound.frequencies[1])



main()

