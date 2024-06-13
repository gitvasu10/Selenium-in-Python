from selenium.webdriver.common.by import By
class CheckoutPage:

    def __init__(self,driver):
        self.driver = driver
    card_title = (By.CSS_SELECTOR,".card-title a")
    card_footer = (By.CSS_SELECTOR,".card-footer button")

    def getCardTitles(self):
        return self.driver.find_elements(CheckoutPage.card_title)

    def getCardFooter(self):
        return self.driver.find_elements(CheckoutPage.card_title)