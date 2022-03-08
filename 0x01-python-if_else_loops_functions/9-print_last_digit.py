#!/usr/bin/python3
def print_last_digit(number):
    lastDigit = int(repr(number)[-1])
    print('{}'.format(lastDigit), end='')
    return lastDigit
print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
