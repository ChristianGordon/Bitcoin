from socket import *

#Runs client and server program on same machine
serverName = 'localhost'     

#Defines port number for server
serverPort = 12000       

#creates socket 'clientSocket'
clientSocket = socket(AF_INET, SOCK_DGRAM)  

# Asks user to enter sentance and stores it in 'message'
message = input('Input lowercase sentence:')   

#sends socket AFTER encoding to the destination 'serverName & server port'
clientSocket.sendto(message.encode(),(serverName, serverPort)) 

#recieves message through socket from server (2048 is size buffer)
#modified message is stored in 'modifiedMessage'
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

#prints modified message AFTER decoding
print (modifiedMessage.decode())

#closes socket
clientSocket.close()
