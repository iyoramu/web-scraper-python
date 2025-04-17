TARGET_URLS = {
    "news_site": {
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
    },
    "ecommerce_site": {
        "url": "https://shop.com/products",
        "selectors": {
            "item_selector": "div.product-card",
            "fields": {
                "name": "h3.product-name",
                "price": "span.price",
                "rating": "div.star-rating",
                "link": "a.product-link"
            }
        }
    }
}

# Request settings
REQUEST_SETTINGS = {
    "timeout": 10,
    "delay_between_requests": 2,
    "max_retries": 3
}
