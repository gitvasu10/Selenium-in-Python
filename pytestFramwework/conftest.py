#This file serves the purpose of sharing data through fixtures across various files

import pytest

@pytest.fixture(scope="class")
def setup():
    print("This line of code is inside the conftest file!")

#-----------------------Returning Data from the fixture-----------------------------------
@pytest.fixture()
def dataLoad():
    print("Inside the data load fixture")
    return ["My", "Name", "is"] #Returning the list


#---------14th May----------------------------Opening same test case in multiple browsers----------Running tests in multiple datasets----------
@pytest.fixture(params=["Chrome", "Firefox", "IE"])
def browsers(request):
    return request.param

