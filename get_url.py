from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def gen_sitemap_urls():
    for num in range(1, 2):
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


def write_to_file(count):
    file = open('online_khabar_urls.txt', "a")
    for url in get_links():
        # print(url)
        if len(url) > 10:
            file.write(url + '\n')
            count += 1
            print(count, url)
    file.close()


if __name__ == "__main__":
    file = open('online_khabar_urls.txt', 'w')
    file.close()
    write_to_file(count=0)
