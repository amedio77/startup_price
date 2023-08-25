# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StartupItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class NewsItem(scrapy.Item):
    date = scrapy.Field()
    category = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    snippet = scrapy.Field()