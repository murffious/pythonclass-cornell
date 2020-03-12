"""
Module of functions utilizing divide-and-conquer.

In each of these functions, the recursive steps are not explict.  Instead, they use
divide-and-conquer to solve a problem.

Author: Paul Murff
Date: 20 Jan 2020 
"""


def prod(tup):
    """
    Returns the product of the integers in tup. Returns 1 if empty.
    
    Examples: 
        prod((12,)) returns 12
        prod((7,12,1,2,2)) returns 336
        prod((7,12,0,2,2)) returns 0
        prod(()) returns 1
    
    Parameter tup: the tuple to multiply
    Precondition: tup is a tuple of ints
    """
    if len(tup) == 0:
        return 1
    left = prod(tup[0])
    right = prod(tup[1:])

    return left * right 

def replace(tup,a,b):
    """
    Returns a copy of tup but with all occurrences of a replaced by b.
    
    Examples: 
        replace((1,2,3,1), 1, 4) returns (4,2,3,4)
        replace((1,2,3,1), 4, 1) returns (1,2,3,1)
        replace((), 1, 4) returns ()
    
    Parameter tup: The tuple to copy
    Precondition: tup is a tuple of ints
    
    Parameter a: The value to replace
    Precondition: a is an int
    
    Parameter b: The value to replace with
    Precondition: b is an int
    """
    pass