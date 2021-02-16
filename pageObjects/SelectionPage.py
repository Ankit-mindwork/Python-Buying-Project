from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class SelectionPage:
    def __init__(self, driver):
        self.driver = driver

    ChangeCity = (By.XPATH, "//a[@class='link']")
    OtherCity = (By.CSS_SELECTOR, "input[class='field']")
    CitySelect = (By.XPATH, "//ul[@class='dropdown']/li[2]")
    Rentals = (By.XPATH, "(//div[@class='bottom-part'])")
    Mobilelist = (By.XPATH, "//div[@class='product-card-v2__item']")
    Addtocart = (By.XPATH, "//div[@class='hubble-price-bar__price-cta']/a")

    def changecity(self):
        return self.driver.find_element(*SelectionPage.ChangeCity)

    def othercity(self):
        return self.driver.find_element(*SelectionPage.OtherCity)

    def cityselect(self):
        return self.driver.find_element(*SelectionPage.CitySelect)

    def rentalslist(self):
        return self.driver.find_elements(*SelectionPage.Rentals)

    def mobilelist(self):
        return self.driver.find_elements(*SelectionPage.Mobilelist)

    def addtocart(self):
        self.driver.find_element(*SelectionPage.Addtocart).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage