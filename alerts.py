import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name = "Shashwat Malasi"
driver.find_element(By.ID,"name").send_keys(name)
driver.find_element(By.XPATH, "//input[@value = 'Alert']").click()

alert = driver.switch_to.alert #For reading the alert message
alertText = alert.text
print(alertText)

alert.accept()





time.sleep(5)