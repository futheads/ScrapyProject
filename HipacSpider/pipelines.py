# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from HipacSpider import settings
import mysql.connector
from HipacSpider.items import ProductInfoItem, ImageItem


MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOSTS, database=MYSQL_DB)
cur = cnx.cursor(buffered=True)


class Sql:

    @classmethod
    def insert_product(cls, pid, name, code, params, detail_url, _type, title, description):
        sql = "INSERT INTO `test`.`scrapy_product` (`name`, `code`, `params`, `detail_url`, `type`, `title`, " \
              "`description`, `pid`) VALUES (%(name)s, %(code)s, %(params)s, %(detail_url)s, %(type)s, %(title)s, " \
              "%(description)s, %(pid)s)"
        value = {
            "pid": pid,
            "name": name,
            "code": code,
            "params": params,
            "detail_url": detail_url,
            "type": _type,
            "title": title,
            "description": description
        }
        cur.execute(sql, value)
        cnx.commit()

    @classmethod
    def insert_image(cls, _type, url, pid):
        sql = "INSERT INTO `scrapy_product_img` (`type`, `url`, `pid`) VALUES (%(type)s, %(url)s, %(pid)s)"
        value = {
            'type': _type,
            'url': url,
            'pid': pid
        }
        cur.execute(sql, value)
        cnx.commit()

    @classmethod
    def select_pid(cls, pid):
        sql = "SELECT EXISTS(SELECT 1 FROM scrapy_product WHERE pid=%(pid)s)"
        value = {
            "pid": pid
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]


class HipacspiderPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item, ProductInfoItem):
            pid = item["pid"]
            ret = Sql.select_pid(pid)
            if ret[0] == 1:
                print('已经存在了')
                pass
            else:
                pid = item["pid"]
                name = item["name"]
                code = item["code"]
                params = item["params"]
                detail_url = item["detail_url"]
                _type = item["type"]
                title = item["title"]
                description = item["description"]
                Sql.insert_product(pid, name, code, params, detail_url, _type, title, description)
        if isinstance(item, ImageItem):
            _type = item["type"]
            url = item["url"]
            pid = item["pid"]
            Sql.insert_image(_type, url, pid)
