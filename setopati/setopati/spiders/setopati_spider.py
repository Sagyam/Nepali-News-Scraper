import scrapy
from ..items import SetopatiItem
from config import START_INDEX, END_INDEX


def gen_urls():
    for i in range(START_INDEX, END_INDEX):
        yield 'https://www.setopati.com/politics/' + str(i)


def clean_text(text):
    text = text.replace('\n', '')
    text = text.replace('\t', '')
    text = text.replace('\xa0', '')
    text = text.strip()
    return text


class SetopatiSpiderSpider(scrapy.Spider):
    name = 'setopati_spider'

    start_urls = [url for url in gen_urls()]

    def parse(self, response):
        item = SetopatiItem()
        item['Title'] = response.css('.news-big-title::text').extract_first()
        item['Url'] = response.request.url
        item['News'] = response.css('div.editor-box').css('p::text').extract()

        '''
        Some pages do nat have <p> tag. 
        So, if no news was scraped then 
        we need to extract text directly 
        from th div
        '''

        if len(item['News']) == 0:
            item['News'] = response.css('div.editor-box::text').extract()

        # Join all articles into single string and remove new lines
        item['News'] = ''.join(item['News'])
        item['News'] = clean_text(item['News'])

        return item
