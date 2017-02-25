# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SubtitlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class BookName(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
class BookContent(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()