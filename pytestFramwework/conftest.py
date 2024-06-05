#This file serves the purpose of sharing data through fixtures across various files

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
# @pytest.fixture(scope="class")
# def setup():
#     print("This line of code is inside the conftest file!")
#     yield
#     print("The line inside the yield will be executed at the very last!")
#
# #-----------------------Returning Data from the fixture-----------------------------------
# @pytest.fixture()
# def dataLoad():
#     print("Inside the data load fixture")
#     return ["My", "Name", "is"] #Returning the list
#
#
# #---------14th May----------------------------Opening same test case in multiple browsers----------Running tests in multiple datasets----------
# @pytest.fixture(params=["Chrome", "Firefox", "IE"])
# def browsers(request):  #The params will be passed in the request parameter and this request param would work further
#     return request.param


#--------30th May------use of fixtures in the e2eTest file(copy) to reduce the code redundancy-----------
from selenium import webdriver
from selenium.webdriver.common.by import By

#scope="class" ensures that it's executed only once per test class rather than for every individual test method

#This fixture will be used in the e2e_test_fixture_copy file
#-----------------Till lecture 88------------------------------------------
# @pytest.fixture(scope="class")
# def setup(request):
#     driver = webdriver.Firefox()
#     #driver.implicitly_wait(4)
#     driver.get("https://rahulshettyacademy.com/angularpractice/")
#     driver.maximize_window()
#     request.cls.driver = driver #This line passes this driver into the e2eTest class driver
#     yield
#     driver.close()
#---------------------------------------------------------------------------
def pytest_adoption(parser):
    parser.adoption(
        "--browser_name", action="store", default="chrome"
    )
@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name") # Th
    if browser_name == "chrome":
        driver = webdriver.Chrome()

    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    elif browser_name == "IE":
        driver = webdriver.Firefox()

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver #This line passes this driver into the e2eTest class driver
    yield
    driver.close()
