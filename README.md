![Logo](https://raw.githubusercontent.com/Sagyam/Nepali-News-Scraper/master/scrapy.png)
![GitHub](https://img.shields.io/github/license/sagyam/Nepali-News-Scraper?style=for-the-badge)
[![wakatime](https://wakatime.com/badge/user/4ce09006-1b8c-491f-ace1-a70b32d5fc1c/project/0b636540-37fc-48d2-a90e-0d43d369708f.svg?style=for-the-badge)](https://wakatime.com/badge/user/4ce09006-1b8c-491f-ace1-a70b32d5fc1c/project/0b636540-37fc-48d2-a90e-0d43d369708f?style=for-the-badge)

# Nepali News Scraper

A crawler that scrapes news from various nepali news portals.

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

Start Crawling Ekantipur

```bash
  cd ekantipur
  scrapy crawl ekantipur_spider
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
