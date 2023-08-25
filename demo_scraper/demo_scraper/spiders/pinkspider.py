import scrapy


class PinkspiderSpider(scrapy.Spider):
    name = "pinkspider"
    allowed_domains = ["pinkvilla.com"]
    start_urls = ["https://pinkvilla.com"]

    def parse(self, response):
        pass
