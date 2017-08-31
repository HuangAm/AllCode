# def eater(name):
#     print('%s start to eat food' %name)#第一个print
#     while True:
#         food=yield
#         print('%s get %s ,to start eat'%(name,food))#第二个print
#     print('done')
# e=eater('钢蛋')#e是生成器
# print(e)#打印生成器的内存地址
# print(next(e))#next触发函数执行，执行第一个print后碰到yield是停止，但yield后面没有值，所以返回None
# # >>钢蛋 start to eat food
# # >>None
# print(next(e))#next触发函数执行，再上一个yield处开始运行，打印第二个print-->while true->又碰到yield后停止，但yield后面没有值，所以返回None
# # >>钢蛋 get None ,to start eat
# # >>None
# def eater(name):
#     print('%s start to eat food' %name)#第一个print
#     while True:
#         food=yield
#         print('%s get %s ,to start eat'%(name,food))#第二个print
#     print('done')
# e=eater('钢蛋')#e是生成器
# next(e)#next触发执行一次打印第一个print后碰到yield停止，这里没有打印
# # >>钢蛋 start to eat food
# e.send('包子')#send和next一样都会触发函数运行，碰到yield后停止得到一个返回值，不一样的地方就是send会把自己的参数交给当前暂停的yield，再由yield交给他赋值给的对象，这里是food，然后打印第二个print在经过whiletrue碰到yield停止，这里没有打印
# # >>钢蛋 get 包子 ,to start eat
# print(e.send('包子'))#加上上面的运行结果后，还要返回None,因为yield后面依旧没有值，所以send执行完后他传入的参数也没了
# # >>钢蛋 get 包子 ,to start eat
# # >>None
# def eater(name):
#     print('%s start to eat food' %name)#第一个print
#     food_list=[]
#     while True:
#         food=yield food_list
#         print('%s get %s ,to start eat'%(name,food))#第二个print
#         food_list.append(food)
#     print('done')
# e=eater('钢蛋')#e是生成器
# print(next(e))
# print(e.send('包子'))
# print(e.send('韭菜包子'))
# print(e.send('榴莲包子'))

#运行结果如下：
# 钢蛋 start to eat food
# []
# 钢蛋 get 包子 ,to start eat
# ['包子']
# 钢蛋 get 韭菜包子 ,to start eat
# ['包子', '韭菜包子']
# 钢蛋 get 榴莲包子 ,to start eat
# ['包子', '韭菜包子', '榴莲包子']


#利用装饰器帮助协程函数省去初始化步骤
# def next_free(func):
#     def wrapper(*args,**kwargs):
#         res = func(*args,**kwargs)
#         next(res)
#         return res#???
#     return wrapper
# @next_free #eater=next_free(eater)
# def eater(name):
#     print('%s start to eat food' %name)#第一个print
#     food_list=[]
#     while True:
#         food=yield food_list
#         print('%s get %s ,to start eat'%(name,food))#第二个print
#         food_list.append(food)
#     print('done')
# g=eater('agon')
