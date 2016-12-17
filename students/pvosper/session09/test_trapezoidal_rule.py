#!/usr/bin/env python3

'''
Test code for trapezoidal_rule.py

'''


def line(x):
    '''a very simple straight horizontal line at y = 5'''
    return 5

area = trapz(line, 0, 10)

area
50