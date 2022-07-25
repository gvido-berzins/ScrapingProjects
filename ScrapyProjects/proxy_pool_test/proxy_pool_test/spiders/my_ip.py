import json

import scrapy
from scrapy.responsetypes import Response


class MyIpSpider(scrapy.Spider):
    name = "my_ip"
    allowed_domains = ["httpbin.org"]
    start_urls = ["http://httpbin.org/ip"]

    def parse(self, response: Response):
        for _ in range(5):
            item = json.loads(response.body)
            print(item)
            yield item
