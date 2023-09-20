import tkinter as tk
import imp
#import numpy
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


def run_scan(port_entry, target_entry):
    target = target_entry.get()
    portscan = [int(port.get()) for port in ports]

    if len(portscan) == 0:
        fullscan(target)
    else:
        partialscan(target, portscan)


root = tk.Tk()
root.title("PORT SCANNER")


banner_label = tk.Label(root, text="PORT SCANNER")
banner_label.pack(pady=10)

target_frame = tk.Frame(root)
target_frame.pack()

target_label = tk.Label(target_frame, text="Target IP:")
target_label.pack(side="left", padx=10)

target_entry = tk.Entry(target_frame)
target_entry.pack(side="left", padx=10)

ports = []
ports_frame = tk.Frame(root)
ports_frame.pack()

port_label = tk.Label(ports_frame, text="Enter ports to be scanned:")
port_label.pack(side="left", padx=10)

port_entry = tk.Entry(ports_frame)
port_entry.pack(side="left", padx=10)


def enter_nmap():
    run_scan(port_entry, target_entry)

button = tk.Button(root, text="Enter data", command=enter_nmap)
button.pack(pady=10)


root.mainloop()
