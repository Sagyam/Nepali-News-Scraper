# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RatopatiItem(scrapy.Item):
    # define the fields for your item here like:
    Title = scrapy.Field()
    Url = scrapy.Field()
    News = scrapy.Field()
