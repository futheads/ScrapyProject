# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class CommonspiderSpiderMiddleware(object):
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


class CommonspiderDownloaderMiddleware(object):
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
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

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

import random
from scrapy.conf import settings

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        if spider.name == "proxySpider":
            proxy = random.choice(settings["PROXIES"])
            request.meta["proxy"] = proxy

class UAMiddleware(object):
    def process_request(self, request, spider):
        ua = random.choice(settings['USER_AGENT_LIST'])
        request.headers['User-Agent'] = ua

class LoginMiddleware(object):
    def process_request(self, request, spider):
        if spider.name == 'loginSpider':
            cookies = {
                "__cfduid": "d38263651ad8236175a7893f4beba79301544273385",
                "session": ".eJwljkuKwzAQRK8ieh2CZLd-PsXshzC0pJJtxnEGy1mF3D2CWRVFPYr3op-6SVvQaPp-kTp70B2tyQy60NcGaVDbY1brrs6Hkpz7qM5lbeqvM1e6vW-XfnKgLTSdxxO9rYUmyjZxinGMIweXpHhjqkX1iSt7yeNoQ3JOwCzGVi6So2QPuKFUY7MURLAuejAupKJDEbiKQapnzmJt9dbpBOiBE2sOKcLAakneGRSuXf_ZcPzL_K77vMsd9P4AL-1Krw.Du5pfg.wBWgWzhdbtBjU8QWLvyfCSN9Zng"
            }
            request.cookies = cookies

from selenium import webdriver
import time
from scrapy.http import HtmlResponse

class SeleniumMiddleware(object):
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        self.driver = webdriver.Chrome(executable_path="D:/program/webdriver/chromedriver.exe", chrome_options=options)

    def process_request(self, request, spider):
        # if spider.name == 'seleniumSpider':
        self.driver.get(request.url)
        time.sleep(1)
        body = self.driver.page_source
        return HtmlResponse(self.driver.current_url, body=body, encoding='utf-8', request=request)

import datetime
from CommonSpider.items import ErrorItem

class ExceptionCheckSpider(object):
    def process_spider_exception(self, response, exception, spider):
        print('返回的内容是：{}\n报错原因：{}'.format(response.body.decode(), type(exception)))
        page = response.meta["page"]
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_item = ErrorItem()
        error_item["page"] = page
        error_item["error_time"] = now_time
        yield error_item