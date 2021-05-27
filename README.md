# Nepali-News-Scraper

Nepali News Scraper Bot written with Scrapy

## Setup

### **Clone the repo**

`git clone https://github.com/Sagyam/Nepali-News-Scraper.git`

### **If virtualenv is not installed then**

`pip install virtualenv`

### **Create a virtual enviroment**

`virtualenv venv`

### **Activate the virual enviroment**

_Windows_

`venv\Scripts\activate`

_Linux or OS X_

`source venv/bin/activate`

### **Install Dependencies**

`pip install -r requirements.txt`

## Usage

### **Goto scraper directory**

`cd sraper`

**Save data as csv**

`scrapy crawl online_khabar -o ../data/data.csv `
