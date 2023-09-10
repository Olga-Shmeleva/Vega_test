import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Main_page_furniture(Base):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # product group
    living_room_furniture = '/html/body/div[1]/div[2]/div/header/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]' \
                            '/div/div/div[2]/div/div/ul/li[2]/div/div/div/div/div[1]/ul/li[1]/a'
    stands_for_tv ='//*[@id="mfilter-content-container"]/div[2]/div/div[14]/a[2]'

    #locator STANDS FOR TV filters
    outer_sizes_90X40X43 = '//*[@id="mfilter-content-opts-0-2"]/div/div/div/div[1]/label'
    outer_sizes_120X44X40 = '//*[@id="mfilter-content-opts-0-2"]/div/div/div/div[2]/label'
    outer_sizes_120X45X50 = '//*[@id="mfilter-content-opts-0-2"]/div/div/div/div[3]/label'
    outer_sizes_140X45X56 = '//*[@id="mfilter-content-opts-0-2"]/div/div/div/div[4]/label'
    outer_sizes_141X40X43 = '//*[@id="mfilter-content-opts-0-2"]/div/div/div/div[5]/label'
    outer_sizes_143X40X40 = '//*[@id="mfilter-content-opts-0-2"]/div/div/div/div[6]/label'
    outer_sizes_145X48X52 = '//*[@id="mfilter-content-opts-0-2"]/div/div/div/div[7]/label'
    outer_sizes_150X43X44 = '//*[@id="mfilter-content-opts-0-2"]/div/div/div/div[8]/label'
    outer_sizes_162X42X45 = '//*[@id="mfilter-content-opts-0-2"]/div/div/div/div[9]/label'
    outer_sizes_170X44X45 = '//*[@id="mfilter-content-opts-0-2"]/div/div/div/div[10]/label'
    outer_sizes_200X45X50 = '//*[@id="mfilter-content-opts-0-2"]/div/div/div/div[11]/label'

    made_in_Armenia = '//*[@id="mfilter-box-43"]/div/ul/li[4]/div[2]/div[1]/div[1]/div/div/div/div/label'

    materials_laminate_metal = '//*[@id="mfilter-box-43"]/div/ul/li[5]/div[2]/div[1]/div[1]/div/div/div/div[1]/label'
    materials_laminated_chipboard ='//*[@id="mfilter-box-43"]/div/ul/li[5]/div[2]/div[1]/div[1]/div/div/div/div[2]/label'

    slider_right = '//*[@id="mfilter-price-slider"]/span[1]'
    slider_left = '//*[@id="mfilter-price-slider"]/span[2]'
    manufacturers_hobel = '//*[@id="mfilter-box-43"]/div/ul/li[2]/div[2]/div[1]/div[1]/div/div/div/div[1]/label'
    manufacturers_vega = '//*[@id="mfilter-box-43"]/div/ul/li[2]/div[2]/div[1]/div[1]/div/div/div/div[2]/label'
    manufacturers_vega_ex = '//*[@id="mfilter-box-43"]/div/ul/li[2]/div[2]/div[1]/div[1]/div/div/div/div[3]/label'
    selected_product = '//*[@id="product-43965"]/div[2]/div[1]/a'
    selected_product_price = '//*[@id="product-43965"]/div[2]/div[2]/span[2]'

    check_word = '//*[@id="mfilter-content-container"]/div[1]/h1'


    # getters
    def get_living_room_furniture(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.living_room_furniture)))
    def get_stands_for_tv(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.stands_for_tv)))
    def get_outer_sizes_90X40X43(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.outer_sizes_90X40X43)))
    def get_outer_sizes_120X44X40(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.outer_sizes_120X44X40)))
    def get_outer_sizes_120X45X50(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.outer_sizes_120X45X50)))
    def get_outer_sizes_140X45X56(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.outer_sizes_140X45X56)))
    def get_outer_sizes_141X40X43(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.outer_sizes_141X40X43)))
    def get_outer_sizes_143X40X40(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.outer_sizes_143X40X40)))
    def get_outer_sizes_145X48X52(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.outer_sizes_145X48X52)))
    def get_outer_sizes_150X43X44(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.outer_sizes_150X43X44)))
    def get_outer_sizes_162X42X45(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.outer_sizes_162X42X45)))
    def get_outer_sizes_170X44X45(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.outer_sizes_170X44X45)))
    def get_outer_sizes_200X45X50(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.outer_sizes_200X45X50)))
    def get_made_in_Armenia(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.made_in_Armenia)))
    def get_materials_laminate_metal(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.materials_laminate_metal)))
    def get_materials_laminated_chipboard(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.materials_laminated_chipboard)))
    def get_slider_left(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider_left)))
    def get_slider_right(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider_right)))
    def get_manufacturers_hobel(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.manufacturers_hobel)))
    def get_manufacturers_vega(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.manufacturers_vega)))
    def get_manufacturers_vega_ex(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.manufacturers_vega_ex)))
    def get_selected_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.selected_product)))
    def get_selected_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.selected_product_price)))

    # actions
    def click_living_room_furniture(self):
        self.get_living_room_furniture().click()
    def click_stands_for_tv(self):
        self.get_stands_for_tv().click()
    def click_outer_sizes_90X40X43(self):
        self.get_outer_sizes_90X40X43().click()
    def click_outer_sizes_120X44X40(self):
        self.get_outer_sizes_120X44X40().click()
    def click_outer_sizes_120X45X50(self):
        self.get_outer_sizes_120X45X50().click()
    def click_outer_sizes_140X45X56(self):
        self.get_outer_sizes_140X45X56().click()
    def click_outer_sizes_141X40X43(self):
        self.get_outer_sizes_141X40X43().click()
    def click_outer_sizes_143X40X40(self):
        self.get_outer_sizes_143X40X40().click()
    def click_outer_sizes_145X48X52(self):
        self.get_outer_sizes_145X48X52().click()
    def click_outer_sizes_150X43X44(self):
        self.get_outer_sizes_150X43X44().click()
    def click_outer_sizes_162X42X45(self):
        self.get_outer_sizes_162X42X45().click()
    def click_outer_sizes_170X44X45(self):
        self.get_outer_sizes_170X44X45().click()
    def click_outer_sizes_200X45X50(self):
        self.get_outer_sizes_200X45X50().click()
    def click_made_in_Armenia(self):
        self.get_made_in_Armenia().click()
    def click_materials_laminate_metal(self):
        self.get_materials_laminate_metal().click()
    def click_materials_laminated_chipboard(self):
        self.get_materials_laminated_chipboard().click()
    def click_manufacturers_hobel(self) :
        self.get_manufacturers_hobel().click()
    def click_manufacturers_vega(self):
        self.get_manufacturers_vega().click()
    def click_manufacturers_vega_ex(self):
        self.get_manufacturers_vega_ex().click()
    def click_selected_product(self):
        self.get_selected_product().click()
    def value_selected_product(self):
        value_price = self.get_selected_product_price().text.replace('₾', '').replace(' ', '')
        return self.get_selected_product().text.lower(), float(value_price)
    def click_slider(self):
        action = ActionChains(self.driver)
        time.sleep(5)
        action.click_and_hold(self.get_slider_left()).move_by_offset(-30, 0).release().perform()
        action.click_and_hold(self.get_slider_right()).move_by_offset(10, 0).release().perform()

    def opening_Furniture(self):
        self.click_living_room_furniture()
        self.click_stands_for_tv()
        self.assert_url('https://vega.ge/en/living-room-furniture/stands-for-tv/')
        self.assert_word(self.check_word, 'STANDS FOR TV')
        print('opening_Furniture-done')


    def select_filter_furniture(self):
        self.click_slider()
        self.click_manufacturers_hobel()
        self.click_manufacturers_vega()
        self.click_manufacturers_vega_ex()
        self.click_outer_sizes_90X40X43()
        self.click_outer_sizes_120X44X40()
        self.click_outer_sizes_120X45X50()
        self.click_outer_sizes_140X45X56()
        self.click_outer_sizes_141X40X43()
        self.click_outer_sizes_143X40X40()
        self.click_outer_sizes_145X48X52()
        self.click_outer_sizes_150X43X44()
        self.click_outer_sizes_162X42X45()
        self.click_outer_sizes_170X44X45()
        self.click_outer_sizes_200X45X50()
        self.click_made_in_Armenia()
        self.click_materials_laminate_metal()
        self.click_materials_laminated_chipboard()
        time.sleep(3)
        value_selected_product = self.value_selected_product()
        self.get_screenshot()
        self.click_selected_product()
        print('select_filter_furniture - done')
        return value_selected_product




