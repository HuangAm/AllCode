#递归函数：可以调用其它函数。如果一个函数在内部调用自身本身，这个函数就是递归函数
#例如，阶乘n!=1x2x3x...xn,用函数fact()表示，可以看出：
#fact(n)=n!=1x2x3x...x(n-1)xn=(n-1)!xn=fact(n-1)xn 所以,fact(n)可以表示成nxfact(n-1),只有n=1时需要特殊处理。
# def fact(n):
#     if n==1:
#         return 1
#     return n*fact(n-1)
# print(fact(5))
# def fact(n):
#     return fact_iter(n,1)
# def fact_iter(num,product):
#     if num == 1:
#         return product
#     return fact_iter(num-1,num*product)
# print(fact(5))
#d={"name":"agon","age":"22"}
s=input(">>:")
print(eval(s)["name"])