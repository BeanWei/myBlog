# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class JuejinItem(scrapy.Item):
    articleUrl = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    publishtime = scrapy.Field()
    category = scrapy.Field()
    tag = scrapy.Field()
    content = scrapy.Field()
