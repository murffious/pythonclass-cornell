"""
Functions for simple reading to and writing from a file.

Author: Paul Murff
Date:   March 4 2020
"""


def count_lines(filepath):
    """
    Returns the number of lines in the given file.
    
    Lines are separated by the '\n' character, which is standard for Unix files.
    
    Parameter filepath: The file to be read
    Precondition: filepath is a string with the FULL PATH to a text file
    """
    # HINT: Remember, you can use a file in a for-loop
   
    acum = 0
    with open(filepath, 'r') as f:
        for line in f:
            acum += 1
    
    return acum

def write_numbers(filepath,n):
    """
    Writes the numbers 0..n-1 to a file.
    
    Each number is on a line by itself.  So the first line of the file is 0,
    the second line is 1, and so on. Lines are separated by the '\n' character, 
    which is standard for Unix files.  The last line (the one with the number
    n-1) should NOT end in '\n'
    
    Parameter filepath: The file to be written
    Precondition: filepath is a string with the FULL PATH to a text file
    
    Parameter n: The number of lines to write
    Precondition: n is an int > 0.
    """
    # HINT: You can only write strings to a file, so convert the numbers first
    file = open(filepath, 'a')
    count = 0 
    file.write(str(count)+ '\n')
    while count < n-1:
        count += 1
        if count == n-1:
            file.write(str(count))
        else:
            file.write(str(count)+ '\n')

    file.close()
 