# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors
from CommonSpider.items import CommonspiderItem
import pymongo


class CommonspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(host="localhost",
                                       port=3306,
                                       db="test",
                                       user="futhead",
                                       passwd="futhead",
                                       charset="utf8",
                                       use_unicode=True)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.cursor.execute("""INSERT INTO mingyan(tag, cont, author) VALUES (%s, %s, %s);""",
                            (item["tag"], item["cont"], item["author"]))
        self.connect.commit()
        return item     # 这个必须有

from CommonSpider.items import ErrorItem

class MongodbPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient("127.0.0.1", 27017)
        self.db = client["test"]

    def process_item(self, item, spider):
        if isinstance(item, ErrorItem):
            post = self.db["error"]
        else:
            post = self.db["mingyan"]
        post.insert(dict(item))
        return item

if __name__ == '__main__':
    item = CommonspiderItem()
    item["tag"] = "tag"
    item["cont"] = "cont"
    item["author"] = "author"
    mysql_pipeline = MysqlPipeline()
    mysql_pipeline.process_item(item, None)