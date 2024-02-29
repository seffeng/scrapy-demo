import scrapy

class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["www.test.com"]
    start_urls = ["https://www.test.com"]

    def parse(self, response):
        print(response.xpath('//title/text()').extract_first())
        ## 爬取下一页面
        #url = response.url
        #if url != None:
        #    yield scrapy.Request(url, self.parse)
        pass
