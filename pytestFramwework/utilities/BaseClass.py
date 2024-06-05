import pytest
from selenium import webdriver


@pytest.mark.usefixtures(
    "setup")  #In the conftest, we create a fixture and in this base class, we are using the fixture, thereafter this class is being inherited by the e2e_copy file
class BaseClass:
    def __init__(self):
        self.driver = webdriver.Chrome()
    pass
