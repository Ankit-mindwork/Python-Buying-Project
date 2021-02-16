from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    Remove = (By.CSS_SELECTOR, "button[class='btn-delete data-omni-remove']")

    def removebutton(self):
        return self.driver.find_element(*CheckoutPage.Remove)