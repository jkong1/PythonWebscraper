from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic%20card'

filename = "products.csv"
f = open(filename, "w")
headers = "brand, product_name, shipping\n"

f.write(headers)

#opening up connection and read page
client = uReq(my_url)
page_html = client.read()
#close connection
client.close()
#html paser
page_soup = soup(page_html, "html.parser")
#grab each product
containers = page_soup.findAll("div",{"class":"item-container"})
print(containers[0].find("li","price-ship" ).text.strip())

for contain in containers:
    brand = contain.find("div","item-branding").img["title"]
    name = contain.find("a","item-title").text
    shipping = contain.find("li","price-ship").text.strip()
    f.write(brand + "," + name.replace(",", "|") + "," + shipping + "\n")
f.close()
