# TCP client

# Libraries
import argparse
import socket
import random
import threading
import sys
import time

# Initialize parser : This is a parser that verifies if all the required parameters are given
parser = argparse.ArgumentParser(description="Connect to the chat room, by typing 'client.py' 'localhost' 'port' "
                                             "'bot/host'")

# Adding arguments
parser.add_argument("IP", type=str, help="The IP address of the server to which the client is connected.")
parser.add_argument("port", type=int, help="The port to which the client is connected.")
parser.add_argument("name", type=str, help="Connect as a client or a bot. Bot's that are available are: '"
                                           "alex, smartBot, familyBot, nicky'")

# Read arguments from command line
args = parser.parse_args()

IP = args.IP
port = args.port
name = args.name

# Creating a socket
# socket.AF_INET - address family, IPv4, some other possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
# socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams,
# socket.SOCK_RAW - raw IP packets
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establishes a connection between the bot and the server
clientSocket.connect((IP, port))

# A welcome message
print(f"Hello {name}! You have now established a connection!!!")

# An array with the names of all bot's
botNames = ["alex", "smartbot", "familybot", "nicky"]

# A collection of both good and bad actions
good_actions = ["read", "learn", "play", "travel", "fly", "love", "enjoy", "jump"]
bad_actions = ["smack", "hack", "steal", "crash", "slap", "steal", "cry", "chase"]

# The alex function : chatbot takes the verb from the verbChecker function and examines the list of
# good and negative actions. It depends on whether the verb is defined in the good or negative action
# list of the code. If it discovers a verb that suits, it should generate a random string format from
# the phrases below. A plain text will be returned if this is not the case.

def alex(message):
    if message in good_actions:
        return random.choice([
            "{}: I think {} sounds great!".format(name, message + "ing"),
            "{}: Did you say {}? That'd be amazing!".format(name, message + "ing")
        ])

    elif message in bad_actions:
        return random.choice([
            "{}: I’II double check and let you know.".format(name, message + "ing"),
            "{}: Sorry, but that's just boring..".format(name, message + "ing"),
            "{}: I've got better things to do than {}..".format(name, message + "ing")
        ])

    else:
        return "{}: You must be out of your mind!".format(name)


# The smartbot function : chatbot takes the verb from the verbChecker function and examines the list of
# good and negative actions. It depends on whether the verb is defined in the good or negative action
# list of the code. If it discovers a verb that suits, it should generate a random string format from
# the phrases below. A plain text will be returned if this is not the case.

def smartbot(message):
    if message in good_actions:
        return random.choice([
            "{}: Somebody suggested {}? Sure, I'm up for anything!".format(name, message + "ing"),
            "{}: Awesome! I've been longing for some {} all week!".format(name, message + "ing")
        ])

    elif message in bad_actions:
        return random.choice([
            "{}: Are you serious? {} is the last thing we need".format(name, message + "ing"),
            "{}: Again with the {}!".format(name, message + "ing")
        ])

    else:
        return "{}: Good idea, let's do it!".format(name)


# The familybot function : chatbot takes the verb from the verbChecker function and examines the list of
# # good and negative actions. It depends on whether the verb is defined in the good or negative action
# # list of the code. If it discovers a verb that suits, it should generate a random string format from
# # the phrases below. A plain text will be returned if this is not the case.

def familybot(message):
    if message in good_actions:
        return random.choice([
            "{}: I mean.. I guess {} isn't that bad.".format(name, message + "ing"),
            "{}: Finally we can start {}!".format(name, message + "ing"),
        ])

    elif message in bad_actions:
        return random.choice([
            "{}: {} seems negative. And I wanted more choices!That's it then?".format(name, message + "ing"),
            "{}: Oh, {}, excellent idea. Could also nag maybe?".format(name, message + "ing"),
            "{}: {} sounds really boring..".format(name, message + "ing")
        ])

    else:
        return "{}: I don't want to do that.".format(name)


# The smartbot function : chatbot takes the verb from the verbChecker function and examines the list of
# # good and negative actions. It depends on whether the verb is defined in the good or negative action
# # list of the code. If it discovers a verb that suits, it should generate a random string format from
# # the phrases below. A plain text will be returned if this is not the case.

def nicky(message):
    if message in good_actions:
        return random.choice([
            "{}: Meh. I did some {} last night. I'll complain maybe.".format(name, message + "ing"),
            "{}: {}?? Sure, why not?".format(name, message + "ing")
        ])

    elif message in bad_actions:
        return random.choice([
            "{}: {}...? You can't be serious..".format(name, message + "ing"),
            "{}: {}?? Sure, why not?".format(name, message + "ing")
        ])

    else:
        return "{}: That’s exactly what I’m seeking to answer.".format(name)


# The verbChecker function : receives the host's message and selects the appropriate verb from the phrase.
# Then it looks over the list of positive and poor actions. It is determined by whether the verb is defined
# in the code's good or bad action list. Based on which bot talks to the host, the verb will be passed to
# the bots' functionality, which will choose a random sentence to send to the host.

def verbChecker(message):
    # An empty string
    verb = ""

    # Checks if the verb is in the list of good actions.
    for good_words in range(len(good_actions)):
        if good_actions[good_words] in message.lower():
            verb = good_actions[good_words]

    # Checks if the verb is in the list of bad actions.
    for bad_words in range(len(bad_actions)):
        if bad_actions[bad_words] in message.lower():
            verb = bad_actions[bad_words]

    # Creates a new variable which is empty at the start
    botMessage = ""

    # Checks if the bots name is in lower letters, and sends the verb in the function as a parameter
    if name.lower() == "alex":
        botMessage = alex(verb)

    elif name.lower() == "smartbot":
        botMessage = smartbot(verb)

    elif name.lower() == "familybot":
        botMessage = familybot(verb)

    elif name.lower() == "nicky":
        botMessage = nicky(verb)

    return botMessage


# A function that takes care of the messages that come in from server
def messageMangaer():
    # The while loop verifies the message and runs indefinitely
    while True:

        # Receives message from the server
        message = clientSocket.recv(1024).decode("utf-8")

        # Checks if  is equal to "name", thats we gets from the server side.
        # Then its returns name after it encodes to bytes.
        if message == "REQUESTNAME":
            clientSocket.send(name.encode("utf-8"))

        else:

            # If there is a colon in the message
            if ":" in message:

                # Splits the message after colon
                messageSplit = message.split(": ")

                # Checks if it is a person or a bot who sends the message, if bots sends message go to else-clause
                # otherwise, it is a host who send message then it will go to if-clause
                if messageSplit[0].lower() not in botNames:

                    # The sentence that the bot function chose for the host
                    botMessage = verbChecker(message)

                    print(botMessage)
                    clientSocket.send(botMessage.encode("utf-8"))

                else:
                    print(message)

            else:
                print(message)


# A function which is in-charge of the host's ability to write.
def clientTransmitter():
    while True:
        try:
            time.sleep(3)
            message = f'{name}: {input()}'

            print(message)
            clientSocket.send(message.encode('utf-8'))
        except:
            print("You've logged out of the chat room.")
            sys.exit()


# The messageMangaer - and clientTransmitter functions are both started utilizing two threads.
receive_thread = threading.Thread(target=messageMangaer)
receive_thread.start()

# Only host is allowed to write the message
if name not in botNames:
    send_thread = threading.Thread(target=clientTransmitter)
    send_thread.start()
