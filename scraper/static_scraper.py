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
    soup = BeautifulSoup(response.text, 'html.parser')

    listings = []
    for post in soup.find_all('li', class_='result-row'):
        try:
            title = post.find('a', class_='result-title').text
            price = post.find('span', class_='result-price').text
            link = post.find('a', class_='result-title')['href']

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