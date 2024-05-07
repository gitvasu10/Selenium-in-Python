import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)
#Input the text in the search bar
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

resultList = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print("The count of the products is {}".format(len(resultList)))

#ADDING THE DESIRED COMPONENTS IN THE CART
#Chaining of parent-to-child components
for result in resultList:
    button = result.find_element(By.XPATH, "div/button") #This is done to prevent the StaleElementReferenceException
    button.click() #Everytime finding the fresh references for the buttons

#The concept of waits is included since there exists a loading lag among various componenets of dynamic websites.
#In this codes, the website includes the coupon code box which takes more time to get loaded than the rest of the components. Hence, explicit wait



#CLICKING ON THE CART BUTTON
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()

driver.find_element(By.XPATH,"//button[@type='button']").click()

#ENTERING THE PROMO CODE IN THE TEXT BOX
driver.find_element(By.XPATH, "//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")

#CLICKING ON THE Apply BUTTON
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

text_to_print = driver.find_element(By.CLASS_NAME, "promoInfo")
print(text_to_print.text)

# class NoSuchElementException:
#     pass
#
#
# try:
#     promo_info_element = driver.find_element(By.CLASS_NAME, "promoInfo")
#     print(promo_info_element.text)
# except NoSuchElementException:
#     print("Element with class name 'promoInfo' not found.")

#CLICKING THE 'Place Order' BUTTON
driver.find_element(By.XPATH,"//button[text()='Place Order']").click()

#driver.find_element(By.XPATH, "//button[contains(text(), 'Place Order')]").click()


