"""  
A function to check the validity of a numerical string

Author: Paul Murff
Date: 14 Jan 2020 
"""
import introcs


def valid_format(s):
    """
    Returns True if s is a valid numerical string; it returns False otherwise.
    
    A valid numerical string is one with only digits and commas, and commas only
    appear at every three digits.  In addition, a valid string only starts with
    a 0 if it has exactly one character.
    
    Pay close attention to the precondition, as it will help you (e.g. only numbers
    < 1,000,000 are possible with that string length).
    
    Examples: 
        valid_format('12') returns True
        valid_format('apple') returns False
        valid_format('1,000') returns True
        valid_format('1000') returns False
        valid_format('10,00') returns False
        valid_format('0') returns True
        valid_format('012') returns False
    
    Parameter s: the string to check
    Precondition: s is nonempty string with no more than 7 characters
    """
    if len(s) > 7:
        return False
    elif '0' in s and len(s) == 1:
        return True
    elif s[0] == '0' and len(s) > 1:
        return False
    elif introcs.isalpha(s):
        return False
    elif (len(s) > 3) and (introcs.count_str(s, ',') == 0):
        return False
    elif introcs.count_str(s, ',') == 0:
        return introcs.isdecimal(s)
    elif introcs.count_str(s, ',') > 1:
        return False
    elif ',' in s and introcs.count_str(s,',') == 1:
        comma_check = s[introcs.find_str(s, ',')+1:]
        before_comma_check = s[:introcs.find_str(s, ',')]
        introcs.isdecimal(before_comma_check)
        return (True if len(comma_check) == 3 else False) and introcs.isdecimal(before_comma_check)
  