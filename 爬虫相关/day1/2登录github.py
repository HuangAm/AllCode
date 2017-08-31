# import requests
# from bs4 import BeautifulSoup
#
# #获取token
# r1 = requests.get('https://github.com/login')
# s1 = BeautifulSoup(r1.text,'html.parser')
# token = s1.find(name='input',attrs={'name':'authenticity_token'}).get('value') #获取token
# r1_cookie_dict = r1.cookies.get_dict()
# #github的认证模式是get请求的时候就给你cookie了,提交登录信息的时候要带上,所以这里要拿上
#
# #将用户名密码token发送到服务端,post
# """
# commit:Sign in
# utf8:✓
# authenticity_token:Lk8pXXeDjYMKxkfE9t0LpBMVHupIHWXBaCaCSHVA1zAkI123kdjfBO18M0mI6KDOGmfWxmxcNMfeNc04lzfoBg==
# login:sdf
# password:asdf
# """
# r2 = requests.post(
#     'https://github.com/session',
#     data={
#         "utf8":"✓",
#         'authenticity_token':token,
#         'login':'317828332@qq.com',
#         'password':'alex3714',
#         'commit':'Sign in'
#     },
#     cookies=r1_cookie_dict
# )
# # print(r2.text)
#
# r2_cookie_dict = r2.cookies.get_dict()
# cookie_dict = {}
# cookie_dict.update(r1_cookie_dict)
# cookie_dict.update(r2_cookie_dict)
# r3 = requests.get(
#     url='https://github.com/settings/emails',
#     cookies=cookie_dict
# )
# print(r3.text) #没有找到邮箱地址



# import requests
# from bs4 import BeautifulSoup
#
# #获取token
# r1 = requests.get('https://github.com/login')
# s1 = BeautifulSoup(r1.text,'html.parser')
# token = s1.find(name='input',attrs={'name':'authenticity_token'}).get('value')
# r1_cookie_dict = r1.cookies.get_dict()
# """
# commit:Sign in
# utf8:✓
# authenticity_token:Lk8pXXeDjYMKxkfE9t0LpBMVHupIHWXBaCaCSHVA1zAkI123kdjfBO18M0mI6KDOGmfWxmxcNMfeNc04lzfoBg==
# login:sdf
# password:asdf
# """
# r2 = requests.post(
#     'https://github.com/session',
#     data={
#         "utf8":'✓',
#         "authenticity_token":token,
#         'login':'317828332@qq.com',
#         'password':'alex3714',
#         'commit':'Sign in'
#     },
#     cookies = r1_cookie_dict
# )
# r2_cookie_dict = r2.cookies.get_dict()
# cookie_dict = {}
# cookie_dict.update(r1_cookie_dict)
# cookie_dict.update(r2_cookie_dict)
# r3 = requests.get(
#     url='https://github.com/settings/emails',
#     cookies=cookie_dict
# )
# print(r3.text)


# import requests
# from bs4 import BeautifulSoup
#
# #获取token
# r1 = requests.get('https://github.com/login') #发送get请求
# s1 = BeautifulSoup(r1.text,'html.parser') #将返回的结果
# token = s1.find(name='input',attrs={'name':'authenticity_token'}).get('value')
# print(token)
# r1_cookie_dict = r1.cookies.get_dict()
#
# #将用户名和密码发送到服务端,post
# """
# commit:Sign in
# utf8:✓
# authenticity_token:Lk8pXXeDjYMKxkfE9t0LpBMVHupIHWXBaCaCSHVA1zAkI123kdjfBO18M0mI6KDOGmfWxmxcNMfeNc04lzfoBg==
# login:sdf
# password:asdf
# """
# r2 = requests.post(
#     'https://github.com/session',
#     data={
#         'utf8':'✓',
#         'authenticity_token':token,
#         'login':'317828332@qq.com',
#         'password':'alex3714',
#         'commit':'Sign in'
#     },
#     cookies=r1_cookie_dict
# )
# print(r2.status_code)
# r2_cookie_dict = r2.cookies.get_dict()
# cookie_dict = {}
# cookie_dict.update(r1_cookie_dict)
# cookie_dict.update(r2_cookie_dict)
# r3 = requests.get(
#     url='https://github.com/settings/emails',
#     cookies=cookie_dict
# )
# print(r3.text)


import requests
from bs4 import BeautifulSoup
#获取token
r1 = requests.get('https://github.com/login') #get请求或取token和cookies
s1 = BeautifulSoup(r1.text,'html.parser') #把拿到的结果实例化一个对象
token = s1.find(name='input',attrs={'name':'authenticity_token'}).get('value')#find只找到第一个
print(token)
r1_cookie_dict = r1.cookies.get_dict()
#将用户名密码和cookie还有token发送给服务端
"""
下面这些信息在Network下的all下的Form Data里
commit:Sign in
utf8:✓
authenticity_token:zDzV47SyMrUVVyg5wM5iXkp+roNhLcpciQjYOrBuVUs3bbAkBXDmmUzxZkLsBc0rVfHKtUJdTtwz3kdjAwyz9w==
login:sd
password:asf
"""
r2 = requests.post(
    'https://github.com/session',
    data={
        'utf8':'✓',
        'authenticity_token':token,
        'login':'317828332@qq.com',
        'password':'alex3714',
        'commit':'Sign in'
    },
    cookies=r1_cookie_dict
)
r2_cookie_dict = r2.cookies.get_dict()
cookie_dict = {}
cookie_dict.update(r1_cookie_dict)
cookie_dict.update(r2_cookie_dict)
r3 = requests.get(
    url='https://github.com/settings/emails',
    cookies=cookie_dict
)
print(r3.text)
print(r3.url)


# h = 'hello  world'
# import re
# l = re.split("\s",h)
# print(l)