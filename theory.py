from urllib.request import urlopen
from bs4 import *
# Defines web page to be scraped and sets variable name for scraped tags
html = urlopen("https://www.theory.com/mens-sale/")
soup = BeautifulSoup(html, 'html.parser')

for product in soup.find_all(class_='product-name'):   # Pulls tags by product name from 'html'
    print(product.get_text())           # Strips tags from from products and converts to string
