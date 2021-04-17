import requests
from bs4 import BeautifulSoup

url = "https://www.mediamarkt.nl/nl/category/_laptops-482723.html"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

print(soup.prettify())
