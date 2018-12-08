# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
import re

class ImagespiderPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # for img_url in item["img_urls"]:
        yield Request(item["img_url"], meta={"name": item["img_name"]})

    # 图片重命名
    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split("/")[-1]
        name = request.meta["name"]
        name = re.sub("[？\\*|“<>:/]", "", name)
        filename = "{0}/{1}".format(name, image_guid)
        return filename