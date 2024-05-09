import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://github.com/gitvasu10")
#opening a new tab in the browser
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.CONTROL + 't')
time.sleep(2)
#Open a new wesite in the tab
#Storing all the opened windows in the list
# opened_windows = driver.window_handles
#
# driver.switch_to.window(opened_windows[1])

driver.get("https://github.com/gitvasu10/JavaPractice")
time.sleep(2)


#print(driver.find_element(By.))
