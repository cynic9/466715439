# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem


class Cuiyu1Pipeline(object):
    def __init__(self, path):
        self.f = None
        self.path = path

    @classmethod
    def from_crawler(cls, crawler):
        path = crawler.settings.get('HREF_FILE_PATH')  # 从所有配置文件中找
        return cls(path)

    def open_spider(self,spider):
        # 不同的爬虫选择不同的操作
        # if spider.name == 'chouti':
        self.f = open(self.path, mode='a+', encoding='utf-8')

    def process_item(self, item, spider):
        self.f.write(item['href']+'\n')
        return item  # 值返回给下一个类的process_item
        # raise DropItem()  # 不想让下面处理，抛出异常

    def close_spider(self, spider):
        self.f.close()


# class Cuiyu2Pipeline(object):
#     def __init__(self, path):
#         self.f = None
#         self.path = path
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         path = crawler.settings.get('HREF_FILE_PATH')  # 从所有配置文件中找
#         return cls(path)
#
#     def open_spider(self,spider):
#         self.f = open(self.path, mode='a+', encoding='utf-8')
#
#     def process_item(self, item, spider):
#         self.f.write(item['href']+'\n')
#         return item
#
#     def close_spider(self, spider):
#         self.f.close()
