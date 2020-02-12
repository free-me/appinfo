#!/usr/bin
#_*_encoding:utf-8 _*_
import scrapy
import json
from appinfo.appstorItem import qihustoryItem

class yybappinfo(scrapy.Spider):
# 应用宝网站数据获取

	name = "yybappinfo1"
	start_urls = [
	'https://sj.qq.com/myapp/searchAjax.htm?kw=%E5%8F%91%E7%A5%A8%E3%80%81&pns=MTA=&sid=0',
	'https://sj.qq.com/myapp/searchAjax.htm?kw=%E5%8F%91%E7%A5%A8%E3%80%81&pns=MjA=&sid=0',
	'https://sj.qq.com/myapp/searchAjax.htm?kw=%E5%8F%91%E7%A5%A8%E3%80%81&pns=MzA=&sid=0',
	'https://sj.qq.com/myapp/searchAjax.htm?kw=%E5%8F%91%E7%A5%A8%E3%80%81&pns=NDA=&sid=0']

	#写文件
	


	def parse(self,response):
		#json请求地址：
		#https://sj.qq.com/myapp/searchAjax.htm?kw=%E5%8F%91%E7%A5%A8%E3%80%81&pns=MTA=&sid=0
		#https://sj.qq.com/myapp/searchAjax.htm?kw=%E5%8F%91%E7%A5%A8%E3%80%81&pns=MjA=&sid=0
		#https://sj.qq.com/myapp/searchAjax.htm?kw=%E5%8F%91%E7%A5%A8%E3%80%81&pns=MzA=&sid=0
		#https://sj.qq.com/myapp/searchAjax.htm?kw=%E5%8F%91%E7%A5%A8%E3%80%81&pns=NDA=&sid=0
		js = json.loads(response.body)
		item = qihustoryItem()
		appSo ='应用宝网站数据获取'
		appList =  js['obj']['appDetails']
		for ite in appList:
			item['appname'] = ite['appName']
			item['author'] = ite['authorName']
			item['version'] = ite['versionName']
			item['fileSize'] = ite['fileSize']
			item['downCount'] = ite['appDownCount']
			item['description'] = ite['description']
			item['downUrl'] = ite['apkUrl']
			item['channel'] = response.xpath('//title/text()').extract_first()
			yield item
			# with open('yyb.txt','a+',encoding='utf8') as f:
			# 	msg ='---------------------appinfo-------------------------------\n'
			# 	msg = '应用名称：'+appName+'\t'+'发布者'+authorName+'\t'+versionName+'\t'+'应用大小：'+str(fileSize)+'\t'+'下载量：'+str(appDownCount)+'\t'+'功能介绍：'+description+'\t'+'下载链接：'+apkUrl+'\n'
			# 	f.write('===================================应用信息分割线===================================\n')
			# 	f.write(msg)
			# print('='*300)

			#print(appName+authorName+versionName+fileSize+appDownCount+description+apkUrl)
			
			

