#import socket module
from http import server
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverSocket.bind(("127.0.0.1", 8080))
serverSocket.listen()
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1] 
        f = open(filename[1:]) 
        outputdata = ["HTTP/1.1 200 OK", "Content-Type: text/html", "", f.read()]
        #Send one HTTP header line into socket
        #Fill in start
        #Fill in end 
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError as e:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not found\r\n\r\n".encode())
        #Close client socket
        connectionSocket.close()
        print(e)
        serverSocket.close()
        sys.exit()#Terminate the program after sending the corresponding data 