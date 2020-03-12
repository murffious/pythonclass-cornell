"""  
A test script for the function iso_8601.

Author: Paul Murff
Date: Jan 14 2020 
"""
import func
import introcs


def test_iso_8601():
    """
    Test procedure for the function iso_8601()
    """
    print('Testing iso_8601()')
    
    # Put your test cases here    
    result = func.iso_8601('12:12:12')
    introcs.assert_equals(True,result)

    result = func.iso_8601('1:12:12')
    introcs.assert_equals(True,result)

    result = func.iso_8601('222:12:12')
    introcs.assert_equals(False,result)
    
    result = func.iso_8601('12:212:12')
    introcs.assert_equals(False,result)
    
    result = func.iso_8601('12:21:123')
    introcs.assert_equals(False,result)
    
    result = func.iso_8601('')
    introcs.assert_equals(False,result)
    
    result = func.iso_8601(':21:1')
    introcs.assert_equals(False,result)
    
    result = func.iso_8601('12::12')
    introcs.assert_equals(False,result)
    
    result = func.iso_8601('12:21:')
    introcs.assert_equals(False,result)
    
    result = func.iso_8601('22:1:8')
    introcs.assert_equals(False,result)
    
if __name__ == '__main__':
    test_iso_8601()
    print('Module func passed all tests.')