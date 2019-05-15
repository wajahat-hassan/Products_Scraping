# Scraping products name from a shopping website
# First Project

from urllib.request import urlopen
from bs4 import BeautifulSoup

my_url = 'https://homeshopping.pk/categories/DSLR-Cameras-in-Pakistan/?sort=popular&brandid=66'
html_getter = urlopen(my_url)
all_html = html_getter.read()

my_soup = BeautifulSoup(all_html, "html.parser")
container = my_soup.findAll("div", {"class": "product-box"})



products = []
for box in container:
    products.append(box.div.h5.a.string)


# Exporting list Projects to excel

from xlwt import Workbook
ws = Workbook()
sheet1 = ws.add_sheet("Sheet1")
sheet1.col(0).width = 10000


i = 0
for pr in products:
    sheet1.write(i,0, pr)
    i += 1

ws.save("xlwt products.xls")

