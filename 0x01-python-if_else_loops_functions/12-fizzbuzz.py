#!/usr/bin/python3
"""
This prints the numbers from 1 to 100
multiples of three print Fizz
instead of the number and
multiples of five print Buzz
numbers which are multiples of both
three and five print FizzBuzz
"""


def fizzbuzz():
    for i in range(1, 101):
        elif i % 3 == 0 and i % 5 == 0:
            print('{}'.format("FizzBuzz"), end=' ')
        if i % 3 == 0:
            print('{}'.format("Fizz"), end=' ')
        elif i % 5 == 0:
            print('{}'.format("Buzz"), end=' ')
        else:
            print('{}'.format(i), end=' ')
