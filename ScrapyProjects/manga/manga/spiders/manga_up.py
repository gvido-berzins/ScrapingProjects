import scrapy
from scrapy.responsetypes import Response

BASE_URL = "https://global.manga-up.com/_next/data/AosrEeX6Cm_qhYedApqpE/en/manga/"


class MangaUpSpider(scrapy.Spider):
    name = "manga_up"
    allowed_domains = ["global.manga-up.com"]
    start_urls = [
        "https://global.manga-up.com/_next/data/AosrEeX6Cm_qhYedApqpE/en/search.json"
    ]

    def parse(self, response: Response):
        for it in response.json()["pageProps"]["data"]["titles"]:
            id_ = it["titleId"]
            next_url = f"{BASE_URL}{id_}.json"
            yield response.follow(next_url, callback=self.parse_item)

    def parse_item(self, response: Response):
        props = response.json()["pageProps"]
        it = props["data"]
        yield dict(
            id=props["titleId"],
            title=it["titleName"],
            author=it["authorName"],
            image=it["mainThumbnailUrl"],
            description=it["description"],
            url=it["sns"]["url"],
            next_update=it["nextUpdateInfo"],
            genres=[g["name"] for g in it["genres"]],
            last_ch_name=it["chapters"][-1]["mainName"],
            last_ch_id=it["chapters"][-1]["id"],
        )
