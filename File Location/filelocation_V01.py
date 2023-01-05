import csv
import os


# Read the CSV file
with open('file_locations.csv', 'r') as f:
  reader = csv.reader(f, delimiter=',')
  file_locations = list(reader)

# Create a new list to store the results
results = []

# Check each file location and store the result in the list
for file_location in file_locations:
  print(file_location[1])
  if os.path.exists(file_location[1]):
    results.append([file_location[0], file_location[1], 'Located'])
  else:
    results.append([file_location[0], file_location[1], 'Not Located'])

# Write the results to a new CSV file
with open('results.csv', 'w', newline='') as f:
  writer = csv.writer(f)
  writer.writerows(results)
