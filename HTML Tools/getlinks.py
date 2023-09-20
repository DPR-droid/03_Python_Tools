import requests
from bs4 import BeautifulSoup
import json


#######################
# Read from save file
#######################

# Open the HTML file
with open('htmlextractlinks.html', 'r', encoding="utf-8") as file:
    content = file.read()

# Parse the HTML
soup = BeautifulSoup(content, 'html.parser')

# Extract all the anchor tags
extract = soup.find_all('a')

links = []
# Print the URLs of the links
for link in extract:
    # links.append(link.get('href'))
    print(link.get('href'))

# # Print the links
# print(links)

# #######################
# # Read from url
# #######################
# # Make an HTTP request to the web page
# url = 'https://www.example.com'
# response = requests.get(url)

# # Parse the HTML content of the page
# soup = BeautifulSoup(response.content, 'html.parser')

# #######################

# # Find all the <a> elements and extract the href attributes
# links = []
# for a in soup.find_all('a', href=True):
#     links.append(a['href'])

# # Print the links
# print(links)




# # Extract all the anchor tags
# links = soup.find_all('a')

# # Print the URLs of the links
# for link in links:
#     print(link.get('href'))



# import json
# from firefox_remote import FirefoxRemote

# # Connect to Firefox
# firefox = FirefoxRemote()



# # Create a new bookmark folder
# folder = firefox.bookmarks.create({
#     "title": "PenTest+",
#     "type": "folder"
# })

# # Add links to the folder
# for link in links:
#     firefox.bookmarks.create({
#         "title": link,
#         "url": link,
#         "parentId": folder["id"]
#     })

# print("Links have been added to the bookmark folder.")