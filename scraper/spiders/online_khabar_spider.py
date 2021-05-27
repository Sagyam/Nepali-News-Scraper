import scrapy
from ..items import ScraperItem
from langdetect import detect
import os

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def gen_sitemap_urls():
    for num in range(1, 122):
        gen_url = 'https://www.onlinekhabar.com/wp-sitemap-posts-post-' + \
            str(num) + '.xml'
        yield gen_url


def get_links():
    for url in gen_sitemap_urls():
        req = Request(url,  headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req).read().decode('utf-8')
        parser = 'lxml'
        soup = BeautifulSoup(response, parser)
        links = soup.text
        links = ['https://' +
                 half_link for half_link in links.split('https://')]
        for link in links:
            yield link


def write_to_file():
    file = open('./data/online_khabar_urls.txt', "a")
    for url in get_links():
        if len(url) > 10:
            url = url.strip('\n')
            file.write(url + '\n')
            print(url, 'Found')
    file.close()


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
        nepali_date_time = response.css(
            'div.post__time').css('span::text').get()
        category = response.css('a.current_page::text').get()
        news = response.css(
            'div.main__read--content').xpath('.//p/text()').getall()

        # Join all articles into single string and remove new lines
        news = ''.join(news)
        news = news.replace('\n', '')

        # Detect language
        lang = detect(news)

        # Extract Nepali date time from a string
        # string format->  २०७८ जेठ १२ गते १३:०८ मा प्रकाशित
        nepali_date_time = nepali_date_time.split(' ')
        nepali_year = nepali_date_time[0]
        nepali_month = nepali_date_time[1]
        nepali_date = nepali_date_time[2]
        nepali_time = nepali_date_time[4]

        '''
        Date Format --> १३:०८
        1 split by :
        2 map into int so that  devnagari numbers convert to english
        3 cast the map to list
        4 map the list of int back to str
        5 cast the map to list
        6 concat the mapped list with :
        '''
        time = ':'.join(
            list(map(str, list(map(int, nepali_time.split(':'))))))
        nepali_date = nepali_year + '-' + nepali_month + '-' + nepali_date

        items['Title'] = title
        items['English_Date'] = year + '-' + month
        items['Nepali_Date'] = nepali_date
        items['Time'] = time
        items['Category'] = category
        items['News'] = news
        items['Link'] = response.url
        items['Language'] = lang
        # items['Extra'] = extra

        yield items
