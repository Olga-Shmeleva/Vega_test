# import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.account_page_1 import My_account_page_1
from pages.adding_products_page import Adding_products_page
from pages.cart_page_and_CHECKOUT import Checkout_cart_page

from pages.login_page import Login_page
from pages.main_home_and_garden import Main_page_home_and_garden
from pages.main_page_appliences import Main_page_appliences
from pages.main_page_furniture import Main_page_furniture



def test_buy_product_all():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    print('start test')

    login = Login_page(driver)
    login.autorizathion()

    ap = My_account_page_1(driver)
    ap.check_page_account()
    ap.select_home_appliences()

    products_dict = {}
    products_adding_dict = {}

# notebook
    mpa = Main_page_appliences(driver)
    mpa.opening_home_appliances()
    products_home_appliences, price_home_appliences = mpa.select_filter_home_appliances()
    products_dict.setdefault(products_home_appliences, price_home_appliences)

    adp = Adding_products_page(driver)
    products_home_appliences_adding_dict, price_home_appliences_adding_dict = adp.add_all_products_page()
    products_adding_dict.setdefault(products_home_appliences_adding_dict, price_home_appliences_adding_dict)

    adp.check_all_products_page()

# table for tv
    ap = My_account_page_1(driver)
    ap.select_furniture()

    mpf = Main_page_furniture(driver)
    mpf.opening_Furniture()
    products_home_furniture, price_home_furniture = mpf.select_filter_furniture()
    products_dict.setdefault(products_home_furniture, price_home_furniture)

    adp = Adding_products_page(driver)
    products_furniture_adding_dict, price_furniture_adding_dict = adp.add_all_products_page()
    products_adding_dict.setdefault(products_furniture_adding_dict, price_furniture_adding_dict)

    adp.check_all_products_page()

# blanket
    ap = My_account_page_1(driver)
    ap.select_home_and_garden()

    mphg = Main_page_home_and_garden(driver)
    mphg.opening_home_and_garden()
    products_main_page_home_and_garden, price_main_page_home_and_garden = mphg.select_filter_home_and_garden()
    products_dict.setdefault(products_main_page_home_and_garden, price_main_page_home_and_garden)

    adp = Adding_products_page(driver)
    products_home_and_garden_adding_dict, price_home_and_garden_adding_dict = adp.add_all_products_page()
    products_adding_dict.setdefault(products_home_and_garden_adding_dict, price_home_and_garden_adding_dict)
    adp.check_all_products_page()

    cpc = Checkout_cart_page(driver)
    cpc.entering_personal_data()
    finish_dict = cpc.entering_all_product_data()

    assert products_adding_dict == finish_dict == products_dict
    print('test_all_products - done')


