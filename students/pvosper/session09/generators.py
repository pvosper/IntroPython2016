#!/usr/bin/env python3

'''
Write a few generators:

    Sum of integers
    Doubler
    Fibonacci sequence
    Prime numbers

(test code in test_generator.py)

Descriptions:

Sum of the integers:

    keep adding the next integer
    0 + 1 + 2 + 3 + 4 + 5 + ...
    so the sequence is:
    0, 1, 3, 6, 10, 15 .....

Doubler:

    Each value is double the previous value:
    1, 2, 4, 8, 16, 32,

Fibonacci sequence:

    The fibonacci sequence as a generator:
    f(n) = f(n-1) + f(n-2)
    1, 1, 2, 3, 5, 8, 13, 21, 34...

Prime numbers:

    Generate the prime numbers (numbers only divisible by them self and 1):
    2, 3, 5, 7, 11, 13, 17, 19, 23...

Others to try:
    Try x^2, x^3, counting by threes, x^e, counting by minus seven, ... 
'''

def soti(start = 0, stop = 10, step = 1):

    i = start
    j = start
    while i < stop:
        yield j
        i += step
        j += i

def doubler(start = 0, stop = 10, step = 1):

    i = start
    j = 1
    while i < stop:
        yield j
        i += step
        j *= 2

def fib(start = 0, stop = 10, step = 1):

# n2 n1 n0
# -  -  1
#    n2 n1 n0
#    -  1  1
#       n2 n1 n0
#       1  1  2
#          n2 n1 n0
#          1  2  3
#             n2 n1 n0

    i = start
    n0 = 1
    n1 = 1
    n2 = 0
    while i < stop:
        yield n0
        i += step
        n0 = n1 + n2
        n2 = n1
        n1 = n0
