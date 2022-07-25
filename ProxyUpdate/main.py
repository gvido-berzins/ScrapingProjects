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
    speed: int = 1,
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
    ip_port = resp.get("data")[0]["ipPort"]
    proxy = dict(http=ip_port, https=ip_port)
    return proxy


def get_proxy(**kwargs: KwArgs) -> dict[str, str]:
    url = BASE_URL
    resp = send_request(url, **kwargs)
    ip_port = resp.get("data")[0]["ipPort"]
    return ip_port
