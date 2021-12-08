import scrapy
from ..items import RatopatiItem
from config import START_INDEX, END_INDEX


def gen_urls():
    for i in range(START_INDEX, END_INDEX):
        yield 'https://ratopati.com/story/' + str(i)


class RatopatiSpiderSpider(scrapy.Spider):
    name = 'ratopati_spider'

    start_urls = [url for url in gen_urls()]

    def parse(self, response):
        item = RatopatiItem()
        item['Title'] = response.css('h1::text').extract_first()
        item['Url'] = response.request.url
        item['News'] = response.css('div.imgAdj').css(
            'div.imgAdj').css('p::text').getall()

        # Join all articles into single string and remove new lines
        item['News'] = ''.join(item['News'])
        item['News'] = item['News'].replace('\n', '')
        item['News'] = item['News'].replace('\xa0', '')

        yield item
