#!/usr/bin/env python

'''
In the Examples/session09 dir, you will find: iterator_1.py

Extend (iterator_1.py ) to be more like range() – add three input parameters:
    iterator_2(start, stop, step=1)
What happens if you break from a loop and try to pick it up again:

it = IterateMe_2(2, 20, 2)
for i in it:
    if i > 10:  break
    print(i)

for i in it:
    print(i)

Does range() behave the same?
    make yours match range()
    is range an iterator or an iteratable?

The main thing that differentiates an iterator from an iterable (sequence) is
    that an iterator saves state.

iteratables are not only for 'for'

They can be used with anything that expects an iterable:

sum, tuple, sorted, and list
'''


class IterateMe_1(object):
    '''
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like range(4) )
    '''
    def __init__(self, stop=5):
        self.current = -1
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        self.current += 1
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration

class IterateMe_2:
    '''
    extend IterateMe_1
    '''
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start - step
    def __iter__(self):
        self.current = self.start - self.step
        return self
    def __next__(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration

if __name__ == '__main__':

    print('IterateMe_1()')
    for i in IterateMe_1():
        print(i)

    print('IterateMe_1(6)')
    for i in IterateMe_1(6):
        print(i)

#     TypeError: unorderable types: int() < list_iterator()
#     print('IterateMe_1(a_list = [7,3,29,14,2,10,64])')
#     a_list = [7,3,29,14,2,10,64]
#     for i in IterateMe_1(iter(a_list)):
#         print(i)

    print('range(6)')
    rit = range(6)
    for i in rit:
        if i > 3:  break
        print(i)

    print('--- break ---')

    for i in rit:
        print(i)

    print('IterateMe_1(6)')
    iit = IterateMe_1(6)
    for i in iit:
        if i > 3:  break
        print(i)

    print('--- break ---')

    for i in iit:
        print(i)

    print('IterateMe_2(2, 20, 2)')
    it = IterateMe_2(2, 20, 2)
    for i in it:
        if i > 10:  break
        print(i)

    print('--- break ---')

    for i in it:
        print(i)

