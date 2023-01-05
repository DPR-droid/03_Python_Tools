import csv
import os

# Read the CSV file
with open('file_locations.csv', 'r') as f:
  reader = csv.reader(f)
  file_locations = list(reader)

# Check each file location
for file_location in file_locations:
  if os.path.exists(file_location[0]):
    print(f"{file_location[0]} exists on the Windows file system")
  else:
    print(f"{file_location[0]} does not exist on the Windows file system")