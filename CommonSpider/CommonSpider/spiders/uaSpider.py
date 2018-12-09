import scrapy

class CommonSpider(scrapy.Spider):
    name = 'uaSpider'
    allowed_domains = ['exercise.kingname.info']
    start_urls = ["http://exercise.kingname.info/exercise_middleware_ua"]

    def parse(self, response):
        print(response.xpath("/html/body//text()").extract_first())