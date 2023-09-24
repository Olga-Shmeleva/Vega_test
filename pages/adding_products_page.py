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
        driver.implicitly_wait(10)


    # locators
    add_to_cart = '//input[@id="button-cart"]'
    plus_button = '//a[@id="q_up"]'
    minus_button = '//a[@id ="q_down"]'
    amount_button = '//input[@id="quantity_wanted"]'
    order_button = 'a[href="https://vega.ge/en/checkout-en/"]'
    pop_up_window = '//*[@id="tawk-mpreview-close"]'
    open_cart = '//a[@class="open-cart"]'
    # locator_all_products = '//*[@id="quickview_product"]/div[2]/h1'
    locator_all_products = '//h2[@class="tt-title"]'
    locator_all_products_price = 'span[id="price-special"]'
    locator_appliences_price = '/html/body/div[1]/div[2]/div/div[6]/div[2]/div[2]/div/div/div/div/div[1]/div[2]' \
                               '/div/div/div/div[2]/div[3]/span[2]/span'
    locator_furniture_price = '/html/body/div[1]/div[2]/div/div[6]/div[2]/div[2]/div/div/div/div/div[1]/div[2]' \
                              '/div/div/div/div[2]/div[3]/span[2]/span'
    locator_home_and_garden_price = '/html/body/div[1]/div[2]/div/div[6]/div[2]/div[2]/div/div/div/div/div[1]' \
                                    '/div[2]/div/div/div/div[2]/div[3]/span/span'

    url_appliences = 'https://vega.ge/en/notebook-lenovo-ideapad-3-17iau7-i3-1215u-173-8gb-512gb-gr-82rl005grk.html'
    url_furniture = 'https://vega.ge/en/stand-for-tv-vega-x53.html'
    url_home_and_garden = 'https://vega.ge/en/bed-cover-vetexus-ntf-2019-bc-220x240.html'
    check_word = 'a[data-toggle="modal"]'


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
        time.sleep(3)
        return (self.driver.find_elements(By.CSS_SELECTOR, self.order_button))
    def get_open_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.open_cart)))
    def get_pop_up_window(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pop_up_window)))

    def get_locator_all_products(self):
        time.sleep(3)
        return (self.driver.find_elements(By.XPATH, self.locator_all_products))
    def get_locator_all_products_price(self):
        time.sleep(3)
        return (self.driver.find_elements(By.CSS_SELECTOR, self.locator_all_products_price))

    def get_locator_appliences_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.locator_appliences_price)))
    def get_locator_furniture_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.locator_furniture_price)))
    def get_locator_home_and_garden_price (self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.locator_home_and_garden_price)))
    def get_check_word(self):
        time.sleep(10)
        return (self.driver.find_elements(By.CSS_SELECTOR, self.check_word))



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
        print(self.get_order_button()[2].text)
        self.get_order_button()[2].click()

    def click_open_cart(self):
        self.get_open_cart().click()

     # Methods

    def add_all_products_page(self):
        print('start add_all_products_page')
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 300);")
        time.sleep(3)
        self.assert_word(self.get_check_word()[0], 'FREE DELIVERY TO TBILISI')
        time.sleep(3)
        if 'Notebook LENOVO IdeaPad' in self.get_locator_all_products()[0].text:
            self.assert_url(self.url_appliences)
        elif 'Stand For Tv' in self.get_locator_all_products()[0].text:
            self.assert_url(self.url_furniture)
        elif 'Bed Cover' in self.get_locator_all_products()[0].text:
            self.assert_url(self.url_home_and_garden)
        for i in range(2):
            self.click_plus_button()
        time.sleep(2)
        self.click_minus_button()
        time.sleep(2)
        self.click_amount_button()
        time.sleep(3)
        time.sleep(5)
        self.get_screenshot()
        self.click_add_to_cart()
        time.sleep(5)
        a = self.get_locator_all_products()[0].text.lower()
        print(len(self.get_locator_all_products_price()))
        time.sleep(5)
        print(self.get_locator_all_products_price()[2].text)
        time.sleep(3)
        print(self.get_locator_all_products_price()[1].text)
        time.sleep(3)
        amount_locators = self.get_locator_all_products_price()[2].text.replace('₾', '').replace(' ', '')
        time.sleep(5)
        self.click_order_button()
        print('add_all_products_page - done')
        return a, float(amount_locators)


    #
    # def check_all_products_page(self):
    #
    #     print('check_all_products_page-done')













