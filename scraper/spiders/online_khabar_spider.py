import scrapy
from ..items import ScraperItem
import get_urls


class OnlineKhabarSpider(scrapy.Spider):
    name = 'online_khabar'
    get_urls.write_to_file()
    with open("../data/online_khabar_urls.txt", "rt") as f:
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
        # items['Extra'] = extra

        yield items
