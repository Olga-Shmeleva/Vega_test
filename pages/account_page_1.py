import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from base.base_class import Base

class My_account_page_1(Base):

    url = 'https://vega.ge/en'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # locators:
    home_appliences = 'with-sub-menu.hover.furniture1-rooms'
    furniture = 'li.with-sub-menu.hover.furniture100-rooms'
    home_and_garden = 'li.with-sub-menu.hover.furniture200-rooms'
    locator = '//a[@class="clearfix"]'
    remover_locators = 'a[title="Remove"]'
    locator_cart = 'i.cart-count'
    empty_cart = '//div[@class="empty"]'


    # getters
    def get_home_appliences(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, self.home_appliences)))
    def get_furniture(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.furniture)))
    def get_home_and_garden(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.home_and_garden)))
    def get_locator_cart(self):
        time.sleep(3)
        return (self.driver.find_elements(By.CSS_SELECTOR, self.locator_cart))

    def get_empty_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.empty_cart)))
    def get_remover_locators(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.remover_locators)


    # actions
    def click_home_appliences(self):
        time.sleep(3)
        self.get_home_appliences().click()
    def click_furniture(self):
        time.sleep(3)
        self.get_furniture().click()
    def click_home_and_garden(self):
        time.sleep(3)
        self.get_home_and_garden().click()
    def click_locator_cart(self):
        time.sleep(3)
        self.get_locator_cart()[1].click()
        time.sleep(5)

    def get_value_empty(self):
        return self.get_empty_cart().text
    def click_remover_locators(self):
        time.sleep(1)
        self.get_remover_locators()[0].click()


     # Methods

    def dell_locators(self):
        value_locator_cart = self.get_locator_cart()[1].text
        value_empty = 'cart is empty'
        if str(value_locator_cart) not in '0':
            self.click_locator_cart()
            while value_locator_cart not in [0, '0']:
                time.sleep(2)
                self.check_locators_products(self.get_remover_locators()[0])
                value_locator_cart = self.get_locator_cart()[1].text
            value_empty = self.get_value_empty()
        return value_locator_cart, value_empty


    def check_page_account(self):
        print('start check_page_account')
        time.sleep(5)
        self.assert_url('https://vega.ge/en/index.php?route=account/account')
        remover, value_empty = self.dell_locators()
        assert str(remover) == '0'
        print(value_empty)
        print('check_page_account-done')


    def select_home_appliences(self):
        total = 0
        if self.get_home_appliences().is_displayed():
            total = total+1
        else:
            print("Элемент скрыт на странице.")

        if self.get_home_appliences().is_enabled():
            print("Элемент активен и готов к взаимодействию.")
            total = total + 1
        else:
            print("Элемент неактивен и не реагирует на действия пользователя.")

        if total == 2:
            print('print("Элемент видим на странице.click_home_appliences()")')
            self.click_home_appliences()


    def select_furniture(self):
        total = 0
        if self.get_furniture().is_displayed():
            total = total + 1
        else:
            print("Элемент скрыт на странице.")

        if self.get_furniture().is_enabled():
            print("Элемент активен и готов к взаимодействию.")
            total = total + 1
        else:
            print("Элемент неактивен и не реагирует на действия пользователя.")

        if total == 2:
            print("Элемент видим на странице.click_furniture()")
            self.click_furniture()

    def select_home_and_garden(self):
        total = 0
        if self.get_home_and_garden().is_displayed():
            total = total + 1
        else:
            print("Элемент скрыт на странице.")

        if self.get_home_and_garden().is_enabled():
            print("Элемент активен и готов к взаимодействию.")
            total = total + 1
        else:
            print("Элемент неактивен и не реагирует на действия пользователя.")

        if total == 2:
            print('print("Элемент видим на странице.click_home_and_garden()")')
            self.click_home_and_garden()
