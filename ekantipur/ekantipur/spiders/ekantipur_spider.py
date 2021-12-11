import scrapy
from ..items import EkantipurItem
from datetime import date, timedelta
from config import START_DATE, END_DATE
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def split_date(date_str):
    year = int(date_str.split('-')[0])
    month = int(date_str.split('-')[1])
    day = int(date_str.split('-')[2])
    return year, month, day


def get_dates():
    start_year, start_month, start_day = split_date(START_DATE)
    end_year, end_month, end_day = split_date(END_DATE)

    start_date = date(start_year, start_month, start_day)
    end_date = date(end_year, end_month, end_day)
    delta = end_date - start_date

    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        day = str(day)
        day = day.replace('-', '/')
        yield day


def get_urls():
    parser = 'lxml'
    for date in get_dates():
        url = "https://ekantipur.com/news/" + date
        req = Request(url,  headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req).read().decode('utf-8')
        soup = BeautifulSoup(response, parser)
        articles = soup.find_all('article')
        for article in articles:
            h2 = article.find('h2')
            for link in h2.find_all('a', href=True):
                yield 'https://ekantipur.com' + link['href']


def clean_text(text):
    text = text.replace('\n', '')
    text = text.replace('\xa0', '')
    text = text.strip()
    return text


class EkantipurSpiderSpider(scrapy.Spider):
    name = 'ekantipur_spider'
    allowed_domains = ['ekantipur.com']
    start_urls = (url for url in get_urls())

    def parse(self, response):
        item = EkantipurItem()

        item['Title'] = response.css(
            'div.article-header').css('h1::text').extract_first()
        item['Url'] = response.request.url
        item['News'] = response.css(
            'div.description.current-news-block').css('p::text').extract()

        # Join all articles into single string and remove new lines
        item['News'] = ''.join(item['News'])
        item['News'] = clean_text(item['News'])
        return item
