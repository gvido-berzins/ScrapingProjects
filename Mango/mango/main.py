from mango.models import Manga
from mango.sources.types import MangaScrapper


def _latest(scrapper: MangaScrapper) -> list[Manga]:
    ...


def _browse(scrapper: MangaScrapper) -> list[Manga]:
    items = scrapper.browse()
    for item in items:
        print(item)


def main() -> int:
    print("In main")
    scrapper = MangaScrapper(
        source_name="Mangaplus",
        latest_url="https://mangaplus.shueisha.co.jp/manga_list/all",
        browse_url="https://mangaplus.shueisha.co.jp/manga_list/all",
        item_sel=".AllTitle-module_allTitle_1CIUC",
        title_sel=".AllTitle-module_title_20PzS",
        url_sel="",
        image_sel=".AllTitle-module_image_JIEI9",
    )
    print("browsing")
    _browse(scrapper)
    return 0


if __name__ == "__main__":
    main()
