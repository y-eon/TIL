### 텍스트 마이닝 논문 구현

###### - 한 날짜의 네이버 뉴스 url 갖고오기

```
import re
import scrapy
from naver_crawler.items import NaverCrawlerItem
class NaverSpider(scrapy.Spider):
    name = "naver"

    def start_requests(self):
        for date
        start_urls = 'https://search.naver.com/search.naver?&where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_pge&sort=1&photo=0&field=0&reporter_article=&pd=3&ds=2020.07.15&de=2020.07.15&docid=&nso=so:dd,p:from20200715to20200715,a:all&mynews=0&start=1&refresh_start=0'
        yield scrapy.Request(url = start_urls,callback = self.total_page)
    
    def total_page(self, response):
        text = response.xpath('//*[@id="main_pack"]/div[2]/div[1]/div[1]/span/text()').get()
        txt = re.sub(",","",(re.findall('/ ([0-9,]+)건',text)[0]))
        length = (int(txt) // 10) + 1
        for i in range(length):
            yield scrapy.Request('https://search.naver.com/search.naver?&where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_pge&sort=1&photo=0&field=0&reporter_article=&pd=3&ds=2020.07.15&de=2020.07.15&docid=&nso=so:dd,p:from20200715to20200715,a:all&mynews=0&start={}&refresh_start=0'.format(i*10+1),
            self.parse_url)
    
    def parse_url(self, response):
        item = NaverCrawlerItem()
        item['url'] =  response.xpath('//*/dl/dt/a/@href').extract()
        yield item
```

###### - 날짜마다 모든 url 갖고오기 + 쿠키(연합, 연합인포맥스, 이데일리) 설정

```
import re
import scrapy
import pandas as pd
import datetime
import time
from naver_crawler.items import NaverCrawlerItem
class NaverSpider(scrapy.Spider):
    name = "naver"

    def start_requests(self):
        start_urls = 'https://search.naver.com/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=2005.01.01&de=2005.01.01&docid=&nso=so%3Ar%2Cp%3Afrom20050101to20050101%2Ca%3Aall&mynews=0&refresh_start=0&related=0'
        yield scrapy.Request(url = start_urls,callback = self.chg_date)

    def chg_date(self, response):
        for term in range(0, 3): #총 4748개
            date = (datetime.date(2020, 7, 15) + datetime.timedelta(+term)).strftime('%Y%m%d')
            date_dot = (datetime.date(2020, 7, 15) + datetime.timedelta(+term)).strftime('%Y.%m.%d')
            url = 'https://search.naver.com/search.naver?&where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_pge&sort=1&photo=0&field=0&reporter_article=&pd=3&ds={0}&de={0}&docid=&nso=so:dd,p:from{1}to{1},a:all&mynews=0&start=1&refresh_start=0'.format(date_dot, date)
            yield scrapy.Request(url = url,callback = self.total_page)

    def total_page(self, response):
        text = response.xpath('//*[@id="main_pack"]/div[2]/div[1]/div[1]/span/text()').get()
        txt = re.sub(",","",(re.findall('/ ([0-9,]+)건',text)[0]))
        length = (int(txt) // 10) + 1
        for term in range(0, 3):
                # datetime을 이용한 특정 기간 출력 (20170417 ~ 20170509)
            date = (datetime.date(2020, 7, 15) + datetime.timedelta(+term)).strftime('%Y%m%d')
            date_dot = (datetime.date(2020, 7, 15) + datetime.timedelta(+term)).strftime('%Y.%m.%d')
            for i in range(length):
                yield scrapy.Request('https://search.naver.com/search.naver?&where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=3&ds={0}&de={0}&docid=&nso=so:r,p:from{1}to{1},a:all&mynews=0&cluster_rank=29&start={2}&refresh_start=0'.format(date_dot,date,i*10+1),
                self.parse_url)
    
    def parse_url(self, response):
        item = NaverCrawlerItem()
        item['url'] =  response.xpath('//*/dl/dt/a/@href').extract()
        yield item
```

###### - 연합인포맥스, 이데일리, 연합뉴스대로 url 따로 받기(진행중)

```
import re
import scrapy
import pandas as pd
import datetime
import time
from naver_crawler.items import NaverCrawlerItem
class NaverSpider(scrapy.Spider):
    name = "naver"

    def start_requests(self):
        start_urls = 'https://search.naver.com/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=2005.01.01&de=2005.01.01&docid=&nso=so%3Ar%2Cp%3Afrom20050101to20050101%2Ca%3Aall&mynews=0&refresh_start=0&related=0'
        yield scrapy.Request(url = start_urls, cookies={'news_office_checked':'1001,1018,2227'}, callback = self.chg_date)

    def chg_date(self, response):
        for term in range(0, 1): #총 4748개
            date = (datetime.date(2020, 7, 15) + datetime.timedelta(+term)).strftime('%Y%m%d')
            date_dot = (datetime.date(2020, 7, 15) + datetime.timedelta(+term)).strftime('%Y.%m.%d')
            url = 'https://search.naver.com/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds={0}&de={0}&docid=&nso=so%3Ar%2Cp%3Afrom{1}to{1}%2Ca%3Aall&mynews=1&refresh_start=0&related=0'.format(date_dot, date)
            yield scrapy.Request(url = url,cookies={'news_office_checked':'1001,1018,2227'}, callback = self.total_page)

    def total_page(self, response):
        text = response.xpath('//*[@id="main_pack"]/div[2]/div[1]/div[1]/span/text()').get()
        txt = re.sub(",","",(re.findall('/ ([0-9,]+)건',text)[0]))
        length = (int(txt) // 10) + 1
        for term in range(0, 1):
            date = (datetime.date(2020, 7, 15) + datetime.timedelta(+term)).strftime('%Y%m%d')
            date_dot = (datetime.date(2020, 7, 15) + datetime.timedelta(+term)).strftime('%Y.%m.%d')
            for i in range(length):
                news_urls = 'https://search.naver.com/search.naver?&where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=3&ds={0}&de={0}&docid=&nso=so:r,p:from{1}to{1},a:all&mynews=0&cluster_rank=29&start={2}&refresh_start=0'.format(date_dot,date,i*10+1)
                yield scrapy.Request(url = news_urls,cookies={'news_office_checked':'1001,1018,2227'}, callback=self.news_name)

    def news_name(self, response):
        li_list = response.xpath('//*[@id="main_pack"]/div[2]/ul/li')
        for i in li_list:
            x = i.xpath('./dl/dd[1]/span[1]/text()').get()
            print('-------------------------------------------------------------------------------------')
            print(x)
            print('-------------------------------------------------------------------------------------')


    def parse_url(self, response):
        item = NaverCrawlerItem()
        item['url'] = response.xpath('//*[@id="main_pack"]/div[2]/ul/li/dl/dt/a/@href').extract()
        yield item
```

