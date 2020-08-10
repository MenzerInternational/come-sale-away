from urllib.request import urlopen
from bs4 import *
# Defines web page to be scraped and sets variable name for scraped tags
html = urlopen("https://www.theory.com/mens-sale/")
soup = BeautifulSoup(html, 'html.parser')

for product in soup.find_all(class_='tile product-tile'):
    item  = 'data-gtmtitle'
    price = product.find(class_='price-sales')
    print(product.get(item))
    print(price.get_text())
