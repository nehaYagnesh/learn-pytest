import pytest

"""
This module contains basic unit tests for math operations
to understand pytest framework
"""

#--------------------------------------------------------
# A most basic test function
#--------------------------------------------------------

@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 == 2

#---------------------------------
# A test function to show assertion introspection
#---------------------------------

@pytest.mark.math
def test_one_plus_two():
    a=1
    b=2
    c=3
    assert a+b==c

#------------------------------------
# A test function that verifies an exception
#------------------------------------

@pytest.mark.math
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
     num = 1/0 
    
    assert 'division by zero' in str(e.value)

#------------------------------------
# Multiplication test ideas

# two positive integers
# Indentity : multiplying any number by 1
# Zero : multiplying any number by 0
# positive by a negative
# negative by a negative
# multiply floats
#-------------------------------------
"""
def test_multiply_two_positive_ints():
    assert 2*3==6

def test_multiply_identity():
    assert 1*99==99

def test_multiply_zero():
    assert 0*100==0

#DRY Principle : Don't Repeat Yourself!
"""

#---------------------------------------
# A parameterized test function
#---------------------------------------

products={
    (2,3,6),   #two positive integers
    (1,99,99), #Indentity : multiplying any number by 1
    (0,100,0), # Zero : multiplying any number by 0
    (-3,4,-12), #positive by a negative
    (-5,-4,20), #negative by a negative
    (2.5,6.7,16.75) #floats
}
@pytest.mark.math
@pytest.mark.parametrize('a,b,product',products)
def test_multiplication(a,b,product):
    assert a * b == product