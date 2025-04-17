import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
from config import TARGET_URLS, SELECTORS
from utils.helpers import setup_logger, save_to_csv
from utils.selectors import validate_selectors

logger = setup_logger()

def scrape_website(url, selector_config):
    """Scrape data from a single website based on selector configuration"""
    try:
        logger.info(f"Scraping URL: {url}")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        scraped_data = []
        
        # Extract data based on selectors
        for item in soup.select(selector_config['item_selector']):
            data_point = {}
            for field, selector in selector_config['fields'].items():
                element = item.select_one(selector)
                data_point[field] = element.get_text(strip=True) if element else None
            
            if any(data_point.values()):  # Only add if we got some data
                scraped_data.append(data_point)
        
        return scraped_data

    except Exception as e:
        logger.error(f"Error scraping {url}: {str(e)}")
        return []

def main():
    """Main function to run the scraper"""
    for site_name, config in TARGET_URLS.items():
        logger.info(f"Processing {site_name}...")
        
        # Validate selectors before scraping
        if not validate_selectors(config['selectors']):
            logger.error(f"Invalid selectors for {site_name}. Skipping...")
            continue
            
        data = scrape_website(config['url'], config['selectors'])
        
        if data:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"data/{site_name}_{timestamp}.csv"
            save_to_csv(data, filename)
            logger.info(f"Saved {len(data)} items to {filename}")
        else:
            logger.warning(f"No data scraped from {site_name}")

if __name__ == "__main__":
    main()
