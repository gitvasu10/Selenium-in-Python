import time

from selenium import webdriver
#'By' is a class provided in this module, used to create locator strategies for finding the web elements on a web page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select #Select is a class in Selenium for the selection of the static dropdowns in web pages

#chrome driver
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

#locators ---> XPath, CSS selector, ClassName, name, linkText
driver.find_element(By.NAME, "email").send_keys("yoyovasu@hotmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("yoyovasu10@")
driver.find_element(By.ID, "exampleCheck1").click()

#Create Xpath for the locators not present in the inspection
# //tagname[@attribute='value'] -> //input[@type='submit']
driver.find_element(By.XPATH, "//input[@value='Submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert").text
print(message)

#CSS Selector
#tagname[attribute='value'] OR #tagname(#id) OR '.className' --> CSS selector for the class name

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Shashwat Malasi")

assert "Success" in message, "The word cannot be located! Please look up for the correct word..."

#Check the Radio button for Employement type
driver.find_element(By.ID, "inlineRadio1").click()

#check the input box based on the specific XPath selector
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Into the 2 way binding box")


#Static dropdowns --> Male/Female
#Using the Select class in Selenium

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female")




time.sleep(7)

