"""
Functions demonstrating string methods.

Neither this module nor any of these functions should import the introcs module.
In addition, you are not allowed to use loops or recursion in either function.

Author: Paul Murff
Date: Feb 6 2020 
"""


def first_in_parens(s):
    """
    Returns: The substring of s that is inside the first pair of parentheses.
    
    The first pair of parenthesis consist of the first instance of character
    '(' and the first instance of ')' that follows it.
    
    Examples: 
        first_in_parens('A (B) C') returns 'B'
        first_in_parens('A (B) (C)') returns 'B'
        first_in_parens('A ((B) (C))') returns '(B'
    
    Parameter s: a string to check
    Precondition: s is a string with a matching pair of parens '()'.
    """
    left_p = s.find('(')
    right_p = s.find(')')
    if right_p < left_p:
        right_p = s[left_p:].find(')')
        right_p += left_p
    return s[left_p+1:right_p]


def isnetid(s):
    """
    Returns True if s is a valid Cornell netid.
    
    Cornell network ids consist of 2 or 3 lower-case initials followed by a 
    sequence of digits.
    
    Examples:
        isnetid('wmw2') returns True
        isnetid('2wmw') returns False
        isnetid('ww2345') returns True
        isnetid('w2345') returns False
        isnetid('WW345') returns False
    
    Parameter s: the string to check
    Precondition: s is a string
    """
    return s[:3].islower() and s.isalnum() and (s[3:].isdigit() or s[2:].isdigit())
