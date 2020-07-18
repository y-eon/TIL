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



