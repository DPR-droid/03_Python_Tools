# Python port scanner
# https://www.youtube.com/watch?v=XGFDXGyd7Uw

import imp
from numpy import append
import pyfiglet
import sys
import socket
from datetime import datetime


def fullscan(target):
    try:
        for port  in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)

            print(str(port))
            result = s.connect_ex((target,port))
            if result == 0:
                print("[*] Port {} is open".format(port))
            s.close
    except KeyboardInterrupt:
        print("Existing")
        sys.exit()
""" 
    except socket.error:
        print("Host not responding")
        sys.exit() """


def partialscan(target, portscan):
    try:
        for port  in portscan:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)

            print(str(port))
            result = s.connect_ex((target,port))
            if result == 0:
                print("[*] Port {} is open".format(port))
            s.close
    except KeyboardInterrupt:
        print("Existing")
        sys.exit()

"""     except socket.error:
        print("Host not responding")
        sys.exit() """

ascii_banner = pyfiglet.figlet_format('PORT SCANNER')
print(ascii_banner)
target = input(str("Target IP: "))

# Port scan
portscan = []
i=0

while 1:
    i+=1
    try:
        portscan.append(int(input("Enter ports to be scanned: " )))
    except:
        break
print(portscan)

if len(portscan) == 0:
    fullscan(target)
else:
    partialscan(target, portscan)
    

print("_" * 50)
print("Scanning Target: " + target)
print("Scanning Target: " + str(portscan))
print("Scanning started at: " + str(datetime.now()))
print("_" * 50)
