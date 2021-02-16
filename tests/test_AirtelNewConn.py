from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import time
from selenium.common.exceptions import StaleElementReferenceException

from TestData.HomePageData import HomePageData
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestAirtel(BaseClass):
    def test_NewConn(self, getData):
        log = self.getLogger()
        log.info("Entering Airtel URL")
        self.airtelurl()
        homepage = HomePage(self.driver)
        log.info("Click on broadband option")
        homepage.broadband().click()
        log.info("click on Buy New Connection option")
        selectionpage = homepage.buynewconnection()
        log.info("Click on Change City option")
        self.changecities()
        selectionpage.changecity().click()
        log.info("Enter City Name "+getData["City"])
        selectionpage.othercity().send_keys(getData["City"])
        log.info("Finally City name is selected")
        selectionpage.cityselect().click()
        log.info("List of all Monthly Rentals")
        rentals = selectionpage.rentalslist()
        try:
            for rental in rentals:
                log.info("Selecting one by one Rental from Monthly Rentals list")
                MonthlyRental = rental.find_element_by_xpath("div[1]/p").text
                if MonthlyRental == "₹799":
                    log.info("Selecting the required Rental Plan")
                    BuyNow = rental.find_element_by_xpath("div[2]/span")
                    self.driver.execute_script("arguments[0].click();", BuyNow)
                    confirmpage = ConfirmPage(self.driver)
                    log.info("Enter the Customer Name "+getData["Name"])
                    confirmpage.name().send_keys(getData["Name"])
                    log.info("Enter the Customer Mobile Number " + getData["Mobile"])
                    confirmpage.mobilenumber().send_keys(getData["Mobile"])
                    log.info("Click on Checkmark")
                    confirmpage.checkmark().click()
                    log.info("Enter the Customer Address " + getData["Address"])
                    confirmpage.address().send_keys(getData["Address"])
                    log.info("Click on Submit Option")
                    confirmpage.submit().click()
        except StaleElementReferenceException:
            pass




    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param