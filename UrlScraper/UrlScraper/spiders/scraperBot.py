import time
import scrapy
from UrlScraper.items import urlData
from scrapy.crawler import CrawlerProcess
from scrapy.http import HtmlResponse

class ScraperbotSpider(scrapy.Spider):
    name = "scraperBot"

    def __init__(self, *args, **kwargs):
        super(ScraperbotSpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('start_url')]
        
    def parse(self, response):
        name = response.css('body').xpath("//*[@href]")
        items = urlData()
        test = name.css('a::attr(href)').extract()
        yield ({self.start_url: test})

