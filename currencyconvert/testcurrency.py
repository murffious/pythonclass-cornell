"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Paul Murff
Date: Dec 11 2019
"""

import introcs
import currency


def test_before_space():
    """Test procedure for before_space"""
    print('Testing before_space') 
    
    
    # Test case 1
    result = currency.before_space('0.863569 Euros')
    introcs.assert_equals('0.863569',result)
    
    
    # Test case 2
    result = currency.before_space('0.863569  Euros')
    introcs.assert_equals('0.863569',result)
    
    
    # Test case 3
    result = currency.before_space(' 0.863569 Euros ')
    introcs.assert_equals('',result)
    
    
    # Test case 4
    result = currency.before_space('0.863569 Euros           ff')
    introcs.assert_equals('0.863569',result)
    
    
    # Test case 5
    result = currency.before_space(' ')
    introcs.assert_equals('',result)
    
    
def test_after_space(): 
    """Test procedure for after_space"""
    print('Testing after_space') 
     
        
    # Test case 1
    result = currency.after_space('5454 ABC')
    introcs.assert_equals('ABC',result)
    
    
    # Test case 2
    result = currency.after_space('A BC')
    introcs.assert_equals('BC',result)
    
    
    # Test case 3
    result = currency.after_space(' ABC 67')
    introcs.assert_equals('ABC 67',result)
    
    
    # Test case 4
    result = currency.after_space('  ABC ')
    introcs.assert_equals(' ABC ',result)
    
    
    # Test case 5
    result = currency.after_space('  ABC sdf 3434    ')
    introcs.assert_equals(' ABC sdf 3434    ',result)
    
    
    # Test case 6
    result = currency.after_space(' ')
    introcs.assert_equals('',result)
    
    
def test_first_inside_quotes(): 
    """Test procedure for first_inside_quotes"""
    print('Testing first_inside_quotes') 
    
    
    # Test case 1
    result = currency.first_inside_quotes('A "B C" D')
    introcs.assert_equals('B C',result)
    
    
    # Test case 2
    result = currency.first_inside_quotes('"ACB"')
    introcs.assert_equals('ACB',result)
    
    
    # Test case 3
    result = currency.first_inside_quotes('ACB "1" .   ')
    introcs.assert_equals('1',result)
    
    
    # Test case 4
    result = currency.first_inside_quotes('"ABC" test "CDE"')
    introcs.assert_equals('ABC',result)
    
    
    # Test case 5
    result = currency.first_inside_quotes('  "ABC" "sdf" "3434"    ')
    introcs.assert_equals('ABC',result)
    
    
    # Test case 6
    result = currency.first_inside_quotes('""')
    introcs.assert_equals('',result)
    
    
def test_get_src():  
    """Test procedure for get_src"""
    print('Testing get_src')
    
    # Test case 1
    result = currency.get_src('{"success": true, "src": "2 United States Dollars",' +\
                                '"dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars',result)
    
    
    # Test case 2
    result = currency.get_src('{"success": true, "src":" 2 United States Dollars ",' +\
                              '"dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals(' 2 United States Dollars ',result)
    
    
    # Test case 3
    result = currency.get_src('{"success":false,"src":"","dst":"",' +\
                              '"error":"Source currency code is invalid."}')
    introcs.assert_equals('',result)
    
    
    # Test case 4
    result = currency.get_src('{"success":false,"src": "","dst":"",' +\
                              '"error":"Source currency code is invalid."}')
    introcs.assert_equals('',result)
  
    
def test_get_dst(): 
    """Test procedure for get_dst"""
    print('Testing get_dst') 

    
     # Test case 1
    result = currency.get_dst('{"success":false,"src": "2 United States Dollars",' +\
                              '"dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros',result)
    
    
    # Test case 2
    result = currency.get_dst('{"success":false,"src":" 2 United States Dollars ",' +\
                              '"dst":"1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros',result)
    
    
    # Test case 3
    result = currency.get_dst('{"success":false,"src":"","dst": "",' +\
                              '"error":"Source currency code is invalid."}')
    introcs.assert_equals('',result)
    
    
    # Test case 4
    result = currency.get_dst('{"success":false,"src": "","dst":"",' +\
                              '"error":"Source currency code is invalid."}')
    introcs.assert_equals('',result)
  
    
def test_has_error(): 
    """Test procedure for has_error"""
    print('Testing has_error') 
    
    
    # Test case 1
    result = currency.has_error('{"success":false,"src": "2 United States Dollars", ' +\
                                '"dst": "1.772814 Euros", "error":""}')
    introcs.assert_equals(False,result)
    
    
    # Test case 2
    result = currency.has_error('{"success":false,"src":" 2 United States Dollars ",' +\
                                '"dst":"1.772814 Euros", "error": ""}')
    introcs.assert_equals(False,result)
    
    
    # Test case 3
    result = currency.has_error('{"success":false,"src":"","dst": "",' +\
                                '"error":"Source currency code is invalid."}')
    introcs.assert_equals(True,result)
    
    
    # Test case 4
    result = currency.has_error('{"success":false,"src": "","dst":"", ' +\
                                '"error": "Source currency code is invalid."}')
    introcs.assert_equals(True,result)
  
    
def test_service_response(): 
    """Test procedure for service_response"""
    print('Testing service_response') 


    # Test case 1
    result = currency.service_response('USD', 'EUR', 2)
    introcs.assert_equals('{"success": true, "src": "2.0 United States Dollars", ' +\
                          '"dst": "1.772814 Euros", "error": ""}',result)
    
    
    # Test case 2
    result = currency.service_response('USD', 'Euros', 2)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", ' +\
                          '"error": "The rate for currency EUROS is not present."}',result)
    
    
    # Test case 3
    result = currency.service_response('USD', 'BTC', -2)
    introcs.assert_equals('{"success": true, "src": "-2.0 United States Dollars", ' +\
                          '"dst": "-0.00017878293 Bitcoins", "error": ""}',result)
    
    
    # Test case 4
    result = currency.service_response('US', 'Euros', 2.5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", ' +\
                          '"error": "The rate for currency US is not present."}',result)
  

def test_iscurrency(): 
    """Test procedure for iscurrency"""
    print('Testing iscurrency') 
    
    
    # Test case 1
    result = currency.iscurrency('USD')
    introcs.assert_equals(True,result)
    
    
    # Test case 2
    result = currency.iscurrency('Euros')
    introcs.assert_equals(False,result)
    
    
def test_exchange(): 
    """Test procedure for exchange"""
    print('Testing exchange')  

    
    # Test case 1
    result = currency.exchange('USD', 'EUR', 2)
    introcs.assert_floats_equal(1.772814,result)
    
    
    # Test case 2
    result = currency.exchange('USD', 'BTC', -2)
    introcs.assert_floats_equal(-0.00017878293,result)
    
    
test_before_space()
test_after_space() 
test_first_inside_quotes()  
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()
    
print('All tests completed succesfully')