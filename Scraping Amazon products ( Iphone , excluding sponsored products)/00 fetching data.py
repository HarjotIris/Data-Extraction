import requests

API_KEY = "397a4c2c951cdb70873ad43ee651270c"  
url = "https://timesofindia.indiatimes.com/city/delhi"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

# Send request through ScraperAPI with headers
response = requests.get(
    "http://api.scraperapi.com/",
    params={"api_key": API_KEY, "url": url},
    headers=headers
)

# Print the scraped content
print(response.text)

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, "w", encoding='utf-8') as f:
        f.write(r.text)



fetchAndSaveToFile(url, "data/times.html")
