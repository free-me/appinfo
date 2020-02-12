#!/usr/bin/env python
#_*_encoding:utf-8

import scrapy

class meizustor(scrapy.Spider):
    name = 'meizustor'
    start_urls = ['http://app.meizu.com/apps/public/search?keyword=%E5%8F%91%E7%A5%A8']

    def parse(self,response):
        pass