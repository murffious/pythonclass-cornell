#!/usr/local/bin/python3
"""
Assess part 1, the remaining bugs in time_to_military

This file is insecurely available to students, but if they find it and modify it, they
really did not need this course.

Author: Walker M. White
Date:   July 31, 2018
"""
import verifier
import sys


def check_func2(file):
    """
    Checks that the remaining busg in time_to_military are fixed.
    
    Parameter file: The file to check
    Precondition: file is a string
    """
    result = verifier.grade_military(file,1)
    if not result[0]:
        print("The function 'time_to_military' appears to be correct.")
    return result[0]


if __name__ == '__main__':
    sys.exit(check_func2('funcs.py'))
