import pytest

@pytest.fixture(scope="class")
def setup():
    print("This line of code is inside the conftest file!")

#-----------------------Returning Data from the fixture-----------------------------------
@pytest.fixture()
def dataLoad():
    print("Inside the data load fixture")
    return ["My", "Name", "is"] #Returning the list