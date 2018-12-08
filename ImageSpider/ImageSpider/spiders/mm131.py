# -*- coding: utf-8 -*-
import scrapy
from ImageSpider.items import ImagespiderItem
import re

class Mm131Spider(scrapy.Spider):
    name = 'mm131'
    allowed_domains = ['www.mm131.com']
    start_urls = ["http://www.mm131.com/xinggan/",
                  "http://www.mm131.com/qingchun/",
                  "http://www.mm131.com/xiaohua/",
                  "http://www.mm131.com/chemo/",
                  "http://www.mm131.com/qipao/",
                  "http://www.mm131.com/mingxing/"]

    def parse(self, response):
        list = response.css(".list-left dd:not(.page)")
        for img in list:
            # img_name = img.css("a::text").extract_first()
            img_url = img.css("a::attr(href)").extract_first()
            yield scrapy.Request(img_url, callback=self.content)
        next_url = response.css(".page-en:nth-last-child(2)::attr(href)").extract_first()
        if next_url is not None:
            yield response.follow(next_url, callback=self.parse)

    def content(self, response):
        item = ImagespiderItem()
        img_name = response.css(".content h5::text").extract_first()
        item["img_name"] = re.sub("[(\d)]", "", img_name)

        item["img_url"] = response.css(".content-pic img::attr(src)").extract_first()
        yield item
        next_url = response.css(".page-ch:last-child::attr(href)").extract_first()
        if next_url is not None:
            yield response.follow(next_url, callback=self.content)
