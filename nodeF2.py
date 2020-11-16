from socket import *

#defines port number
serverPort = 20000 #F2

#Creates socket 'serverSocket'
serverSocket = socket(AF_INET, SOCK_DGRAM)

#binds program (socket) to server port (11000)
serverSocket.bind(('', serverPort))

#variable to determin which node is mining
turn = 2

#prints message
print ('The server is ready to receive')

#infinate loop to recieve message from client
while 1:
    #uses socket to recieve message from client and stores it in 'message'
    #clientAdress is to know who sent you a request and lets you reply
    message, clientAddress = serverSocket.recvfrom(2048)

    #capatalizes all letters in string AFTER decoding
    modifiedMessage = message.decode().upper()

    #Sends modified message through socket to the client (clientAddress)
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
