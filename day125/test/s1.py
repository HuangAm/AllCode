import tornado.ioloop
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        url1 = self.application.reverse_url('n1')
        print(url1)
        url2 = self.application.reverse_url('n2',666)
        print(url2)
        self.write("Hello,World")


class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello,world")


application = tornado.web.Application([
    (r"/index",IndexHandler,{},"n1"),
    (r"/home/(\d+)",HomeHandler,{},'n2')
])
if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()