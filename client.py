# A simple TCP client
# Written by Ben Delp
#
###___________________ ________   
###\______   \_   ___ \\______ \  
### |   |  _/    \  \/ |    |  \ 
### |   |   \     \____|    |   \
###/______  /\______  /_______  /
###       \/        \/        \/ 
# Written on 1674827360

# For now, this will serve as a learning excercise. It may serve as a building block for future projects, it may sit and collect dust.

# Inspiration: Black Hat Python by Justin Seitz & Tim Arnold;  Sentdex's Youtube playlist: Sockets tutorial with Python 3
# 
#Libraries, we need 'em:
import socket
import threading

# define local socket
# Configure for IPv4 TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Configure address and port
s.connect(("127.0.0.1", 1337))

# Create an rx buffer
Full_msg = ''

# Create a loop to add recieved data to the rx buffer
while True:
    msg = s.recv(8)
    if len(msg) <=0 :
        break
    Full_msg += msg.decode("utf-8")

# Print the received message
print(Full_msg)


