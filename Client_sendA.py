#To send Tx to the full node.
from socket import *

#Runs client and server program on same machine
serverName = 'localhost'

#Defines port number for server
serverPort = 10000

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

f = open('Temp_T.txt', 'r')
file_contents = f.read()
contents = file_contents.splitlines()  # splits the contents into list by new line
file_contents = contents[0].split(':')  # splits first item in list into multiple by ':'
file_contents = file_contents + contents[1].split(':')  # splits secont itm in list into multiple by ':'

if payer == 1:   #from first account
    temp = int(file_contents[1], 16)    #converts unconfirmed fro first account to int
    temp = temp - amt                   #subtracts amount they are sending
    temp = hex(temp)                    #converts back into hex
    file_contents[1] = temp

elif payer == 2:  #from second account
    temp = int(file_contents[4], 16)    #converts unconfirmed from second account to int
    temp = temp - amt                   #subtracts amount they are sending
    temp = hex(temp)                    #converts back into hex

f.write(file_contents)
f.close()


#prints modified message AFTER decoding
print (modifiedMessage.decode())
print (modifiedMessage2.decode())
print (modifiedMessage3.decode())

#closes socket
clientSocket.close()

def newTran():
    amount = input("How much would you like to send?\n")
    sendTo = input("Which account would you like to send it TO?\n")
    sentFrom = input("Select the Payer:\n1. ", )
    print(amount)
    print(sendTo)
    print(sentFrom)

def viewBalance():
    f = open('Confirmed_T.txt', 'r')                        #opens file
    file_contents = f.read()                                #inserts file contents into variable
    contents = file_contents.splitlines()                   #splits the contents into list by new line
    file_contents = contents[0].split(':')                  #splits first item in list into multiple by ':'
    file_contents = file_contents + contents[1].split(':')  #splits secont itm in list into multiple by ':'

    A1 = file_contents[0]               #Grabs first item in list (account number)
    A2 = file_contents[3]               #Grabs third item in list (account number)
    A1 = A1[0] + A1[-1]                 #finds first and last elements in str
    A2 = A2[0] + A2[-1]                 #finds first and last elements in str

    #converts account balances to int
    file_contents[1] = int(file_contents[1], 16)
    file_contents[2] = int(file_contents[2], 16)
    file_contents[4] = int(file_contents[4], 16)
    file_contents[5] = int(file_contents[5], 16)

    print('Account:', A1, '\nUnconfirmed Balance: {1}\nConfirmed Balance: {2}\n\n'.format(*file_contents),'Account:', A2, '\nUnconfirmed Balance: {4}\nConfirmed Balance: {5}'.format(*file_contents))
    f.close()


def get_menu_choice():
    def print_menu():
        print(30 * "-", " Choices ", 30 * "-")
        print("1. Enter a new transaction.")
        print("2. View current balance for each account.")
        print("3. Print unconfirmed transactions.")
        print("4. Print the last X number of confirmed transactions (Either as Payee or Payer).")
        #Get the blockchain from the full node and print it in a structured
        #format block by block. Separate the fields of each block as well: 10 points Extra credit
        print("5. Print the blockchain.")
        print("6. Exit")
        print(73 * '-')

    loop = True
    int_choice = -1

    while loop:
        print_menu()
        choice = input("Enter your choice (1 - 6): ")

        if choice == '1':
            #create a new transaction
            int_choice = 1
            newTran()
        elif choice == '2':
            #Shows the balances of each account
            int_choice = 2
            viewBalance()
        elif choice == '3':
            #Shows unconfirmed transactions
            int_choice = 3
            print("Sup")
        elif choice == '4':
            #Shows the last few numbers of confirmed transactions
            int_choice = 4
            print("")
        elif choice == '5':
            #Extra Credit
            #Prints the blockchain
            int_choice = 5
            print("")
        elif choice == '6':
            #ends the loop
            int_choice = -1
            print("Exiting..")
            loop = False
        else:
            #If there is an input other than accepted paramaters this will show
            int_choice = -1
            input("Wrong menu selection. Enter any key to try again..\n")
    return [int_choice, choice]

    return(get_menu_choice())

print(get_menu_choice())

