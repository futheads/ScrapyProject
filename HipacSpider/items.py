# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductInfoItem(scrapy.Item):
    """
    产品信息Item
    """
    pid = scrapy.Field()
    name = scrapy.Field()
    code = scrapy.Field()
    params = scrapy.Field()
    detail_url = scrapy.Field()
    type = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()


class ImageItem(scrapy.Item):
    """
    图片信息Item
    """
    type = scrapy.Field()
    url = scrapy.Field()
    pid = scrapy.Field()
