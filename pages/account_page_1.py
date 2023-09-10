import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class My_account_page_1(Base):

    url = 'https://vega.ge/en'

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


    # locators:

    home_appliences = '/html/body/div[1]/div[2]/div/header/div[2]/div[2]/div[2]' \
                      '/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/ul/li[1]'
    furniture = '/html/body/div[1]/div[2]/div/header/div[2]/div[2]/div[2]/div[2]' \
                '/div/div/div/div[2]/div/div/div[2]/div/div/ul/li[2]'
    home_and_garden = '/html/body/div[1]/div[2]/div/header/div[2]/div[2]/div[2]' \
                      '/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/ul/li[3]'
    stand_for_tv_vega_remover = """//*[@id="cart_content_ajax"]/div[1]/table/tbody/tr[1]/td[5]/a"""
    bed_cover_remover = """//*[@id="cart_content_ajax"]/div[1]/table/tbody/tr[2]/td[5]/a"""
    notebook_lenovo_remover = """//*[@id="cart_content_ajax"]/div[1]/table/tbody/tr[3]/td[5]/a"""
    close_window = '//*[@id="tawk-mpreview-close"]/i'

    locator_cart = '//*[@id="cart_block"]/div[1]/i'
    remove_cart_button = '//a[@title="Remove"]'
    cart_total = '//*[@id="cart_content_ajax"]/div[2]/table/tbody/tr[2]/td[2]'

    # getters
    def get_home_appliences(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.home_appliences)))
    def get_furniture(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.furniture)))
    def get_home_and_garden(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self. home_and_garden)))
    def get_locator_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_cart)))
    def get_remove_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.remove_cart_button)))
    def get_stand_for_tv_vega_remover(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.stand_for_tv_vega_remover)))
    def get_bed_cover_remover(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.bed_cover_remover)))
    def get_notebook_lenovo_remover(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.notebook_lenovo_remover)))
    def get_close_window(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close_window)))
    def get_cart_total(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_total)))


    # actions
    def click_home_appliences(self):
        self.get_home_appliences().click()
    def click_furniture(self):
        self.get_furniture().click()
    def click_home_and_garden(self):
        self.get_home_and_garden().click()
    def click_locator_cart(self):
        self.get_locator_cart().click()
        time.sleep(5)
    def click_remove_cart_button(self):
        self.get_remove_cart_button().click()
    def click_stand_for_tv_vega_remover(self):
        self.get_stand_for_tv_vega_remover().click()
    def click_bed_cover_remover(self):
        self.get_bed_cover_remover().click()
    def click_notebook_lenovo_remover(self):
        self.get_notebook_lenovo_remover().click()
    def click_close_window(self):
        self.get_close_window()

    def remover_locators(self):
        locators = [
            self.bed_cover_remover,
            self.stand_for_tv_vega_remover,
            self.notebook_lenovo_remover
        ]
        value_locator_cart = self.get_locator_cart().text
        print(value_locator_cart, type(value_locator_cart))
        if str(value_locator_cart) not in '0':
            self.click_locator_cart()
            for element in locators:
                time.sleep(5)
                self.check_locators_products(element)
                value_locator_cart = self.get_locator_cart().text
        return value_locator_cart

    def check_page_account(self):
        time.sleep(5)
        self.assert_url('https://vega.ge/en/index.php?route=account/account')
        remover = self.remover_locators()
        assert str(remover) == '0'
        print('check_page_account-done')

    def select_home_appliences(self):
        time.sleep(5)
        self.click_home_appliences()

    def select_furniture(self):
        time.sleep(5)
        self.click_furniture()

    def select_home_and_garden(self):
        time.sleep(5)
        self.click_home_and_garden()

