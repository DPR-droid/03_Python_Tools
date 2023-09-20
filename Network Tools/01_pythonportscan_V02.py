# Author: David Ryan
# pythonportscan_V02.py
# SMB Share Scanning**: The program can discover available SMB shares on a network or target system.
# Connection Establishment**: It can establish connections to identified SMB shares using the built-in `smbprotocol` library.
# File Inspection**: The program inspects files within the shares to identify suspicious scripts and text files.
# Authentication**: If required, the program can attempt to log in as a Domain Administrator (DA) for more extensive access.

import netifaces as ni
import ipaddress
import sqlite3
import requests
import datetime


################################
# Function Retrieve information from local computer
################################

def netmask_to_cidr(netmask):
    try:
        cidr = sum([bin(int(x)).count("1") for x in netmask.split(".")])
        return str(cidr)
    except Exception as e:
        print(f"Error converting netmask to CIDR notation: {str(e)}")
        return ""


def get_lan_ip_addresses():
    try:
        # Get the network interfaces
        interfaces = ni.interfaces()

        subnet_info = {}
        for interface in interfaces:
            try:
                addrs = ni.ifaddresses(interface)
                ipv4_info = addrs[ni.AF_INET][0]
                ip = ipv4_info['addr']
                netmask = ipv4_info['netmask']

                network = ipaddress.IPv4Network(f"{ip}/{netmask}", strict=False)
                
                # Ignore loopback interfaces
                if not ipaddress.IPv4Address(ip) in ipaddress.IPv4Network("127.0.0.0/8"):
                    cidr = netmask_to_cidr(netmask)
                    subnet_info[interface] = {
                        'ip': ip,
                        'subnet': str(network.network_address),
                        'cidr': cidr,
                    }

            except (ValueError, KeyError):
                pass

        return subnet_info
    except Exception as e:
        return None

# Get WAN IP Address 
def get_external_ip():
    try:
        # Use a public API to fetch the external IP address
        response = requests.get("https://api.ipify.org?format=json")
        data = response.json()
        external_ip = data['ip']

        return external_ip
    except Exception as e:
        return None


#####################################
# SQLite Database
####################################

# Create the SQLite3 database and tables
def create_ip_info_db():
    try:
        conn = sqlite3.connect('ip_info.db')
        cursor = conn.cursor()

        # Create a table for WAN information
        cursor.execute('''CREATE TABLE IF NOT EXISTS wan
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, ip TEXT UNIQUE, last_checked TEXT)''')

        # Create a table for LAN information
        cursor.execute('''CREATE TABLE IF NOT EXISTS lan
                          (interface TEXT PRIMARY KEY, ip TEXT UNIQUE, subnet TEXT, cidr TEXT, last_checked TEXT)''')

        conn.commit()
        conn.close()
        print("Database 'ip_info.db' and tables 'wan' and 'lan' created.")
    except Exception as e:
        print(f"Error creating the database and tables: {str(e)}")

# Save LAN information to the 'lan' table
def save_lan_info_to_db(LAN):
    try:
        conn = sqlite3.connect('ip_info.db')
        cursor = conn.cursor()

        # Insert or replace LAN information into the 'lan' table
        for interface, info in LAN.items():
            cursor.execute("INSERT OR REPLACE INTO lan (interface, ip, subnet, cidr, last_checked) VALUES (?, ?, ?, ?, ?)",
                           (interface, info['ip'], info['subnet'], info['cidr'], datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        conn.commit()
        conn.close()
        print("LAN information saved to 'lan' table.")
    except Exception as e:
        print(f"Error saving LAN information to the 'lan' table: {str(e)}")

# Save WAN information to the 'wan' table
def save_wan_ip_to_db(wan):
    try:
        conn = sqlite3.connect('ip_info.db')
        cursor = conn.cursor()

        # Insert or replace WAN information into the 'wan' table
        cursor.execute("INSERT OR REPLACE INTO wan (ip, last_checked) VALUES (?, ?)",
                       (wan, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        conn.commit()
        conn.close()
        print("WAN information saved to 'wan' table.")
    except Exception as e:
        print(f"Error saving WAN information to the 'wan' table: {str(e)}")


################################
# Call the function
################################

#
create_ip_info_db()

# LAN information
subnet_info = get_lan_ip_addresses()
if subnet_info:
    print("\nSubnet Information:")
    for interface, info in subnet_info.items():
        print(f"Interface: {interface}")
        print(f"IP Address: {info['ip']}")
        print(f"Subnet: {info['subnet']}")
        print(f"cidr: {info['cidr']}\n")

    # Save to database
    save_lan_info_to_db(subnet_info)
else:
    print("Unable to retrieve subnet information.")

# WAN information
external_ip = get_external_ip()

if external_ip:
    print(f"External IP Address: {external_ip}")

    # Save the external IP address to the database
    save_wan_ip_to_db(external_ip)
else:
    print("Unable to retrieve external IP address.")

