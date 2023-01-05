import csv
import os
import openpyxl

file_locations=[]  

# Read the CSV file
with open('file_locations.csv', 'r') as f:
  reader = csv.reader(f, delimiter=',')
  for row in reader:
      #
      file_locations.append(row[1])

# Create a new Excel workbook and sheet
workbook = openpyxl.Workbook()
sheet = workbook.active

# Add a header row to the sheet
sheet.append(['File Location', 'Result'])

# Check each file location and add a row to the sheet
for file_location in file_locations:
  if os.path.exists(file_location):
    print(file_location)
    sheet.append([file_location, 'Located'])
  else:
    sheet.append([file_location, 'Not Located'])

# Format the cells in the sheet
for row in sheet.rows:
  if row[1].value == 'Located':
    row[1].font = openpyxl.styles.Font(color='00FF00')
  else:
    row[1].font = openpyxl.styles.Font(color='FF0000')

# Save the workbook to a file
workbook.save('results.xlsx')