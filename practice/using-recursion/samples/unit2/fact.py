"""
Recursive implementation of factorial

This function should be copied into the Python Tutor.  That way you can
see how recursion affects the call stack.

Author: Walker M. White
Date:   April 15, 2019
"""
import sys

# Allow us to go really deep
sys.setrecursionlimit(999999999)


def factorial(n):
    """
    Returns: n!
    
    Parameter n: the number to compute
    Precondition: n is a nonnegative integer
    """
    #if n==0: # Base case
    #    return 1
    
    # Recursive case.
    return n*factorial(n-1)

# Factorial Call
x = factorial(5)
