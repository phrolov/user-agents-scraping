# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from useragents.items import UserAgentItemLoader


class WhatismybrowserSpider(CrawlSpider):
    name = 'whatismybrowser'
    allowed_domains = ['developers.whatismybrowser.com']
    start_urls = ['https://developers.whatismybrowser.com/useragents/explore/software_name/']

    rules = (
        Rule(LinkExtractor(allow=r'/software_name/', deny=r'order_by='), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        for selector in response.css('.content-base section .corset table tbody tr'):
            item = UserAgentItemLoader(selector=selector)
            item.add_css('useragent' , 'td:nth-child(1) a::text')
            item.add_css('version'   , 'td:nth-child(2)::text')
            item.add_css('os'        , 'td:nth-child(3)::text')
            item.add_css('hardware'  , 'td:nth-child(4)::text')
            item.add_css('popularity', 'td:nth-child(5)::text')
            yield item.load_item()
