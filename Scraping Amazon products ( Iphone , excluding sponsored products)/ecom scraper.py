import requests
from bs4 import BeautifulSoup
import pandas as pd

data = {'Title': [], 'Price': []}

payload = {'api_key': 'Your API Key', 'url':'https://www.amazon.in/s?k=iphone&crid=OKWUIIVXRU2D&sprefix=iphon%2Caps%2C276&ref=nb_sb_noss_2' }

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

# Send request through ScraperAPI with headers
r = requests.get(
    "http://api.scraperapi.com/",
    params= payload,
    headers=headers
)

soup = BeautifulSoup(r.text, "html.parser")
# print(soup.prettify())

# Find all <h2> elements with the specific class
h2_elements = soup.find_all("h2", class_="a-size-medium a-spacing-none a-color-base a-text-normal")

# Extract text from <span> elements without converting to a list of strings immediately
spans = [h2.find("span") for h2 in h2_elements if h2.find("span")]

prices = soup.select("span.a-price-whole")


# spans contains BeautifulSoup elements
for span in spans:
    # print(span.string)  
    data["Title"].append(span.string)

for price in prices:
    print(price.get_text())
    data["Price"].append(price.get_text())


df = pd.DataFrame.from_dict(data)
df.to_excel("data.xlsx", index = False)
