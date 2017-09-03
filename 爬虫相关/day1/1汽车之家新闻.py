# import requests
# from bs4 import BeautifulSoup
# #pip3 install requests
# #pip3 install BeautifulSoup4
# response = requests.get('http://www.autohome.com.cn/news/')
# response.encoding = 'gbk'
# soup = BeautifulSoup(response.text,'html.parser')
# tag = soup.find(id='auto-channel-lazyload-article')
# h3 = tag.find(name='h3')
# print(h3)
#
# from bs4 import BeautifulSoup
# response = requests.get('http://www.autohome.com.cn/news/')
# response.encoding = 'gbk'
# soup = BeautifulSoup(response.text,'html.parser')
# tag = soup.find(id='auto-channel-lazyload-article')
# h3 = tag.find(name='h3')
# print(h3)
#
# from bs4 import BeautifulSoup
# response = requests.get('http://www.autohome.com.cn/news/')
# response.encoding = 'gbk'
# soup = BeautifulSoup(response.text,'html.parser')
# tag = soup.find(id='auto-channel-lazyload-article')
# h3 = tag.find(name='h3')
# print(h3)
#
# from bs4 import BeautifulSoup
# response = requests.get('http://www.autohome.com.cn/news/')
# response.encoding = 'gbk'
# soup = BeautifulSoup(response.text,'html.parser') #'html.parser'专门解析html标签用的  parser:解析器
# tag = soup.find(id='auto-channel-lazyload-article')
# h3 = tag.find(name='h3')
# print(h3)

# import requests
# from bs4 import BeautifulSoup
# response = requests.get('http://www.autohome.com.cn/news/')#response默认是字节形式的
# response.encoding = 'gbk' #response.text是字符串格式,response.content是字节形式
# soup = BeautifulSoup(response.text,'html.parser') #实例化出标签对象
# tag = soup.find(id='auto-channel-lazyload-article') #find找到第一个标签
# h3 = tag.find(name='h3') #找到第一个h3标签
# print(h3)

import requests
from bs4 import BeautifulSoup
# response = requests.get('http://www.autohome.com.cn/news/')
# response.encoding='gbk'
# soup = BeautifulSoup(response.text,'html.parser')
# li_list = soup.find(id='auto-channel-lazyload-article').find_all('li')
# for li in li_list:
#     title = li.find('h3')
#     if not title:
#         continue
#     print(title.text)
#     summary = li.find('p').text
#     #li.find('a').attrs获取a标签的所有属性
#     url = li.find('a').get('href') #只获取a标签的href属性
#     img = li.find('img').get('src')
#     print(title.text,url,summary,img)
#     import re
#     img_name = re.split("/*",img).pop()
#     print(img_name)

response = requests.get('http://wx4.sinaimg.cn/mw600/8ae91e74gy1fj6iu9269ej21kw16odvs.jpg')
print(response.content)
with open("bb.jpg",'wb+')as f:
    f.write(response.content)