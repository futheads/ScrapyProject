# -*- coding: utf-8 -*-
import time
import re

import scrapy
from HipacSpider.items import ProductInfoItem, ImageItem
import execjs
import json
from scrapy.http import Request
import urllib

# init environment
node = execjs.get()

file = "sign.js"
ctx = node.compile(open(file, encoding="utf-8").read())


class Sign:
    @classmethod
    def get_sign(cls, api_name, version, param, time):
        return ctx.eval("sign('{}', '{}', '{}', {})".format(api_name, version, param, time))


class HipacSpider(scrapy.Spider):
    name = 'hipac'
    allowed_domains = ['api.hipac.cn']

    @staticmethod
    def get_product_detail_url(pid):
        url = "http://api.hipac.cn/process/prod/1.0.3/mall.item.detail.pc/?" \
              "appKey=1300&os=Chrome&t={}&sign={}&data={}"
        api_name = "mall.item.detail.pc"
        version = "1.0.3"
        param = '{"itemId":"%d"}'
        data = param % pid
        t = int(time.time() * 1000)
        sign = Sign.get_sign(api_name, version, data, t)
        return url.format(t, sign, data)

    @staticmethod
    def get_image_item(_type, url, pid):
        item = ImageItem()
        item["type"] = _type
        item["url"] = url
        item["pid"] = pid
        return item

    start_urls = [
        'https://api.hipac.cn/process/prod/1.0.2/mall.item.searchItemListWithFlashBuyAct.pc/?appKey=1300&os=Chrome&data={"pageNo":5,"pageSize":20,"cateIds":"257","sortType":"3","itemSearchTypes":"","itemChildTypes":null,"searchSource":"cate","source":"pc"}&signType=new&t=1554191260062&sign=b7182c6c9e81c078bb2fea4ce975c6f6'
    ]

    def parse(self, response):
        """
        列表页请求
        :param response:
        :return:
        """
        url_template = "https://api.hipac.cn/process/prod/1.0.2/mall.item.searchItemListWithFlashBuyAct.pc/?appKey=1300&os=Chrome&t={}&sign={}&data={}"
        api_name = "mall.item.searchItemListWithFlashBuyAct.pc"
        version = "1.0.2"

        url = urllib.parse.unquote(str(response.url))
        content = json.loads(response.text)

        regex = '"cateIds":"(.*?)"'
        cate_id = re.search(regex, url, re.S).group(1).strip()
        total_page = content["data"]["totalPage"]
        for num in range(1, int(total_page) + 1):
            param = '{"pageNo":%s,"pageSize":20,"cateIds":"%s","sortType":"3","itemSearchTypes":"","itemChildTypes":null,"searchSource":"cate","source":"pc"}'
            data = param % (num, cate_id)
            t = int(time.time() * 1000)
            sign = Sign.get_sign(api_name, version, data, t)
            list_url = url_template.format(t, sign, data)
            yield Request(list_url, callback=self.get_list)

    def get_list(self, response):
        """
        解析摘要信息
        :param response:
        :return:
        """
        content = json.loads(response.text)
        for item in content["data"]["itemList"]:
            pid = item["id"]
            detail_url = self.get_product_detail_url(pid)
            yield Request(detail_url, callback=self.get_detail, meta={"pid": pid})

    def get_detail(self, response):
        """
        解析详情信息
        :param response:
        :return:
        """
        pid = response.meta["pid"]
        url = urllib.parse.unquote(str(response.url))
        content = json.loads(response.text)
        if "data" in content:
            data = content["data"]
            name = data["name"]
            code = ""
            params = dict()
            if "itemAttrInfo" in data:
                item_attr_info = data["itemAttrInfo"]
                for attr in item_attr_info:
                    if attr["name"] == "条形码":
                        code = attr["value"]
                    params[attr["name"]] = attr["value"]
            _type = ""
            title = ""
            extension_fields = data["extensionFields"]
            if "extensionFields" in data:
                for field in extension_fields:
                    if "featureType" in field and field["featureType"] == "4":
                        titles = []
                        for t in field["values"]:
                            titles.append(t["name"])
                        title = ":::".join(titles)
                        _type = field["name"]
            product = ProductInfoItem()
            product["pid"] = pid
            product["name"] = name
            product["code"] = code
            product["params"] = json.dumps(params, ensure_ascii=False)
            product["detail_url"] = url
            product["type"] = _type
            product["title"] = title
            product["description"] = data["descp"]
            yield product
            yield self.get_image_item(data["pic"], "主图", pid)
            for detail_pic_url in data["detailPics"]:
                yield self.get_image_item(detail_pic_url, "详情图", pid)
            for carousel_pic_url in data["mainPics"]:
                yield self.get_image_item(carousel_pic_url, "轮播图", pid)
