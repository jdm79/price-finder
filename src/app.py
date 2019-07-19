import requests
from bs4 import BeautifulSoup


url = "https://www.argos.co.uk/product/8838047"
html_snippet = {
    "class": "price product-price-primary",
    "itemprop": "price",
    "content": "34.99"
}

request = requests.get(url)
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("li", html_snippet)
string_price = element.text

budget = 30
price = float(string_price[1:])

if price < budget:
    print("This tent is less than £30 - buy it!")
else:
    print("This tent is too damn expensive!")
    # else
    # print("This tent is too expensive. stand down, soldier.")





# <li class="price product-price-primary"
# itemprop="price" content="34.99">
# <span itemprop="priceCurrency" content="GBP"></span>£34.99</li>