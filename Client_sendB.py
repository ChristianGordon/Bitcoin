#To send Tx to the full node.
from socket import *

#Runs client and server program on same machine
serverName = 'localhost'

#Defines port number for server
serverPort = 20000

#creates socket 'clientSocket'
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Asks user to enter sentance and stores it in 'message'

payer = input('Select the Payer:\n1. A0000001\n2. A0000002\nChoice: ')
payee = input('Select the Payee:\n1. B0000001\n2. B0000002\nChoice: ')
amt = input('Enter the amount of payment in decimal:\n')

#sends socket AFTER encoding to the destination 'serverName & server port'
clientSocket.sendto(payer.encode(),(serverName, serverPort))
clientSocket.sendto(payee.encode(),(serverName, serverPort))
clientSocket.sendto(amt.encode(),(serverName, serverPort))


#recieves message through socket from server (2048 is size buffer)
#modified message is stored in 'modifiedMessage'
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
modifiedMessage2, serverAddress = clientSocket.recvfrom(2048)
modifiedMessage3, serverAddress = clientSocket.recvfrom(2048)

print(serverAddress)

#prints modified message AFTER decoding
print (modifiedMessage.decode())
print (modifiedMessage2.decode())
print (modifiedMessage3.decode())

#closes socket
clientSocket.close()
