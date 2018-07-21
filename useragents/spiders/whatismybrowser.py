# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from useragents.items import UserAgentItemLoader


class WhatismybrowserSpider(CrawlSpider):
    name = 'whatismybrowser'
    allowed_domains = ['developers.whatismybrowser.com']

    def __init__(self, category='software_name', *args, **kwargs):
        self.start_urls = [
            'https://developers.whatismybrowser.com/useragents/explore/%s/' % category
        ]
        self.rules = (
            Rule(LinkExtractor(allow=r'/%s/' % category, deny=r'order_by='),
                 callback='parse_item', follow=True),
        )
        super(WhatismybrowserSpider, self).__init__(*args, **kwargs)
        

    def parse_item(self, response):
        for selector in response.css('.content-base section .corset table tbody tr'):
            item = UserAgentItemLoader(selector=selector)
            item.add_css('useragent' , 'td:nth-child(1) a::text')
            item.add_css('version'   , 'td:nth-child(2)::text')
            item.add_css('os'        , 'td:nth-child(3)::text')
            item.add_css('hardware'  , 'td:nth-child(4)::text')
            item.add_css('popularity', 'td:nth-child(5)::text')
            yield item.load_item()
