import scrapy
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware

class RotatingProxySpider(scrapy.Spider):
    name = "rotating_proxy_spider"

    # List of proxies for rotation
    proxy_list = [
        'http://192.168.1.1:8000',
        'http://192.168.1.2:8000',
        'http://192.168.1.3:8000',
    ]

    def start_requests(self):
        urls = ['https://example.com']
        for url in urls:
            yield scrapy.Request(url, callback=self.parse, meta={'proxy': self.get_random_proxy()})

    def parse(self, response):
        # Scraping logic here
        pass

    def get_random_proxy(self):
        import random
        return random.choice(self.proxy_list)
