import subprocess as sp
import time

user = open("res/username.txt", 'r')
username = user.read()


while True:
    command = input(f'{username}@Recovery:~$ ')
    if command == "status":
        time.sleep(1)
        if display_driver == True:
            print('Everything OK')
        else:
            print('No display driver')
            print('Else OK')
    if command == "intrecover":
        import intrecover
    if command == "clear":
        tmp = sp.call('clear', shell=True)
    if command == 'sysedit':
        import sysedit
    if command == 'ddtrue':
        display_driver = True
    else:
        if command == 'ddfalse':
            display_driver = False
