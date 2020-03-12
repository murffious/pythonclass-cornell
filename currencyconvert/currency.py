"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: Paul Murff
Date: Dec 11 2019
"""

import introcs

APIKEY = 'O2bnuSqiTe7aSGmFJGvy10eZCEIBpBRfOw4bmsou9Jge'


def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    
    assert introcs.count_str(s, ' ') >= 1, 'Precondition not met'
    
    space_one_index = introcs.find_str(s, ' ')
    before = s[:space_one_index]
    return before


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: before_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    
    assert introcs.count_str(s, ' ') >= 1, 'Precondition not met'

    
    space_one_index = introcs.find_str(s, ' ')
    after = s[space_one_index+1:]
    return after


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a 
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only 
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """
    
    assert introcs.count_str(s, '"') >= 2, 'Precondition not met'

    first_quotes = introcs.find_str(s, '"')
    second_quotes = introcs.find_str(s, '"',first_quotes+1)
    inside_fun = s[first_quotes+1:second_quotes]
    return inside_fun


def get_src(json):
    """
    Returns the src value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"src"'. For example,
    if the json is
    
        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '2 United States Dollars' (not '"2 United States Dollars"'). 
    On the other hand if the json is 
    
        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON
    
        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
    
    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    
    assert type(json) == str
    
    
    src_index = introcs.find_str(json, '"src"')
    src = json[src_index+5:]
    src_inner = first_inside_quotes(src)
    return src_inner


def get_dst(json):
    """
    Returns the dst value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"dst"'. For example,
    if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '1.772814 Euros' (not '"1.772814 Euros"'). On the other
    hand if the json is 

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    dst_index = introcs.find_str(json, '"dst"')
    dst = json[dst_index+5:]
    dst_inner = first_inside_quotes(dst)
    return dst_inner
    
    
def has_error(json):
    """
    Returns True if the response to a currency query encountered an error.

    Given a JSON string provided by the web service, this function returns True if the
    query failed and there is an error message. For example, if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns True (It does NOT return the error message 
    'Source currency code is invalid'). On the other hand if the json is 

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns False.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    
    error_index = introcs.find_str(json, '"error"')
    error_obj = json[error_index+7:]
    error_inner = first_inside_quotes(error_obj)
    error_str = len(error_inner)
    return error_str > 0


def service_response(src, dst, amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the currency dst. The response 
    should be a string of the form

        '{"success": true, "src": "<src-amount>", dst: "<dst-amount>", error: ""}'

    where the values src-amount and dst-amount contain the value and name for the src 
    and dst currencies, respectively. If the query is invalid, both src-amount and 
    dst-amount will be empty, and the error message will not be empty.

    There may or may not be spaces after the colon.  To test this function, you should
    chose specific examples from your web browser.

    Parameter src: the currency on hand
    Precondition src is a nonempty string with only letters

    Parameter dst: the currency to convert to
    Precondition dst is a nonempty string with only letters

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """
    
    # Precondition 1
    assert introcs.isalpha(src)
    
    
    # Precondition 2
    assert introcs.isalpha(dst)

    
    # Precondition 3
    assert type(amt) == int or type(amt)  == float
    
    
    q = 'https://ecpyfac.ecornell.com/python/currency/fixed?' +\
        'src=' + src + '&' +\
        'dst=' + dst + '&'+\
        'amt=' + str(amt) +\
        '&key=' + (APIKEY)
        
    res = introcs.urlread(q)
    return res


def iscurrency(currency):
    """
    Returns True if currency is a valid (3 letter code for a) currency.

    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a nonempty string with only letters
    """
    
    assert introcs.isalpha(currency)
    
    currency_list_url = 'https://openexchangerates.org/api/currencies.json'
    res = introcs.urlread(currency_list_url)
    check_result = currency in res
    return check_result


def exchange(src, dst, amt):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency src to the currency 
    dst. The value returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter src: the currency on hand
    Precondition src is a string for a valid currency code

    Parameter dst: the currency to convert to
    Precondition dst is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """
    
    assert type(src) == str and type(dst) == str
    
    valid_src = iscurrency(src) 
    valid_dst = iscurrency(dst) 
    
    assert valid_src
    assert valid_dst
    assert type(amt) == int or type(amt) == float
    
    res = service_response(src, dst, amt)
    
    assert not has_error(res) == True 
    amt_exchanged = before_space(get_dst(res))
   
    return float(amt_exchanged)
  