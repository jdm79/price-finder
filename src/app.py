import requests
from bs4 import BeautifulSoup


url = "https://www.argos.co.uk/product/8838047"

request = requests.get(url)
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("li", {
    "class": "price product-price-primary",
    "itemprop": "price",
    "content": "34.99"
})
print(element.text)




# <li class="price product-price-primary"
# itemprop="price" content="34.99">
# <span itemprop="priceCurrency" content="GBP"></span>£34.99</li>