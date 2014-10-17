import urlparse

from scrapy import Request
from scrapy.spider import BaseSpider

from altucher_podcast_scraper.items import AltucherItem


class AltucherTestSpider(BaseSpider):
    name = "AltucherTest"
    allowed_domains = ["stansberryradio.com"]
    start_urls = ["http://www.stansberryradio.com/James-Altucher/Latest-Episodes"]

    #rules = (Rule(LinkExtractor(allow=("Next", ))), )

    def parse(self, response):
        # Get deep inside the episode entries.
        for sel in response.xpath("//div[@class='ep-blo']"):
            link = sel.xpath("h3/a/@href").extract()[0]
            yield Request(urlparse.urljoin("http://www.stansberryradio.com/", link), callback=self.parse_inner_entry)

        # Advance to next page.
        sel = response.xpath("//div[@class='pager']")[0]
        for subsel in sel.xpath("ul/li"):
            if "next" in subsel.xpath("a/text()").extract()[0].lower():
                link = subsel.xpath("a/@href").extract()[0]
                yield Request(urlparse.urljoin("http://www.stansberryradio.com/", link), callback=self.parse)

    def parse_inner_entry(self, response):
        sel = response.xpath("//div[@class='main-col']/h1")
        title = sel.xpath("text()").extract()[0]

        sel = response.xpath("//a[@id='downloadLnk']")
        assert len(sel) == 1
        link_text = sel.xpath("text()").extract()[0]
        download_link = sel.xpath("@href").extract()[0]

        altucher_item = AltucherItem()
        altucher_item["name"] = title
        altucher_item["download_link"] = urlparse.urljoin("http://www.stansberryradio.com/", download_link)
        altucher_item["download_link_text"] = link_text
        yield altucher_item






