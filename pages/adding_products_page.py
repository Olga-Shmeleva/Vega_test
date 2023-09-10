import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Adding_products_page(Base):



    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.products_dict = {}


    # locators
    add_to_cart = '//*[@id="button-cart"]'
    plus_button = '//a[@id="q_up"]'
    minus_button = '//a[@id ="q_down"]'
    amount_button = '//input[@id="quantity_wanted"]'
    order_button = '//*[@id="modalAddToCartProduct"]/div/div/div[2]/div[2]/div/div[2]/a[2]'
    pop_up_window = '//*[@id="tawk-mpreview-close"]'
    open_cart = '//a[@class="open-cart"]'
    check_word = '//*[@id="tab-attribute"]/div/h3'
    locator_all_products = '//*[@id="quickview_product"]/div[2]/h1'
    locator_appliences_price = '/html/body/div[1]/div[2]/div/div[6]/div[2]/div[2]/div/div/div/div/div[1]/div[2]' \
                               '/div/div/div/div[2]/div[3]/span[2]/span'
    locator_furniture_price = '/html/body/div[1]/div[2]/div/div[6]/div[2]/div[2]/div/div/div/div/div[1]/div[2]' \
                              '/div/div/div/div[2]/div[3]/span[2]/span'
    locator_home_and_garden_price = '/html/body/div[1]/div[2]/div/div[6]/div[2]/div[2]/div/div/div/div/div[1]' \
                                    '/div[2]/div/div/div/div[2]/div[3]/span/span'

    url_appliences = 'https://vega.ge/en/notebook-lenovo-ideapad-3-17iau7-i3-1215u-173-8gb-512gb-gr-82rl005grk.html'
    url_furniture = 'https://vega.ge/en/stand-for-tv-vega-x53.html'
    url_home_and_garden = 'https://vega.ge/en/bed-cover-vetexus-ntf-2017-bc-220x240.html'


    # getters

    def get_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart)))
    def get_plus_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.plus_button)))
    def get_minus_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.minus_button)))
    def get_amount_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.amount_button)))
    def get_order_button(self):
        return WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, self.order_button)))
    def get_open_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.open_cart)))
    def get_pop_up_window(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pop_up_window)))

    def get_locator_all_products(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.locator_all_products)))

    def get_locator_appliences_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.locator_appliences_price)))
    def get_locator_furniture_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.locator_furniture_price)))
    def get_locator_home_and_garden_price (self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.locator_home_and_garden_price)))




    # actions
    def click_pop_up_window(self):
        self.get_pop_up_window().click()
    def click_add_to_cart(self):
        self.check_get_pop_up_window(self.add_to_cart)
        self.get_add_to_cart().click()
    def click_plus_button(self):
        self.get_plus_button().click()
    def click_minus_button(self):
        self.get_minus_button().click()

    def click_amount_button(self):
        self.get_amount_button().clear()
        time.sleep(2)
        self.get_amount_button().click()
        self.get_amount_button().send_keys("1")

    def click_order_button(self):
        print(self.get_order_button().text)
        self.get_order_button().click()

    def click_open_cart(self):
        self.get_open_cart().click()


    def add_all_products_page(self):
        locators = [self.locator_appliences_price,
                    self.locator_furniture_price, self.locator_home_and_garden_price]
        for element in range(len(locators)):
            amount_locators = self.check_locators_products(locators[element])
            if amount_locators is not None:
                amount_locators = amount_locators.replace('₾', '').replace(' ', '')
                return self.get_locator_all_products().text.lower(), float(amount_locators)
        print('add_all_products_page - done')

    def check_all_products_page(self):
        if 'Notebook LENOVO IdeaPad' in self.get_locator_all_products().text:
            self.assert_url(self.url_appliences)
        elif 'Stand For Tv' in self.get_locator_all_products().text:
            self.assert_url(self.url_furniture)
        elif 'Bed Cover' in self.get_locator_all_products().text:
            self.assert_url(self.url_home_and_garden)
        self.assert_word(self.check_word, 'Attributes')
        self.driver.execute_script("window.scrollTo(0, 300);")
        for i in range(2):
            self.click_plus_button()
        time.sleep(2)
        self.click_minus_button()
        time.sleep(2)
        self.click_amount_button()
        time.sleep(3)
        self.click_add_to_cart()
        time.sleep(2)
        self.get_screenshot()
        self.click_order_button()
        print('check_all_products_page-done')













