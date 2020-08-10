from urllib.request import urlopen
from bs4 import *

html = urlopen('https://needsupply.com/life/sale?lang=en_US')
soup = BeautifulSoup(html, 'lxml')


for product in soup.find_all(class_='product-tile'):
    item = 'data-name'
    item_price = 'data-price'

    print(product.get(item))
    print(product.get(item_price))
