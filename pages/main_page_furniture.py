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
    living_room_furniture = 'a[href="en/living-room-furniture"]'
    stands_for_tv ='span[class="cat-title"]'

    #locator STANDS FOR TV filters
    outer_sizes_90X40X43 = 'label[for=mfilter-opts-attribs-43-889974-b311b3810284864b5cab2091988fd94a]'
    outer_sizes_120X44X40 = 'label[for=mfilter-opts-attribs-43-889974-4ab83f79a4faf94e6b4cb7182b7be291]'
    outer_sizes_120X45X50 = 'label[for=mfilter-opts-attribs-43-889974-1df8909032912b3e809ebc6d8131859b]'
    outer_sizes_140X45X56 = 'label[for=mfilter-opts-attribs-43-889974-7d0833cf1da2e5240a64aff5b9eb1f3e]'
    outer_sizes_141X40X43 = 'label[for=mfilter-opts-attribs-43-889974-414a36888ce7c795cc36f00221b7d105]'
    outer_sizes_143X40X40 = 'label[for=mfilter-opts-attribs-43-889974-7bdad8f2ca649c1cafc267fa7c8e6b51]'
    outer_sizes_145X48X52 = 'label[for=mfilter-opts-attribs-43-889974-88c8d73187b43cf407274ecfec5e4161]'
    outer_sizes_150X43X44 = 'label[for=mfilter-opts-attribs-43-889974-cb93054c7420afe99ec81dd0e6bdf617]'
    outer_sizes_162X42X45 = 'label[for=mfilter-opts-attribs-43-889974-f2522fc7ff86682e741025e74fd73eaa]'
    outer_sizes_170X44X45 = 'label[for=mfilter-opts-attribs-43-889974-0853bd01aac640513a77f6168df430a9]'
    outer_sizes_200X45X50 = 'label[for=mfilter-opts-attribs-43-889974-86f011fde2b7eac8e0d2c6dc79cd3a26]'

    made_in_Armenia = 'label[for=mfilter-opts-attribs-43-8810064-a00c273f0f497484093fa94865cf5ca5]'

    materials_laminate_metal = 'label[for=mfilter-opts-attribs-43-885084-62dfdf0c132dbdda7ceddd8cf222421c]'
    materials_laminated_chipboard ='label[for=mfilter-opts-attribs-43-885084-05f806a9331a4cd451269cffab431dc4]'

    slider_right = 'span.ui-slider-handle.ui-state-default.ui-corner-all'
    manufacturers_hobel = 'label[for=mfilter-opts-attribs-43-manufacturers-3617]'
    manufacturers_vega = 'label[for=mfilter-opts-attribs-43-manufacturers-153]'
    manufacturers_vega_ex = 'label[for=mfilter-opts-attribs-43-manufacturers-2584]'
    selected_product = 'a[href="https://vega.ge/en/stand-for-tv-vega-x53.html"]'
    selected_product_price = 'span[class="price-new"]'

    check_word = """a[href="https://vega.ge/en/living-room-furniture/stands-for-tv/"""


    # getters
    def get_living_room_furniture(self):
        return (self.driver.find_elements(By.CSS_SELECTOR, self.living_room_furniture))
    def get_stands_for_tv(self):
        return (self.driver.find_elements(By.CSS_SELECTOR, self.stands_for_tv))
    def get_outer_sizes_90X40X43(self):
        return (self.driver.find_elements(By.CSS_SELECTOR, self.outer_sizes_90X40X43))
    def get_outer_sizes_120X44X40(self):
        return (self.driver.find_elements(By.CSS_SELECTOR, self.outer_sizes_120X44X40))
    def get_outer_sizes_120X45X50(self):
        return (self.driver.find_elements(By.CSS_SELECTOR, self.outer_sizes_120X45X50))
    def get_outer_sizes_140X45X56(self):
        return (self.driver.find_elements(By.CSS_SELECTOR, self.outer_sizes_140X45X56))
    def get_outer_sizes_141X40X43(self):
        return (self.driver.find_elements(By.CSS_SELECTOR, self.outer_sizes_141X40X43))
    def get_outer_sizes_143X40X40(self):
        return (self.driver.find_elements(By.CSS_SELECTOR, self.outer_sizes_143X40X40))
    def get_outer_sizes_145X48X52(self):
        return (self.driver.find_elements(By.CSS_SELECTOR, self.outer_sizes_145X48X52))
    def get_outer_sizes_150X43X44(self):
        return (self.driver.find_elements(By.CSS_SELECTOR, self.outer_sizes_150X43X44))
    def get_outer_sizes_162X42X45(self):
        return (self.driver.find_elements(By.CSS_SELECTOR, self.outer_sizes_162X42X45))
    def get_outer_sizes_170X44X45(self):
        return (self.driver.find_elements(By.CSS_SELECTOR, self.outer_sizes_170X44X45))
    def get_outer_sizes_200X45X50(self):
        return (self.driver.find_elements(By.CSS_SELECTOR, self.outer_sizes_200X45X50))
    def get_made_in_Armenia(self):
        return (self.driver.find_elements(By.CSS_SELECTOR, self.made_in_Armenia))
    def get_materials_laminate_metal(self):
        return (self.driver.find_elements(By.CSS_SELECTOR,self.materials_laminate_metal))
    def get_materials_laminated_chipboard(self):
        return (self.driver.find_elements(By.CSS_SELECTOR,self.materials_laminated_chipboard))
    def get_slider_left(self):
        time.sleep(3)
        return (self.driver.find_elements(By.CSS_SELECTOR, self.slider_right))

    def get_manufacturers_hobel(self):
        return (self.driver.find_elements(By.CSS_SELECTOR, self.manufacturers_hobel))
    def get_manufacturers_vega(self):
        return (self.driver.find_elements(By.CSS_SELECTOR, self.manufacturers_vega))
    def get_manufacturers_vega_ex(self):
        return (self.driver.find_elements(By.CSS_SELECTOR, self.manufacturers_vega_ex))
    def get_selected_product(self):
        return (self.driver.find_elements(By.CSS_SELECTOR, self.selected_product))
    def get_selected_product_price(self):
        return (self.driver.find_elements(By.CSS_SELECTOR, self.selected_product_price))
    def get_check_word(self):
        time.sleep(3)
        return (self.driver.find_elements(By.CSS_SELECTOR, self.check_word))

    # actions
    def click_living_room_furniture(self):
        time.sleep(3)
        self.get_living_room_furniture()[0].click()
    def click_stands_for_tv(self):
        time.sleep(3)
        self.get_stands_for_tv()[14].click()
    def click_outer_sizes_90X40X43(self):
        self.get_outer_sizes_90X40X43()[0].click()
    def click_outer_sizes_120X44X40(self):
        self.get_outer_sizes_120X44X40()[0].click()
    def click_outer_sizes_120X45X50(self):
        self.get_outer_sizes_120X45X50()[0].click()
    def click_outer_sizes_140X45X56(self):
        self.get_outer_sizes_140X45X56()[0].click()
    def click_outer_sizes_141X40X43(self):
        self.get_outer_sizes_141X40X43()[0].click()
    def click_outer_sizes_143X40X40(self):
        self.get_outer_sizes_143X40X40()[0].click()
    def click_outer_sizes_145X48X52(self):
        self.get_outer_sizes_145X48X52()[0].click()
    def click_outer_sizes_150X43X44(self):
        self.get_outer_sizes_150X43X44()[0].click()
    def click_outer_sizes_162X42X45(self):
        self.get_outer_sizes_162X42X45()[0].click()
    def click_outer_sizes_170X44X45(self):
        self.get_outer_sizes_170X44X45()[0].click()
    def click_outer_sizes_200X45X50(self):
        self.get_outer_sizes_200X45X50()[0].click()
    def click_made_in_Armenia(self):
        self.get_made_in_Armenia()[0].click()
    def click_materials_laminate_metal(self):
        self.get_materials_laminate_metal()[0].click()
    def click_materials_laminated_chipboard(self):
        self.get_materials_laminated_chipboard()[0].click()
    def click_manufacturers_hobel(self):
        self.get_manufacturers_hobel()[0].click()
    def click_manufacturers_vega(self):
        self.get_manufacturers_vega()[0].click()
    def click_manufacturers_vega_ex(self):
        self.get_manufacturers_vega_ex()[0].click()
    def click_selected_product(self):
        self.get_selected_product()[3].click()
    def value_selected_product(self):
        value_price = self.get_selected_product_price()[16].text.replace('₾', '').replace(' ', '')
        return self.get_selected_product()[3].text.lower(), float(value_price)
    def click_slider(self):
        action = ActionChains(self.driver)
        time.sleep(5)
        action.click_and_hold(self.get_slider_left()[1]).move_by_offset(-30, 0).release().perform()
        action.click_and_hold(self.get_slider_left()[0]).move_by_offset(30, 0).release().perform()

    #Methods

    def opening_Furniture(self):
        self.click_living_room_furniture()
        self.click_stands_for_tv()
        self.assert_url('https://vega.ge/en/living-room-furniture/stands-for-tv/')
        self.assert_word(self.get_check_word()[1], 'STANDS FOR TV')
        print('opening_Furniture-done')


    def select_filter_furniture(self):
        self.click_slider()
        self.click_outer_sizes_90X40X43()
        self.click_manufacturers_hobel()
        self.click_manufacturers_vega()
        self.click_manufacturers_vega_ex()
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
