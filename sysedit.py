import fileinput

sysprop = 'res/sysprop.txt'
print('Welcome to sysedit!\nBeware! Only modify the sysprop if you know what you are doing!')

while True:
    command = input(': ')
    if command == 'ddfalse':
        for line in fileinput.input(sysprop, inplace = 1):
            print(line.replace('ddtrue', 'ddfalse'))
    else:
        if command == 'ddtrue':
            for line in fileinput.input(sysprop, inplace = 1):
                print(line.replace('ddfalse', 'ddtrue'))

    if command == 'exit':
        import main
