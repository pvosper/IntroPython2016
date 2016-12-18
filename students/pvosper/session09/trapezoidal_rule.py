#!/usr/bin/env python3

'''
Your task is to write a trapz() function that will compute the area under an
arbitrary function, using the trapezoidal rule.

The function will take another function as an argument, as well as the start
and end points to compute, and return the area under the curve.

- create a list of x values from a to b (maybe 100 or so values to start)
- compute the function for each of those values and double them
- add them all up
- multiply by the half of the difference between a and b divided by the number
    of steps.
'''


def trapz(fun, a, b):
    '''
    Compute the area under the curve defined by
    y = fun(x), for x between a and b

    :param fun: the function to evaluate
    :type fun: a function that takes a single parameter

    :param a: the start point for the integration
    :type a: a numeric value

    :param b: the end point for the integration
    :type b: a numeric value
    '''
    
    samples = 100
    
    # Create list of values
    increment = (b - a) / samples
    l = []
    for value in range(samples + 1):
        l.append(a + (value * increment))
        
    # Compute function for each value
    sum = (fun(l[0]) + fun(l[-1])) / 2
    for entry in l[1:-1]:
        sum += fun(entry)
        
    # Return results
    return increment * sum
