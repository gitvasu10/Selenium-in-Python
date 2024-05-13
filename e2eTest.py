import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

#This approach would only find the product 'name' only
#itemList = driver.find_elements(By.CSS_SELECTOR, "h4")

itemList = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

#Extract the text from the parent div---> Apply chaining of the web elements
for item in itemList:
    name = item.find_element(By.XPATH, "div/h4/a")
    if name.text == "Blackberry":
        print("Required item found!")
        item.find_element(By.XPATH, "div/button ").click()
        print("Item added in the cart!")
        break

driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()

#driver.get_screenshot_as_file("Blackberry.png")
driver.find_element(By.XPATH, "//button[contains(@class,'btn btn-success')]").click()

#Autosuggestive dropdown
driver.find_element(By.XPATH, "//input[@id='country']").send_keys("ind")

#Waiting till the complete name appears on the screen
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

#When appears automating the click operation
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
print(driver.find_element(By.CLASS_NAME, "alert").text)

driver.close()
