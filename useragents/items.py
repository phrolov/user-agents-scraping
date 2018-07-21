# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose


class UserAgentItem(Item):
    useragent  = Field()
    version    = Field()
    os         = Field()
    hardware   = Field()
    popularity = Field()


class UserAgentItemLoader(ItemLoader):
    default_item_class       = UserAgentItem
    default_output_processor = TakeFirst()
