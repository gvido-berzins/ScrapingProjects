# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import os
from typing import Optional

from scrapy import signals, Request, Spider
from proxy import get_proxy


class AttachProxyMiddleware:
    def process_request(self, request: Request, spider: Spider) -> Optional[Request]:
        self._set_env_proxy()
        return None

    def _set_env_proxy(self):
        proxy = get_proxy()
        print(f"Got proxy: {proxy}")
        os.environ["http_proxy"] = proxy
        os.environ["https_proxy"] = proxy
