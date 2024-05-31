#This file is created for better comprehending the use of fixtures in any class to reduce code redundancy 
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pytestFramwework.utilities.base_class import base_class


#@pytest.mark.usefixtures("setup") #Globally declaring the fixture
class e2e_fixture(base_class):
    #def fixture_func(self,setup):
    def fixture_func(self):
        self.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

#This approach would only find the product 'name' only
#itemList = driver.find_elements(By.CSS_SELECTOR, "h4")

        itemList =self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

#Extract the text from the parent div---> Apply chaining of the web elements
        for item in itemList:
            name = item.find_element(By.XPATH, "div/h4/a")
            if name.text == "Blackberry":
                print("Required item found!")
                item.find_element(By.XPATH, "div/button ").click()
                print("Item added in the cart!")
            break

        self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()

#driver.get_screenshot_as_file("Blackberry.png")
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn btn-success')]").click()

#Autosuggestive dropdown
        self.driver.find_element(By.XPATH, "//input[@id='country']").send_keys("ind")

#Waiting till the complete name appears on the screen
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

#When appears automating the click operation
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        print(self.driver.find_element(By.CLASS_NAME, "alert").text)
