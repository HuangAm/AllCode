# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from ..items import Sp2Item


class JandanSpider(scrapy.Spider):
    name = 'jandan'
    allowed_domains = ['jandan.net']
    start_urls = ['http://jandan.net/']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url,dont_filter=True,callback=self.parse1)

    def parse1(self, response):
        hxs = Selector(response)
        tag_list = hxs.xpath('//div[@class="indexs"]/h2')
        for tag in tag_list:
            url = tag.xpath('./a/@href').extract_first()
            text = tag.xpath('./a/text()').extract_first()
            yield Sp2Item(url=url,text=text) #做结构化的
        # [@class="post f list-post"]
        # tag_list = hxs.xpath('//div[@id="content"]//div[contains(@class, "f")]/div[@class="thumbs_b"]//img/@src').extract()
        # print(tag_list)


