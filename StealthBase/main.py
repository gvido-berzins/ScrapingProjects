import random
from pathlib import Path
from pprint import pprint
from typing import Literal, TypedDict

import requests
from environs import Env
from peewee import CharField, IntegerField, Model
from playhouse.db_url import connect

env = Env()
env.read_env()
DATABASE_URL: str = env("MYSQL_DATABASE_URL")
db = connect(DATABASE_URL)


ProxyDict = dict[str, str]


class BaseModel(Model):
    """A base model that will use our MySQL database"""

    class Meta:
        database = db


class Proxies(BaseModel):
    ip = CharField()
    port = IntegerField()
    protocol = CharField()

    @property
    def proxies(self) -> ProxyDict:
        proxy = f"{self.protocol}://{self.ip}:{self.port}"
        return dict(http=proxy, https=proxy)


def get_random_user_agent() -> str:
    lines = Path("user_agents.txt").read_text().splitlines(keepends=False)
    return random.choice(lines)


def get_all_proxies() -> list[Proxies]:
    return list(Proxies.select().execute())


def get_proxies(protocol: str = "http") -> ProxyDict:
    proxies: list[Proxies] = list(Proxies.select().where(Proxies.protocol == protocol))

    if not proxies:
        raise RuntimeError("Failed to get proxies")
    proxy_dict = random.choice(proxies).proxies
    return proxy_dict


def test(url: str = "https://api.myip.com") -> requests.Response:
    r = requests.post(
        url,
        headers={"User-Agent": get_random_user_agent()},
        proxies=get_proxies(),
        timeout=1,
    )
    if not r.ok:
        raise RuntimeError("Request not ok")
    return r


def main() -> int:
    url = "https://requestbin.io/1iktkd01"
    # url = "https://httpbin.org/ip"
    while True:
        try:
            print(test(url).json())
        except:
            pass
        else:
            break
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
