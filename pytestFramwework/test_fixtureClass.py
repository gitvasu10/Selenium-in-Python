import pytest


@pytest.mark.usefixtures("setup") #Globally declaring the fixture
class TestClass:
#No need to define in the individual test methods
    def test_confTest1(self):

        print("This line was run by using the conftest file...")

    def test_confTest2(self):
        print("This line was run by using the conftest file...")

    def test_confTest3(self):
        print("This line was run by using the conftest file...")

    def test_confTest4(self):
        print("This line was run by using the conftest file...")


