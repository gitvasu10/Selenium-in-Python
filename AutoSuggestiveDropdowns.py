#This file shows that for the dynamic dropdowns, we do not require the 'Select' class of Selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print("The number of countries in this dropdown menu are: {}".format(len(countries)))

for country in countries:
   if(country.text == "India"):
  # assert country.text == "India", "Country could not be found!"
        country.click()
        break

#print(driver.find_element(By.ID, "autosuggest").text) # This only helps in case of the pre-filled text data, not for the dynamically filled text
print(driver.find_element(By.ID, "autosuggest").get_attribute("value")) #This method helps to catch the dynamically filled data
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"

time.sleep(5)
