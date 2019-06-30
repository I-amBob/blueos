import subprocess as sp
import time

sysprop_raw = open('res/sysprop.txt', 'r')
sysprop_read = sysprop_raw.read()
sysprop = sysprop_read.split()

# START INITIALIZE FROM SYSPROP
######################################################################
sysgood = True
# display_driver
if sysprop[0] == 'ddtrue':
    display_driver = True
else:
    if sysprop[0] == 'ddfalse':
        display_driver = False
    else:
        print('Warning! SYSPROP not valid!\nSystem integrity compromised!\nWaiting 10 seconds...')
        sysgood = False
        time.sleep(10)

#
######################################################################
#END INITIALIZE FROM SYSPROP

tmp = sp.call('clear',shell=True)
print("Loading...")

time.sleep(2)
tmp = sp.call('clear',shell=True)

if sysgood == True:
    print('''
    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    WWW                          WWW
    WWW        ***        ***    WWW
    WWW             \____/       WWW
    WWW                          WWW
    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    ''')
else:
    print('''
    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    WWW                          WWW
    WWW        ***        ***    WWW
    WWW             ____         WWW
    WWW            /    \        WWW
    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    ''')

time.sleep(3)
tmp = sp.call('clear',shell=True)

print('''
 ____________________________
|                            |
|   Welcome to Mechintosh!   |
|                            |
|____________________________|
''')

time.sleep(3)
tmp = sp.call('clear',shell=True)
print("Welcome to Mechintosh!")

import main
