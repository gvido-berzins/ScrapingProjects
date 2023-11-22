from enum import Enum
from datetime import datetime

import attrs


class StatusType(Enum):
    ONGOING = "Ongoing"
    COMPLETED = "Completed"


@attrs.define
class Chapter:
    url: str
    name: str
    chapter: int
    pages: int
    date_uploaded: datetime
    next_update: datetime


class SeriesType:
    MANGA = "Manga"
    MANHWA = "Manhwa"
    MANHUA = "Manhua"
    COMIC = "Comic"
    WEBTOON = "Webtoon"


@attrs.define
class Manga:
    source: str
    title: str
    url: str
    thumbnail_url: str
    artists: list[str]


@attrs.define
class DBManga:
    source: str
    title: str
    description: str
    url: str
    thumbnail_url: str
    artists: list[str]
    genres: list[str]
    tags: list[str]
    status: StatusType
    series_type: SeriesType
    chapters: list[Chapter]


@attrs.define
class MangaPage:
    mangas: list[Manga]
    has_next_page: bool


@attrs.define
class Page:
    index: int
    url: str
    image_url: str
