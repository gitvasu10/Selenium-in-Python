import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/loginpagePractise")

dropdown = Select(driver.find_element(By.XPATH, "//select[@class='form-control']"))
dropdown.select_by_value("stud")
dropdown.select_by_index(2)












time.sleep(5)