# -*- coding: utf-8 -*-
import scrapy


class Mm131Spider(scrapy.Spider):
    name = 'mm131'
    allowed_domains = ['www.mm131.com']
    start_urls = ['http://www.mm131.com/']

    def parse(self, response):
        pass
