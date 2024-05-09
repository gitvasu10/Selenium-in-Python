import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
#action.click_and_hold(driver.find_element()).perform()      #Long click
#action.context_click().perform()                            #Right click
#action.double_click().perform()                             #Double click

driver.implicitly_wait(15)
driver.maximize_window()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
time.sleep(2)
#wait = WebDriverWait(driver, 10)
#wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Top")))
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
time.sleep(2)
#action.move_to_element(driver.find_element(By.XPATH, "//input[@value='radio2']")).click().perform()     #Hover over the button
time.sleep(2)
