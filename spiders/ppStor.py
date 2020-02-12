#!/usr/bin/env python
#_*_encoding:utf-8 _*_

import scrapy
from appinfo.appstorItem import qihustoryItem

class ppstor(scrapy.Spider):
    name = 'ppstor'
    start_urls = ['https://www.25pp.com/android/search_app/%E5%8F%91%E7%A5%A8/']
    tempUrls = []

    def parse(self, response):
        data = response.css('li')
        for url in data.css('a ::attr(href)').extract():
            self.tempUrls.append(url)
        nextPageD = response.css('.page-wrap')
        nextPage = nextPageD.css('.page-next::attr(href)').extract_first()
        fullUrl = response.urljoin(nextPage)
        if(len(fullUrl)>4):
            yield scrapy.Request(url=fullUrl,callback=self.parse)

        for url in self.tempUrls:
            fullUrl = response.urljoin(url)
            yield scrapy.Request(url=fullUrl,callback=self.parse2)
    #应用信息提取
    def parse2(self,response):
        item = qihustoryItem()
        item['appname'] = response.css('.app-title::text').extract_first()
        appInfoD = response.css('.app-detail-info')
        versionInfo = appInfoD.css('.ellipsis strong').extract()[2]
        item['version'] = versionInfo[versionInfo.find('strong>')+7:versionInfo.find('</')]
        filesizeD = appInfoD.css('.ellipsis strong').extract()[1]
        item['fileSize'] = filesizeD[filesizeD.find('strong>')+7:filesizeD.find('</')]
        dateTimeD = appInfoD.css('.ellipsis strong').extract()[0]
        item['dataTime'] = dateTimeD[dateTimeD.find('strong>')+7:dateTimeD.find('</')]
        downCount = response.css('.app-downs::text').extract_first()
        item['downCount'] = downCount[:downCount.find('|')-3]
        descriptionD = response.css('.app-detail-intro').extract_first()
        item['description'] = descriptionD[descriptionD.find('">')+2:]
        downUrlD = response.css('.app-install')
        item['downUrl'] = downUrlD.css('a::attr(href)').extract()[1]
        item['channel'] = response.xpath('//title/text()').extract_first()
        print(item['appname'])

        yield item

        # with open('ppstor.txt', 'a+', encoding='utf8') as f:
        #     msg = '应用名称：' + appname + '\t' + '应用版本：'+version + '\t' + '应用大小：' + filesize + '\t' + '发布时间' + dateTime + '\t' + '下载量：' + downCount + '\t' + '功能介绍：' + description + '\t' + '下载链接：' + downUrl + '\n'
        #     f.write('===================================应用信息分割线===================================\n')
        #     f.write(msg)
        #     f.close()


