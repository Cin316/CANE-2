from bluetooth import *

#client_address = "B8:27:EB:D4:16:2E"
client_address = "B8:27:EB:6E:D4:DF"

def main():
    global server_sock
    global client_sock
    server_sock = BluetoothSocket( RFCOMM )
    server_sock.bind(("",PORT_ANY))
    server_sock.listen(1)
    
    port = server_sock.getsockname()[1]
    
    print "Waiting for connection on RFCOMM channel %d" % port
    
    client_sock, client_info = server_sock.accept()
    print "Accepted connection from ", client_info
    print "client_address:" + str(client_address)
    
    connection_address = client_info[0]
    print "connection_address:" + str(connection_address)
    if connection_address == client_address:
        try:
            while True:
                data = raw_input()
                client_sock.send(data)
                dropOffCommand()
                sideUltrasonicCommand()
                frontUltrasonicCommand()
        except IOError:
            pass
    
    print "disconnected"
    
    client_sock.close()
    server_sock.close()
    print "all done"

def dropOffCommand():
    global client_sock
    client_sock.send("getDropOff")
    data = client_sock.recv(1024)
    print data
    return;

def sideUltrasonicCommand():
    global client_sock
    client_sock.send("getSideUltrasonic")
    data = client_sock.recv(1024)
    print data
    return;

def frontUltrasonicCommand():
    global client_sock
    client_sock.send("getFrontUltrasonic")
    data = client_sock.recv(1024)
    print data
    return;


main()

