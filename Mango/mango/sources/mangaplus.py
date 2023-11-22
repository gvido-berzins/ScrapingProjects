from typing import Any, Protocol

from requests import Response
from bs4.element import PageElement

from mango.models import Manga


class MangaplusScrapper:
    sources: list[str]
    latest_url: str
    browse_url: str

    def parse_manga_search(self, el: PageElement) -> Manga:
        ...

    def parse_latest_manga(self, el: PageElement) -> Manga:
        ...

    def parse_browse_manga(self, el: PageElement) -> Manga:
        ...
