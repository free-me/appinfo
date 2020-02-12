#!/usr/bin
#_*_encoding:utf-8 _*_

import scrapy
from appinfo.appstorItem import qihustoryItem

class xiaomistor(scrapy.Spider):
	name = 'xiaomistor'
	start_urls=['http://app.mi.com/search?keywords=%E5%8F%91%E7%A5%A8']
	tempUrls = []

	def parse(self,response):
		tempData = response.css('.applist')
		appinfo =tempData.css('li h5')
		for temU in appinfo.css('a::attr(href)').extract():
			self.tempUrls.append(temU)
		#self.tempUrl.append(appinfo.css('a::attr(href)').extract())

		for url in self.tempUrls:
			fullUrl = response.urljoin(url)
			yield scrapy.Request(url=fullUrl,callback=self.parse2)

	def parse2(self,response):
		item = qihustoryItem()
		item['appname'] =response.css('.intro-titles h3').extract_first()[4:-5]
		item['author'] = response.css('.intro-titles p').extract_first()[3:-4]
		versionD = response.css('.look-detail')
		versionD = versionD.css('.weight-font')
		datainfo = versionD.xpath('//li').extract()
		versionD = ''.join(datainfo)
		tmp = versionD[versionD.find('版本号')+13:]
		version = tmp[:tmp.find('</li>')]
		item['version'] = '应用版本：'+version
		filesizetemp = versionD[versionD.find('软件大小')+14:]		
		item['fileSize'] = filesizetemp[:filesizetemp.find('</li>')]
		tmpD = versionD[versionD.find('更新时间')+14:]
		item['dataTime'] = tmpD[:tmpD.find('</li')]
		descriptionTmp = response.css('.app-text')
		descriptionTmp = descriptionTmp.css('.pslide')
		description = descriptionTmp.css('.pslide').extract_first()
		item['description'] = description[description.find('">')+2:]
		downUrl = response.css('.download::attr(href)').extract_first()
		item['downUrl'] = response.urljoin(downUrl)
		item['channel'] = response.xpath('//title/text()').extract_first()

		print(item['appname'])
		yield item
		# with open('xiaomiappstor1.txt','a+',encoding='utf8') as f:
		# 	msg= '应用名称：'+appname+'\t'+'发布者：'+author+'\t'+version+'\t'+'应用大小：'+filesize+'\t'+'发布时间：'+dataTime+'\t'+'功能介绍：'+description+'\t'+'下载链接：'+downUrl+'\n'
		# 	f.write('===================================应用信息分割线===================================\n')
		# 	f.write(msg)
		# 	f.close()







