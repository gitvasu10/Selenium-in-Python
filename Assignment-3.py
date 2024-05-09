#This code does go the first website and from there goes to the second usign the hyperlink and extract a section of text out of it
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.rahulshettyacademy.com/loginpagePractise/") #Parent website


driver.find_element(By.CLASS_NAME, "blinkingText").click() #Click the hyperlink

#Transfer the control to the new window
opened_windows = driver.window_handles
driver.switch_to.window(opened_windows[1])
print(driver.find_element(By.XPATH, "//a[text()='mentor@rahulshettyacademy.com']").text) #Extract the text content from this website

 



