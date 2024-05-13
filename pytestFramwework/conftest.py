import pytest

@pytest.fixture()
def setup():
    print("This line of code is inside the conftest file!")