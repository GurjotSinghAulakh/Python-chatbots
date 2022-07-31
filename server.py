# TCP Server

# Libraries
import argparse
import socket
import threading
import time
import sys

# Initialize parser : This is a parser that verifies if all the required parameters are given
parser = argparse.ArgumentParser(description="Start the chat server and wait for connections to come in. "
                                             "server.py 4242 is an example.")

# Adding argument
parser.add_argument("port", type=int, help="The port on which the server is executing. The input must be in "
                                           "a certain format, such as 1234.")

# Read arguments from command line
args = parser.parse_args()

port = args.port

# Here we start the Server by binding the host and port, then it listens
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# This code is used to allow you to utilize the same port several times (REUSE ADDRESS).
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# The needed data for connection
serverSocket.bind(("localhost", port))

# Listen for connections
serverSocket.listen()

# To get the host IP
host = socket.gethostbyname(socket.gethostname())

# The Server prints out this when it has connected successfully
print("Chat server started...\nPort: " + str(port) + "\nHost: " + str(host))

# Creates an empty list for client name
clientList = []

# Creates an empty list for the socket instance
nameList = []


# A client's message is broadcast to all others clients
def broadcastMessageHost(message, client):
    for newHost in clientList:

        # Avoids sending message back to original client
        if newHost is not client:
            time.sleep(0.5)
            newHost.send(message)


# A feature that allows clients to speak with one another (host and bots)
# Handles chatting inbetween the clients(host and bots)
def handleClient(client):
    while True:
        try:

            # Receives message from the client
            message = client.recv(1024)
            msg = message.decode("utf-8")

            # Splits the message after colon
            messageSplit = msg.split(": ")

            # If messageSplit's first index equals "quit," all clients will be disconnected, and the connection
            # will be closed. After the server states, the entire system is shut off. Otherwise, in else-clause,
            # the broadcasting messages sends to all except itself
            if messageSplit[1] == "quit":
                time.sleep(1)
                print("Disconnecting clients...")
                for i in clientList:
                    i.close()
                print("Server status: Down\nStopped listening to connections...")
                sys.exit()

            else:

                # Broadcasting Messages
                broadcastMessageHost(message, client)

        except:
            # Removing And Closing Clients

            # The index is obtained from the client connection
            index = clientList.index(client)

            # Revomes the client from the list (array)
            clientList.remove(client)

            # Closes the Socket Connection
            client.close()

            # The index is found by using nameList.
            name = nameList[index]

            broadcastMessageHost(f'{name} has disconnected from the chat room!'.encode("utf-8"), None)
            print(f'{name} disconnected from the chat room')
            nameList.remove(name)
            break


# Chatroom : connect arriving clients to the server and set the server's status
def receive():
    print('\nServer status: Running\nListening to connections...\n')
    while True:

        # Accepting Connection
        client, address = serverSocket.accept()

        # Request and store REQUESTNAME
        client.send('REQUESTNAME'.encode('utf-8'))
        name = client.recv(1024).decode('utf-8')
        nameList.append(name)
        clientList.append(client)

        # Print and broadcast name
        print(f"Successfully established a connection with {name} {str(address)}")
        broadcastMessageHost(f"{name} has connected to the chat room".encode("utf-8"), client)

        # Start handling thread for client
        thread = threading.Thread(target=handleClient, args=(client,))
        thread.start()


receive()
