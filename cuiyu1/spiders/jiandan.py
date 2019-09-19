# -*- coding: utf-8 -*-
import scrapy
from cuiyu1.items import Cuiyu1Item


class JiandanSpider(scrapy.Spider):
    name = 'jiandan'
    allowed_domains = ['jandan.net']
    start_urls = ['http://jandan.net/']
    i = 0
    def parse(self, response):
        # print(response.text)
        self.i += 1
        # f = open('news.log',mode='a+',encoding='utf-8')
        # content_list = response.xpath('//div[@id="content"]/div[@class="post f list-post"]')  # //表示当前页面的子子孙孙中找，/往孩子下面继续找
        print(response.request.url)
        # for item in content_list:
        #     text = item.xpath('.//a/text()').extract_first()
        #     href = item.xpath('.//a/@href').extract_first()
        #     print(href, text.strip())
        #     f.write(href+text.strip()+'\n')
        #     yield Cuiyu1Item(title=text, href=href)  # 实例化对象，返回两个值
        # f.close()

        # 寻找页码
        if self.i < 3:
            page = response.xpath('//div[@class="wp-pagenavi"]/a/@href').extract()[0]
            from scrapy.http import Request
            page = "http://jandan.net" + page  # 页码拼接
            yield Request(url=page, callback=self.parse)

        else:
            page = response.xpath('//div[@class="wp-pagenavi"]/a/@href').extract()[1]
            from scrapy.http import Request
            page = "http://jandan.net" + page  # 页码拼接
            yield Request(url=page, callback=self.parse)
