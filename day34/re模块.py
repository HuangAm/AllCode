#元字符：. ^ $ + ? {}
import re
# ret= re.findall("a..in","helloalvin")
# print(ret)
# ret=re.findall("^a...n","albinhelloawwm")
# print(ret)
# ret = re.findall('a..n$','albinhhelloawwn')
# print(ret)
# ret = re.findall('abc*','abcccc')#[0,+oo]
# print(ret)
# ret=re.findall('abc?','abccc')#[0,1]
# print(ret)
# ret=re.findall('abc+','abccc')#[1,+oo]
# print(ret)
# ret=re.findall('abc{1,4}','abccc')
# print(ret)
#注意：上面的*?+{}都是贪婪匹配，也就是尽可能匹配，后面加问号使其变为惰性匹配
# ret=re.findall('abc*?',"abccccc")
# print(ret)
#元字符集[]: 任意一个 .*+都没有意义 -^\ 有意义
# ret=re.findall('a[bc]d','acdabd')
# print(ret)
# ret=re.findall('[a-z]',"acd")
# print(ret)
# ret=re.findall("[.*+]",'a.cd+')
# print(ret)
# ret=re.findall('[1-9]','45dha3')
# print(ret)
# ret=re.findall('[^ab]','45bdha3') #不是a或b
# print(ret)
# ret=re.findall('[\d]','45bdh3')
# print(ret)
'''
\d  [0-9] 匹配任何十进制数
\D  [^0-9] 匹配任何非数字字符
\s  [\t\n\r\f\v] 匹配任何空白字符
\S  [^\t\n\r\f\v] 匹配任何非空白字符
\w  [a-zA-Z0-9] 匹配任何字母数字字符
\W  [^a-zA-Z0-9] 匹配任何非字母数字字符
\b  空格，&，#等 匹配一个特殊字符边界
'''
# ret=re.findall('I\b','I am LIST')#python解释器把\b按ascma表进行处理了，等正则表达式拿上的时候是"I="等号代表\b在ascma中对应的功能
# print(ret)#[]
# ret=re.findall(r'I\b','I am LIST')#r是告诉解释器不要管引号里面的\，直接交给正则就好了
# ret=re.findall('I\\b','I am LIST')#解释器碰到双斜杠知道这是代表转意，把\\变为\交给了正则
# ret=re.findall('I','I am LIST')
# print(ret)
# m=re.findall('\bblow','blow')
# print(m)
# ret=re.findall('a\\\\k','a\kaaa')#Python解释器会识别转义符然后去掉转义符传给正则正则而拿到的就是"a\\k",正则也在识别转义符，处理后为"a\k"
# print(ret)
# print("a\\\\b")#a\\b
# print("a\\\b")#a
# print("a\\b")#a\b
# print("a \b")#空白
# print("abc\b")#ab,懂了吧，妈的\b在这里会实现它的功能
#元字符分组()
# m=re.findall(r'(ad)+','add')
# print(m)#ad

# ret=re.findall(r"(\d)+yuan","adad678423yuan345")
# print(ret)#['3'],只会打印3，如果想全部打印看下面
# ret=re.findall(r"(?:\d)+yuan","adad678423yuan345")
# print(ret)#['678423yuan'],这就是个语法，记住就好了，取消分组的特权

# ret=re.search('(?P<id>\d{2})/(?P<name>\w{3})',"23/com")
# print(ret.group())
# print(ret.group('id'))#一定要记得加引号

#元字符 |  或
# print(re.findall("www.(?:oldboy|baidu).com","www.oldboy.com.www.baidu.com"))#['www.oldboy.com', 'www.baidu.com']
# print(re.findall("www.(?:oldboy)|(?:baidu).com","www.oldboy.com.www.baidu.com"))#['www.oldboy', 'baidu.com']

# print(re.search("\d+\.?\d*\*\d+\.?\d*","2*6*7*45+1.4*3-8/4").group())
# print(re.findall("\d+\.?\d*\*\d+\.?\d*","2*6+7*45+1.4*3-8/4"))
# print(re.findall("\w","sadfsdgasg"))
# print(re.findall("f\s","sdf safsd"))
# print(re.findall("\S","sdf s afsd"))
# print(re.findall("I","I am LI"))
# print(re.findall(r"\bI","hello :I am LI"))#不打印特殊边界
# print(re.findall(r"c\\l","abc\l"))

#re模块下得常用方法
# print(re.findall("a","alvin yuan")) #返回所有满足匹配条件的结果，放在列表里

# ret=re.search("a","alvin yuan") #函数会在字符串内查找模式匹配,只找到第一个匹配然后返回一个包含匹配信息的对象
# print(ret)#如果匹配到，返回一个对象，如果匹配失败返回None
# print(ret.group())#对象通过group()方法得到匹配的字符串

# ret=re.match('a',"abc")#基本上和serch一样，只是从头匹配，没有就返回None
# print(ret)
# print(ret.group())

# ret=re.finditer("\d+","ad3456asdf23") #返回可调用的迭代器对象
# print(ret)
# print(next(ret).group())
# print(next(ret).group()) #不会提示方法
# for i in ret:
#     print(i.group()) #会提示方法

# s=re.split("\d+","dsfgret3456ljl456jkl7hjk",2)#以\d+作为分隔符进行分割
# print(s)#['dsfgret', 'ljl', 'jkl'] 拿到列表

# ret=re.sub("\d","A","hjkl678ghj")#全部替换
# print(ret)
# ret=re.sub("\d","A","hjkl678ghj",1)#只替换一个
# print(ret)
# ret=re.subn("\d","A","hjkl678ghj")#返回一个元组，里面有替换的结果，和次数
# print(ret)#('hjklAAAghj', 3)

# ret=re.compile("\d+")#就是可以省一个规则，对多个字符串进行统一规则处理
# res=ret.findall("sdf23df")
# print(res)

# x='(-40/5)'
# a=re.search(r"\d+\.?\d*/-?\d+\.?\d*",x).group()
# l=a.split("/")
# b=float(l[0])/float(l[1])
# x=re.sub(r"\d+\.?\d*/-?\d+\.?\d*",str(b),x)
# print(x)
# print(1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) ))




