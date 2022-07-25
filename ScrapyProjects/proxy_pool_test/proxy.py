import concurrent.futures
from pathlib import Path
import random
from typing import Optional

from pydantic import BaseModel
import requests

BLACKLIST_PATH = Path("blackisted.txt")
WHITELIST_PATH = Path("whitelisted.txt")
ANON_MAP = {
    "A": "non anon",
    "N": "anon",
    "H": "high anon",
}


class Proxy(BaseModel):
    ip: str
    port: int
    country: str
    anonimity: str
    type: str
    google: bool

    @property
    def string(self) -> str:
        return f"{self.type}://{self.ip}:{self.port}"


def download_proxy_file():
    url = "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt"
    r = requests.get(url)
    return r.text


def process(text: str) -> list[Proxy]:
    proxies: list[Proxy] = []
    for line in text.splitlines(keepends=False):
        try:
            proxy = parse_line(line)
        except ValueError:
            pass
        else:
            proxies.append(proxy)
    return proxies


def parse_line(line: str) -> Proxy:
    ip_port, codes, google = line.strip().split(" ")
    ip, port = ip_port.split(":")
    ccode, anon, *type_ = codes.split("-")
    if not type_:
        protocol = "http"
    else:
        if type_[0] == "S":
            protocol = "https"
        else:
            protocol = "http"

    return Proxy(
        ip=ip,
        port=port,
        country=ccode,
        anonimity=ANON_MAP.get(anon, ""),
        type=protocol,
        google=google == "+",
    )


def filter_proxies(
    proxies: list[Proxy],
    google: bool = False,
    protocol: Optional[str] = None,
) -> list[Proxy]:
    proxies = blacklist_filter(proxies)
    filtered = filter(lambda x: x.google is google, proxies)
    if protocol is not None:
        filtered = filter(lambda x: x.type == protocol, proxies)

    return list(filtered)


def test_proxy(proxy: Proxy, timeout: float = 5.0) -> tuple[Proxy, bool]:
    try:
        requests.get(
            url="https://syberu.xyz",
            proxies=dict(http=proxy.string, https=proxy.string),
            timeout=timeout,
        )
    except requests.RequestException:
        print(f"Bad proxy: {proxy.string}")
        return proxy, False
    else:
        print(f"Good proxy: {proxy.string}")
        return proxy, True


def test_proxies(proxies: list[Proxy]) -> tuple[list[Proxy], list[Proxy]]:
    goods: list[Proxy] = []
    bads: list[Proxy] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(test_proxy, p): p for p in proxies}
        try:
            for future in concurrent.futures.as_completed(futures):
                proxy, is_good = future.result()
                if is_good:
                    goods.append(proxy)
                else:
                    bads.append(proxy)
        except KeyboardInterrupt:
            for future in futures:
                future.cancel()

    return goods, bads


def get_proxy_list(path: Path) -> set[str]:
    if not path.is_file():
        return set()
    return set(path.read_text().splitlines(keepends=False))


def blacklist_filter(proxies: list[Proxy]) -> list[Proxy]:
    filtered = filter(lambda x: x.string not in get_proxy_list(BLACKLIST_PATH), proxies)
    return list(filtered)


def update_blacklist(proxies: list[Proxy]) -> None:
    dump_proxies(BLACKLIST_PATH, proxies)


def update_whitelist(proxies: list[Proxy]) -> None:
    dump_proxies(WHITELIST_PATH, proxies)


def dump_proxies(path: Path, proxies: list[Proxy]) -> None:
    new_proxies: set[str] = set(x.string for x in proxies)
    listed = get_proxy_list(path)
    listed.update(new_proxies)
    path.write_text("\n".join(listed))


def get_proxy(**kwargs) -> str:
    text = download_proxy_file()
    proxies = process(text)
    proxies = filter_proxies(proxies, **kwargs)
    proxies, bad_proxies = test_proxies(proxies)
    update_blacklist(bad_proxies)
    update_whitelist(proxies)
    if not proxies:
        raise Exception("No proxies available")
    return random.choice(proxies).string
