import json
from pathlib import Path
from pprint import pprint

import click

SOURCE_PATH = Path("sources")


def get_sources() -> list[Path]:
    return list(p for p in SOURCE_PATH.glob("*json"))


def find_by_title(
    title: str, case_insensitive: bool = False, first: bool = False
) -> list[dict[str, str]]:
    finds: list[dict[str, str]] = []
    for source in get_sources():
        for it in json.loads(source.read_bytes()):
            it_title = it["title"]
            if it_title is None:
                continue
            if case_insensitive is False:
                it_title = it_title.lower()
                title = title.lower()
            if title in it_title:
                if first is False:
                    finds.append(it)
                else:
                    return [it]
    return finds


@click.argument("title")
@click.command()
def main(title: str):
    items = find_by_title(title)
    if items:
        print(f"{len(items)} Items found matching title {title!r}")
        print("".center(60, "-"))
    else:
        print(f"No items found with title {title!r}")

    for item in items:
        pprint(item)


if __name__ == "__main__":
    main()
