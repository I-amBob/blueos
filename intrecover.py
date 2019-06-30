import subprocess as sp
import time
import os

tmp = sp.call('clear',shell=True)
print('Welcome to Internet Recovery!')
time.sleep(1)
while True:
    command = input(': ')
    if command == 'exit':
        import main
    if command == 'sysprop':
        os.system('rm res/sysprop.txt')
        os.system('wget -c http://mechintosh-server.rf.gd/res/sysprop.txt res/sysprop.txt')
