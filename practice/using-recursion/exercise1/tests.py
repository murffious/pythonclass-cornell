"""  
A completed test script for the recursive functions.

Author: Walker M. White
Date: July 30, 2019
"""
import funcs
import introcs


def test_hanoi():
    """
    Test procedure for the function hanoi()
    """
    print('Testing hanoi()')
    
    result = funcs.hanoi(1)
    introcs.assert_equals(1,result)
    
    result = funcs.hanoi(2)
    introcs.assert_equals(3,result)
    
    result = funcs.hanoi(3)
    introcs.assert_equals(7,result)
    
    result = funcs.hanoi(4)
    introcs.assert_equals(15,result)
    
    result = funcs.hanoi(5)
    introcs.assert_equals(31,result)
    
    result = funcs.hanoi(6)
    introcs.assert_equals(63,result)
    
    result = funcs.hanoi(7)
    introcs.assert_equals(127,result)


def test_lucas():
    """
    Test procedure for the function lucas()
    """
    print('Testing lucas()')
    
    result = funcs.lucas(0,1,-1)
    introcs.assert_equals(0,result)
    
    result = funcs.lucas(1,1,-1)
    introcs.assert_equals(1,result)
    
    result = funcs.lucas(2,1,-1)
    introcs.assert_equals(1,result)
    
    result = funcs.lucas(6,1,-1)
    introcs.assert_equals(8,result)
    
    result = funcs.lucas(6,2,-1)
    introcs.assert_equals(70,result)
    
    result = funcs.lucas(6,1,1)
    introcs.assert_equals(0,result)
    
    result = funcs.lucas(6,1,2)
    introcs.assert_equals(5,result)


if __name__ == '__main__':
    test_hanoi()
    test_lucas()
    print('Module funcs passed all tests.')