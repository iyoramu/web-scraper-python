import csv
import logging
from datetime import datetime
import os
import time

def setup_logger():
    """Configure and return a logger instance"""
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f"logs/scraper_{datetime.now().strftime('%Y%m%d')}.log"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

def save_to_csv(data, filename):
    """Save scraped data to CSV file"""
    if not data:
        return False
    
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        return True
    except Exception as e:
        logging.error(f"Error saving to CSV: {str(e)}")
        return False

def request_with_retry(url, headers, max_retries=3, delay=2):
    """Make HTTP request with retry logic"""
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(delay)
                continue
            raise e
