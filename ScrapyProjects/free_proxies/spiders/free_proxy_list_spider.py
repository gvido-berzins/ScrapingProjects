import scrapy
from free_proxies.items import ProxyItem


class FreeProxyListSpider(scrapy.Spider):
    name = "free_proxy_list"

    def start_requests(self):
        urls = ["https://free-proxy-list.net/"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        rows = response.css("div.fpl-list table tr")
        for r in rows:
            r_data = r.css("td::text").getall()
            try:
                ip, port, *_, is_https, _ = r_data
                schema = "https" if is_https.lower() == "yes" else "http"

            except ValueError:
                self.log("Invalid data row. Couldn't scrape")
            else:
                item = ProxyItem(ip=ip, port=port, protocol=schema)
                yield item.dict()
