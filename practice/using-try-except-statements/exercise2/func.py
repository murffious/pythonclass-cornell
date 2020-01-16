"""  
A function to test for floats in European format

Author: Paul Murff
Date: Jan 14 2020 
"""
import introcs


def iseurofloat(s):
    """
    Returns True if s is a float in European format.  Returns False otherwise.
    
    In European format, a comma is used in place of a decimal point.  So '12,5' stands
    for 12.5, '0,12' stands for 0.12 and so.  Formally, a string is in European format
    if it is of the form <d1>,<d2> where d1 and d2 are ints (and d2 >= 0).  See
        
        https://en.wikipedia.org/wiki/Decimal_separator
    
    for more information.
    
    This function does not recognize floats in scientific notation (e.g. '1e-2').
    
    Examples: 
        iseurofloat('12,5') returns True
        iseurofloat('-12,5') returns True
        iseurofloat('12') returns False
        iseurofloat('12,-5') returns False
        iseurofloat(',5') returns False
        iseurofloat('apple') returns False
        iseurofloat('12,5.3') returns False
        iseurofloat('12,5,3') returns False
        iseurofloat('1e-2') returns False
    
    Parameter s: The string to check
    Precondition: s is a string
    """
    # You MAY NOT use conditionals anywhere in this function.
  
    try:
        pos = introcs.index_str(s, ',')
        pos2 = introcs.find_str(s, ',',pos+1)
        d1 = int(s[:pos])
        d2 = int(s[pos+1:])
        check_d2 = d2 >= 0
        return True 
    except:
        return False