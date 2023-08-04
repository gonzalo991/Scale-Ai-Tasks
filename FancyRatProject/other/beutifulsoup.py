# Importing libraries
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Reading web page
url = "https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/jesus.html"
page = urlopen(url)
html = page.read().decode("utf-8")

# Reading HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
print(type(soup))
print(soup.prettify())