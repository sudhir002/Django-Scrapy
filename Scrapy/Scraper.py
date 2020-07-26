import time
import scrapy
# from UrlScraper.UrlScraper.items import urlData
from scrapy.crawler import CrawlerProcess
from scrapy.http import HtmlResponse


class ScraperbotSpider(scrapy.Spider):
    name = "scraperBot"

    def __init__(self, *args, **kwargs):
        super(ScraperbotSpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('start_url')]

        '''self.name = name
        self.allowed_domains = [a]
        self.start_urls = [b]
        name = 'scraperBot'
        allowed_domains = [a] #['kiksarvr.com']
        start_urls = [b] #['https://www.kiksarvr.com']
        print("-=-=-")'''

    def parse(self, response):
        name = response.css('body').xpath("//*[@href]")
        # items = urlData()
        test = name.css('a::attr(href)').extract()
        yield {'title': test}
        # items['image_urls'] = test
        # print("======", items)
        # return items


# if __name__ == "__main__":
#     process = CrawlerProcess()
#     process.crawl(ScraperbotSpider())
#     process.start()
