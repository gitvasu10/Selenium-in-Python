import time
from selenium import webdriver
from selenium.webdriver.common.by import By


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



#CLICKING ON THE CART BUTTON
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()

driver.find_element(By.XPATH,"//button[@type='button']").click()

#ENTERING THE PROMO CODE IN THE TEXT BOX
driver.find_element(By.XPATH, "//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")

#CLICKING ON THE Apply BUTTON
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

#print(driver.find_element(By.CLASS_NAME, ".promoInfo").text)
#CLICKING THE 'Place Order' BUTTON
driver.find_element(By.XPATH,"//button[text()='Place Order']").click()

#driver.find_element(By.XPATH, "//button[contains(text(), 'Place Order')]").click()


