# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
# import sys,os,io
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
import scrapy
from scrapy.http.cookies import CookieJar
from scrapy.http import Request
from urllib.parse import urlencode

class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['https://dig.chouti.com/']
    cookie_dict = {}
    def parse(self, response):
        """
        第一次访问抽屉返回的内容：response
        :param response:
        :return:
        """

        # 去响应头中获取cookie


        # 去响应头中获取cookie，cookie保存在cookie_jar对象
        cookie_jar = CookieJar()
        cookie_jar.extract_cookies(response, response.request)

        # 去对象中将cookie解析到字典
        for k, v in cookie_jar._cookies.items():
            for i, j in v.items():
                for m, n in j.items():
                    self.cookie_dict[m] = n.value

        yield Request(
            url='https://dig.chouti.com/login',
            method='POST',
            body="phone=8613121758648&password=woshiniba&oneMonth=1",# # body=urlencode({})"phone=8615131255555&password=12sdf32sdf&oneMonth=1"
            cookies=self.cookie_dict,
            headers={
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            },
            callback=self.check_login
        )

    def check_login(self,response):
        print(response.text)

        yield Request(
            url='https://dig.chouti.com/all/hot/recent/1',
            cookies=self.cookie_dict,
            callback=self.index
        )

    def index(self,response):
        news_list = response.xpath('//div[@id="content-list"]/div[@class="item"]')
        for new in news_list:
            link_id = new.xpath('.//div[@class="part2"]/@share-linkid').extract_first()
            yield Request(
                url='http://dig.chouti.com/link/vote?linksId=%s' % (link_id,),
                method='POST',
                cookies=self.cookie_dict,
                callback=self.check_result
            )

        page_list = response.xpath('//div[@id="dig_lcpage"]//a/@href').extract()
        for page in page_list:
            page = "https://dig.chouti.com" + page
            yield Request(url=page, callback=self.index)  # https://dig.chouti.com/all/hot/recent/2

    def check_result(self, response):
        print(response.text)

