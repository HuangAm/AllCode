# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.http.cookies import CookieJar
from scrapy.selector import Selector


class ChoutiSpider(scrapy.Spider):
    """
    抽屉自动登录点赞
    """
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['http://chouti.com/'] #起始url,把他封装成一个request对象放到调度器里面
    cookie_dict = {}

    def start_requests(self): #自定制起始url
        for url in self.start_urls:
            yield Request(url,dont_filter=True,callback=self.parse1)

    def parse1(self, response):
        cookie_jar = CookieJar() #对象,中封装了cookies
        cookie_jar.extract_cookies(response,response.request) #去响应中获取cookie
        # cookie_dict = {}
        for k,v in cookie_jar._cookies.items():
            for i,j in v.items():
                for m,n in j.items():
                    self.cookie_dict[m] = n.value
        post_dict = {
            'phone':8617602112290,
            'password':'woshiniba',
            'oneMonth':1
        }
        import urllib.parse
        yield Request(
            url='http://dig.chouti.com/login',
            cookies=self.cookie_dict,
            body=urllib.parse.urlencode(post_dict),
            method='POST',
            headers={'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'},
            callback=self.parse2
        )

    def parse2(self,response):
        # print(response.text)
        #获取新闻列表
        yield Request(url='http://dig.chouti.com/',cookies=self.cookie_dict,callback=self.parse3)

    def parse3(self,response):
        hxs = Selector(response)
        linkId_list = hxs.xpath('//div[@class="part2"]/@share-linkid').extract()
        # print(linkId_list)
        for linkId in linkId_list:
            #获取每一个id去点赞
            base_url = "http://dig.chouti.com/link/vote?linksId=%s" %(linkId)
            yield Request(url=base_url,method='POST',cookies=self.cookie_dict,callback=self.parse4)
        page_list = hxs.xpath('//div[@id="dig_lcpage"]//a/@href').extract()
        # print(page_list)
        for page in page_list:
            page_url = "http://dig.chouti.com%s" %(page)
            yield Request(url=page_url,method='GET',callback=self.parse3)

    def parse4(self,response):
        print(response.text)



# import scrapy
# from scrapy.http import Request
# from scrapy.selector import Selector
#
#
# class ChoutiSpider(scrapy.Spider):
#     name = 'chouti'
#     allowed_domains = ['chouti.com']
#     start_urls = ['http://chouti.com/']
#     cookie_dict = {}
#     """
#     1. 发送一个GET请求,抽屉
#        获取cookie
#
#     2. 用户密码POST登录：携带上一次cookie
#        返回值：9999
#
#     3. 为所欲为，携带cookie
# 	"""
#
#     def start_requests(self):
#         for url in self.start_urls:
#             yield Request(url, dont_filter=True, callback=self.parse1)
#
#     def parse1(self, response):
#         # response.text 首页所有内容
#         from scrapy.http.cookies import CookieJar
#         cookie_jar = CookieJar()  # 对象，中封装了 cookies
#         cookie_jar.extract_cookies(response, response.request)  # 去响应中获取cookies
#
#         for k, v in cookie_jar._cookies.items():
#             for i, j in v.items():
#                 for m, n in j.items():
#                     self.cookie_dict[m] = n.value
#         post_dict = {
#             'phone': '8615131255089',
#             'password': 'woshiniba',
#             'oneMonth': 1,
#         }
#         import urllib.parse
#
#         # 目的：发送POST进行登录
#         yield Request(
#             url="http://dig.chouti.com/login",
#             method='POST',
#             cookies=self.cookie_dict,
#             body=urllib.parse.urlencode(post_dict),
#             headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
#             callback=self.parse2
#         )
#
#     def parse2(self, response):
#         print(response.text)
#         # 获取新闻列表
#         yield Request(url='http://dig.chouti.com/', cookies=self.cookie_dict, callback=self.parse3)
#
#     def parse3(self, response):
#
#         # 找div，class=part2, 获取share-linkid
#         hxs = Selector(response)
#         link_id_list = hxs.xpath('//div[@class="part2"]/@share-linkid').extract()
#         print(link_id_list)
#         for link_id in link_id_list:
#             # 获取每一个ID去点赞
#             base_url = "http://dig.chouti.com/link/vote?linksId=%s" % (link_id,)
#             yield Request(url=base_url, method="POST", cookies=self.cookie_dict, callback=self.parse4)
#
#         page_list = hxs.xpath('//div[@id="dig_lcpage"]//a/@href').extract()
#         for page in page_list:
#             # http://dig.chouti.com/ /all/hot/recent/2
#             page_url = "http://dig.chouti.com%s" % (page,)
#             yield Request(url=page_url, method='GET', callback=self.parse3)
#
#     def parse4(self, response):
#         print(response.text)