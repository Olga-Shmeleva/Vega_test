import datetime
import inspect
import time
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base():

    def __init__(self, driver):
        self.driver = driver
        driver.implicitly_wait(10)


    """method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print('current url ' + get_url)

    """method assert word"""
    # def assert_word(self, word, result):
    #     time.sleep(5)
    #     value_word = self.driver.find_element(By.CSS_SELECTOR, word).text
    #     print('value_word =', value_word)
    #     assert value_word == result
    def assert_word(self, word, result):
        time.sleep(5)
        value_word = word.text
        print('value_word =', value_word)
        assert value_word == result

    """ method screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%M.%d.%H.%M.%S')
        name_screenshot = 'save_screenshot' + now_date + '.png'
        # self.driver.get_screenshot_as_file('C:\\Users\\User\\PycharmProjects\\Vega\\screen\\' + name_screenshot)

    """method assert url"""
    def assert_url(self, result):
        time.sleep(5)
        get_url = self.driver.current_url
        print('get_url = ', get_url)
        assert get_url == result
        print('good value url, assert_url')

    """ catching exceptions """
    def check_get_pop_up_window(self, locator):
        try:
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locator)))
        except ElementClickInterceptedException as exception:
            screen_height = self.driver.execute_script("return window.innerHeight;")
            scroll_pixels = int(screen_height / 3)
            self.driver.execute_script(f'window.scrollBy(0, {scroll_pixels});')
            time.sleep(5)
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locator)))
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    """ Получение имя модуля (файла) и имя класса """

    def get_calling_module_name(self):
        # Получаем информацию о вызывающем кадре (фрейме)
        caller_frame = inspect.currentframe().f_back
        # Получаем информацию о модуле, из которого был вызван текущий метод
        caller_module = inspect.getmodule(caller_frame)
        # Получаем имя модуля (файла) и имя класса
        module_name = caller_module.__name__
        class_name = caller_frame.f_locals.get('self', None).__class__.__name__
        return module_name, class_name

    '''проверка локаторов'''
    def check_locators_products(self, locator):
        error_dict = {}
        module_name, class_name = self.get_calling_module_name()
        try:
            element_product = locator.text
        except NoSuchElementException:
            return error_dict.setdefault(locator, "Элемент с локатором не найден")
        except Exception as e:
            error_dict.setdefault(locator, f"Произошла ошибка при поиске элемента с локатором {e}")
        else:
            if class_name == 'My_account_page_1':
                locator.click()
            else:
                return element_product














