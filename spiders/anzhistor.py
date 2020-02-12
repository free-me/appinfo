#!/usr/bin
#_*_encoding:utf-8 _*_
#用于爬取安智市场指定应用

import scrapy
from appinfo.appstorItem import qihustoryItem

class AZstor(scrapy.Spider):
	name = 'azstor'
	start_urls = [
				   'http://www.anzhi.com/search.php?keyword=%E5%8F%91%E7%A5%A8',
				   'http://www.anzhi.com/search.php?keyword=%E5%8F%91%E7%A5%A8&page=2',
				   'http://www.anzhi.com/search.php?keyword=%E5%8F%91%E7%A5%A8&page=3',
				   'http://www.anzhi.com/search.php?keyword=%E5%8F%91%E7%A5%A8&page=4',
				   'http://www.anzhi.com/search.php?keyword=%E5%8F%91%E7%A5%A8&page=5',
				   'http://www.anzhi.com/search.php?keyword=%E5%8F%91%E7%A5%A8&page=6',
				   'http://www.anzhi.com/search.php?keyword=%E5%8F%91%E7%A5%A8&page=7',
				   'http://www.anzhi.com/search.php?keyword=%E5%8F%91%E7%A5%A8&page=8',
				   'http://www.anzhi.com/search.php?keyword=%E5%8F%91%E7%A5%A8&page=9',
				   'http://www.anzhi.com/search.php?keyword=%E5%8F%91%E7%A5%A8&page=10',
				   'http://www.anzhi.com/search.php?keyword=%E5%8F%91%E7%A5%A8&page=11',
				   'http://www.anzhi.com/search.php?keyword=%E5%8F%91%E7%A5%A8&page=12',
				   'http://www.anzhi.com/search.php?keyword=%E5%8F%91%E7%A5%A8&page=13',
				   'http://www.anzhi.com/search.php?keyword=%E5%8F%91%E7%A5%A8&page=14',
				   'http://www.anzhi.com/search.php?keyword=%E5%8F%91%E7%A5%A8&page=15']
	tempUrls = []

	def parse(self,response):
		tmpD = response.css('.app_list')
		urlList = tmpD.css('.app_name a::attr(href)').extract()
		for url in urlList:
			self.tempUrls.append(url)

		for url in self.tempUrls:
			fullUrl = response.urljoin(url)
			yield scrapy.Request(url=fullUrl,callback=self.parse2)

	def parse2(self,response):
		item = qihustoryItem()
		item['appname'] = response.css('.detail_line h3').extract_first()[4:-5]
		tempD = response.css('.detail_description')
		tempD = tempD.extract_first()
		authorD = tempD[tempD.find('作者：'):]
		item['author'] = authorD[:authorD.find('</')]
		tempV = response.css('.app_detail_version').extract_first()
		item['version'] = '版本号：' + tempV[tempV.find('">(')+3:tempV.find(')</span')]
		tempSi = tempD[tempD.find('大小')+3:]
		item['fileSize'] = tempSi[:tempSi.find('</span')]
		tempTime = tempD[tempD.find('时间')+3:]
		item['dataTime'] = tempTime[:tempTime.find('</li')]
		tempCount = tempD[tempD.find('下载')+3:]
		item['downCount'] = tempCount[:tempCount.find('</span>')]
		tempDesc = response.css('.app_detail_infor').extract_first()
		item['description'] = tempDesc[tempDesc.find('<p>')+11:-16]
		#下载链接地址格式
		#http://www.anzhi.com/dl_app.php?s=3091483&n=5
		tempID = response.css('.detail_down').extract_first()
		id = tempID[tempID.find('opendown')+9:tempID.find(')')]
		downUrl = 'http://www.anzhi.com/dl_app.php?s=ID&n=5'
		item['downUrl'] = downUrl.replace('ID',str(id))
		item['channel'] = response.xpath('//title/text()').extract_first()
		yield item
		# print(appname)
		# with open('anzhistor.txt','a+',encoding='utf8') as f:
		# 	msg= '应用名称：'+appname+'\t'+'发布者'+author+'\t'+version+'\t'+'应用大小：'+filesize+'\t'+'发布时间'+dataTime+'\t'+'下载量：'+downCount+'\t'+'功能介绍：'+description+'\t'+'下载链接：'+downUrl+'\n'
		# 	f.write('===================================应用信息分割线===================================\n')
		# 	f.write(msg)
		# 	f.close()



