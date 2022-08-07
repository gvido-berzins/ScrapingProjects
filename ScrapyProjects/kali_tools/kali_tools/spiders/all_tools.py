import scrapy


class AllToolsSpider(scrapy.Spider):
    name = "all_tools"
    allowed_domains = ["www.kali.org"]
    start_urls = ["https://www.kali.org/tools/all-tools/"]

    def parse(self, response):
        for tool in response.css("#topics .card > ul > li"):
            name = tool.css("a::text").get().strip()
            url = tool.css("a::attr(href)").get()
            pkgs = tool.css("ul > li > a .ti-package")
            packages: list[dict[str, str | list[str]]] = []
            if not pkgs:
                commands = tool.css("ul > li > ul > li > a::text").getall()
                packages.append(dict(name=name, commands=commands))
            else:
                for pkg in pkgs:
                    name = pkg.xpath("parent::a/text()").get().strip()
                    commands = pkg.xpath("parent::a/parent::li/ul/li/a/text()").getall()
                    packages.append(dict(name=name, commands=commands))

            yield dict(name=name, url=url, packages=packages)
