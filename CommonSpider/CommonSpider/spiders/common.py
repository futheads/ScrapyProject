# -*- coding: utf-8 -*-
import scrapy


class CommonSpider(scrapy.Spider):
    name = 'common'
    allowed_domains = ['exercise.kingname.info']
    start_urls = ['http://exercise.kingname.info/']

    def parse(self, response):
        pass
