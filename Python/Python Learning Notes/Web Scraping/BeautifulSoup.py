# beauty_soup.py

from bs4 import BeautifulSoup
from urllib.request import urlopen

'''
- Opens the URL http://olympus.realpython.org/profiles/dionysus by using urlopen() from the urllib.request module
- Reads the HTML from the page as a string and assigns it to the html variable
- Creates a BeautifulSoup object and assigns it to the soup variable
'''
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# get all the text from the webpage and automatically remove HTML tags
print(soup.get_text())

# to get the <title> tag in a document,  use the .title property
print(soup.title)
print(soup.title.string) # remove tags