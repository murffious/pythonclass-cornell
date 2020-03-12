"""
Recursive implementation of the fibonacci sequence

This function should be copied into the Python Tutor.  That way you can
see how recursion affects the call stack.

Author: Walker M. White
Date:   April 15, 2019
"""

# Function Definition
def fibonacci(n):
    """
    Returns: Fibonacci number a_n
    
    Parameter n: the position to compute
    Precondition: n is a nonnegative integer
    """
    if n == 0 or n == 1:
        return 1
    
    one_back = fibonacci(n-1)
    two_back = fibonacci(n-2)
    return one_back+two_back

# Function Call
x = fibonacci(5)
