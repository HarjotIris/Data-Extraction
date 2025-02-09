import requests
from bs4 import BeautifulSoup
import pandas as pd

data = {'Headline': [], 'Description': []}

payload = {'api_key': '397a4c2c951cdb70873ad43ee651270c', 'url':'https://www.bbc.com/news/wales' }

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

articles = soup.find_all("div", {"data-testid" :"card-text-wrapper"})

for article in articles:
    headline_tag = article.find("h2", {"data-testid":"card-headline"})

    if not headline_tag:
        continue

    description_tag = article.find("p", {"data-testid":"card-description"})

    headline = headline_tag.get_text()
    description = description_tag.get_text() if description_tag else "-"

    data["Headline"].append(headline)
    data["Description"].append(description)

df = pd.DataFrame.from_dict(data)
save_path = save_path = r"C:\Desktop\Data Extraction\BBC News Headlines\News\UK Latest\Wales Latest\Wales latest updates.xlsx"

df.to_excel(save_path, index=False)

