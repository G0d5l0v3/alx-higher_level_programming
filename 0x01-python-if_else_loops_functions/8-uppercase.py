#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 95 and ord(i) <= 124:
            str = chr(ord(i) - 32)
            print('{}'.format(str), end='')
        print('')
