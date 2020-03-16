"""
Functions for parsing time values and determining daylight hours.

Both of these functions will be used in the main project.  You should hold on to them.

Author: Paul Murff
Date:   Mar 12 2020
"""
import datetime
import pytz
from dateutil.parser import parse
from dateutil import tz

def str_to_time(timestamp,tz=None):
    """
    Returns the datetime object for the given timestamp (or None if stamp is invalid)
    
    This function should just use the parse function in dateutil.parser to
    convert the timestamp to a datetime object.  If it is not a valid date (so
    the parser crashes), this function should return None.
    
    If the timestamp has a timezone, then it should keep that timezone even if
    the value for tz is not None.  Otherwise, if timestamp has no timezone and 
    tz if not None, this this function will assign that timezone to the datetime 
    object. 
    
    The value for tz can either be a string or a time OFFSET. If it is a string, 
    it will be the name of a timezone, and it should localize the timestamp. If 
    it is an offset, that offset should be assigned to the datetime object.
    
    Parameter timestamp: The time stamp to convert
    Precondition: timestamp is a string
    
    Parameter tz: The timezone to use (OPTIONAL)
    Precondition: tz is either None, a string naming a valid time zone,
    or a time zone OFFSET.
    """
    # HINT: Use the code from the previous exercise and update the timezone
    # Use localize if timezone is a string; otherwise replace the timezone if not None
    try:
        d = parse(timestamp)
        if d.tzinfo is None and tz is not None:
            if type(tz) == str:
                timezone_work = pytz.timezone(tz).localize(d)
                return datetime.datetime(d.year, d.month, d.day, d.hour, d.minute, d.second, tzinfo=timezone_work.tzinfo)

            else:    
                return datetime.datetime(d.year, d.month, d.day, d.hour, d.minute, d.second, tzinfo=tz)

        if d.tzinfo is None:
            return datetime.datetime(d.year, d.month, d.day, d.hour, d.minute, d.second)


        if d.tzinfo is not None:
            e = d.replace(tzinfo=d.tzinfo)   
            return datetime.datetime(e.year, e.month, e.day, e.hour, e.minute, e.second, tzinfo=e.tzinfo)
    except:
        return 

    

    


def daytime(time,daycycle):
    """
    Returns true if the time takes place during the day.
    
    A time is during the day if it is after sunrise but before sunset, as
    indicated by the daycycle dicitionary.
    
    A daycycle dictionary has keys for several years (as int).  The value for
    each year is also a dictionary, taking strings of the form 'mm-dd'.  The
    value for that key is a THIRD dictionary, with two keys "sunrise" and
    "sunset".  The value for each of those two keys is a string in 24-hour
    time format.
    
    For example, here is what part of a daycycle dictionary might look like:
    
        "2015": {
            "01-01": {
                "sunrise": "07:35",
                "sunset":  "16:44"
            },
            "01-02": {
                "sunrise": "07:36",
                "sunset":  "16:45"
            },
            ...
        }
    
    In addition, the daycycle dictionary has a key 'timezone' that expresses the
    timezone as a string. This function uses that timezone when constructing
    datetime objects from this set.  If the time parameter does not have a timezone,
    we assume that it is in the same timezone as the daycycle dictionary
    
    Parameter time: The time to check
    Precondition: time is a datetime object
    
    Parameter daycycle: The daycycle dictionary
    Precondition: daycycle is a valid daycycle dictionary, as described above
    """
    # HINT: Use the code from the previous exercise to get sunset AND sunrise
    # Add a timezone to time if one is missing (the one from the daycycle)
#    sunset = ''
#    sunrise = ''

    
#    days_l = list(daycycle.items())
#    days_only = dict(days_l[5:])
#    tz_dict = days_l[4][1]
#    tzone = tz.gettz(tz_dict)
#    print('tzone',tzone)
#    for p_year, p_day in days_only.items():       
#        if int(p_year) == time.year:
#            for key in p_day:
#                if key == time.strftime("%m-%d"):
#                     print('incoming tz:',time.tzinfo, )
#                    sunset = p_day[key]["sunset"]
#                    sunrise = p_day[key]["sunrise"]
#                     print(type(sunrise), type(sunset), type(time.strftime("%H:%M")))
#                     print(sunset, sunrise, time.strftime("%H:%M"))
#                     sunrise_t = datetime.datetime.strptime(sunrise,'%H:%M')
#                     sunset_t = datetime.datetime.strptime(sunset,'%H:%M')
#                     incoming_t = datetime.datetime.strptime(time.strftime("%H:%M"),'%H:%M')
#                     tzinfo=days_l[4][1]
#                    incoming = time.strftime("%m-%d")
#                    sunrise_t = datetime.datetime.combine(datetime.date(int(p_year), int(time.month), int(time.day)), datetime.time(int(p_day[key]["sunset"][:2]),int(p_day[key]["sunset"][3:])))
#                    sunset_t = datetime.datetime.combine(datetime.date(int(p_year), int(time.month), int(time.day)), datetime.time(int(p_day[key]["sunrise"][:2]),int(p_day[key]["sunrise"][3:])))
#                    incoming_t = datetime.datetime.combine(datetime.date(int(p_year), int(time.month), int(time.day)), datetime.time(int(incoming[:2]),int(incoming[3:])))
#                    print('sunset', sunset_t,'sunrise',sunrise_t,'incoming',incoming_t)
    
#                    if incoming_t > sunrise_t and incoming_t < sunset_t: 
#                        return True
#                    else:
#                        return False

    import pytz
    year  = str(time.year)


    day  = None
    data = daycycle[year]
    key  = '%02d-%02d' % (time.month,time.day)


    day = data[key]
    tz  = daycycle['timezone']
    rise = str_to_time(year+'-'+key+'T'+day['sunrise'],tz)
    sets = str_to_time(year+'-'+key+'T'+day['sunset'],tz)

    if time.tzinfo is None:
        time = pytz.timezone(tz).localize(time)

    return rise < time < sets


