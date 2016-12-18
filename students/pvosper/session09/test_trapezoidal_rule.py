#!/usr/bin/env python3

'''
Test code for trapezoidal_rule.py

'''

import math

from trapezoidal_rule import trapz

def test_line():

    def line(x):
        '''a very simple straight horizontal line at y = 5'''
        return 5

    area = trapz(line, 0, 10)

    assert area == 50

def test_sloped_line_a():

    def s_line_a(x):
        '''a sloped line'''
        return x / 2 + 2

    area = trapz(s_line_a, -2, 23)

    assert area == 181.25

def test_sloped_line_b():

    def s_line_b(x):
        '''a sloped line'''
        return x * -1 + 5

    area = trapz(s_line_b, -13, -4)

    assert area == 121.5

def test_quadratic_a():

    def quad_a(x):
        '''a simple quadratic'''
        return  x**2 - x - 2
        
    area = trapz(quad_a, -10, 10)
    
    assert math.isclose(area, 626.8, rel_tol=0.05)

def test_quadratic_b():

    def quad_b(x):
        '''a simple quadratic'''
        return  27 * x**2 + 2 * x - 32
        
    area = trapz(quad_b, 7, 9)
    
    assert math.isclose(area, 3442, rel_tol=0.05)
    
    