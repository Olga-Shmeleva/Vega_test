import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Login_page(Base):

    url = 'https://vega.ge/en'

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    single_neutral = "//a[@class='my-account']"
    user_name = "//input[@id='input-email']"
    password = "//input[@id='input-password']"
    submit_button = "//input[@type='submit']"
    select_language = '//a[@class="dropdown-toggle"]'
    select_language_eng = '//*[@id="language_form"]/div/ul/li[1]/a'
    select_language_kartuli = '//*[@id="language_form"]/div/ul/li[3]/a/img'
    check_word = '/html/body/div[1]/div[2]/div/header/div[2]/div[2]/div[2]/div[2]' \
                 '/div/div/div/div[2]/div/div/div[2]/div/div/ul/li[1]'



    # getters
    def get_single_neutral(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.single_neutral)))
    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))
    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))
    def get_submit_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.submit_button)))
    def get_home_appliences(self):
        return self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/header/div[2]/div[2]'
                                                 '/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/ul/li[1]')
    def get_select_language(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_language)))
    def get_select_language_eng(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_language_eng)))
    def get_select_language_kartuli(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_language_kartuli)))

    # actions

    def input_single_neutral(self, single_neutral):
        self.get_user_name().send_keys(single_neutral)

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)

    def input_password(self, password):
        self.get_password().send_keys(password)

    def click_single_neutral(self):
        self.get_single_neutral().click()

    def click_submit_button(self):
        self.get_submit_button().click()

    def click_select_language (self):
        self.get_select_language().click()

    def click_select_language_eng(self):
        self.get_select_language_eng().click()

    def click_select_language_kartuli(self):
        self.get_select_language_kartuli().click()


   #Methods
    def autorizathion(self):

        print('start autorizathion')
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_select_language()
        self.click_select_language_kartuli()
        time.sleep(5)
        self.assert_url('https://vega.ge/ge')
        self.assert_word(self.check_word, 'Საყოფაცხოვრებო Ტექნიკა')
        self.get_screenshot()
        time.sleep(5)
        self.click_select_language()
        self.click_select_language_eng()
        self.assert_url('https://vega.ge/en')
        self.assert_word(self.check_word, 'Home appliances')
        time.sleep(5)
        self.click_single_neutral()
        self.input_user_name('kamchatkaptz@gmail.com')
        self.input_password('Adapsish41')
        self.click_submit_button()
        print('autorizathion-done')


