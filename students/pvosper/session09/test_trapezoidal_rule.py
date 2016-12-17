#!/usr/bin/env python3

'''
Test code for trapezoidal_rule.py

'''

from trapezoidal_rule import trapz

def test_line():

    def line(x):
        '''a very simple straight horizontal line at y = 5'''
        return 5

    area = trapz(line, 0, 10)

    assert area == 50