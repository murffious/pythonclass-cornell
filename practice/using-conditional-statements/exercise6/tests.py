"""  
A completed test script for the Pig Latin module.

Author: Paul Murff
Date: Jan 14 2020 
"""
import funcs
import introcs


def test_first_vowel():
    """
    Test procedure for the function first_vowel()
    """
    print('Testing first_vowel()')
    # No vowels
    result = funcs.first_vowel('grrm')
    introcs.assert_equals(-1,result)
    
    # Letter a
    result = funcs.first_vowel('pat')
    introcs.assert_equals(1,result)
    
    # Letter e
    result = funcs.first_vowel('step')
    introcs.assert_equals(2,result)
    
    # Letter i
    result = funcs.first_vowel('strip')
    introcs.assert_equals(3,result)
    
    # Letter o
    result = funcs.first_vowel('stop')
    introcs.assert_equals(2,result)
    
    # Letter u
    result = funcs.first_vowel('truck')
    introcs.assert_equals(2,result)
    
    # Letter y, not a vowel
    result = funcs.first_vowel('ygglx')
    introcs.assert_equals(-1,result)
    
    # Letter y as vowel
    result = funcs.first_vowel('sky')
    introcs.assert_equals(2,result)
    
    # Various multi-vowel combinations
    result = funcs.first_vowel('apple')
    introcs.assert_equals(0,result)
    
    result = funcs.first_vowel('sleep')
    introcs.assert_equals(2,result)
    
    result = funcs.first_vowel('year')
    introcs.assert_equals(1,result)
    
    # Feel free to add more


def test_pigify():
    """
    Test procedure for the function pigify()
    """
    print('Testing pigify()')
    result = funcs.pigify('grrm')
    introcs.assert_equals('grrmay',result)
    
    # Letter a
    result = funcs.pigify('pat')
    introcs.assert_equals('atpay',result)
    
    # Letter e
    result = funcs.pigify('step')
    introcs.assert_equals('epstay',result)
    
    # Letter i
    result = funcs.pigify('strip')
    introcs.assert_equals('ipstray',result)
    
    # Letter o
    result = funcs.pigify('stop')
    introcs.assert_equals('opstay',result)
    
    # Letter u
    result = funcs.pigify('truck')
    introcs.assert_equals('ucktray',result)
    
    # Letter y, not a vowel
    result = funcs.pigify('ygglx')
    introcs.assert_equals('ygglxay',result)
    
    # Letter y as vowel
    result = funcs.pigify('sky')
    introcs.assert_equals('yskay',result)
    
    # Various multi-vowel combinations
    result = funcs.pigify('apple')
    introcs.assert_equals('applehay',result)
    
    result = funcs.pigify('sleep')
    introcs.assert_equals('eepslay',result)
    
    result = funcs.pigify('year')
    introcs.assert_equals('earyay',result)
    
    # qu
    result = funcs.pigify('queen')
    introcs.assert_equals('eenquay',result) 
    
    
test_first_vowel()
test_pigify()
print('Module funcs passed all tests.')