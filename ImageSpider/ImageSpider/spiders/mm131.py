# -*- coding: utf-8 -*-
import scrapy
from ImageSpider.items import ImagespiderItem


class Mm131Spider(scrapy.Spider):
    name = 'mm131'
    # allowed_domains = ['www.mm131.com']
    # start_urls = ['http://www.mm131.com/']

    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html',
                  "http://lab.scrapyd.cn/archives/57.html"]

    def parse(self, response):
        item = ImagespiderItem()  # 实例化item
        item["img_urls"] = response.css(".post img::attr(src)").extract()  # 注意这里是一个集合也就是多张图片
        item["img_name"] = response.css(".post-title a::text").extract_first()
        yield item
