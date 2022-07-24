import ipaddress
from typing import Literal

import scrapy
from pydantic import BaseModel, Field, IPvAnyAddress, conint, validator


class ProxyItem(BaseModel):
    ip: str
    port: conint(gt=1, lt=65536)
    protocol: Literal["http", "https"]

    @validator("ip")
    def ip_valid(cls, v):
        assert ipaddress.ip_address(v)
        return v

    @property
    def proxies(self) -> dict[str, str]:
        return {self.protocol: f"{self.ip}:{self.port}"}
