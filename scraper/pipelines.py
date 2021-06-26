# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class ScraperPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('./data/news.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""
                            CREATE TABLE IF NOT EXISTS news_table(
                            Url text PRIMARY KEY,
                            Title text,
                            Category text,
                            English_Date text,
                            Nepali_Date text,
                            Time text,
                            Language text,
                            News text
)""")

    def store_to_db(self, item):
        try:
            self.curr.execute("""
                                INSERT INTO news_table VALUES (?,?,?,?,?,?,?,?)""", (
                item['Link'],
                item['Title'],
                item['Category'],
                item['English_Date'],
                item['Nepali_Date'],
                item['Time'],
                item['Language'],
                item['News']

            ))
            self.conn.commit()
            print(item['Link'] + ' Written to DataBase')
        except sqlite3.IntegrityError:
            print(item['Link'] + " was a duplicate")

    def process_item(self, item, spider):
        self.store_to_db(item)
        return item
