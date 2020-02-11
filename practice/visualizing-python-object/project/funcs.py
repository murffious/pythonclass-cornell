"""
Functions demonstrating using other functions as parameters.

These two functions are implementations of the famous fold functions.  A variation of
fold is called "reduce", which is part of Google's famous map-reduce set-up.

Author: Paul Murff
Date: Feb 10 2020 
"""


def fold_left(f,seq,value):
    """
    Returns the result of folding f left over seq, starting with value.
    
    To fold a function f from the left, we 
    * Start with value in the accumulator
    * Iterate over the sequence normally
    * At each step, apply f to the accumulator and the next element
    * After applying f, make the new value the accumulator
    
    Example: Suppose f is - (subtraction), seq is (1,2,3,4) and value is 0.  Then
    the result is
        
        ((((0-1)-2)-3)-4) = -10
    
    Parameter f: the function to fold
    Precondition: f is a function that takes two arguments of the same time, and
    returning a value of the same type
    
    Parameter seq: the sequence to fold
    Precondition: seq is a sequence (tuple, string, etc.) whose elements are the
    same type as that returned by f
    
    Parameter value: the initial starting value
    Precondition: value has the same type as the return type of f
    """
    accum = value
    for item in seq:
        accum = (f(accum,item))
    return accum
 
def fold_right(f,seq,value):
    """
    Returns the result of folding f right over seq, starting with value.
    
    To fold a function f from the right, we 
    * Start with value in the accumulator
    * Iterate over the sequence right-to-left
    * At each step, apply f to the next element and the accumulator
    * After applying f, make the new value the accumulator
    
    Example: Suppose f is - (subtraction), seq is (1,2,3,4) and value is 0.  Then
    the result is
        
        (1-(2-(3-(4-0)))) = -2
    
    Parameter f: the function to fold
    Precondition: f is a function that takes two arguments of the same time, and
    returning a value of the same type
    
    Parameter seq: the sequence to fold
    Precondition: seq is a sequence (tuple, string, etc.) whose elements are the
    same type as that returned by f
    
    Parameter value: the initial starting value
    Precondition: value has the same type as the return type of f
    """
    accum = value
    yo = reversed(seq)
    for item in yo:
        accum = (f(item,accum)) 
    return accum
