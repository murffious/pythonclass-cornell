"""
Module with range-based for-loop functions.

Author: Paul Murff
Date: Jan 16 2020 
"""

def factorial(n):
    """
    Returns n! = n * (n-1) * (n-2) ... * 1
    
    0! is 1.  Factorial is undefined for integers < 0.
    
    Examples:
        factorial(0) returns 1
        factorial(2) returns 2
        factorial(3) returns 6
        factorial(5) returns 120
    
    Parameter n: The integer for the factorial
    Precondition: n is an int >= 0
    """
    acum = 1
    for i in range(0,n): 
        acum *= (n-i)         
    return acum 

def revrange(a,b):
    """
    Returns the tuple (b-1, b-2, ..., a)
    
    Note that this tuple is the reverse of tuple(range(a,b))
    
    Parameter a: the "start" of the range
    Precondition: a is an int <= b
    
    Parameter b: the "end" of the range
    Precondition: b is an int >= a
    """
    acum = 0
    result = ()
    for x in range(a,b):
        acum+=1
        result = result + ( b - acum,)    
    return result 