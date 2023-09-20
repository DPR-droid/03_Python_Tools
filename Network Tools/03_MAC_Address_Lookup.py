import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import sqlite3

def download_latest_csv():
    try:
        # URL of the page
        url = "https://maclookup.app/downloads/csv-database"

        # Send an HTTP GET request
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the link with text "Download CSV database"
        download_link = soup.find('a', text=re.compile(r'Download CSV database'))

        if download_link:
            # Extract the href attribute
            href = download_link['href']

            # Construct the full URL of the download link
            full_download_url = f"https://maclookup.app{href}"

            # Send an HTTP GET request to download the CSV file
            csv_response = requests.get(full_download_url)
            csv_response.raise_for_status()

            # Save the CSV file
            with open('latest_maclookup.csv', 'wb') as csv_file:
                csv_file.write(csv_response.content)

            print("Latest CSV file downloaded successfully.")
        else:
            print("Download link not found on the page.")

    except Exception as e:
        print(f"Error downloading the latest CSV file: {str(e)}")

# Call the function to download the latest CSV file
download_latest_csv()


def import_csv_to_sqlite(csv_file_path, db_file_path, table_name):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file_path)

        # Establish a connection to the SQLite database
        conn = sqlite3.connect(db_file_path)

        # Write the DataFrame to the database
        df.to_sql(table_name, conn, if_exists='replace', index=False)

        # Close the database connection
        conn.close()

        print(f"CSV data imported into '{table_name}' table in SQLite database.")

    except Exception as e:
        print(f"Error importing CSV data into SQLite database: {str(e)}")

# Specify the paths and table name
csv_file_path = 'latest_maclookup.csv'
db_file_path = 'ip_info.db'
table_name = 'maclookup'

# Call the function to import the CSV data into the SQLite database
import_csv_to_sqlite(csv_file_path, db_file_path, table_name)