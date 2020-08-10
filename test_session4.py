import pytest
import inspect
#from test_utils import *
import re

import session4

num = 256
x = 1

def test_fourspace():


    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert re.search('[a-zA-Z#@\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@\n\"\']', '', space)) % 4 == 0, \
        "Your code intentation does not follow PEP8 guidelines" 
    
def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
    
def test_qualean_repr():
    r = session4.Qualean(x)
    assert r.__repr__() == f'Qualean({x})', 'The representation of the Qualean object does not meet expectations'

def test_qualean_str():
    r = session4.Qualean(x)
    assert r.__str__() == f'Qualean: Num = {x}', 'The print of the Qualean object does not meet expectations'

def test_Qualean_input():    
    with pytest.raises(ValueError) as e_info:
        r = session4.Qualean(num)

QUALEAN_FUNCTION_CHECK_FOR = [
    'and',
    'or',
    'repr',
    'str',
    'add',
    'eq',
    'float',
    'ge',
    'gt',
    'invertsign',
    'le',
    'lt',
    'mul',
    'sqrt',
    'bool'
]

def test_qualean_functions_avaiable():
    QUALEANFUNCTIONSAVAILABLE = True
    f = open("session4.py", "r")
    content = f.read()
    f.close()
    for c in QUALEAN_FUNCTION_CHECK_FOR:
        if c not in content:
            QUALEANFUNCTIONSAVAILABLE = False
            pass
    assert QUALEANFUNCTIONSAVAILABLE == True, "You have not implemented all the functions in your Qualean class"
    
def test_add_equals_multiply():
    obj = session4.Qualean(1)
    value = obj.__magic_num__()
    mul = value * 100
    for i in range(100):
        value =+ value
    assert mul == value, "Adding a value 100 times does not equal to multiplying value with 100"
    

        
    
        
    
