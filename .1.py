import sys,os,time,marshal
from time import sleep
from sys import exit
from os import system


try:
    file = input("\033[1;33m[+] \033[1;37mScript > \033[1;32m")
    o = file.replace('.py','')
except KeyboardInterrupt:
    exit()
except EOFError:
    exit()
else:
    try:
        fileopen = open(file, 'r').read()
    except IOError:
        exit("\033[1;31m[!] \033[1;37mfile not exist")
    try:
        code = compile(fileopen, '','exec')
        data = marshal.dumps(code)
    except TypeError:
        print("\033[1;31m[!] \033[1;37mFile already to compiled")
        exit()
a = open(o+'_enc.py','w')
a.write("#Compiled By Aslanz\n#https://youtube.com/aslanz\nimport marshal\nexec(marshal.loads("+repr(data)+"))")
print("\033[1;33m[\033[1;32m+\033[1;33m] \033[1;37mSuccessfully encrypt seved as \033[1;32m"+o+"_enc.py")
