import scrapy

class CommonSpider(scrapy.Spider):
    name = 'loginSpider'
    allowed_domains = ['exercise.kingname.info']
    start_urls = ["http://exercise.kingname.info/exercise_login_success"]

    def parse(self, response):
        print(response.xpath("/html/body/div/text()").extract_first())