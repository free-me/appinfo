import scrapy
import requests
import os

class girlsky(scrapy.Spider):
    name = 'girlsky'
    start_urls = ['http://www.girlsky.cn/']
    navList = []


    #提取图片分组函数
    def parse(self, response):
        #获取图片分组
        for url in response.css('.ShowNav a::attr(href)').extract():
            self.navList.append(url)
        for url in self.navList:
            yield scrapy.Request(url=url,callback=self.images)
    def images(self,response):
        imageUrlList = response.css('.TypeList a::attr(href)').extract()
        for imageInfo in imageUrlList:
            yield scrapy.Request(url=imageInfo,callback=self.downImage)
        nexP = response.css('.NewPages li a::attr(href)').extract()[-2]
        fullU = response.urljoin(nexP)
        yield scrapy.Request(url=fullU,callback=self.images)
    #提取图片信息并下载
    def downImage(self,response):
        downUrl = response.css('.ImageBody img::attr(src)').extract_first()
        tags= response.css('.column a::text').extract_first()
        imagesTitle = response.css('.ArticleTitle h1::text').extract_first()
        imgsrc = response.css('.ImageBody img::attr(src)').extract_first()
        r = requests.get(imgsrc)

        filename = os.path.basename(imgsrc)
        print(filename)
        with open('down/'+filename, "wb") as code:
            code.write(r.content)
            code.close()
        print('============下载成功===============')
        nextPage =response.css('.NewPages li a::attr(href)').extract()[-1]
        fullUrl = response.urljoin(nextPage)
        yield scrapy.Request(url=fullUrl,callback=self.downImage)

