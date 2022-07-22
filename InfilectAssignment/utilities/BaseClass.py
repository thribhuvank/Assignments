import time

import pytest
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:
    def scrollDown(self, scroll_time,  scrollXpath):
        scroll = self.driver.find_element_by_xpath(scrollXpath)
        for num in range(0, scroll_time):
            scroll.send_keys(Keys.PAGE_DOWN)

    def addProductByKeyword(self, keyword):
        Products = self.driver.find_elements_by_xpath(
            "//p[contains(text(), '" + keyword + "')]/following-sibling::p[contains(text(), 'Price')]")
        priceList = []
        for price in Products:
            price = price.text
            price = price.split()
            if price[-1].isdigit():
                priceList.append(price[-1])
        print(priceList)
        print(min(priceList))
        leastprice = min(priceList)
        locator = "//p[contains(text(), '" + keyword + "')]/following-sibling::p[contains(text(), '" + str(leastprice) + "')]/following-sibling::button"
        locator = self.waitForElement(locator, "xpath")
        locator.click()
        time.sleep(3)

    def verifyXpathPresence(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        wait.until(EC.element_to_be_clickable((By.XPATH, locator)))

    def switchToIFrame(self):
        iframe = self.driver.find_element_by_xpath("//iframe[@class='stripe_checkout_app']")
        self.driver.switch_to.frame(iframe)

    def waitForElement(self, locatorvalue, locatorType):
        locatorType = locatorType.lower()
        element = None
        wait = WebDriverWait(self.driver, 30, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        if locatorType == "xpath":
            element = wait.until(lambda x: x.find_element_by_xpath('%s' % (locatorvalue)))
            return element
        else:
            self.log.info("Locator value " + locatorvalue + "not found")

        return element