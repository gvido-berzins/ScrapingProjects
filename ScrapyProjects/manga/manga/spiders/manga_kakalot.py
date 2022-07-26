import functools
from typing import Any, Callable, Iterable, Optional

import scrapy
from scrapy.responsetypes import Response
from scrapy.selector import Selector

BASE_URL = "https://mangakakalot.com/manga_list?page="


class MangaKakalotSpider(scrapy.Spider):
    name = "manga_kakalot"
    allowed_domains = ["mangakakalot.com"]
    page_num = 1
    start_urls = ["https://mangakakalot.com/manga_list"]

    def parse(self, response: Response):
        for a in response.css(".list-truyen-item-wrap"):
            item_url = a.css("h3 a::attr(href)").get()
            self.log(f"Item url: {item_url}")
            yield response.follow(item_url, callback=self.parse_item)

        last_page = int(response.css(".page_last::text").re_first(r"\d+"))
        current_page = int(response.css(".page_select::text").get())
        self.log(f"{last_page=}, {current_page=}")
        if current_page <= last_page:
            self.page_num += 1
            next_page = f"{BASE_URL}{self.page_num}"
            self.log(f"Next page: {next_page}")
            if current_page != last_page:
                yield response.follow(next_page, callback=self.parse)

    def parse_item(self, response: Response):
        col_processor: Callable[[str], str] = lambda x: x.split(" : ")[-1]
        pss = functools.partial(_css, response)
        yield dict(
            genres=pss(
                ".manga-info-text :contains(Genr) a::text",
                ":contains('Genres') ~ .table-value .a-h::text",
                method="a",
            ),
            status=pss(
                ".manga-info-text :contains(Status) ::text",
                ":contains('Status') ~ .table-value::text",
                processor=col_processor,
            ),
            alt_title=pss(
                ":contains('Alternative') ~ .table-value h2::text",
                ".story-alternative ::text",
                processor=col_processor,
            ),
            authors=pss(
                ".manga-info-text :contains(Author) a::text",
                ":contains('Author') ~ .table-value a::text",
                method="a",
            ),
            updated=pss(
                ".manga-info-text :contains(updated) ::text",
                ".story-info-right-extent .stre-value::text",
                processor=col_processor,
            ),
            title=pss(".story-info-right h1::text", ".manga-info-text h1::text"),
            description=_join(
                pss(
                    "#noidungm::text",
                    ".panel-story-info-description::text",
                    method="a",
                )
            ),
            url=response.url,
            image=pss(".manga-info-pic img::attr(src)", ".info-image img::attr(src)"),
            latest_ch_url=pss(".chapter-list a::attr(href)", ".chapter-name::attr(href)"),
            latest_ch_title=pss(
                ".chapter-list a::attr(title)", ".chapter-name::attr(title)"
            ),
        )


def _css(
    r: Response,
    *selectors,
    method: str = "get",
    processor: Callable[[str], str] = None,
) -> Optional[str]:
    for selector in selectors:
        sel = r.css(selector)
        res = sel.getall() if method == "a" else sel.get()
        if res:
            if processor is not None:
                res = processor(res)
            return res
    else:
        return None


def _join(l: Any) -> str:
    if isinstance(l, str):
        return l

    if not isinstance(l, (list, tuple, Iterable)):
        return ""
    else:
        return _strip("\n".join(l))


def _strip(el: Any) -> str:
    if el is None:
        return ""
    if isinstance(el, str):
        return el.strip()
    else:
        return str(el)
