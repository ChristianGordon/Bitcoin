from socket import *

#defines port number
serverPort = 10000 #F1

#Creates socket 'serverSocket'
serverSocket = socket(AF_INET, SOCK_DGRAM)

#binds program (socket) to server port (10000)
serverSocket.bind(('', serverPort))

#variable to determin which node is mining
turn = 1

#prints message
print ('The server is ready to receive')

#infinate loop to recieve message from client
while 1:
    #uses socket to recieve message from client and stores it in 'payer, payee and amt'
    #clientAdress is to know who sent you a request and lets you reply
    payer, clientAddress = serverSocket.recvfrom(2048)
    payee, clientAddress = serverSocket.recvfrom(2048)
    amt, clientAddress = serverSocket.recvfrom(2048)



    #if message is Transaction (Tx) (from client) run TTT instructions


    #else if the message is Tx or block (from the other full node),
    #   a) send block to blockchain.txt file
    #   b) remove the 4 Tx of the block from Temp_T.txt
    #   c) check the 4 Tx of the block and send the Tx where its client is a payer or payee to the client.

    #decoding
    modifiedMessage = payer.decode()
    modifiedMessage2 = payee.decode()
    modifiedMessage3 = amt.decode()

    #Sends modified message through socket to the client (clientAddress)
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    serverSocket.sendto(modifiedMessage2.encode(), clientAddress)
    serverSocket.sendto(modifiedMessage3.encode(), clientAddress)

