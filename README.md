# Vega_test
Site testing project https://vega.ge/en using pytest.
1. Project structure:
    /base/
        base_class.py
    /pages/
        account_page_1.py
        adding_products_page.py
        cart_page_and_CHECKOUT.py
       login_page.py
       main_home_and_garden.py
       main_page_appliences.py
       main_page_furniture.py

    /scrinshots/
    /tests/
       test all products.py
   2. Test steps :
     1. go to the page https://vega.ge/en
     2. Click language change button, select Georgian
     3. Check URL
     4. Click language change button, select English
     5. Check URL
     6. Click authorization button
     7. Check URL
     8. Enter E-Mail Address and Password
     9. Click Login
     10. Сhecking the quantity of goods in the cart
     11. if the quantity of the product is not zero then delete the products
     12. Click Home appliances
     13. Click Computers and Laptops
     14. Click NOTEBOOKS
     15. Check URL
     16. select all filters for 10 september 2023
     17. move the left slider 30 pixels to the right
     18. move the right slider 10 pixels to the left
     19. Сreate dictionary and enter the price and name of the product(products_dict)
     20. select notebook LENOVO IdeaPad 3 17IAU7 (i3-1215U) 17.3 8GB 512GB (GR)
     21. Click on the link notebook LENOVO IdeaPad 3 17IAU7 (i3-1215U) 17.3 8GB 512GB (GR) (under the picture)
     22. Check URL
     23. Сreate dictionary and  enter the price and name of the product (products_adding_dict)
     24. Click ADD TO CART
     25. Click order
     26. Click Furniture
     27. Click Living room furniture
     28. Click Stands for tv
     29. Check URL
     30. select all filters for 10 september 2023
     31. move the left slider 30 pixels to the right
     32. move the right slider 10 pixels to the left
     33. select stand for tv VEGA X53
     34. Сreate  create a dictionary and enter the price and name of the product(products_dict)
     35. Click on the link stand for tv VEGA X53 (under the picture)
     36. Check URL
     37. Сreate dictionary and  enter the price and name of the product (products_adding_dict)
     38. Click ADD TO CART
     39. Click order
     40. Click Home and garden
     41. Click textile
     42. Click BED COVERS
     43. Check URL
     44. select all filters for 10 september 2023
     45. Select bed cover VETEXUS NTF 2017 BC 220X240
     46. Сreate a dictionary and enter the price and name of the product(products_dict)
     47. Click on the link bed cover VETEXUS NTF 2017 BC 220X240 (under the picture)
     48. Check URL
     49. Сreate dictionary and  enter the price and name of the product (products_adding_dict)
     50. Click ADD TO CART
     51. Click order
     52. Enter Billing Details( First Name ,Last Name, Phone,Phone 2, Address)
     53. enter data in the field USE REWARD POINTS
     54. Сreate dictionary and  enter the price and name of the product (finish_dict)
     55. checking 3 dictionaries(finish_dict,products_dict,products_adding_dict), they must be equal
     56. checking the sum of the dictionary values, it must be equal to the Total field
     57. if points 44 and 45 are completed, then the test is passed successfully

3.Test results:
test all products.py::test_buy_product_all PASSED                        [100%]start test
start autorizathion
get_url =  https://vega.ge/ge
good value url, assert_url
value_word = Საყოფაცხოვრებო Ტექნიკა
get_url =  https://vega.ge/en
good value url, assert_url
value_word = Home appliances
autorizathion-done
get_url =  https://vega.ge/en/index.php?route=account/account
good value url, assert_url
1 <class 'str'>
check_page_account-done
current url https://vega.ge/en/computers-and-laptops/notebooks/
get_url =  https://vega.ge/en/computers-and-laptops/notebooks/
good value url, assert_url
value_word = NOTEBOOKS
opening_Home_appliances-done
select_filter_home_appliances - done
get_url =  https://vega.ge/en/notebook-lenovo-ideapad-3-17iau7-i3-1215u-173-8gb-512gb-gr-82rl005grk.html
good value url, assert_url
value_word = Attributes
ORDER
check_all_products_page-done
get_url =  https://vega.ge/en/living-room-furniture/stands-for-tv/
good value url, assert_url
value_word = STANDS FOR TV
opening_Furniture-done
select_filter_furniture - done
get_url =  https://vega.ge/en/stand-for-tv-vega-x53.html
good value url, assert_url
value_word = Attributes
ORDER
check_all_products_page-done
current url https://vega.ge/en/textile/bed-covers/
get_url =  https://vega.ge/en/textile/bed-covers/
good value url, assert_url
value_word = BED COVERS
opening_Home_appliances-done
select_filter_home_and_garden - done
get_url =  https://vega.ge/en/bed-cover-vetexus-ntf-2017-bc-220x240.html
good value url, assert_url
value_word = Attributes
ORDER
check_all_products_page-done
Payment Method
get_url =  https://vega.ge/en/checkout-en/
good value url, assert_url
value_word = Payment Method
entering_personal_data - done
bed cover VETEXUS NTF 2017 BC 220X240
notebook LENOVO IdeaPad 3 17IAU7 (i3-1215U) 17.3 8GB 512GB (GR)
entering_all_product_data - done
test_all_products - done


======================== 1 passed in 306.55s (0:05:06) ========================

Process finished with exit code 0

4. libraries used in the project:
attrs==23.1.0
certifi==2023.7.22
cffi==1.15.1
colorama==0.4.6
exceptiongroup==1.1.3
h11==0.14.0
idna==3.4
iniconfig==2.0.0
outcome==1.2.0
packaging==23.1
Pillow==10.0.0
pluggy==1.2.0
pycparser==2.21
PySocks==1.7.1
pytest==7.4.0
selenium==4.11.2
Selenium-Screenshot==2.1.0
sniffio==1.3.0
sortedcontainers==2.4.0
tomli==2.0.1
trio==0.22.2
trio-websocket==0.10.3
urllib3==2.0.4
wsproto==1.2.0
         
     



       
