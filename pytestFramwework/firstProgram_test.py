#1 Ant pytest file either must start with 'test' or end with 'test'
#2 Methods' name must begin with 'test'
#3 The entire code logic should be encapsulated in the method body

#4 -v --> Verbose, provides extra details regarding the test cases
#  -s --> Fof printing the entire contents from the test methods
#  -k --> For running the specific test methods from different files
#  -m --> For marking the test cases to run some specific ones only
#  We can declare any mark as a custom mark in pytest

#fixtures are used as setup and teardown methods for test cases- conftest file to generalize
#fixture and make it available to all test cases(givin fixture name into parameters of methods)

#data driven and parameterization can be done with return statemtents in tuple format
#When we define fixture scope to class only, it will run once before class is initiated and at the end

import pytest
@pytest.mark.skip
def test_firstFunction():
   #print("This is a pytest test function!")
    message = "Hello"
    assert message == "Hi", "The strings do not match!"

def test_secondFunction():
    #print("Into the second test function!")
    a = 4
    b = 6
    assert b-2 == a, "The values do not match!"


def test_shopping_cart():
    print("This is the shopping cart test case in 1st file")

@pytest.mark.PistonCup
def test_car():
    print("I am speed!")