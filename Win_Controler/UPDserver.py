import socket
import keyboard
#pocitac
#msgFromServer       = "Hello UDP Client" správa ktorá sa pošle naspat ako odpoved
#bytesToSend         = str.encode(msgFromServer) správu zakoduje
serverAddressPort   = ("192.168.1.151", 20001) #IP adresa pocitaca
bufferSize  = 1024

# Create a datagram socket
Jakubko = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
Jakubko.bind(serverAddressPort)

print("Server is started") #text zistenie či program funguje

bytesAddressPair = Jakubko.recvfrom(bufferSize)
message = bytesAddressPair[0]
address = bytesAddressPair[1]
clientMsg = "Message from Client:{}".format(message)
clientIP  = "Client IP Address:{}".format(address)
    
print(clientMsg)
print(clientIP)

# Listen for incoming datagrams
while(True):
    cislo = 0
    cislo2 = 0

    if keyboard.is_pressed("w") and not keyboard.is_pressed("s"):
        cislo = 255

    if keyboard.is_pressed("s") and not keyboard.is_pressed("w"):
        cislo = -255
    
    if keyboard.is_pressed("w") and keyboard.is_pressed("s"):
        cislo = 0

    if not keyboard.is_pressed("w") and not keyboard.is_pressed("s"):
        cislo = 0

    if keyboard.is_pressed("a") and not keyboard.is_pressed("d"):
        cislo2 = 255

    if keyboard.is_pressed("d") and not keyboard.is_pressed("a"):
        cislo2 = -255
    
    if keyboard.is_pressed("a") and keyboard.is_pressed("d"):
        cislo2 = 0
    
    if not keyboard.is_pressed("a") and not keyboard.is_pressed("d"):
        cislo2 = 0

    packet = str(cislo) + "," + str(cislo2)

    # Sending a reply to client
    Jakubko.sendto(str.encode(packet), address)