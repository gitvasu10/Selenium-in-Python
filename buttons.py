import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#driver.find_element(By.XPATH, "//input[@id='checkBoxOption1']").click() #This approach works only when we are sure of the position of the checkBox

# checkBoxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
# print("The number of checkboxes returned into the list are: {}".format(len(checkBoxes)))
# for checkBox in checkBoxes:
#     assert checkBox.get_attribute("value") == 'option1', "The test case failed!"
#     checkBox.click()
#     print("The test case for checkbox passed successfully!")
#     break

radioButtons = driver.find_elements(By.XPATH, "//input[@type='radio']")
print("The number of radio buttons is {}".format(len(radioButtons)))

for radioButton in radioButtons:
    #assert radioButton.get_attribute("value") == 'radio2', "The test case failed !"    #assert will work only for the first(initial) value only, that's why it is giving false for the radio button 2.
    if radioButton.get_attribute("value") == 'radio2':
        radioButton.click()
        assert radioButton.is_selected()
        print("The radio button is selected: {}".format(radioButton.is_selected()))
        break


















time.sleep(5)