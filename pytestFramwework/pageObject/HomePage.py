from selenium.webdriver.common.by import By


class HomePage:
    #This is done so that whosover calls this class, has to pass a driver object as an argument
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopitem(self):
        return self.driver.find_element(*HomePage.shop)
