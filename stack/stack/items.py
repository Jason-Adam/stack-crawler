# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StackItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    excerpt = scrapy.Field()
    question = scrapy.Field()
