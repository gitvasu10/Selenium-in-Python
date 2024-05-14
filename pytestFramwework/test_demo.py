import pytest
#No need to write the line below. If the files are present in the same folder, pytest will import the file all by itself
#import conftest
def test_demoFunction():
    print('Hello!')

def test_shopping():
    print("This is the test case for shopping cart in the second file!")

@pytest.mark.PistonCup
def test_car():
    print("I am Lightning McQueen!")

# @pytest.fixture()
# def setup(): #Not in the format of pytest
#     print("This is inside the fixture. ")
#     yield
#     print("This line will be executed at the last!")


# def test_fixtureDemo(setup): #On running the entire file. this function will be running and the contents of the fxiture method will be printed but void of the function name
#     print("It will be printed after the fixture!")


def test_confTest(setup):
    print("This line was run by using the conftest file...")

#----------------------------------14th May-----------------------------------------------------

def test_browser(browsers):
    print(browsers)

