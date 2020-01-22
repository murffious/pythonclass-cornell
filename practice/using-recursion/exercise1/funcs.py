"""
Module of recursively defined functions.

In each of these functions, the recursive steps are explicit in the specification.

Author: Paul Murff
Date: Jan 20 2020
"""


def hanoi(n):
    """
    Returns the number of moves needed to solve a Tower of Hanoi of height n.
    
    If m(n) is the number of moves needed to solve a Tower of Hanoi of height n,
    then it is computed from the recursive definition:
        
        m(1) = 1
        m(n) = 2*m(n-1)+1
    
    For more details, see
        
        https://en.wikipedia.org/wiki/Tower_of_Hanoi
    
    Parameter n: The height of the tower
    Precondition: n is an int > 0
    """
    # Do not use loops or ** anywhere in your code.
    if n == 1:
        return 1
    else:    
        return (2*hanoi(n-1)+1)

def lucas(n,p,q):
    """
    Returns the nth Lucas number for coefficients p and q.
    
    A Lucas number is a generalization of the Fibonacci Sequence.  The nth Lucas
    number L(n) is given by the recursive definition
        
        L(0) = 0
        L(1) = 1
        L(n) = p*L(n-1) - q*L(n-2)
    
    Parameter n: The position in the Lucas sequence
    Precondition: n is an int >= 0
    
    Parameter p: The p coefficient
    Parameter p is an int
    
    Parameter q: The q coefficient
    Parameter q is an int
    """
    # Do not use loops or ** anywhere in your code.
    if n == 0:
        return 0
    elif n == 1:
        return 1 
    else:    
        return p*lucas(n-1, p, q) - q*lucas(n-2, p, q)
