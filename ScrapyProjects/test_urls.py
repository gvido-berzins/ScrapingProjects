import json
import time
from pathlib import Path
from pprint import pprint

import requests
from pydantic import BaseModel, parse_raw_as
from pydantic.json import pydantic_encoder

from free_proxies.items import ProxyItem as Proxy

MODULE_DIR = Path(__file__).parent


DEFAULT_TEST_URL: str = "https://syberu.xyz"
DEFAULT_TIMEOUT: float = 0.1
SAVE_PATH: Path = MODULE_DIR / "good_proxies.json"


def import_proxies(path: Path) -> list[Proxy]:
    json_raw = path.read_bytes()
    proxies = parse_raw_as(list[Proxy], json_raw)
    return proxies


def test_proxy(
    proxy: Proxy, url: str = DEFAULT_TEST_URL, timeout: float = DEFAULT_TIMEOUT
) -> bool:
    try:
        r = requests.get(url, proxies=proxy.proxies, timeout=timeout)
    except (
        requests.exceptions.ReadTimeout,
        requests.exceptions.ConnectTimeout,
        requests.exceptions.ConnectionError,
    ):
        return False
    return r.ok


def find_ok_proxies(proxies: list[Proxy]) -> list[Proxy]:
    return list(filter(test_proxy, proxies))


def save_proxies(proxies: list[Proxy], path: Path = SAVE_PATH) -> None:
    with path.open("w") as f:
        json.dump(proxies, f, default=pydantic_encoder)


def test_and_save() -> None:
    path = Path("list.json")
    print(f"Importing from {path}")
    proxies = import_proxies(path)

    print(f"Testing for good proxies")
    proxies = find_ok_proxies(proxies)

    print(f"Exporting good proxies")
    save_proxies(proxies)


def main() -> int:
    test_and_save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
