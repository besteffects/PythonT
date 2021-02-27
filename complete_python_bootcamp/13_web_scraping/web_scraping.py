import requests
import bs4

# TASK 1: Use requests library and BeautifulSoup to connect to http://quotes.toscrape.com/ and get the HMTL text from the homepage.

res = requests.get('http://quotes.toscrape.com/')
print(res.text)

#TASK 2: Get the names of all the authors on the first page.


