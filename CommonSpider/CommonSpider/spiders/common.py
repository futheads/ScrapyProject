# -*- coding: utf-8 -*-
import scrapy
from CommonSpider.items import CommonspiderItem

class CommonSpider(scrapy.Spider):
    # name = 'common'
    # allowed_domains = ['exercise.kingname.info']
    # start_urls = ['http://exercise.kingname.info/']
    #
    # def parse(self, response):
    #     pass

    name = "common"
    allowed_domains = ["lab.scrapyd.cn"]
    start_urls = ["http://lab.scrapyd.cn"]

    def parse(self, response):
        mingyan = response.css("div.quote")

        item = CommonspiderItem()
        for v in mingyan:
            item["cont"] = v.css('.text::text').extract_first()  # 提取名言
            item["author"] = v.css('.author::text').extract_first()  # 提取作者
            item["tag"] = ",".join(v.css('.tags .tag::text').extract())
            yield item

            next_page = response.css("li.next a::attr(href)").extract_first()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
