# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random

from scrapy import signals


class HipacspiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class HipacspiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.process_request

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called

        request.headers[
            "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
        request.headers["Host"] = "api.hipac.cn"

        cookies = [
            "acw_tc=2f624a3515525447331993547e61488470c932a13415163c14a7d1b308a802; uid=3a174da55e814f19a088f57b53cf611a; hipac.cn_USERID=3a174da55e814f19a088f57b53cf611a; df=1f3fe8ed63ad88558e8c516f85b26a20-1697ae097cd_tongdun; yduss_production=M6zhthVOv904OhWpFYuNLJjk-Pp6ZAbwDQscSIN_eNs0uBdq5o8JkDS3WvOXPhvo18IPHuUW43slhaE5RMC2AgbP_iNT01tYb18w-3HPAAmxS2mbySuIPJTKR9uQ721q_A1xvprE73TuqUOEegTrRzX9leKeNvEMeoxvjJ3Z7U26ELiggXYM-W3KPBWGO9rptue_RgeeGwYlL37ZfLxDmr0cNrtMc_w_4JicN7nVtdEcTYjIcMoPN-tP5QLWu5aouv_9XEvFmk6zB4CAq78q2kMm5jVvbS3VlUxaFzf1qxKY4O3edYxG1BkSMpM9alFpyM78kIX8kohBdKnBhGwyEBjHaTe9qTx9aXcCKFrTBB0l4AbjiqQXQ4xO65pu7cm5iI6MTbWhD0EpUOhjYKWPa9USed1ZWxbsCED5qYIsQ6OEr6YvDgL7LxRUD00IIXCsJfg1zZ8WAPjT0fP0m2Mq3PxlC2UzrWoq-rFmQQw0FJfcfSJ1pzCo0iR1-zGodoSYrUqO8jGkJ76wKyTbdAyhLXJBb4wHr-L1ODwhaeBVWIRy9YrPhRQhh-8MPGJ0dEoji8EvcOxwUvs.; hipac.cn_LASTLOGINTIME=1554169787426; hipac.cnuser_uuid=b18329f5-05ce-4ce4-9736-bba86814ee0a; SERVERID=703df12c9070c5b89b89c38696dbd8d2|1554191346|1554115585",
        ]
        cookie = random.choice(cookies)
        for kv in cookie.split("; "):
            key_value = kv.split("=")
            request.cookies[key_value[0]] = key_value[1]

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
