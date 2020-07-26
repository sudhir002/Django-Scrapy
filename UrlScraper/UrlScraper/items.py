import scrapy
from scrapy.item import Item

class UrlscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class urlData(Item):
    image_urls=scrapy.Field()
