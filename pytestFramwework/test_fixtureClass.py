import pytest


@pytest.mark.usefixtures("setup")
class testClass:

    def test_confTest1(self):
        print("This line was run by using the conftest file...")

    def test_confTest2(self):
        print("This line was run by using the conftest file...")

    def test_confTest3(self):
        print("This line was run by using the conftest file...")

    def test_confTest4(self):
        print("This line was run by using the conftest file...")
