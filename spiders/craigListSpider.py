# -*- coding: utf-8 -*-
import scrapy


class CraigSpider(scrapy.Spider):
    name = 'craig'
    allowed_domains = ['craigslist.org']
    start_urls = ['http://craigslist.org/']

    def parse(self, response):
        pass
