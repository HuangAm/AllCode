#作业一
# import time
# def cat(file_path):
#     with open("a.txt",encoding="utf8") as f:
#         f.seek(0,2)
#         line=f.readline()
#         while True:
#             if not line :
#                 time.sleep(0.5)
#                 continue
#             else:
#                 yield line.strip()
# def grep(word,g):
#     for line in g:
#         if word in line :
#             yield line.strip()
#
# g1=cat("/tmp/a.txt")
# g2=grep("apple",g1)
#
# for i in g2:
#     print(i)

#作业二
# from urllib.request import urlopen
# def get(url):
#     def index():
#         while True:
#             return urlopen(url).read()
#     return index
#
#
# from urllib.request import urlopen
# def index(*args,**kwargs):
#     while True:
#         url=yield
#         print(urlopen(url).read())
# g=index()
# next(g)
# g.send("http://www.python.org")
#
#
# from urllib.request import urlopen
# def get(url):
#     def index():
#         while True:
#             yield urlopen(url).read()
#             # print(urlopen(url).read())
#     yield url
# g=get(index())
# g.send(url)
#
# from urllib.request import urlopen
# def get(url):
#     def index():
#         while True:
#             return urlopen(url).read()
#     return index















