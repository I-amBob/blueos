import subprocess as sp
import time

user = open("res/username.txt", 'w')

tmp = sp.call('clear',shell=True)
print("Loading...")

time.sleep(2)
tmp = sp.call('clear',shell=True)
print('''
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWW                          WWW
WWW        ***        ***    WWW
WWW             \____/       WWW
WWW                          WWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
''')

time.sleep(3)
tmp = sp.call('clear',shell=True)

print('''
 ____________________________
|                            |
|   Welcome to machintosh!   |
|                            |
|____________________________|
''')

time.sleep(5)
tmp = sp.call('clear',shell=True)
print("Welcome to Machintosh Installer!")
username = input("Username: ")
user.write(username)
