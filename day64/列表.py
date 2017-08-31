#多级评论原理简单原理,弄完之后发现基础白学了
msg_list = [
    {'id':1,'content':'xxx','parent_id':None},
    {'id':2,'content':'xxx','parent_id':None},
    {'id':3,'content':'xxx','parent_id':None},
    {'id':4,'content':'xxx','parent_id':1},
    {'id':5,'content':'xxx','parent_id':4},
    {'id':6,'content':'xxx','parent_id':2},
    {'id':7,'content':'xxx','parent_id':5},
    {'id':8,'content':'xxx','parent_id':3},
]
#python里面的apend之类的东西都是引用的原来数据的内从地址,对原数据进行操作的话
#我们引用的数据也会发生一样的变化(字典列表之类的)

#骗子的方法
# for i in msg_list:
#     i['child']=[]
# for i in range(len(msg_list)-1,-1,-1):
#     if msg_list[i]['parent_id']:
#         msg_list[msg_list[i]['parent_id'] - 1]['child'].append(msg_list[i])
# new_msg_list = [i for i in msg_list if i['parent_id'] is None]
# print(new_msg_list)

#老师讲的方法
# v=[row.setdefault('child',[]) for row in msg_list] #这和地下的第一个for循环的作用是一样的,给每一个元素加一个'child':[]
# print(msg_list)
#如果我们想加快索引(快点找到数据的话)就建一个字典的数据结构
msg_list_dict={} #加快索引,节省时间
for item in msg_list:
    item['child']=[]
    msg_list_dict[item['id']]=item #字典中key为item['id']，value为item
    #把字典数据结构填上数据,能够加快索引,而且我们数据还是占得原来的内从空间
    #我们只是引用了数据的内容空间,所以不存在新的数据结构浪费空间一说
result=[]
for item in msg_list:
    pid=item['parent_id']
    if pid: #如果parent_id不为空,说明它是子级,要把自己加入对应的父级
        msg_list_dict[pid]['child'].append(item)
    else: #如果为空,说明他是父级,要把它单独领出来用
        result.append(item)
#result就是我们最终要的结果,因为这里面全是引用,所有数据的内存地址都没有变
#只不过被多个数据结构引用了而已
print(result)














