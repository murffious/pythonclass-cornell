#!/usr/local/bin/python3
"""
Assess part 4, adding a limiter to partition

This file is insecurely available to students, but if they find it and modify it, they
really did not need this course.

Author: Walker M. White
Date:   July 31, 2018
"""
import verifier
import sys


def check_func4(file):
    """
    Checks that the function partition has limiting code
    
    Parameter file: The file to check
    Precondition: file is a string
    """
    result = verifier.verify_trace2(file,0)
    if not result[0]:
        print("The limiting code looks correct.")
    return result[0]


if __name__ == '__main__':
    sys.exit(check_func4('funcs.py'))
