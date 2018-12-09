# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CommonspiderItem(scrapy.Item):
    tag = scrapy.Field()
    cont = scrapy.Field()
    author = scrapy.Field()


class ErrorItem(scrapy.Item):
    page = scrapy.Field()
    error_time = scrapy.Field()