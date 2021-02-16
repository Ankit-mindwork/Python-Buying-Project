from selenium.webdriver.common.by import By

from pageObjects.SelectionPage import SelectionPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    Broadband = (By.XPATH, "//div[@class='header-main-actions-list-content']/div[3]/h3")
    BuyNewConnection = (By.XPATH, "(//a[contains(text(),'Buy New Connection')])[2]")
    Mobile = (By.XPATH, "(//div[@class='gnb__main'])/ul/li[1]/a/span")
    Smartphones = (By.XPATH, "(//ul[@class='gnb__depth2 active'])/li[2]/a/span")
    Seeall = (By.XPATH, "(//ul[@class='gnb__depth2 active'])/li[2]/div/div/ul/li[9]/a/span")

    def broadband(self):
        return self.driver.find_element(*HomePage.Broadband)

    def buynewconnection(self):
        self.driver.find_element(*HomePage.BuyNewConnection).click()
        selectionpage = SelectionPage(self.driver)
        return selectionpage

    def mobile(self):
        return self.driver.find_element(*HomePage.Mobile)

    def smartphones(self):
        return self.driver.find_element(*HomePage.Smartphones)

    def seeallmobiles(self):
        return self.driver.find_element(*HomePage.Seeall)
