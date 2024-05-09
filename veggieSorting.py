import time

from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("headless")

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
print(driver.title)




driver.find_element(By.XPATH, "//span[normalize-space()='Veg/fruit name']").click()

newListToBeSorted = []
#Collecting the vegetables' name in the list
initialBrowserList = driver.find_elements(By.XPATH, "//tr/td[1]")

for item in initialBrowserList:
    newListToBeSorted.append(item.text)



originalList = newListToBeSorted.copy()
newListToBeSorted.sort()

assert originalList == newListToBeSorted, "The lists do not match!"

#time.sleep(2)