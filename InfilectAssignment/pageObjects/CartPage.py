from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    cartcount = (By.XPATH, "//span[@id='cart']")
    cartButton = (By.XPATH, "//button[@onClick='goToCart()']")

    def getCartCount(self):
        count = self.driver.find_element(*CartPage.cartcount).text
        for num in count.split():
            if num.isdigit():
                return num

    def clickOnCart(self):
        return self.driver.find_element(*CartPage.cartButton).click()

    # veriify cart page
    tableheaders = (By.XPATH, "//tr/th")

    def getTableHeaders(self):
        TableHeaders = []
        headers = self.driver.find_elements(*CartPage.tableheaders)
        for header in headers:
            TableHeaders.append(header.text)
        return TableHeaders

    # Place order
    paywithcard = (By.XPATH, "//button[@type='submit']")
    companyname = (By.XPATH, "//h1[contains(@class, 'companyName')]")
    email = (By.XPATH, "//input[@type='email']")
    cardnumber = (By.XPATH, "//input[@placeholder='Card number']")
    monthyear = (By.XPATH, "//input[@placeholder='MM / YY']")
    cvc = (By.XPATH, "//input[@placeholder='CVC']")
    zipcode = (By.XPATH, "//input[@placeholder='ZIP Code']")
    paybutton = (By.XPATH, "//button[contains(@class, 'Button-animation')]")
    paymentsuccess = (By.XPATH, "//p[@class='text-justify']")
    popupverify = "//input[@type='email']"

    def clickOnPayWithCart(self):
        return self.driver.find_element(*CartPage.paywithcard).click()

    def getCompanyNameOnPopup(self):
        return self.driver.find_element(*CartPage.companyname).text

    def enterEmail(self):
        return self.driver.find_element(*CartPage.email).send_keys("abc@gmail.com")

    def enterCartNumber(self):
        return self.driver.find_element(*CartPage.cardnumber).send_keys("4242424242424242")

    def enterValidMonthYear(self):
        return self.driver.find_element(*CartPage.monthyear).send_keys("12 / 21")

    def enterCVC(self):
        return self.driver.find_element(*CartPage.cvc).send_keys("123")

    def enterZipCode(self):
        return self.driver.find_element(*CartPage.zipcode).send_keys("562110")

    def clickOnPay(self):
        return self.driver.find_element(*CartPage.paybutton).click()

    def getPaymentSuccessMessage(self):
        return self.driver.find_element(*CartPage.paymentsuccess).text




