# import spam
'''
第一件事：创建名称空间，用来存放spam.py中定义的名字
第二件事：基于刚刚创建的名称空间来执行spam.py
第三件事：创建名字spam指向该名称空间，spam.名字的操作，都是以spam.py为准
'''
# print(spam.money)
# spam.read1()
# spam.read2()
# spam.change()
# print(spam.money)

# from spam import money,read1,read2
# money=1000000
# print(money)
# read1=1234567
# read1()
#
# read2()

# def test():
#     x=1
#     return x
# print(test.__dict__)
# dir()
# import sys
# print(sys.modules)
#fib.py

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))