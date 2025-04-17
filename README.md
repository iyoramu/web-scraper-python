# Web Scraper Python Project

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A professional web scraping solution built with Python using Requests and BeautifulSoup. This project extracts structured data from websites and stores it in CSV format with proper error handling and logging.

## Features

- **Multi-site support**: Configure different selectors for different websites
- **Robust scraping**: Retry mechanism and error handling
- **Data export**: Clean CSV output with timestamps
- **Logging**: Comprehensive logging for debugging
- **Configurable**: Easy to adapt for new scraping targets

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/iyoramu/web-scraper-python.git
   cd web-scraper-python
   ```

2. **Set up virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Edit `config.py` to add your target websites and selectors:

```python
TARGET_URLS = {
    "example_news": {
        "url": "https://example-news.com/latest",
        "selectors": {
            "item_selector": "article.news-item",
            "fields": {
                "title": "h2.headline",
                "summary": "div.summary",
                "link": "a.read-more",
                "date": "span.publish-date"
            }
        }
    }
}
```

## Usage

### Running the scraper

```bash
python scraper.py
```

Or using the provided script:

```bash
chmod +x run_scraper.sh
./run_scraper.sh
```

### Output

Scraped data will be saved in the `data/` directory with filenames in the format:
```
data/{site_name}_{timestamp}.csv
```

Logs are stored in the `logs/` directory:
```
logs/scraper_{date}.log
```

## Project Structure

```
web-scraper-python/
│
├── scraper.py          # Main scraping logic
├── config.py           # Configuration for target websites
├── requirements.txt    # Python dependencies
├── run_scraper.sh      # Execution script
│
├── data/               # Output CSV files
├── logs/               # Log files
│
└── utils/              # Utility functions
    ├── helpers.py      # Helper functions (logging, file ops)
    └── selectors.py    # Selector validation and management
```

## Customizing for New Websites

1. Identify the HTML structure of your target website
2. Update `config.py` with:
   - The target URL
   - CSS selectors for the container element
   - Field-specific selectors
3. Test with:
   ```bash
   python scraper.py
   ```

## Best Practices

1. **Respect robots.txt**: Check the target website's robots.txt file
2. **Rate limiting**: Add delays between requests
3. **Selector maintenance**: Websites may change structure - monitor logs
4. **Error handling**: The scraper includes basic error recovery

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For issues or feature requests, please [open an issue](https://github.com/iyoramu/web-scraper-python/issues).

---

**Note**: Always ensure your scraping activities comply with the target website's terms of service and relevant laws.
