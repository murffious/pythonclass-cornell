"""
Module with for-loops that loop over positions.

Author: Paul Murff
Date: Jan 16 2020 
"""


def skip(s,n):
    """
    Returns a copy of s, only including positions that are multiples of n
    
    A position is a multiple of n if pos % n == 0.
    
    Examples:
        skip('hello world',1) returns 'hello world'
        skip('hello world',2) returns 'hlowrd'
        skip('hello world',3) returns 'hlwl'
        skip('hello world',4) returns 'hor'
    
    Parameter s: the string to copy
    Precondition: s is a nonempty string
    
    Parameter n: the letter positions to accept
    Precondition: n is an int > 0
    """
    result = ''
    acum = 0
    for x in s:  
        if acum % n == 0:
            result = result + x
        acum += 1     
    return result

def fixed_points(tup):
    """
    Returns a copy of tup, including only the "fixed points".
    
    A fixed point of a tuple is an element that is equal to its position in the tuple.
    For example 0 and 2 are fixed points of (0,3,2).  The fixed points are returned in
    the order that they appear in the tuple.
    
    Examples:
        fixed_points((0,3,2)) returns (0,2)
        fixed_points((0,1,2)) returns (0,1,2)
        fixed_points((2,1,0)) returns ()
    
    Parameter tup: the tuple to copy
    Precondition: tup is a tuple of ints
    """
    result = ()
    acum = 0
    for x in tup:  
        if acum == x :
            result = result + (x,)
        acum += 1     
    return result
