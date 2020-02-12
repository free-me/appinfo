#!/usr/bin
#_*_encoding:utf-8 _*_

import scrapy
from appinfo.appstorItem import qihustoryItem

class bdAppStor(scrapy.Spider):
	name = 'badustor'
	start_urls =[
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page2',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page3',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page4',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page5',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page6',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page7',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page8',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page9',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page10',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page11',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page12',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page13',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page14',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page15',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page16',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page17',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page18',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page19',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page20',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page21',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page22',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page23',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page24',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page25',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page26',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page27',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page28',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page29',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page30',
	'https://shouji.baidu.com/s?wd=%E5%8F%91%E7%A5%A8&data_type=app&f=header_all%40input#page31']

	def parse(self, response):
		item = qihustoryItem()
		applist=response.css('.app')		 
		for app in applist:
			appd = app.css('.little-install')
			for info in appd:
				item['appname'] = info.css('a::attr(data_name)').extract_first()
				print(item['appname'])
				item['version'] = info.css('a::attr(data_versionname)').extract_first()
				item['fileSize'] = info.css('a::attr(data_size)').extract_first()
				item['author'] = info.css('a::attr(data_from)').extract_first()
				item['downUrl'] =  info.css('a::attr(data_url)').extract_first()
			downCount = app.css('.size').extract_first()
			item['downCount'] = downCount[downCount.find('">')+2:-7]
			item['description'] = app.css('.brief::text').extract_first()
			item['channel'] =  response.xpath('//title/text()').extract_first()
			yield item
			# with open('baiduappstor.txt','a+',encoding='utf8') as f:
			# 	msg= '应用名称：'+appname+'\t'+'发布者'+author+'\t'+version+'\t'+'应用大小：'+filesize+'\t'+'下载量：'+downCount+'\t'+'功能介绍：'+description+'\t'+'下载链接：'+downUrl+'\n'
			# 	f.write('===================================应用信息分割线===================================\n')
			# 	f.write(msg)
			# 	f.close()



				

