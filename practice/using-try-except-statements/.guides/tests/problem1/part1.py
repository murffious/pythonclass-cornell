#!/usr/local/bin/python3
"""
Assess part 1, the function time_to_minutes

This file is insecurely available to students, but if they find it and modify it, they
really did not need this course.

Author: Walker M. White
Date:   July 31, 2018
"""
import verifier
import sys


def check_func1(file):
    """
    Checks that time_to_minutes is correct.
    
    Parameter file: The file to check
    Precondition: file is a string
    """
    result = verifier.grade_minutes(file,0)
    if not result[0]:
        print("The function 'time_to_minutes' looks correct.")
    return result[0]


if __name__ == '__main__':
    sys.exit(check_func1('funcs.py'))
