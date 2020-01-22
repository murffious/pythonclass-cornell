"""
A function to find all instances of a substring.

This function is not unlike a 'find-all' option that you might see in a text editor.

Author: Paul Murff
Date: 21 Jan 2020 
"""
import introcs


def findall(text,sub):
    """
    Returns the tuple of all positions of substring sub in text.
    
    If sub does not appears anywhere in text, this function returns the empty tuple ().
    
    Examples:
        findall('how now brown cow','ow') returns (1, 5, 10, 15)
        findall('how now brown cow','cat') returns ()
        findall('jeeepeeer','ee') returns (1,2,5,6)
    
    Parameter text: The text to search
    Precondition: text is a string
    
    Parameter sub: The substring to search for
    Precondition: sub is a nonempty string
    """
    positions = ()
    going = True  
    pos = 0
    while going:
        temp = ''
        pos = introcs.find_str(text, sub,pos)
        if pos != -1:
            positions = positions + (pos,)
            pos+=1
        temp = text[pos+1:]
        if pos == -1:
            going = False 
    return positions    