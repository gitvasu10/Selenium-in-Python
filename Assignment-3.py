
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.rahulshettyacademy.com/loginpagePractise/")


driver.find_element(By.CLASS_NAME, "blinkingText").click()

#Transfer the control to the new window
opened_windows = driver.window_handles
driver.switch_to.window(opened_windows[1])
print(driver.find_element(By.XPATH, "//a[text()='mentor@rahulshettyacademy.com']").text)





