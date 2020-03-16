"""
A simple function comparing datetime objects.

Author: Paul Murff
Date:   Mar 10 2020
"""
import datetime


def is_before(d1,d2):
    """
    Returns True if event d1 happens before d2.
    
    Values d1 and d2 can EITHER be date objects or datetime objects.If a date object,
    assume that it happens at midnight of that day. 
    
    Parameter d1: The first event
    Precondition: d1 is EITHER a date object or a datetime object
    
    Parameter d2: The first event
    Precondition: d2 is EITHER a date object or a datetime object
    """
    # HINT: Check the type of d1 or d2. If not a datetime, convert it for comparison

    if type(d1) == type(d2) and type(d1)== datetime.date:
        return datetime.datetime(d1.year, d1.month, d1.day,0 ) < datetime.datetime(d2.year, d2.month, d2.day,0)
    elif type(d1) != type(d2):
        if type(d1) == datetime.date:
            return datetime.datetime(d1.year, d1.month, d1.day,0 ) < d2
        if type(d2) == datetime.date:
            return d1 < datetime.datetime(d2.year, d2.month, d2.day,0 )
    else:
        return d1 < d2