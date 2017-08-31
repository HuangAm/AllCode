import time
class Open:
    def __init__(self,filepath,mode="r",encoding="utf8"):
        self.filepath=filepath
        self.mode=mode
        self.encoding=encoding
        self.x=open(filepath,mode=mode,encoding=encoding)
    def write(self,line): #需要改写的自定制
        t=time.strftime("%Y-%m-%d %X")
        self.x.write("%s %s"%(t,line))
    def __getattr__(self, item): #需要使用默认的用getattr
        if hasattr(self.x,item):
            return getattr(self.x,item)
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.x)
        print("exit")
        print("exc_type",exc_type)
        print("exc_val",exc_val)
        print("exc_tb",exc_tb)
        # return True
with Open("a.txt") as f:
    print("sssssssss")
    print(f)
    # raise TypeError("madezhihang")
# print("asdfasdfasddf")