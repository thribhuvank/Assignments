from selenium.webdriver.common.by import By


class CurrentTemperature:
    def __init__(self, driver):
        self.driver = driver

    tempheader = (By.XPATH, "//h2[contains(text(), 'temperature')]")
    temperature = (By.CSS_SELECTOR, "#temperature")
    buyoption = (By.XPATH, "//h3")
    buymoist = (By.XPATH, "//button[contains(text(), 'moisturizers')]")
    buysuns = (By.XPATH, "//button[contains(text(), 'sunscreens')]")

    def getTemperatureHeader(self):
        return self.driver.find_element(*CurrentTemperature.tempheader).text

    def getTemperature(self):
        return self.driver.find_element(*CurrentTemperature.temperature).text

    def getBuyOptions(self):
        return self.driver.find_elements(*CurrentTemperature.buyoption)

    def clickOnBuyMoisturizers(self):
        return self.driver.find_element(*CurrentTemperature.buymoist).click()

    def clickOnBuySunscreens(self):
        return self.driver.find_element(*CurrentTemperature.buysuns).click()