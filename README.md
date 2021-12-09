![Logo](https://www.cryt.ie/wp-content/uploads/sites/3/2020/03/scrapy-1024x411.png)

![GitHub](https://img.shields.io/github/license/sagyam/Nepali-News-Scraper?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/Sagyam/Nepali-News-Scraper?style=for-the-badge)
![Lines of code](https://img.shields.io/tokei/lines/github/sagyam/Nepali-News-Scraper?style=for-the-badge)

# Nepali News Scraper

A crawler that scrapes news from a nepali news portal [Online Khabar](onlinekhabar.com)

## Run Locally

Clone the project

```bash
  git clone https://github.com/Sagyam/Nepali-News-Scraper
```

Go to the project directory

```bash
  cd Nepali-News-Scraper
```

Create a virtual enviroment

```bash
 virtualenv venv
```

Activate the virtual enviroment

**For Windows**

```bash
 venv\Scripts\activate
```

**For Linux / OSX**

```bash
source venv/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Open the respective config.py file change parameters as needed

Start Crawling Online Khabar

```bash
  cd scraper
  scrapy crawl online_khabar
```

Start Crawling Ratopati

```bash
  cd ratopati
  scrapy crawl ratopati_spider
```

Start Crawling Setopati

```bash
  cd setopati
  scrapy crawl setopati_spider
```

Start Crawling Gorkhapatra Online

⚠️ Caution: Must read Gorkhapatra config file before scraping⚠️

```bash
  cd gorkhapatra
  scrapy crawl gorkhapatra_spider
```

# Caution ⚠️

- **To pause gracefully crawling hit Ctrl+C once**
- **To pause forcefully hit Ctrl+C twice**
- **For OnlineKhabar it is recommended to scrape 2000 pages in one go**

## Tech Stack

**Tested using:**

- Python 3.7.3
- Scrapy 2.5.0
- BeautifulSoup 4.9.3

## Related

Here are some related projects

- [hemanta212/scrapers](https://github.com/hemanta212/scrapers)

## Feedback

If you have any feedback, please reach out to me at sagyamthapa32@gmail.com
