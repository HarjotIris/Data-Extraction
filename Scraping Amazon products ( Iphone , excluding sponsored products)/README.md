# Amazon iPhone Scraper

This project scrapes Amazon product listings for iPhones using ScraperAPI and BeautifulSoup.

## Features
- Extracts product titles from Amazon search results
- Uses ScraperAPI to bypass bot detection
- Parses HTML using BeautifulSoup
- Outputs extracted data in a structured format

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/amazon-iphone-scraper.git
   cd amazon-iphone-scraper
   ```
2. **Install dependencies**
   ```bash
   pip install requests beautifulsoup4
   ```

## Usage

1. **Set up ScraperAPI**
   - Get a ScraperAPI key from [ScraperAPI](https://www.scraperapi.com/)
   - Replace `your_api_key` in the script with your actual API key

2. **Run the script**
   ```bash
   python scrape_amazon.py
   ```

3. **Expected Output**
   The script prints the extracted iPhone names from the Amazon page:
   ```
   Apple iPhone 15 (128 GB) - Black
   Apple iPhone 14 Pro (256 GB) - Silver
   Apple iPhone 13 Mini (512 GB) - Blue
   ...
   ```

## License
This project is for educational purposes only. Scraping Amazon may violate their Terms of Service; use responsibly.

