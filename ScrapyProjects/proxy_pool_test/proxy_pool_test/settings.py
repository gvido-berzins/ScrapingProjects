BOT_NAME = "proxy_pool_test"

SPIDER_MODULES = ["proxy_pool_test.spiders"]
NEWSPIDER_MODULE = "proxy_pool_test.spiders"

ROBOTSTXT_OBEY = True

PROXY_POOL_ENABLED = True
DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware": 600,
    "proxy_pool_test.middlewares.AttachProxyMiddleware": 610,
    # "scrapy.downloadermiddlewares.httpproxy": 630,
}
