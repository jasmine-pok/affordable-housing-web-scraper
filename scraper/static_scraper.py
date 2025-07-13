"""
    The goal here is to scrape Craigslist's Houston housing listings to extract:
    - Title
    - Price
    - Links to details
"""

import requests
from bs4 import BeautifulSoup
import json

def scrape_static_listings(url):
    response = requests.get(url)
    
    with open("scraper/craigslist_raw.html", "w", encoding="utf-8") as f:
        f.write(response.text)
    
    soup = BeautifulSoup(response.text, 'html.parser')

    listings = []
    for post in soup.select('li.cl-static-search-result')[:5]:
        try:
            title = post.find('div', class_='title').text.strip()
            price = post.find('div', class_='price').text.strip()
            link = post.find('a')['href']

            listings.append({
                "title" : title,
                "price" : price,
                "link" : link
            })
        except Exception as e:
            print(f"Skipping one listing due to error: {e}")
            continue

    with open('scraper/data.json', 'w') as f:
        json.dump(listings, f, indent=2)
    
    print(f"Scraped {len(listings)} listings.")

if __name__ == "__main__":
    craigslist_url = 'https://houston.craigslist.org/search/apa'
    scrape_static_listings(craigslist_url)