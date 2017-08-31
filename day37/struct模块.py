import struct
print(struct.pack("i",13121312))#会把一定长度的数字压缩成固定4个字节
res=struct.pack("i",13121312) #“i”是格式，用i格式打包的也要用i格式解包
print(len(res)) #长度为4
print(struct.unpack("i",res))#(13121312,)得到一个元组，[0]就是原先的数字
#当我们用到粘包中的时候，[0]就是data的字节长度





