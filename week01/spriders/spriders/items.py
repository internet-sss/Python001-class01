# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpridersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    moive_name = scrapy.Field()
    moive_type = scrapy.Field()
    moive_time = scrapy.Field()
