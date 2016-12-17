#!/usr/bin/env python3
''' Lambda Keyword
    Functions are created when they are created
    CHB: "keywords are evaluated when functions are created"
'''


# Simple version w/o lambda 
# def function_builder(n):
#     l = []
#     for i in range(n):
#         print('Creating f with :', i)
#         def f(x, inc = i):
#             return x + inc
#         l.append(f)
#     print("i at end of loop:", i)
#     return l


# Incorporating lambda into for loop
# def function_builder(n):
#     l = []
#     for i in range(n):
#         print('Creating f with :', i)
#         l.append(lambda x: x + i)
#         # l.append(lambda x, inc = i: x + inc)
#     print("i at end of loop:", i)
#     return l


# As list comprehension
def function_builder(n):
    return [lambda x, inc = i: x + inc for i in range(n)]


if __name__ == '__main__':
    print('\n=== MAIN ===\n')


print('function_builder(10): ', function_builder(10))

