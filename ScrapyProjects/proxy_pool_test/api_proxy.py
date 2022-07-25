"""
API doc : http://pubproxy.com/#settings
GitHub  : https://github.com/clarketm/proxy-list
"""
from typing import Literal, TypedDict

import requests

PROTOCOLS = Literal["http", "https", "socks4", "socks5"]
ANON_LEVELS = Literal["anonymous", "elite"]
BASE_URL = "http://pubproxy.com/api/proxy"


class KwArgs(TypedDict):
    type: PROTOCOLS
    google_approved: bool
    level: ANON_LEVELS
    speed: int
    https: bool


def send_request(
    url: str,
    type: PROTOCOLS = "https",
    google_approved: bool = False,
    level: ANON_LEVELS = "anonymous",
    speed: int = 5,
    https: bool = True,
):
    r = requests.get(
        url,
        params=dict(
            limit=1,
            format="json",
            type=type,
            google=google_approved,
            level=level,
            https=https,
            speed=speed,
        ),
    )
    return r.json()


def get_proxy_dict(**kwargs: KwArgs) -> dict[str, str]:
    url = BASE_URL
    resp = send_request(url, **kwargs)
    data = resp.get("data")[0]
    ip_port = data["ipPort"]
    type = data["type"]
    ip_port = f"{type}://{ip_port}"

    proxy = dict(http=ip_port, https=ip_port)
    return proxy


def get_proxy(**kwargs: KwArgs) -> str:
    url = BASE_URL
    resp = send_request(url, **kwargs)
    data = resp.get("data")[0]
    ip_port = data["ipPort"]
    type = data["type"]
    ip_port = f"{type}://{ip_port}"
    return ip_port
