import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chrome_options)
#driver.implicitly_wait(10)
driver.get("https://bugbug.io/blog/testing-frameworks/best-selenium-practice-websites/")

#Scroll to the end of the page
#driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
driver.execute_script("window.scrollBy(0,600);")
time.sleep(1)

#Take a ss
#driver.get_screenshot_as_file("ss2.png")
#driver.get_screenshot_as_png() #Saves the image as a binary data

#driver.save_screenshot("test.jpg") #Warning as the extension is not png

driver.get_screenshot_as_file("test2.jpg") #still got the same warning as before for using the different extension type




time.sleep(1)
