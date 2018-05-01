from bluetooth import *
from threading import Thread
import time
from newUltrasonic import *

#client_address = "B8:27:EB:D4:16:2E"
client_address = "B8:27:EB:6E:D4:DF"

class CANEServer (Thread):
    # A server thead to handle communication with the client Pi
    # and send its information to other parts of the CANE program.

    # server_sock: a socket for listening to clients on
    # client_sock: a socket that points to the currently connected client
    # client_info: an array containing info about the current client
    # sideLeftServerComm: the ServerComm object where the side left ultrasonic sensor data should go
    # frontLeftServerComm: the ServerComm object where the front left ultrasonic sensor data should go
    # dummyLaser: a dummy object to hold the status of the client's laser sensor.

    def __init__(self, sideLeftSC, frontLeftSC, dummyLsr):
        Thread.__init__(self)

        self.sideLeftServerComm = sideLeftSC
        self.frontLeftServerComm = frontLeftSC

        self.dummyLaser = dummyLsr
        
        self.server_sock = BluetoothSocket( RFCOMM )
        self.server_sock.bind(("",PORT_ANY))
        self.server_sock.listen(1)

    def run(self):
        self.listenForClient()
        connection_address = self.client_info[0]

        while connection_address == client_address: # TODO Improve client address checking.
            print("pinging the client...")
            
            sideData = self.sideUltrasonicCommand()
            print("sideData: " + str(sideData))
            self.sideLeftServerComm.blipsFrequency = float(sideData)
            
            frontData = self.frontUltrasonicCommand()
            print("frontData: " + str(frontData))
            self.frontLeftServerComm.blipsFrequency = float(frontData)
            
            dropOffData = self.dropOffCommand()
            print("dropOffData: " + str(dropOffData))
            self.dummyLaser.value = self.convertBool(dropOffData)
            
            time.sleep(0.1)
        
        print("server terminated!")
    
    def listenForClient(self):
        port = self.server_sock.getsockname()[1]
        print("Waiting for connection on RFCOMM channel " + str(port))

        self.client_sock, self.client_info = self.server_sock.accept() # This blocks until a connection is received.
        print("Accepted connection from " + str(self.client_info))
    
    # Each of the client commands to send below blocks while it waits for a response.
    def dropOffCommand(self):
        self.client_sock.send("getDropOff")
        data = self.client_sock.recv(1024)
        return data
    
    def sideUltrasonicCommand(self):
        self.client_sock.send("getSideUltrasonic")
        data = self.client_sock.recv(1024)
        return data
    
    def frontUltrasonicCommand(self):
        self.client_sock.send("getFrontUltrasonic")
        data = self.client_sock.recv(1024)
        return data
    
    # Converts a YES or NO string into a boolean
    def convertBool(self, string):
        if string=="YES":
            return True
        else:
            return False



