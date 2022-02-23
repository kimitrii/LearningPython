#to run this code you will need to install the BeautifulSoup extantion
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#retrieve all of anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
