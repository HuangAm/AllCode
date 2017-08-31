import subprocess
print(subprocess.Popen("dir",shell=True,stdout=subprocess.PIPE))
res=subprocess.Popen("dir",shell=True,stdout=subprocess.PIPE)
print(res.stdout.read())
print(res.stdout.read())#b"",是空的
res=subprocess.Popen("dirrr",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
print(res.stdout.read())#b""
print(res.stderr.read())