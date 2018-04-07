import pytest
import date_simple as ds
import datetime as dt

def test_get_date_object_no_args():
    """Assert that if date_simple.get_date_object() is called with no
    arguments, it will return a date object for today.
    """
    assert ds.get_date_object() == dt.date.today()
    
def test_get_date_object():
    """Assert that if date_simple.get_date_object() is called with a properly
    formatted date string, it will return a date object for that date.
    """
    assert ds.get_date_object('2018-01-01') == dt.date(2018,1,1)
    
def test_get_date_object_value_error():
    """Assert that if date_simple.get_date_object() is called with an
    improperly formatted string date, it will raise a ValueError exception.
    """
    with pytest.raises(ValueError):
        ds.get_date_object('01-2018-01')

def test_get_date_object_type_error():
    """Assert that if date_simple.get_date_object() is called with an object
    that is not type str, it will raise a TypeError exception.
    """
    with pytest.raises(TypeError):
        ds.get_date_object(2018)

def test_get_date_string_no_args():
    """Assert that if date_simple.get_date_string() is called with no
    arguments, it will return a date string for today.
    """
    assert ds.get_date_string() == str(dt.date.today())

def test_get_date_string():
    """Assert that if date_simple.get_date_string() is called with a date
    object, it will return the date string for that date.
    """
    assert ds.get_date_string(date_object = dt.date.today()) ==  \
           str(dt.date.today()) 

def test_get_date_string_format_01():
    """Assert that if date_simple.get_date_string() is called with a supported
    format, it will return a date string in that format.
    """
    assert  ds.get_date_string(date_object = dt.date(2018,1,31), format = 'YYYY-MM-DD' ) == "2018-01-31"

def test_get_date_string_format_02():
    assert  ds.get_date_string(date_object = dt.date(2018,1,31), format = 'MM/DD/YYYY' ) == "01/31/2018"

def test_get_date_string_format_03():
    assert  ds.get_date_string(date_object = dt.date(2018,1,31), format = 'MM/DD/YY'   ) == "01/31/18"

def test_get_date_string_format_04():
    assert  ds.get_date_string(date_object = dt.date(2018,1,31), format = 'DD-Mon-YYYY' ) == "31-Jan-2018"  

def test_get_date_string_format_05():
    assert  ds.get_date_string(date_object = dt.date(2018,1,31), format = 'DD-Mon-YY' ) == "31-Jan-18"

def test_get_date_string_format_06():
    assert  ds.get_date_string(date_object = dt.date(2018,1,31), format = 'YYYYMMDD'  ) == "20180131"               
                
def test_get_date_string_type_error():
    """Assert that if date_simple.get_date_string() is called with an object
    that is not type datetime.date, it will raise a TypeError exception.
    """
    with pytest.raises(TypeError):
        ds.get_date_string(date_object = 2018)                


def test_get_date_string_format_value_error():
    """Assert that if date_simple.get_date_string() is called with a format
    that is not supported, it will raise a ValueError exception.
    """
    with pytest.raises(ValueError):
        ds.get_date_string(format = 'YYYY')                
        