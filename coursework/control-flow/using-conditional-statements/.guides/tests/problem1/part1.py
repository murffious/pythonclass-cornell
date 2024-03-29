#!/usr/local/bin/python3
"""
Assess part 1, the vowel 'a'

This file is insecurely available to students, but if they find it and modify it, they
really did not need this course.

Author: Walker M. White
Date:   July 31, 2018
"""
import verifier
import sys


def check_func1(file):
    """
    Checks that the function works for 'a'.
    
    Parameter file: The file to check
    Precondition: file is a string
    """
    result = verifier.grade_func(file,0)
    if not result[0]:
        print("The function appears to work for vowel 'a'.")
    return result[0]


if __name__ == '__main__':
    sys.exit(check_func1('func.py'))
