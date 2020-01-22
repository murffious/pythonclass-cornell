"""
Recursive functions to count elements in a string.

These functions should be copied into the Python Tutor.  That way you can
see how recursion affects the call stack.

Author: Walker M. White
Date:   April 15, 2019
"""


def num_e(s):
    """
    Returns: number of 'e's in s
    
    Parameter: s the string to count
    Precondition s is a string
    """
    assert type(s) == str, repr(s) + ' is not a string' # get in the habit
    
    # Work on small data  (BASE CASE)
    if s == '':
        return 0
    elif len(s) == 1:
        if s == 'e':
            return 1
        else:
            return 0
    
    # Break up the data   (RECURSIVE CASE)
    left  = num_e(s[0])
    right = num_e(s[1:])
    
    # Combine the results
    return left+right


def length(s):
    """
    Returns: number of characters in s
    
    Parameter: s the string to measure
    Precondition s is a string
    """
    assert type(s) == str, repr(s) + ' is not a string' # get in the habit
    
    # Work on small data  (BASE CASE)
    if s == '':
        return 0
    
    # Break up the data   (RECURSIVE CASE)
    left  = 1               # Length of s[0]
    right = length(s[1:])   # Length of s[1:]
    
    # Combine the results
    return left+right
