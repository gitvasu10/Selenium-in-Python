import pytest

from pytestFramwework.Log import Log


@pytest.mark.usefixtures("dataLoad") #Annotation for including fixtures from the conftest file into the current one
class TestExample(Log):
    def test_edit(self, dataLoad): #If we want to return something from the fixture, then we have to pass the parameter in the function itself
        log = self.log_function()
        log.info(dataLoad[0])
        log.info(dataLoad[1])
#On declaring the fixture name globally, we don;t need to pass the parameter in the function declaration.
#Only in the case where the fixture is returning something that we need to explicitly mention the fixture name in the function parameter list


#--------14th May ------------------Running the data with multiple set of test runs
#Only in the case where the fixture is returning something that we need to explicitly mention the fixture name in the function parameter list.
