'''
    2nd LAB exercise from 161004

    Write a program that prints the numbers from 1 to 100 inclusive.
    But for multiples of three print “Fizz” instead of the number
    For the multiples of five print “Buzz”.
    For numbers which are multiples of both three and five print “FizzBuzz” instead.
'''

fb_list = []

def do_list(fizz, buzz, limit):
    for i in range(0, limit + 1):
        fb_list.append(i)

# You could simplify this into loop 3 times
def do_fizz(fizz, buzz, limit):
    for i in range(0, limit + 1, fizz):
        fb_list[i] = "Fizz"

def do_buzz(fizz, buzz, limit):
    for i in range(0, limit + 1, buzz):
        fb_list[i] = "Buzz"

def do_fizzbuzz(fizz, buzz, limit):
    for i in range(0, limit + 1, fizz * buzz):
        fb_list[i] = "FizzBuzz"

def fizz_buzz(fizz = 3, buzz = 5, limit = 100):
    do_list(fizz, buzz, limit)
    do_fizz(fizz, buzz, limit)
    do_buzz(fizz, buzz, limit)
    do_fizzbuzz(fizz, buzz, limit)
    print(fb_list[1:limit + 1])

fizz_buzz(3, 5, 100)

# ===== This also works =====
# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizzbuzz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     else:
#         print(i)