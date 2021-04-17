import requests
from bs4 import BeautifulSoup

url = "https://www.mediamarkt.nl/nl/category/_laptops-482723.html"

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "html.parser")

lists = soup.find_all("div", {"class": "product-wrapper"})


for list in lists:
    price = list.find("div", {"class": "price"}).text.strip('-').strip(',')

    comp_name = list.h2.text.strip().split("-")[0]

    detail1 = list.find('dl', {'class': 'product-details'}).find_all("dt")
    detail1 = list.find('dl', {'class': 'product-details'}).find_all("dd")

    show = f'Name: {comp_name} \nPrice: {price}'

    print(show)
