import netifaces as ni
import sqlite3
import datetime
import nmap
import json


#####################################
# SQLite Database Create the 'LAN_subnets'
####################################

def create_lan_subnets_table():
    try:
        conn = sqlite3.connect('ip_info.db')
        cursor = conn.cursor()

        # Create the 'LAN_subnets' table with a primary key and date_created
        cursor.execute('''CREATE TABLE IF NOT EXISTS LAN_subnets
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, subnet TEXT UNIQUE, cidr TEXT, date_created TEXT)''')

        conn.commit()
        conn.close()
        print("Table 'LAN_subnets' created.")
    except Exception as e:
        print(f"Error creating 'LAN_subnets' table: {str(e)}")

create_lan_subnets_table() 

# Function to extract subnets and cidrs from 'lan' table and insert into 'LAN_subnets'
def extract_and_insert_lan_subnets():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('ip_info.db')
        cursor = conn.cursor()

        # Query to retrieve unique subnets and cidrs from 'lan' table
        cursor.execute("SELECT DISTINCT subnet, cidr FROM lan")

        # Fetch all the rows
        rows = cursor.fetchall()

        # Get the current date and time
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Insert subnets and cidrs into 'LAN_subnets' table
        for row in rows:
            subnet, cidr = row
            cursor.execute("INSERT OR IGNORE INTO LAN_subnets (subnet, cidr, date_created) VALUES (?, ?, ?)",
                           (subnet, cidr, current_datetime))

        conn.commit()
        conn.close()
        print("Subnets and cidrs inserted into 'LAN_subnets' table.")
    except Exception as e:
        print(f"Error extracting and inserting LAN subnets: {str(e)}")


extract_and_insert_lan_subnets()


def read_lan_subnets():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('ip_info.db')
        cursor = conn.cursor()

        # Query to retrieve subnets and cidrs from 'LAN_subnets' table
        cursor.execute("SELECT subnet, cidr FROM LAN_subnets")

        # Fetch all the rows
        rows = cursor.fetchall()

        # Create a list to store the retrieved subnets and cidrs
        subnets = [{'subnet': row[0], 'cidr': row[1]} for row in rows]

        print(subnets)

        conn.close()
        return subnets

    except Exception as e:
        print(f"Error reading LAN subnets from the database: {str(e)}")
        return []

def insert_scan_results(scan_results):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('ip_info.db')
        cursor = conn.cursor()

        # Create the 'ip_lan_scan' table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS ip_lan_scan
                          (ip TEXT PRIMARY KEY, hostname TEXT, mac_address TEXT, status TEXT, smb_info TEXT, last_checked TEXT )''')

        # Parse the JSON 'scan' and insert scan results into the 'ip_lan_scan' table
        for ip, data in scan_results.items():
            hostname = data.get('hostnames', [{}])[0].get('name', '')
            mac_address = data.get('addresses', {}).get('mac', '')
            status = data.get('status', {}).get('state', '')
            smb_info = json.dumps(data.get('smb', {}))
            

            cursor.execute("INSERT OR REPLACE INTO ip_lan_scan (ip, hostname, mac_address, status, smb_info, last_checked ) VALUES (?, ?, ?, ?, ?, ?)",
                           (ip, hostname, mac_address, status, smb_info, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


        conn.commit()
        conn.close()
        print("Scan results inserted into 'ip_lan_scan' table.")
    except Exception as e:
        print(f"Error inserting scan results into the database: {str(e)}")

################################
# Ping LAN network
################################



def scan_lan_subnets(subnets):
    try:
        # Initialize Nmap
        nm = nmap.PortScanner()
  

        for subnet_info in subnets:
            subnet_str = subnet_info['subnet']
            cidr_str = subnet_info['cidr']

            print(subnet_str + "/" + cidr_str)

            # Scan hosts within the subnet
            scan_args = f"-p 445 --script smb-os-discovery -O -sS {subnet_str}/{cidr_str}"
            #scan_args = f"-p 445 --script smb-os-discovery -O -sT {subnet_str}/{cidr_str}"
            #scan_args = f"-p 445 --script smb-os-discovery -O -sF {subnet_str}/{cidr_str}"
            #scan_args = f"-p 445 --script smb-os-discovery -O -sn {subnet_str}/{cidr_str}"

            output = nm.scan(arguments=scan_args)
            #
            print(output)

            scan_results = output.get('scan', {})
            insert_scan_results(scan_results)

        return

    except Exception as e:
        print(f"Error scanning LAN subnets: {str(e)}")
        return []

################################
# Call Function
################################

subnets = read_lan_subnets()
if subnets:
    scan_results = scan_lan_subnets(subnets)
else:
    print("No LAN subnets found in the database.")



