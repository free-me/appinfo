#!/usr/bin
#_*_encoding:utf-8

import scrapy
import re
from appinfo.appstorItem import qihustoryItem
class qihappinfo(scrapy.Spider):
	name = '360appfino'
	start_urls = [
	'http://zhushou.360.cn/search/index/?kw=%E5%8F%91%E7%A5%A8',
	'http://zhushou.360.cn/search/index/?kw=%E5%8F%91%E7%A5%A8&page=2',
	'http://zhushou.360.cn/search/index/?kw=%E5%8F%91%E7%A5%A8&page=3',
	'http://zhushou.360.cn/search/index/?kw=%E5%8F%91%E7%A5%A8&page=4',
	'http://zhushou.360.cn/search/index/?kw=%E5%8F%91%E7%A5%A8&page=5']
	urls =[]
	pageNum=1

	def parse(self,response):
		applistUrl= response.css('li')
		#self.urls.append(applistUrl.xpath('//h3/a/@href').extract())
		#print(applistUrl)
		addurl=applistUrl.xpath('//h3/a/@href').extract()
		print(addurl)
		for i in addurl:
			print(i)
			self.urls.append(i)
		for i in self.urls:
			print('self.urls==>'+i)
		print(len(self.urls))
		for url in self.urls:
			full_url = response.urljoin(url)
			yield scrapy.Request(url=full_url,callback=self.parse2)
		
	def parse2(self,response):
		item = qihustoryItem()
		appinfo = response.css('dl')
		authorData = response.xpath('//td').extract()[0]
		#author = re.search('/strong>.*</td>',auth[0]).group()
		#author =authorData[authorData.find('/strong>')+8:-5]
		item['author'] = authorData[authorData.find('/strong>')+8:-5]
		appname = response.css('title').extract()[0]
		#appname = appname[0]
		item['appname'] = appname[7:-16]
		version = response.xpath('//td')[2].extract()
		item['version']= '版本号：'+version[24:version.find('<!')]
		numdata = response.css('.s-3').extract()
		filesize = numdata[1]
		filesize = filesize[filesize.find('">')+2:filesize.find('</')]
		dataTime = response.xpath('//td').extract()[1]
		temp = dataTime[dataTime.find('strong>')+7:dataTime.find('strong>')+7+5]
		item['dataTime'] = temp + dataTime[dataTime.find('/strong>')+8:-5]
		downCount = numdata[0]
		item['downCount'] = downCount[downCount.find('">')+2:-7]
		description = response.css('.breif').extract()[0]
		item['description'] = description[description.find('breif">')+20:description.find('<div class="base-info')]
		downUrl = response.css('.js-downLog::attr(href)').extract()[0]
		item['downUrl'] = downUrl[downUrl.find('url=')+4:]
		item['channel'] =  response.xpath('//title/text()').extract_first()
		print(item['appname'])
		yield item
		# with open('360appstor.txt','a+',encoding='utf8') as f:
		# 	msg= '应用名称：'+appname+'\t'+'发布者'+author+'\t'+version+'\t'+'应用大小：'+filesize+'\t'+'发布时间'+dataTime+'\t'+'下载量：'+downCount+'\t'+'功能介绍：'+description+'\t'+'下载链接：'+downUrl+'\n'
		# 	f.write('===================================应用信息分割线===================================\n')
		# 	f.write(msg)
		# 	f.close()












