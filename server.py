# simple python TCP server
# Written by Ben Delp
# ___________________ ________   
# \______   \_   ___ \\______ \  
#  |   |  _/    \  \/ |    |  \ 
#  |   |   \     \____|    |   \
# /______  /\______  /_______  /
#        \/        \/        \/
# Written on: 1674826102

# For now, this will serve as a learning excercise. It may prove of use in the future though as well.
# Inspiration: Black Hat Python by Justin Seitz & Tim Arnold; Sentdex's Youtube playlist: Sockets tutorial with Python 3
# Libraries, we need 'em: 
import socket
import threading

# Define the local socket
# Configure for IPv4 TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Configure address and port
s.bind(("127.0.0.1", 1337))
# PUT SOMETHING HERE 
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f'Connection from {address} has been established!')
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    clientsocket.close()
