# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


import scrapy


class ScraperItem(scrapy.Item):
    # define the fields for your item here like:
    Title = scrapy.Field()
    English_Date = scrapy.Field()
    Nepali_Date = scrapy.Field()
    Time = scrapy.Field()
    Category = scrapy.Field()
    News = scrapy.Field()
    Link = scrapy.Field()
    Language = scrapy.Field()
    # Extra = scrapy.Field()
