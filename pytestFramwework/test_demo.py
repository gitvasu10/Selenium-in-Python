import pytest

def test_demoFunction():
    print('Hello!')

def test_shopping():
    print("This is the test case for shopping cart in the second file!")

@pytest.mark.PistonCup
def test_car():
    print("I am Lightning McQueen!")