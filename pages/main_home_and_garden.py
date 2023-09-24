import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Main_page_home_and_garden(Base):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # locators:

    # product group
    textile = '//a[@href="en/textile"]'
    bed_covers = '//*[@id="mfilter-content-container"]/div[2]/div/div[15]/a[2]'

    #locator BED COVERS filters

    manufacturers_vetexus = 'label[class="mfilter-tb-as-td"]'
    bed_cover_220X240 = '//*[@id="mfilter-box-43"]/div/ul/li[3]/div[2]/div[1]/div[1]/div/div/div/div/label'
    pillow_case_50X70 = '//*[@id="mfilter-box-43"]/div/ul/li[4]/div[2]/div[1]/div[1]/div/div/div/div/label'
    manufacturer_country = '//*[@id="mfilter-box-43"]/div/ul/li[5]/div[2]/div[1]/div[1]/div/div/div/div/label'
    external_fabric_cot_pol ='//*[@id="mfilter-box-43"]/div/ul/li[6]/div[2]/div[1]/div[1]/div/div/div/div/label'
    selected_product ="""a[href="https://vega.ge/en/bed-cover-vetexus-ntf-2019-bc-220x240.html"]"""
    selected_product_price = 'span.price-new'
    check_word = """a[href="https://vega.ge/en/textile/bed-covers/"]"""

    # getters

    def get_textile(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.textile)))
    def get_bed_covers(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.bed_covers)))
    def get_manufacturers_vetexus(self):
        time.sleep(3)
        return self.driver.find_elements(By.CSS_SELECTOR, self.manufacturers_vetexus)
    def get_bed_cover_220X240(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.bed_cover_220X240)))
    def get_pillow_case_50X70(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pillow_case_50X70)))
    def get_manufacturer_country(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.manufacturer_country)))
    def get_external_fabric_cot_pol(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.external_fabric_cot_pol)))
    # def get_slider_left(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider_left)))
    # def get_slider_right(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider_right)))
    # def get_PRICE_min(self):
    #     return(self.driver.find_element(By.XPATH,self.PRICE_min))
    # def get_PRICE_max(self):
    #     return(self.driver.find_element(By.XPATH,self.PRICE_max))
    def get_selected_product(self):
        time.sleep(3)
        return (self.driver.find_elements(By.CSS_SELECTOR, self.selected_product))
    def get_selected_product_price(self):
        time.sleep(3)
        return (self.driver.find_elements(By.CSS_SELECTOR, self.selected_product_price))
    def get_check_word(self):
        time.sleep(3)
        return (self.driver.find_elements(By.CSS_SELECTOR, self.check_word))

    # actions

    def click_textile(self):
        self.get_textile().click()
    def click_bed_covers(self):
        self.get_bed_covers().click()
    def click_manufacturers_vetexus(self):
        self.get_manufacturers_vetexus()[0].click()
    def click_bed_cover_220X240(self):
        self.get_manufacturers_vetexus()[1].click()
    def click_pillow_case_50X70(self):
        self.get_manufacturers_vetexus()[2].click()
    def click_manufacturer_country(self):
        self.get_manufacturers_vetexus()[3].click()
    def click_external_fabric_cot_pol(self):
        self.get_manufacturers_vetexus()[4].click()

    def click_selected_product(self):
        self.get_selected_product()[3].click()
    def value_selected_product(self):
        value_price = self.get_selected_product_price()[4].text.replace('₾', '').replace(' ', '').lower()
        print(value_price)
        return self.get_selected_product()[3].text.lower(), float(value_price)

     # Methods


    def opening_home_and_garden(self):
        print('start opening_home_and_garden' )
        self.click_textile()
        self.click_bed_covers()
        self.get_current_url()
        self.assert_url('https://vega.ge/en/textile/bed-covers/')
        self.assert_word(self.get_check_word()[1], 'BED COVERS')
        print('opening_Home_appliances-done')

    def select_filter_home_and_garden(self):
        print('start select_filter_home_and_garden')
        time.sleep(3)
        self.click_manufacturers_vetexus()
        self.click_pillow_case_50X70()
        self.click_manufacturer_country()
        self.click_external_fabric_cot_pol()
        time.sleep(3)
        value_selected_product = self.value_selected_product()
        self.get_screenshot()
        self.click_selected_product()
        print('select_filter_home_and_garden - done')
        return value_selected_product



