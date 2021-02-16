from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    Name = (By.CSS_SELECTOR, "input[autofocus='true']")
    Mobile = (By.ID, "mobileNumber")
    CheckMark = (By.XPATH, "(//span[@class='checkmark'])[2]")
    Address = (By.ID, "input_type_header")
    Submit = (By.CSS_SELECTOR, "button[type='button']")
    Continue = (By.XPATH, "//div[@class='s-cta-wrap']/a")

    def name(self):
        return self.driver.find_element(*ConfirmPage.Name)

    def mobilenumber(self):
        return self.driver.find_element(*ConfirmPage.Mobile)

    def checkmark(self):
        return self.driver.find_element(*ConfirmPage.CheckMark)

    def address(self):
        return self.driver.find_element(*ConfirmPage.Address)

    def submit(self):
        return self.driver.find_element(*ConfirmPage.Submit)

    def continueoption(self):
        self.driver.find_element(*ConfirmPage.Continue).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage
