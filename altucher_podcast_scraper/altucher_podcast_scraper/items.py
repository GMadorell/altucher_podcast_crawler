# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AltucherItem(scrapy.Item):
    name = scrapy.Field()
    download_link = scrapy.Field()
    download_link_text = scrapy.Field()
