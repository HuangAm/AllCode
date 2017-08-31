import hashlib
# md5 = hashlib.md5() #模块里的类实例化出一个对象
# print(md5) #<md5 HASH object @ 0x0000000000A1FCD8>
# help(md5)
# md5.update("how to use md5 in python hashlib?".encode("utf8"))
# #在Python3中，Unicode-objects must be encoded before hashing
# #在Python2中，不需要解码，因为一运行就是字节
# print(md5.hexdigest())

#如果数据量很大，可以分多次调用update(),最后计算的结果是一样的：
# md5 = hashlib.md5()
# md5.update("how to use md5".encode("utf-8"))
# md5.update("in python hashlib?".encode("utf-8"))
# print(md5.hexdigest())

#MD5是最长见的摘要算法，速度很快，生成结果是固定的128bit字节，通常用一个32位的16进制字符表示。另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：
# sha1 = hashlib.sha1()
# sha1.update("how to use md5".encode("utf-8"))
# sha1.update("in python hashlib?".encode("utf-8"))
# print(sha1.hexdigest())
#sha1结果是160bit字节，通常用一个40位的16进制字符串表示。比sha1更安全的是sha256和sha512，不过越安全的算法越慢，而且摘要长度更长