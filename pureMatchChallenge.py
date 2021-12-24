"""import requests
from bs4 import BeautifulSoup
 
broken_links = 0
valid_links = 0
user_agent = {'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'}

url = 'http://develop.divercity.io/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
for link in soup.find_all('a'):
    print(link.get('href'))

for link in urls:
    if((requests.get(urls)).status_code) != 200:
        broken_links += 1
    else:
        valid_links +=1 


print(str(broken_links) +" broken links found, and " + str(valid_links) + " valid links found" )
"""


# Import libraries
from urllib import request
from bs4 import BeautifulSoup, SoupStrainer
import requests

valid_links = 0
broken_links = 0

# Prompt user to enter the URL
url = input("Enter your url: ")

# Make a request to get the URL
page = requests.get(url)

# Get the response code of given URL
response_code = str(page.status_code)

# Display the text of the URL in str
data = page.text

# Use BeautifulSoup to use the built-in methods
soup = BeautifulSoup(data)

# Iterate over all links on the given URL with the response code next to it
for link in soup.find_all('a'):
    print(f"Url: {link.get('href')} " + f"| Status Code: {response_code}")

    if ((requests.get(url)).status_code) != 200:
        broken_links += 1
    else:
        valid_links += 1

print("There were " +str(broken_links) + " found, and " + str(valid_links) + " valid links found!")