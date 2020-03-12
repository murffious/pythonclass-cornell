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
    # Work on small data  (BASE CASE)
    if s == '':
        return s
    elif len(s) == 1:
        if s == ' ':
            return ''
        else:
            return s
    
    # Break up the data   (RECURSIVE CASE)
    left  = deblank(s[0])
    right = deblank(s[1:])

    # Combine the results
    return left+right


def depunct(s):
    """
    Returns: s but with everything that is not a letter removed
    
    Parameter: s the string to edit
    Precondition s is a string
    """
    # Work on small data  (BASE CASE)
    if s == '':
        return s
    elif len(s) == 1:
        if not introcs.isalpha(s[0]):
            return ''
        else:
            return s
    
    # Break up the data   (RECURSIVE CASE)
    left  = depunct(s[0])
    right = depunct(s[1:])
    
    # Combine the results
    return left+right
