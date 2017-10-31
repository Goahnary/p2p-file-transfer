# CLIENT

import socket
import time

host = str(input("Connect to: "))
port = 9988

data_c = input("Message: ")
c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

c.sendto(bytes(data_c, 'utf-8'),(host,port))

print( c.recv(1024).decode('utf-8'))
