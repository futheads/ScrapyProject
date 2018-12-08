# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class ImagespiderPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for img_url in item["img_urls"]:
            print(img_url)
            yield Request(img_url)