#!/usr/bin
#_*_encoding:utf-8 _*_

import scrapy
from appinfo.appstorItem import qihustoryItem

class liqustor(scrapy.Spider):
	name = 'liqustor1'
	start_urls= ['https://s.liqucn.com/s.php?words=%E5%8F%91%E7%A5%A8']
	tempUrl = []

	def parse(self,response):
		print('=========开始===========')
		tempd = response.css('.sear_app')
		tempU = tempd.xpath('//dl/dd/h3/a/@href').extract()
		for url in tempU:
			self.tempUrl.append(url)
		tempPage = response.css('.page a::attr(href)')
		tempU = tempPage.extract()[5]
		fullUrl = response.urljoin(tempU)
		if len(fullUrl)>10:
			yield scrapy.Request(url=fullUrl,callback=self.parse)
		#开始应用信息爬取
		for url in self.tempUrl:
			infoUrl = response.urljoin(url)
			yield scrapy.Request(url=infoUrl,callback=self.parse2)
	def parse2(self,response):
		item = qihustoryItem()
		tempD = response.css('.info_con')
		tempN = tempD.xpath('//h1').extract_first()
		item['appname'] = tempN[4:-5]
		author = tempD.xpath('//em')[4].extract()
		item['author'] = author[4:-5]
		tempData = response.css('.version_con')
		tempInfo = tempData.xpath('//dl/dd/p')[2].extract()
		version = tempInfo[tempInfo.find('版本')+3:]
		item['version'] = version[:version.find('<br')]
		filesize = tempInfo[tempInfo.find('大小')+3:]
		item['fileSize'] = filesize[:filesize.find('</')]
		tempTime = tempD.xpath('//em')[1].extract()
		item['dataTime'] = tempTime[4:-5]
		tmpCount = tempD.xpath('//em')[2].extract()
		item['downCount'] = tmpCount[4:-5]
		description = response.css('.game_txt').extract_first()
		item['description'] = description[28:-10]
		#下载url
		#https://count.liqucn.com/d.php?id=706758&urlos=android&from_type=web
		tempId = response.css('.version_btn a::attr(href)').extract()[0]
		Id = tempId[tempId.find('rj/')+3:-6]
		downUrl = 'https://count.liqucn.com/d.php?id=ID&urlos=android&from_type=web'
		downUrl.replace('ID',Id)
		item['downUrl']= downUrl
		item['channel'] = response.xpath('//title/text()').extract_first()
		yield item
		print(item['appname'])
		# item['downUrl']
		# with open('liqustor.txt','a+',encoding='utf8') as f:
		# 	msg= '应用名称：'+appname+'\t'+'发布者'+author+'\t'+version+'\t'+'应用大小：'+filesize+'\t'+'发布时间'+dataTime+'\t'+'下载量：'+downCount+'\t'+'功能介绍：'+description+'\t'+'下载链接：'+downUrl+'\n'
		# 	f.write('===================================应用信息分割线===================================\n')
		# 	f.write(msg)
		# 	f.close()








