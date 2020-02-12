import scrapy
import os
class cnvddong(scrapy.Spider):
    name = 'cnvdloudong'
    start_urls = [
        'https://www.cnvd.org.cn/flaw/list.htm',
    ]

    def parse(self, response):
        print('=================================================================')
        os.sleep(40)
