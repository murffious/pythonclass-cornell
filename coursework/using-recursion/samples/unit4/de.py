"""
Recursive functions to remove characters from a string.

These functions should be copied into the Python Tutor.  That way you can
see how recursion affects the call stack.

Author: Walker M. White
Date:   April 15, 2019
"""
import introcs


def deblank(s):
    """
    Returns: s but with blanks removed

    Parameter: s the string to edit
    Precondition s is a string
    """
    assert type(s) == str, repr(s) + ' is not a string' # get in the habit
    
    # Work on small data  (BASE CASE)
    if s == '':
        return s
    
    # Break up the data   (RECUSIVE CASE)
    left = s[0]
    if s[0] == ' ':
        left = ''
    right = deblank(s[1:])
    
    # Combine the results
    return left+right


def depunct(s):
    """
    Returns: s but with everything that is not a letter removed
    
    Parameter: s the string to edit
    Precondition s is a string
    """
    assert type(s) == str, repr(s) + ' is not a string' # get in the habit
    
    # Work on small data  (BASE CASE)
    if s == '':
        return s
    
    # Break up the data   (RECUSIVE CASE)
    left = s[0]
    if not introcs.isalpha(s[0]):
        left = ''
    right = depunct(s[1:])
    
    # Combine the results
    return left+right
