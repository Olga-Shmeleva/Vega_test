import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from base.base_class import Base

class Checkout_cart_page(Base):


    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        driver.implicitly_wait(10)

    # locators
    cart_selected_product_furniture = 'a[href="https://vega.ge/en/stand-for-tv-vega-x53.html"]'
    cart_selected_product_appliences = 'a[href="https://vega.ge/en/notebook-lenovo-ideapad-3-17iau7-i3-1215u-173-8gb-' \
                                       '512gb-gr-82rl005grk.html"]'
    cart_selected_product_home_and_garden = 'a[href="https://vega.ge/en/bed-cover-vetexus-ntf-2019-bc-220x240.html"]'

    product_furniture_price = 'td[class="price1"]'
    product_appliences_price = 'td[class="price1"]'
    product_home_and_garden_price = 'td[class="price1"]'

    quantity_of_product_furniture = '//input[@class="qc-product-qantity form-control text-center"]'
    down_button_furniture = '//*[@id="cart1"]/div/table/tbody/tr[1]/td[3]/div/span[1]/button/i'
    up_button_furniture = '//*[@id="cart1"]/div/table/tbody/tr[1]/td[3]/div/span[2]/button[1]/i'
    remove_button_product_furniture = '//*[@id="cart1"]/div/table/tbody/tr[1]/td[3]/div/span[2]/button[2]/i'

    quantity_of_product_appliences = '//*[@id="cart1"]/div/table/tbody/tr[3]/td[3]/div/input'
    down_button_appliences = '//*[@id="cart1"]/div/table/tbody/tr[3]/td[3]/div/span[1]/button/i'
    up_button_appliences = '//*[@id="cart1"]/div/table/tbody/tr[3]/td[3]/div/span[2]/button[1]/i'
    remove_button_product_appliences = '//*[@id="cart1"]/div/table/tbody/tr[3]/td[3]/div/span[2]/button[2]/i'

    quantity_of_product_home_and_garden = '//*[@id="cart1"]/div/table/tbody/tr[2]/td[3]/div/input'
    down_button_home_and_garden = '//*[@id="cart1"]/div/table/tbody/tr[2]/td[3]/div/span[1]/button/i'
    up_button_home_and_garden = '//*[@id="cart1"]/div/table/tbody/tr[2]/td[3]/div/span[2]/button[1]/i'
    remove_button_home_and_garden = '//*[@id="cart1"]/div/table/tbody/tr[2]/td[3]/div/span[2]/button[2]'


    price_product = '//*[@id="cart1"]/div/table/tbody/tr[1]/td[4]'
    total_product = '//*[@id="cart1"]/div/table/tbody/tr[6]/td[2]'
    finish_amount = '//*[@id="cart1"]/div/table/tbody/tr[2]/td[2]'
    free_Shipping = '//*[@id="cart1"]/div/table/tbody/tr[3]/td[2]'   # must be equal 0
    reward_field = '//input[@name="reward"]'
    first_name = '//input[@id="input-payment-firstname"]'
    last_name = '//input[@id="input-payment-lastname"]'
    Phone = '//input[@id="input-payment-telephone"]'
    Address = '//input[@id="input-payment-address-1"]'
    checkout_word = 'div[class="quickcheckout-heading"]'


    #getters

    def get_cart_selected_product_furniture(self):
        time.sleep(5)
        return self.driver.find_elements(By.CSS_SELECTOR, self.cart_selected_product_furniture)
    def get_cart_selected_product_appliences(self):
        time.sleep(5)
        return self.driver.find_elements(By.CSS_SELECTOR, self.cart_selected_product_appliences)
    def get_cart_selected_product_home_and_garden(self):
        time.sleep(5)
        return self.driver.find_elements(By.CSS_SELECTOR, self.cart_selected_product_home_and_garden)
    def get_quantity_of_product (self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.quantity_of_product_furniture)))
    def get_remove_button_product (self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.remove_button_home_and_garden)))
    def get_down_button (self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.down_button_furniture)))
    def get_up_button (self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.up_button_furniture)))
    def get_total_product (self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total_product)))
    def get_finish_amount(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_amount)))
    def get_free_Shipping(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.free_Shipping)))
    def get_reward_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.reward_field)))
    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))
    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))
    def get_Phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Phone)))
    def get_Address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Address)))
    def get_checkout_word(self):
        time.sleep(5)
        return self.driver.find_elements(By.CSS_SELECTOR, self.checkout_word)

    def get_product_furniture_price(self):
        time.sleep(5)
        return self.driver.find_elements(By.CSS_SELECTOR, self.product_furniture_price)
    def get_product_appliences_price(self):
        time.sleep(5)
        return self.driver.find_elements(By.CSS_SELECTOR, self.product_appliences_price)
    def get_product_home_and_garden_price(self):
        time.sleep(5)
        return self.driver.find_elements(By.CSS_SELECTOR, self.product_home_and_garden_price)

    # actions

    def value_cart_selected_product_furniture(self):
        time.sleep(3)
        return self.get_cart_selected_product_furniture()[3]
    def value_cart_selected_product_appliences(self):
        time.sleep(3)
        return self.get_cart_selected_product_appliences()[3]
    def value_cart_selected_product_home_and_garden(self):
        time.sleep(3)
        return self.get_cart_selected_product_home_and_garden()[3]
    def click_quantity_of_product(self):
        return self.get_quantity_of_product().text
    def click_remove_button_product(self):
        return self.get_remove_button_product().text
    def click_down_button(self):
        return self.get_down_button().text
    def click_up_button(self):
        return self.get_up_button().text
    def value_product_furniture_price(self):
        return self.get_product_furniture_price()[1]
    def value_product_appliences_price(self):
        return self.get_product_appliences_price()[3]
    def value_product_home_and_garden(self):
        return self.get_product_home_and_garden_price()[2]
    def value_total_product(self):
        return self.get_total_product().text
    def value_checkout_word(self):
        return self.get_checkout_word()[3]
    def click_finish_amount(self):
        return self.get_finish_amount().text
    def click_free_Shipping(self):
        return self.get_free_Shipping().text
    def click_reward_field(self):
        self.get_reward_field().click()
        self.get_reward_field().send_keys("successfully")
        time.sleep(5)
        return self.get_reward_field().text
    def input_first_name(self, first_name_1):
        self.get_first_name().clear()
        self.get_first_name().click()
        self.get_first_name().send_keys(first_name_1)
    def input_last_name(self,last_name_1):
        self.get_last_name().clear()
        self.get_last_name().click()
        self.get_last_name().send_keys(last_name_1)
    def input_Phone(self,Phone_1):
        self.get_Phone().clear()
        self.get_Phone().click()
        self.get_Phone().send_keys(Phone_1)
    def input_Address(self,Address_1):
        self.get_Address().clear()
        self.get_Address().click()
        self.get_Address().send_keys(Address_1)

     # Methods

    def create_dict_finish(self):
        finish_dict = {}
        locators_products = [self.value_cart_selected_product_furniture(),
                             self.value_cart_selected_product_appliences(),
                             self.value_cart_selected_product_home_and_garden()]
        locators_price = [self.value_product_furniture_price(),
                          self.value_product_appliences_price(),
                          self.value_product_home_and_garden()]
        for element in range(len(locators_products)):
            product = self.check_locators_products(locators_products[element])
            price = self.check_locators_products(locators_price[element])
            if (product is not None) and (price is not None):
                price = price.replace('₾', '').replace(' ', '')
                finish_dict.setdefault(product.lower(), float(price))
            else:
                return f'ошибка{product,price}'
        return finish_dict

    def entering_personal_data(self):
        print('start entering_personal_data')
        self.value_checkout_word()
        self.assert_url('https://vega.ge/en/checkout-en/')
        self.assert_word(self.get_checkout_word()[3], 'Payment Method')
        time.sleep(2)
        self.input_first_name('first_name')
        self.input_last_name('last_name')
        self.input_Phone('5555555')
        self.input_Address('Address')
        print('entering_personal_data - done')

    def entering_all_product_data(self):
        print('start entering_all_product_data')
        self.click_quantity_of_product()
        for i in range(2):
            self.click_down_button()
        time.sleep(2)
        for i in range(2):
            self.click_up_button()
        self.click_quantity_of_product()
        self.click_finish_amount()
        self.click_free_Shipping()
        self.click_reward_field()
        finish_dict = self.create_dict_finish()
        self.get_screenshot()
        value_total_product = self.value_total_product().replace('₾', '').replace(' ', '')
        print(finish_dict, 'finish_dict')
        print(float(value_total_product), 'float(value_total_product)')
        assert sum(finish_dict.values()) == float(value_total_product)
        print('entering_all_product_data - done')
        return finish_dict










