from selenium import webdriver
import time
from selenium.common.exceptions import StaleElementReferenceException
from pageObjects.HomePage import HomePage
from pageObjects.SelectionPage import SelectionPage
from utilities.BaseClass import BaseClass


class TestSamsung(BaseClass):
    def test_MobilePurchase(self):
        log = self.getLogger()
        log.info("Entering Samsung URL")
        self.samsungurl()
        homepage = HomePage(self.driver)
        log.info("Click on mobile option in navigation bar")
        homepage.mobile().click()
        log.info("Move mouse towards smartphones option")
        homepage.smartphones().click()
        log.info("Then click on SeeAll option")
        SeeAll = homepage.seeallmobiles()
        self.driver.execute_script("arguments[0].click();", SeeAll)
        selectionpage = SelectionPage(self.driver)
        log.info("List of all Mobile Brand")
        cards = selectionpage.mobilelist()
        try:
            for card in cards:
                log.info("Selecting one by one from that mobile list")
                ReqProduct = card.find_element_by_xpath("div/div[3]/a/p").text
                if ReqProduct == "Galaxy S21 5G":
                    log.info("Click on the required mobile product")
                    Abcd = card.find_element_by_xpath("div[2]/div[5]/a")
                    self.driver.execute_script("arguments[0].click();", Abcd)
                    log.info("Click on Add to Cart option")
                    confirmpage = selectionpage.addtocart()
                    log.info("Click on the Continue Option")
                    checkoutpage = confirmpage.continueoption()
                    log.info("Click on Remove Button")
                    checkoutpage.removebutton().click()
        except StaleElementReferenceException:
            pass







