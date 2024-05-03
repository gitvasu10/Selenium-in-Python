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
  # if(country.text == "India"):
   assert country.text == "India", "Country could not be found!"
   country.click()
   break




time.sleep(5)