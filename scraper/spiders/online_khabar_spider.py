import scrapy
from ..items import ScraperItem
from config import MAX_VAL, MIN_VAL
from langdetect import detect
import os

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def gen_sitemap_urls():
    for num in range(MIN_VAL, MAX_VAL):
        gen_url = 'https://www.onlinekhabar.com/wp-sitemap-posts-post-' + \
            str(num) + '.xml'
        yield gen_url


def get_links():
    parser = 'lxml'
    for url in gen_sitemap_urls():
        req = Request(url,  headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req).read().decode('utf-8')
        soup = BeautifulSoup(response, parser)
        links = soup.text
        links = ['https://' +
                 half_link for half_link in links.split('https://')]
        yield from links


def write_to_file():
    with open('./data/online_khabar_urls.txt', "w") as file:
        for url in get_links():
            if len(url) > 10:
                url = url.strip('\n')
                file.write(url + '\n')


def prepare_dir():
    # Check if it's first run
    if not os.path.exists('./data'):
        os.makedirs('./data')
    file = open('./data/online_khabar_urls.txt', 'w')
    file.close()
    write_to_file()


class OnlineKhabarSpider(scrapy.Spider):

    """Note name, start_urls are scrapy varibles
        and must never be renamed """
    name = 'online_khabar'
    prepare_dir()

    with open("./data/online_khabar_urls.txt", "rt") as f:
        start_urls = [url.strip() for url in f.readlines()]

    def parse(self, response):

        items = ScraperItem()
        title = response.css('h2.mb-0::text').extract_first()
        month, year = response.url.split("/")[-2], response.url.split("/")[-3]

        category = response.css('a.current_page::text').get()
        news = response.css(
            'div.main__read--content').xpath('.//p/text()').getall()

        # Join all articles into single string and remove new lines
        news = ''.join(news)
        news = news.replace('\n', '')

        # Detect language
        try:
            lang = detect(news)
        except:
            print(response.url + ' has unkown language')
            lang = None

        items['Title'] = title
        items['English_Date'] = year + '-' + month
        items['Category'] = category
        items['News'] = news
        items['Link'] = response.url
        items['Language'] = lang

        # items['Extra'] = extra

        yield items
