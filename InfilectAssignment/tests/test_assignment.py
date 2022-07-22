from pageObjects.AddProducts import AddProducts
from pageObjects.CartPage import CartPage
from pageObjects.CurrentTemperaturePage import CurrentTemperature
from utilities.BaseClass import BaseClass


class TestSB(BaseClass):
    def test_checkURL(self):
        URL = self.driver.current_url
        assert URL == 'https://weathershopper.pythonanywhere.com/'

    def test_checkTemperatureHeader(self):
        gettemptext = CurrentTemperature(self.driver)
        temptext = gettemptext.getTemperatureHeader()
        assert temptext == 'Current temperature', 'Title not matching'

    def test_getTemperature(self):
        global temperature
        gettemp = CurrentTemperature(self.driver)
        temperature = gettemp.getTemperature()
        temperature = temperature.split()

    def test_get_buy_options(self):
        buyopt = CurrentTemperature(self.driver)
        buyOptions = []
        bOptions = buyopt.getBuyOptions()
        for option in bOptions:
            buyOptions.append(option.text)
        print(buyOptions)

    def test_choose_buy_option_based_on_temperature(self):
        choosebuyopt = CurrentTemperature(self.driver)
        if int(temperature[0]) <= 24:
            print("Too cold, Choose Moisturizers")
            choosebuyopt.clickOnBuyMoisturizers()
        elif int(temperature[0]) > 24:
            print("Hot, choose Sunscreens")
            choosebuyopt.clickOnBuySunscreens()

    def test_add_product_based_on_page_header(self):
        add = AddProducts(self.driver)
        pageHeader = add.getPageHeader()
        self.scrollDown(2, add.scrollXpath)
        if pageHeader == 'Moisturizers':
            try:
                print("Need to add Moisturizers products")
                # least expensive mositurizer that contains Aloe
                self.addProductByKeyword('Aloe')
                # least expensive moisturizer that contains almond
                self.addProductByKeyword('Almond')
            except:
                print("Products not available")

        elif pageHeader == 'Sunscreens':
            try:
                print("Need to add Sunscreens products")
                # least expensive sunscreen that is SPF-50
                self.addProductByKeyword('SPF-50')
                # least expensive sunscreen that is SPF-30
                self.addProductByKeyword('SPF-30')
            except:
                print("Products not available")

    def test_verify_cart_count(self):
        cart = CartPage(self.driver)
        count = cart.getCartCount()
        assert int(count) == 2, "Products Missing"

    def test_verify_cart_page(self):
        cart = CartPage(self.driver)
        cart.clickOnCart()
        print(cart.getTableHeaders())
        if 'Qty' in cart.getTableHeaders():
            print("Qty Header is available")
        else:
            print("Qty header is missing in cart page")
        # assert 'Qty' in cart.getTableHeaders(), 'Qty header is missing in cart page'

    def test_placeOrder_verify_popup(self):
        popup = CartPage(self.driver)
        popup.clickOnPayWithCart()
        self.switchToIFrame()
        self.verifyXpathPresence(popup.popupverify)
        assert 'Stripe.com' == popup.getCompanyNameOnPopup(), 'Company name not valid'

    def test_placeOrder(self):
        placeorder = CartPage(self.driver)
        placeorder.enterEmail()
        placeorder.enterCartNumber()
        placeorder.enterValidMonthYear()
        placeorder.enterCVC()
        placeorder.enterZipCode()
        placeorder.clickOnPay()
        self.driver.switch_to.default_content()
        assert 'Your payment was successful' in placeorder.getPaymentSuccessMessage(), 'Payment not done'
