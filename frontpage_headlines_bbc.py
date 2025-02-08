import requests
from bs4 import BeautifulSoup

# Accessing HTML content from webpage
url = "https://www.bbc.com/"
headers = {"User-Agent": "Mozilla/5.0"} # helps avoid getting blocked

r = requests.get(url, headers = headers)
#print(r.content)

soup = BeautifulSoup(r.content, 'html5lib')

#print (soup.prettify())

headlines = soup.find_all("h2", {"data-testid":"card-headline"})

for idx, headline in enumerate(headlines, 1):
    print(f"{idx}. {headline.text.strip()}")