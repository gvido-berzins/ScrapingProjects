from typing import Any, Optional, Protocol, Generator
import attrs

import requests
from requests import Response
from bs4.element import PageElement
from bs4 import BeautifulSoup

from mango.models import Manga


@attrs.define
class MangaScrapper:
    source_name: str
    latest_url: str
    browse_url: str

    item_sel: str
    title_sel: str
    url_sel: str
    image_sel: str

    def get(self, url, **kwargs) -> PageElement:
        res = requests.get(url, **kwargs)
        if not res.ok:
            raise Exception(f"Bad status code: {res.status_code}")
        soup = BeautifulSoup(res.text, "html.parser")
        return soup

    def _parse_elements(
        self,
        elements: list[PageElement],
        title_sel: str,
        url_sel: str,
        image_sel: str,
    ) -> Generator[Manga, None, None]:
        for el in elements:
            yield Manga(
                source=self.source_name,
                title=el.find(title_sel).text,
                url=el.find(url_sel).text,
                thumbnail_url=el.find(image_sel).text,
            )

    def latest(self) -> list[Manga]:
        ...

    def browse(self) -> list[Manga]:
        soup = self.get(self.browse_url)
        print(soup.html)
        items = soup.find_all(self.item_sel)
        if not items:
            raise Exception(f"No items found with selector: {self.item_sel}")
        print(items)
        found = self._parse_elements(items, self.title_sel, self.url_sel, self.image_sel)
        return list(found)

    def search(self, query: str) -> list[Manga]:
        ...

    def parse_manga_search(self, el: PageElement) -> Manga:
        ...

    def parse_latest_manga(self, el: PageElement) -> Manga:
        ...

    def parse_browse_manga(self, el: PageElement) -> Manga:
        ...
