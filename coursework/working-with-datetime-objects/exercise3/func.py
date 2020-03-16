"""
A simple function computing time elapsed

Author: Paul Murff
Date:   Mar 11 2020
"""
import datetime


def past_a_week(d1,d2):
    """
    Returns True if event d2 happens at least a week (7 days) after d1.
    
    If d1 is after d2, or less than a week has passed, this function returns False.
    Values d1 and d2 can EITHER be date objects or datetime objects.If a date object,
    assume that it happens at midnight of that day. 
    
    Parameter d1: The first event
    Precondition: d1 is EITHER a date objects or a datetime object
    
    Parameter d2: The first event
    Precondition: d2 is EITHER a date objects or a datetime object
    """
    # HINT: Check the type of d1 or d2. If not a datetime, convert it for comparison
    if type(d1) == type(d2) and type(d1)== datetime.date:
        f =  datetime.datetime(d2.year, d2.month, d2.day,0) - datetime.datetime(d1.year, d1.month, d1.day,0 )
        return f.days >= 7
    elif type(d1) != type(d2):
        if type(d1) == datetime.date:
            f = d2 - datetime.datetime(d1.year, d1.month, d1.day,0 ) 
            return f.days >= 7
        if type(d2) == datetime.date:
            datetime.datetime(d2.year, d2.month, d2.day,0 ) - d1
            return f.days >= 7
    else:
        return (d2-d1).days >= 7
