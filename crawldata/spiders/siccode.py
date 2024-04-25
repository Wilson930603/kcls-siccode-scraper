import scrapy,json,re,os,platform
from crawldata.functions import *
from datetime import datetime

class CrawlerSpider(scrapy.Spider):
    name = 'siccode'
    DATE_CRAWL=datetime.now().strftime('%Y-%m-%d')
    #custom_settings={'LOG_FILE':'./log/'+name+'_'+DATE_CRAWL+'.log'}
    if platform.system()=='Linux':
        URL='file:////' + os.getcwd()+'/scrapy.cfg'
    else:
        URL='file:///' + os.getcwd()+'/scrapy.cfg'
    def start_requests(self):
        yield scrapy.Request('https://siccode.com',callback=self.parse,dont_filter=True)
    def parse(self, response):
        Data=response.xpath('//div[@class="sic-code"]/dl//a/span/text()').getall()
        for rs in Data:
            rs=Get_Number(rs)
            if len(rs)>0:
                item={}
                item['Type']='SIC'
                item['Code']=rs
                yield(item)
        Data=response.xpath('//div[@class="naics-code"]/dl//a/span/text()').getall()
        for rs in Data:
            rs=Get_Number(rs)
            if len(rs)>0:
                item={}
                item['Type']='NAICS'
                item['Code']=rs
                yield(item)
        Data=response.xpath('//div[@class="naics-code"]/dl/dt/text()').getall()
        for rs in Data:
            if not '-' in rs and len(Get_Number(rs))>0 and Get_Number(rs)==str(rs).strip():
                item={}
                item['Type']='NAICS'
                item['Code']=rs
                yield(item)
