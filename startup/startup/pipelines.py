# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pyodbc


class StartupPipeline:
    def process_item(self, item, spider):
        return item


class MSSQLPipeline:
    def open_spider(self, spider):
        self.connection = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=(localdb)\\MSSQLLocalDB;"
            "DATABASE=STARTUP;"
            "UID=csadmin;"
            "PWD=CSroqkfwk!!"
        )
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cursor.execute(
            """
            INSERT INTO NewsArticles (Date, Category, Title, Link, Snippet)
            VALUES (?, ?, ?, ?, ?)
            """,
            item['date'], item['category'], item['title'], item['link'], item['snippet']
        )
        self.connection.commit()
        return item