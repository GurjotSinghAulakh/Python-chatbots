# Python-chatbots

*Individual portfolio assignment in the course "DATA2410 - Networking and cloud computing" at Oslo Metropolitan University.* <br />
*Created a Python chat room with bots and a host that can talk to each other through a TCP socket.* <br />

- - - 
## How to run:
1. Begin by typing server.py in a terminal window and passing the port as an argument.
2. The server will then enter listen-mode, waiting for connections and informing us when someone connects.
3. Create at least one bot terminal, or as many as you like. Keep in mind that there are only four bots available: alex, smartbot, familybot & nicky.
4. A terminal for the host-client, commonly known as the user, must also be opened. Although several hosts are permitted, just one is advised for optimal performance.
5. In the new terminals, run client.py with three arguments: IP address, port, and name. Whether you're a bot or a host is determined by your name.
6. The chatroom should now be up and running. The user may type whatever they like, and the bot(s) will answer appropriately.
7. For a collection of verbs, the bots will respond differently.
8. Close the terminal windows to disconnect. The host can also type "exit" to terminate the server and disconnect all clients. When a client disconnects, the server will tell the other clients.
- - - 

  - **server.py: Hosts the chat room.**
    - Requires port number as argument:
      ```console
      for eks. python3 server.py 1234
      ```
    - Type **server.py -h** for more info:
      ```console
      usage: server.py [-h] port

      Start the chat server and wait for connections to come in. server.py 1234 is an example. 

      positional arguments:
      port        The port on which the server is executing. The input must be in a certain format, such as 1234. 

      optional arguments:
      -h, --help  show this help message and exit

      ```
  - **client.py: Bots and host**
    - Requires IP address/hostname, port number and client name as arguments. The client name can be anything, but will become a bot if a bot name is given. 
      ```console
      python3 client.py localhost 1234 Gurjot 
      ```
    - Type **client.py -h** for more info:
      ```console
      usage: client.py [-h] IP port name

      Connect to the chat room, by typing 'client.py' 'localhost' 'port' 'bot/host'

      positional arguments:
      IP          IP address of the server to which the client is connected.
      port        The port to which the client is connected.
      name        Connect as a client or a bot. Bot's that are available are: 'alex, smartBot, familyBot, nicky'

      optional arguments:
      -h, --help  show this help message and exit
      ```
