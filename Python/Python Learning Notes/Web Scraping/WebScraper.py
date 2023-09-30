# Import Packages
from urllib.request import urlopen
import re

# The web page being opened
url = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(url)  # open the web page
# page  # returns an HHTPResponse object

# extract the HTML from the page
html_bytes = page.read()  # returns a sequence of bytes
html = html_bytes.decode("utf-8")  # use UTF-8 to decode the bytes to a string

pattern = "<title.*?>.*?</title.*?>"  # use of regular expressions
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title)  # remove HTML tags
print(title)