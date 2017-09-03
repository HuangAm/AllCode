from scrapy import signals


class MyExtension:
    """
    自定义信号,使用时需要注册
    """
    def __init__(self,value):
        self.value = value

    @classmethod
    def from_crawler(cls,crawler):
        val = crawler.settings.getint('MMM')
        ext = cls(val)
        #在scrapy中注册信号：spider_opened
        #第一个参数ext.opened是触发信号时执行的函数
        crawler.signals.connect(ext.opened,signal=signals.spider_opened)
        #在scrapy中注册信号：spider_closed
        crawler.signals.connect(ext.closed,signal=signals.spider_closed)
        return ext

    def opened(self,spider):
        print('open')

    def closed(self,spider):
        print('close')
