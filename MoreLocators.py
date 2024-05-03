import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/client")

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("yoyovasu10@hotmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("password@123")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(3) input").send_keys("password@123")

#driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
















time.sleep(5)
