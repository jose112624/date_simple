import datetime as dt

SUPPORTED_FORMATS = { 'YYYY-MM-DD'  : '%Y-%m-%d',
                      'MM/DD/YYYY'  : '%m/%d/%Y',
                      'MM/DD/YY'    : '%m/%d/%y',
                      'DD-Mon-YYYY' : '%d-%b-%Y',
                      'DD-Mon-YY'   : '%d-%b-%y',
                      'YYYYMMDD'    : '%Y%m%d'  }

def get_date_object(date = None):
    """takes an optional string date and returns a date object
    if no argument a date object is returned with today's date"""
    if date is None:
        return dt.date.today()
    
    if not isinstance(date, str):
        raise TypeError('Input must be string')
    
    date_obj = None
    for format in SUPPORTED_FORMATS.values():
        try:
            date_obj = dt.datetime.strptime(date, format).date()
        except:
            continue
    
    if date_obj is None:
        raise ValueError('Not supported format. Supported formats:\n{}'.format(', '.join(SUPPORTED_FORMATS.keys())))
    return date_obj
    
    

def get_date_string(date_object = None, format = 'YYYY-MM-DD' ):
    """ takes an optional date object and returns a formatted string and an 
    optional format string"""
    if date_object is None:
        date_object = dt.date.today()
    
    if not isinstance(date_object, dt.date):
        raise TypeError('Input must be datetime.date')
    
    if format not in SUPPORTED_FORMATS.keys():
        raise ValueError('Not supported format. Supported formats:\n{}'.format(', '.join(SUPPORTED_FORMATS.keys())))

    if format is None:
        return dt.datetime.combine(date_object, dt.time()).strftime('%Y-%m-%d')
    else:
        return dt.datetime.combine(date_object, dt.time()).strftime(SUPPORTED_FORMATS[format])

def get_supported_formats():
    return SUPPORTED_FORMATS