#!/usr/local/bin/python3
"""
Assess part 4, the final function call

This file is insecurely available to students, but if they find it and modify it, they
really did not need this course.

Author: Walker M. White
Date:   July 31, 2018
"""
import verifier
import sys


def check_script4(file):
    """
    Checks that the second assignment is correct
    
    Parameter file: The file to check
    Precondition: file is a string
    """
    result = verifier.grade_script(file,3)
    if not result[0]:
        print("The function call (and print) looks correct.")
    return result[0]


if __name__ == '__main__':
    sys.exit(check_script4('script.py'))
