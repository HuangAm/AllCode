# msg = "my name is %s,i am %s years"%("alex",22)
# print(msg)

name = input("name:")
age = input("age:")
job = input("job:")
salary = input("salary:")

info = """
--------info of %s------
NAME: %s
AGE : %s
JOB : %s
Salary: %s
-----------end----------
"""%(name,name,age,job,salary)
print(info)    #%s代表占位符，数字浮点数，字符都可以；%d代表数字，整数；%f代表浮点数，能够把整数自动转成浮点数