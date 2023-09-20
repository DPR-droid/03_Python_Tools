import sqlite3

def print_lan_scan_table_with_vendor():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('ip_info.db') 
        cursor = conn.cursor()

        # Define the SQL query
        sql_query = """
            SELECT ip_lan_scan.ip, ip_lan_scan.smb_info, ip_lan_scan.mac_address, maclookup.Vendor_Name
            FROM ip_lan_scan
            LEFT JOIN maclookup
            ON ip_lan_scan.mac_address LIKE maclookup.Mac_Prefix || '%';
        """

        # Execute the SQL query
        cursor.execute(sql_query)

        # Fetch all the rows
        rows = cursor.fetchall()

        # Print the table header
        print("{:<15} {:<15} {:<20} {:<30}".format("IP", "SMB Info", "MAC Address", "Vendor Name"))
        print("="*75)

        # Print each row of the table
        for row in rows:
            ip, smb_info, mac_address, vendor_name = row
            # Replace None values with an empty string
            vendor_name = vendor_name if vendor_name is not None else ""
            print("{:<15} {:<15} {:<20} {:<30}".format(ip, smb_info, mac_address, vendor_name))

        # Close the database connection
        conn.close()

    except Exception as e:
        print(f"Error: {str(e)}")

# Call the function to print the table
print_lan_scan_table_with_vendor()
