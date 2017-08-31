import time
class Open:
    def __init__(self,filepath,mode="r",encode="utf8"):
        self.f=open(filepath,mode=mode,encoding=encode)
    def write(self):
        print("sdfsfsdf")
    def __del__(self):
        print("---->del")
        self.f.close()
f=Open("a.txt","w")
f.write()
time.sleep(2)
del f
print(111)