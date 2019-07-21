import requests
from bs4 import BeautifulSoup

def webscraper():

    # sometimes you need to add a header (like below) to fool the website
    # into thinking the scraper is a browser
    #
    # request = requests.get("https://www.argos.co.uk/product/8838047", headers={
    #     'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

    url = "https://www.argos.co.uk/product/8838047"
    html_snippet = {
        "class": "price product-price-primary",
        "itemprop": "price"
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

webscraper()



# Below is the original HTML snippet from the Argos website
# <li class="price product-price-primary"
# itemprop="price" content="34.99">
# <span itemprop="priceCurrency" content="GBP"></span>£34.99</li>