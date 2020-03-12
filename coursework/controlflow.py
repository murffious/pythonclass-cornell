"""  
A function to search for the first vowel position

Author: Paul Murff
Date: Jan 8 2020
"""
import introcs


def first_vowel(s):
    """
    Returns the position of the first vowel in s; it returns len(s) if there are no vowels.
    
    We define the vowels to be the letters 'a','e','i','o', and 'u'.  The letter
    'y' counts as a vowel only if it is not the first letter in the string.
    
    Examples: 
        first_vowel('hat') returns 1
        first_vowel('grrm') returns 4
        first_vowel('sky') returns 2
        first_vowel('year') returns 1
    
    Parameter s: the string to search
    Precondition: s is a nonempty string with only lowercase letters
    """
    result = len(s)     #  In case there is no 'a'

    if 'a' in s:
        result = introcs.find_str(s,'a')
        
    if 'e' in s and (introcs.find_str(s,'e') < result):
        result = introcs.find_str(s,'e')
    
    if 'i' in s and (introcs.find_str(s,'i') < result):
        result = introcs.find_str(s,'i')
        
    if 'o' in s and (introcs.find_str(s,'o') < result):
        result = introcs.find_str(s,'o')
    
    if 'u' in s and (introcs.find_str(s,'u') < result):
        result = introcs.find_str(s,'u')
    
    if 'y' in s and introcs.find_str(s,'y',1) != -1 and introcs.find_str(s,'y',1) < result:
        result = introcs.find_str(s,'y',1)
        
    return result