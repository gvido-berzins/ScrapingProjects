import scrapy
from scrapy.responsetypes import Response


class MyIpSpider(scrapy.Spider):
    name = "my_ip"
    allowed_domains = ["httpbin.org"]
    start_urls = ["http://httpbin.org/"]

    def parse(self, response: Response):
        yield json.loads(response.body)
