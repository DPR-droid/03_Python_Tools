import requests

# Set the base URL for the QRadar API
base_url = 'https://qradar.example.com/api/siem/sources'

# Set the API token for authenticating the request
api_token = 'YOUR_API_TOKEN'

# Set the HTTP headers
headers = {
  'Accept': 'application/json',
  'SEC': api_token
}

# Send the GET request to the QRadar API
response = requests.get(base_url, headers=headers)

# Check the status code of the response
if response.status_code == 200:
  # Print the list of sources
  sources = response.json()
  for source in sources:
    print(source['name'])
else:
  # Print an error message
  print(f"Error: {response.status_code}")
