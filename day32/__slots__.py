#把对象自己的名称空间放到类的名称空见，用于一个类要产生千千万万个对象
class People:
    __slots__=["x",'y','z']
p=People()
print(People.__dict__)
p.x=1
p.y=2
p.z=3
print(p.x,p.y,p.z)
print(p.__dict__)
p1=People()
p1.x=10
p1.y=20
p1.z=30
print(p1.x,p1.y,p1.z)
print(p1.__dict__)