from selenium.webdriver.common.by import By


class AddProducts:
    def __init__(self, driver):
        self.driver = driver

    header = (By.XPATH, "//h2")
    price = (By.XPATH, "//p[contains(text(),'Price: ')]")
    scrollXpath = "(//button[text()= 'Add'])[1]"
    productgrid = (By.XPATH, "//div[contains(@class, 'text-center')]")
    productname = (By.XPATH, "//p[contains(@class, 'font-weight-bold')]")
    addproduct = (By.XPATH, "(//button[text()= 'Add'])[2]")

    def getPageHeader(self):
        return self.driver.find_element(*AddProducts.header).text

    def getProductPrice(self):
        return self.driver.find_elements(*AddProducts.price)

    def getProductGrid(self):
        return self.driver.find_elements(*AddProducts.productgrid)

    def getProductName(self):
        return self.driver.find_elements(*AddProducts.productgrid)

    def clickOnAdd(self):
        return self.driver.find_element(*AddProducts.addproduct).click()

