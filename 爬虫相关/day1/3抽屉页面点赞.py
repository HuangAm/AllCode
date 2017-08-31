#1.登录,cookie
#2.标签url
import requests
from bs4 import BeautifulSoup
r0 = requests.get('http://dig.chouti.com/')
r0_cookie_dict = r0.cookies.get_dict()
r1 = requests.post(
    'http://dig.chouti.com/login',
    data={
        'phone':'8615131255089',
        'password':'woshiniba',
        'oneMonth':None
    },
    cookies=r0_cookie_dict
)
r1_cookie_dict = r1.cookies.get_dict()
cookie_dict = {}
cookie_dict.update(r0_cookie_dict)
cookie_dict.update(r1_cookie_dict)
r2 = requests.post(
    'http://dig.chouti.com/link/vote?linksId=13926051',
    cookies=cookie_dict
)
print(r2)