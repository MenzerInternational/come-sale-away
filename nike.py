from urllib.request import urlopen
from bs4 import *

html = urlopen('https://www.nike.com/w/mens-shoes-nik1zy7ok')
soup = BeautifulSoup(html, 'html.parser')

for product in soup.find_all(class_='product-card__body'):
# Finds the individual product within the Nike.com product grid
    title = product.find(class_='product-card__link-overlay')
    print(title.get_text())
    price = product.find(class_='product-card__price')
    print(price.get_text())
