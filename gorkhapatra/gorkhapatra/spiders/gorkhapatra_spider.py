import scrapy
from ..items import GorkhapatraItem
from config import COUNT, TOPICS, START_INDEX, END_INDEX
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def get_pages():
    for topic in TOPICS:
        for i in range(START_INDEX, END_INDEX):
            yield 'https://gorkhapatraonline.com/' + str(topic) + '?page=' + str(i)


def get_urls():
    parser = 'lxml'
    for page in get_pages():
        req = Request(page,  headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req).read().decode('utf-8')
        soup = BeautifulSoup(response, parser)
        soup = soup.select_one('.infinite-scroll')
        soup = soup.select('.business')
        for a_tag in soup:
            for link in a_tag.find_all('a', href=True):
                yield link['href']


def clean_text(text):
    text = text.replace('\n', '')
    text = text.replace('\xa0', '')
    text = text.strip()
    return text


class GorkhapatraSpiderSpider(scrapy.Spider):
    name = 'gorkhapatra_spider'

    start_urls = [url for url in get_urls()]

    def parse(self, response):
        item = GorkhapatraItem()

        item['Title'] = response.css('h1.post-title::text').extract_first()
        item['Url'] = response.request.url
        item['News'] = response.css(
            'div.newstext').css('p::text').extract()

        # Join all articles into single string and remove new lines
        item['News'] = ''.join(item['News'])
        item['News'] = clean_text(item['News'])

        yield item
