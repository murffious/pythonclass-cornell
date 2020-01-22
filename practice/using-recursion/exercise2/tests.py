"""  
A completed test script for the recursive functions.

Author: Walker M. White
Date: July 30, 2019
"""
import funcs
import introcs


def test_prod():
    """
    Test procedure for the function prod()
    """
    print('Testing prod()')
    
    result = funcs.prod((5,))
    introcs.assert_equals(5,result)  
    
    result = funcs.prod((1,2,3,1)) 
    introcs.assert_equals(6,result)
    
    result = funcs.prod(()) 
    introcs.assert_equals(1,result)
    
    result = funcs.prod((7,12,1,2,2))
    introcs.assert_equals(336,result)
    
    result = funcs.prod((7,12,0,2,2))
    introcs.assert_equals(0,result)
    
    result = funcs.prod((1,1,1,1))
    introcs.assert_equals(1,result)


def test_replace():
    """
    Test procedure for the function replace()
    """
    print('Testing replace()')
    
    result = funcs.replace((5,),5,4)
    introcs.assert_equals((4,),result)  
    
    result = funcs.replace((1,2,3,1), 1, 4) 
    introcs.assert_equals((4,2,3,4),result)
    
    result = funcs.replace((1,2,3,1), 4, 1) 
    introcs.assert_equals((1,2,3,1),result)
    
    result = funcs.replace((), 1, 2)
    introcs.assert_equals((),result)
    
    result = funcs.replace((5, 3, 355, 74, 74, 74, 3),3,20)
    introcs.assert_equals((5, 20, 355, 74, 74, 74, 20),result) 
    
    result = funcs.replace((5, 3, 355, 74, 74, 74, 3),74,3)
    introcs.assert_equals((5, 3, 355, 3, 3, 3, 3),result) 


if __name__ == '__main__':
    test_prod()
    test_replace()
    print('Module funcs passed all tests.')