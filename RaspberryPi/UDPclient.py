import socket
import time
from RCcontroler import rc_controller 
#auticko
msgFromClient       = "Rc is ready" 
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("192.168.1.151", 20001)
bufferSize          = 1024
rc_controller = rc_controller()


# Create a UDP socket at client side
socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
socket.sendto(bytesToSend, serverAddressPort)

while True:
    msgFromServer = socket.recvfrom(bufferSize)

    msg = "Message from Server {}".format(msgFromServer[0])
    print(msg)
    #message = msgFromServer[0].split(",") #rozdelenie spravy zo serveru
    #speed = int(message[0]) #zobere to z prvy prvok z pola message a prenesie to do druhej premmenej ako cislo 
    #direction = int(message[1]) ##zobere to z druhy prvok z pola message a prenesie to do prvej premmenej ako cislo
    #rc_controller.set_values(speed,direction)
    '''set_speed(speed)
    change_direction(direction)
    '''