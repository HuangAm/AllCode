# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import json


class Sp2Pipeline(object):
    def __init__(self,v=None):
        self.f = None

    def process_item(self, item, spider):
        """

        :param item:yield后面的item对象
        :param spider:爬虫对象spiders中的脚本中的类的对象
        :return:
        """
        print('='*30)
        print(item)
        return item

    @classmethod
    def from_crawler(cls,crawler):
        """
        初始化时候，用于创建pipeline对象
        :param crawler:
        :return:
        """
        val = crawler.settings.get("MMMM")
        print('执行pipeline的from_crawler,进行实例化对象')
        return cls()

    def open_spider(self,spiders):
        """
        爬虫开始执行时,调用
        :param spiders:
        :return:
        """
        print('打开爬虫')
        self.f = open('a.log','a+')

    def close_spider(self,spider):
        """
        爬虫关闭时,被调用
        :param spider:
        :return:
        """
        print("关闭爬虫")
        self.f.close()

class Sp2Pipeline1(object): #pipeline是全局生效的,所有的爬虫都会执行
    def __init__(self,v=None):
        self.f = None

    def process_item(self, item, spider):
        """

        :param item:yield后面的item对象
        :param spider:爬虫对象spiders中的脚本中的类的对象
        :return:
        """
        # if spider.name == "jandan":
        #     print("专门为jandan定制的,其他的爬虫不能执行")
        # print(type(item))
        # print(item['url'])
        # print(type(item['url']))
        # # self.f.write("hello world!")
        # self.f.write(item['url'])
        # v = json.dumps(dict(item), ensure_ascii=False)

        self.f.write(str(item)+'\r\n')
        # return item #将item传给下一个pipeline的process_item方法
        raise DropItem() #写上他下一个pipeline的process_item就不会再执行了

    @classmethod
    def from_crawler(cls,crawler):
        """
        初始化时候，用于创建pipeline对象
        :param crawler:
        :return:
        """
        #val = crawler.settings.get("MMMM")
        print('执行pipeline11111的from_crawler,进行实例化对象')
        return cls()

    def open_spider(self,spiders):
        """
        爬虫开始执行时,调用
        :param spiders:
        :return:
        """
        print('打开爬虫1111')
        self.f = open('a.log','w+',encoding='utf-8')

    def close_spider(self,spider):
        """
        爬虫关闭时,被调用
        :param spider:
        :return:
        """
        print("关闭爬虫1111")
        self.f.close()