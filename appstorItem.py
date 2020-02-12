import scrapy

class qihustoryItem(scrapy.Item):
    appname = scrapy.Field()
    author = scrapy.Field()
    version = scrapy.Field()
    fileSize = scrapy.Field()
    dataTime = scrapy.Field()
    downCount = scrapy.Field()
    description = scrapy.Field()
    downUrl = scrapy.Field()
    channel = scrapy.Field()
    pass