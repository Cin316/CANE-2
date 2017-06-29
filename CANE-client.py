from bluetooth import *
import sys
import random

host_address = "B8:27:EB:6E:D4:DF"
port = 1

def main():
    global sock
    # Create the client socket
    sock = BluetoothSocket( RFCOMM )
    sock.connect((host_address, port))
    
    while True:
        processCommand(sock.recv(1024))
    sock.close()

def processCommand(command):
    global sock
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
    return "0.0"

def getFrontUltrasonicStatus():
    return "0.0"



main()

