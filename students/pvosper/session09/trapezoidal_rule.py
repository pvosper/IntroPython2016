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


def trapz(fun, a, b, *args, **kwargs):
    '''
    Compute the area under the curve defined by
    y = fun(x), for x between a and b

    :param fun: the function to evaluate
    :type fun: a function that takes a single parameter

    :param a: the start point for the integration
    :type a: a numeric value

    :param b: the end point for the integration
    :type b: a numeric value
    
    CHB:
    s = sum([fun(x, *args, **kwargs) for x in vals[1:-1]])
    s += (fun(a, *args, **kwargs) + fun(b, *args, **kwargs)) / 2
    s *= (b-a) / n

    '''
    
    samples = 100
    
    # Create list of values
    increment = (b - a) / samples
    l = [a + (value * increment) for value in range(samples + 1)]
        
    # Compute function for each value
    sum = (fun(l[0], *args, **kwargs) + fun(l[-1], *args, **kwargs)) / 2
#     sum += sum(fun(entry, *args, **kwargs) for entry in l[1:-1])
#     TypeError: 'float' object is not callable
    for entry in l[1:-1]:
        sum += fun(entry, *args, **kwargs)
        
    # Return results
    return increment * sum
