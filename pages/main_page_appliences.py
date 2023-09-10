import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Main_page_appliences(Base):


    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


    # locators:

    # megamenu-pattern


    # product group
    audio_video_photo = '//a[@href="en/audio-video"]'
    computers_and_laptops ='//a[@href="en/computers-and-laptops"]'
    personal_care = '//a[@href="en/personal-care"]'
    notebooks = '//a[@href="https://vega.ge/en/computers-and-laptops/notebooks/"]'

    #locator Notebooks filters

    MANUFACTURERS_lenovo = '//*[@id="mfilter-opts-attribs-43-manufacturers-342"]'
    MANUFACTURERS_ACER = '//input[@value="206"]'
    MANUFACTURERS_ASUS = '//input[@value="9"]'
    MANUFACTURERS_HP = '//input[@value="65"]'
    MANUFACTURERS_INTEL = '//input[@value="68"]'
    MANUFACTURERS_PRESTIGIO = '//input[@value="931"]'

    TOUCH_SCREEN_NO ='//input[@id="mfilter-opts-attribs-43-886154-bafd7322c6e97d25b6299b5d6fe8920b"]'
    TOUCH_SCREEN_YES = '//input[@id="mfilter-opts-attribs-43-886154-93cba07454f06a4a960172bbd6e2a435"]'

    CLASS_STANDART = '//input[@name="88454-class"]'

    OS_NOT_INSTALLED = '//input[@value="Not Installed"]'
    OS_WINDOWS_10_HOME = '//input[@value="Windows 10 HOME"]'
    OS_WINDOWS_10_PRO = '//input[@value="Windows 10 Pro"]'

    SHOCKPROOF_BODY = '//input[@name="8815666-shockproof-body"]'
    DUST_and_SPLASH_PROTECTION = '//input[@name="8815656-dust-and-splash-protection"]'
    HDD_NO = '//input[@name="886434-hdd-gb"]'

    WEIGHT_165 = '//input[@value="1.65"]'
    WEIGHT_17 = '//input[@value="1.7"]'
    WEIGHT_23 = '//input[@value="2.3"]'
    WEIGHT_16 = '//input[@value="1.6"]'
    WEIGHT_2 = '//input[@value="2"]'
    WEIGHT_128eMMC = '//input[@value="128 eMMC"]'

    SSD256 = '//input[@value="256"]'
    SSD512 = '//input[@value="512"]'

    COLOR_GREY = '//input[@value="Grey"]'
    COLOR_GREEN = '//input[@value="Green"]'
    COLOR_SILVER = '//input[@value="Silver"]'
    COLOR_BLACK = '//input[@value="Black"]'

    gPU_ = '//input[@value="AMD Radeon Vega 7"]'
    gPU_INTEL_IRIS_XE_GRAPHICS = '//input[@value="Intel Iris Xe Graphics"]'
    gPU_Intel_UHD_Graphics = '//input[@value="Intel UHD Graphics"]'
    gPU_Iris_Xe_Graphics_G7 = '//input[@value="Iris Xe Graphics G7"]'
    gPU_NVIDIA_GeForce_MX550_2GB = '//input[@value="NVIDIA GeForce MX550 2GB"]'
    gPU_Radeon_R4_Graphics = '//input[@value="Radeon R4 Graphics"]'


    CPU_intel_1215 = '//input[@value="i3-1215U"]'
    CPU_intel_1235 = '//input[@value="i5-1235U"]'
    CPU_i7_1165G7 = '//input[@value="i7-1165G7"]'
    CPU_i7_1255U = '//input[@value="i7-1255U"]'
    CPU_R5_5600H = '//input[@value="R5-5600H"]'


    FREQUENCY_3334 = '//input[@id="mfilter-opts-attribs-43-885834-4e034ab926f2d2d2ed511551cfecdce7"]'
    FREQUENCY_22 = '//input[@value="2.2"]'
    FREQUENCY_24_up_42 = '//input[@value="2.4 up to 4.2"]'
    FREQUENCY_24_42 = '//input[@value="2.4-4.2"]'
    FREQUENCY_28_47 = '//input[@value="2.8-4.7"]'
    FREQUENCY_30_46 = '//input[@value="3.0-4.6"]'
    FREQUENCY_32_44 = '//input[@value="3.2-4.4"]'
    FREQUENCY_35_47 = '// input[ @ value = "3.5-4.7"]'

    RAM_8 = '//*[@id="mfilter-opts-attribs-43-88884-c9f0f895fb98ab9159f51fd0297e236d"]'
    RAM_4 = '//input[@value="4"]'
    RAM_8_DDR4_3200MHz = '//input[@value="8 DDR4 3200MHz"]'
    RAM_16 = '//input[@value="16"]'

    DISPLAY_SIZE_173 = '//input[@value="17.3"]'
    DISPLAY_SIZE_14 = '//input[@value="14"]'
    DISPLAY_SIZE_14_1 = '//input[@value="14.1"]'
    DISPLAY_SIZE_15_6 = '//input[@value="15.6"]'


    SCREEN_RESOLUTION_1920_1080 = '//input[@id="mfilter-opts-attribs-43-885334-9e523ae15b61dc766f5c818726881ecf"]'
    SCREEN_RESOLUTION_1366x768 = '//input[@value="1366x768 HD TN"]'
    SCREEN_RESOLUTION_1920x1080_FHD_OLED = '//input[@value="1920x1080 (FHD) OLED"]'

    OPTICAL_DRIVE_NO = '//input[@id="mfilter-opts-attribs-43-885344-bafd7322c6e97d25b6299b5d6fe8920b"]'

    slider_right = '//*[@id="mfilter-price-slider"]/span[1]'
    slider_left = '//*[@id="mfilter-price-slider"]/span[2]'

    selected_product = '//*[@id="product-206329"]/div[2]/div[1]/a'
    selected_product_price = '//*[@id="product-206329"]/div[2]/div[2]/span[2]'

    check_word = '//*[@id="mfilter-content-container"]/div[1]/h1'


    # getters

    def get_computers_and_laptops(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.computers_and_laptops)))
    def get_notebooks (self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.notebooks)))
    def get_MANUFACTURERS_lenovo(self):
        return self.driver.find_element(By.XPATH,self.MANUFACTURERS_lenovo)
    def get_TOUCH_SCREEN_NO(self):
        return self.driver.find_element(By.XPATH,self.TOUCH_SCREEN_NO)
    def get_CLASS_STANDART(self):
        return self.driver.find_element(By.XPATH,self.CLASS_STANDART)
    def get_OS_NOT_INSTALLED(self):
        return self.driver.find_element(By.XPATH,self.OS_NOT_INSTALLED)
    def get_OS_WINDOWS_10_HOME(self):
        return self.driver.find_element(By.XPATH,self.OS_WINDOWS_10_HOME)
    def get_SHOCKPROOF_BODY(self):
        return self.driver.find_element(By.XPATH,self.SHOCKPROOF_BODY)
    def get_DUST_and_SPLASH_PROTECTION(self):
        return self.driver.find_element(By.XPATH,self.DUST_and_SPLASH_PROTECTION)
    def get_HDD_NO(self):
        return self.driver.find_element(By.XPATH,self.HDD_NO)
    def get_WEIGHT_165(self):
        return self.driver.find_element(By.XPATH,self.WEIGHT_165)
    def get_WEIGHT_17(self):
        return self.driver.find_element(By.XPATH,self.WEIGHT_17)
    def get_WEIGHT_23(self):
        return self.driver.find_element(By.XPATH,self.WEIGHT_23)
    def get_SSD256(self):
        return self.driver.find_element(By.XPATH,self.SSD256)
    def get_SSD512(self):
        return self.driver.find_element(By.XPATH,self.SSD512)
    def get_COLOR_GREY(self):
        return self.driver.find_element(By.XPATH,self.COLOR_GREY)
    def get_gPU_Intel_UHD_Graphics(self):
        return self.driver.find_element(By.XPATH,self.gPU_Intel_UHD_Graphics)
    def get_CPU_intel_1215(self):
        return self.driver.find_element(By.XPATH,self.CPU_intel_1215)
    def get_CPU_intel_1235(self):
        return self.driver.find_element(By.XPATH,self.CPU_intel_1235)
    def get_FREQUENCY_33_34 (self):
        return self.driver.find_element(By.XPATH,self.FREQUENCY_3334)
    def get_RAM_8(self):
        return self.driver.find_element(By.XPATH,self.RAM_8)
    def get_DISPLAY_SIZE_173(self):
        return self.driver.find_element(By.XPATH,self.DISPLAY_SIZE_173)
    def get_SCREEN_RESOLUTION_1920_1080(self):
        return self.driver.find_element(By.XPATH,self.SCREEN_RESOLUTION_1920_1080)
    def get_OPTICAL_DRIVE_NO(self):
        return self.driver.find_element(By.XPATH,self.OPTICAL_DRIVE_NO)
    def get_slider_left(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider_left)))
    def get_slider_right(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider_right)))
    def get_PRICE_min(self):
        return(self.driver.find_element(By.XPATH,self.PRICE_min))
    def get_PRICE_max(self):
        return(self.driver.find_element(By.XPATH,self.PRICE_max))
    def get_selected_product(self):
        return (self.driver.find_element(By.XPATH, self.selected_product))
    def get_selected_product_price(self):
        return (self.driver.find_element(By.XPATH, self.selected_product_price))


    # actions


    def click_computers_and_laptops(self):
        self.get_computers_and_laptops().click()

    def click_notebooks(self):
        self.get_notebooks().click()

    def click_MANUFACTURERS_lenovo(self):
       self.get_MANUFACTURERS_lenovo().click()

    def click_TOUCH_SCREEN_NO(self):
        self.get_TOUCH_SCREEN_NO().click()

    def click_CLASS_STANDART(self):
        self.get_CLASS_STANDART().click()

    def click_OS_NOT_INSTALLED(self):
        self.get_OS_NOT_INSTALLED().click()

    def click_OS_WINDOWS_10_HOME(self):
        self.get_OS_WINDOWS_10_HOME().click()

    def click_SHOCKPROOF_BODY(self):
        self.get_SHOCKPROOF_BODY().click()

    def click_DUST_and_SPLASH_PROTECTION(self):
        self.get_DUST_and_SPLASH_PROTECTION().click()

    def clickt_HDD_NO(self):
        self.get_HDD_NO().click()

    def click_WEIGHT_165(self):
        self.get_WEIGHT_165().click()

    def click_WEIGHT_17(self):
        self.get_WEIGHT_17().click()

    def click_WEIGHT_23(self):
        self.get_WEIGHT_23().click()

    def click_SSD256(self):
        self.get_SSD256().click()

    def click_SSD512(self):
        self.get_SSD512().click()

    def clickt_COLOR_GREY(self):
        self.get_COLOR_GREY().click()

    def click_gPU_Intel_UHD_Graphics(self):
        self.get_gPU_Intel_UHD_Graphics().click()

    def click_CPU_intel_1215(self):
        self.get_CPU_intel_1215().click()

    def click_CPU_intel_1235(self):
        self.get_CPU_intel_1235().click()

    def click_FREQUENCY_33_34 (self):
        self.get_FREQUENCY_33_34().click()

    def click_RAM_8(self):
        self.get_RAM_8().click()

    def click_DISPLAY_SIZE_173(self):
        self.get_DISPLAY_SIZE_173().click()

    def click_SCREEN_RESOLUTION_1920_1080(self):
        self.get_SCREEN_RESOLUTION_1920_1080().click()

    def click_OPTICAL_DRIVE_NO(self):
        self.get_OPTICAL_DRIVE_NO().click()

    def click_slider(self):
        action = ActionChains(self.driver)
        time.sleep(5)
        action.click_and_hold(self.get_slider_left()).move_by_offset(-30, 0).release().perform()
        action.click_and_hold(self.get_slider_right()).move_by_offset(10, 0).release().perform()


    def click_selected_product(self):
        self.get_selected_product().click()

    def value_selected_product(self):
        value_price = self.get_selected_product_price().text.replace('₾', '').replace(' ', '')
        return self.get_selected_product().text.lower(), float(value_price)

    def opening_home_appliances(self):
        self.click_computers_and_laptops()
        self.click_notebooks()
        self.get_current_url()
        self.assert_url('https://vega.ge/en/computers-and-laptops/notebooks/')
        self.assert_word(self.check_word, 'NOTEBOOKS')
        print('opening_Home_appliances-done')


    def select_filter_home_appliances(self):
        self.click_slider()
        time.sleep(3)
        self.click_MANUFACTURERS_lenovo()
        self.click_TOUCH_SCREEN_NO()
        self.click_CLASS_STANDART()
        self.click_OS_NOT_INSTALLED()
        self.click_OS_WINDOWS_10_HOME()
        self.click_SHOCKPROOF_BODY()
        self.click_DUST_and_SPLASH_PROTECTION()
        self.clickt_HDD_NO()
        self.click_WEIGHT_165()
        self.click_WEIGHT_17()
        self.click_WEIGHT_23()
        self.click_SSD256()
        self.click_SSD512()
        self.clickt_COLOR_GREY()
        self.click_gPU_Intel_UHD_Graphics()
        self.click_CPU_intel_1215()
        self.click_CPU_intel_1235()
        self.click_FREQUENCY_33_34()
        self.click_RAM_8()
        self.click_DISPLAY_SIZE_173()
        self.click_SCREEN_RESOLUTION_1920_1080()
        self.click_OPTICAL_DRIVE_NO()
        time.sleep(5)
        value_selected_product = self.value_selected_product()
        self.get_screenshot()
        self.click_selected_product()
        print('select_filter_home_appliances - done')
        return value_selected_product

