import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
MyAccount = driver.find_element_by_link_text("My Account")
MyAccount.click()
Username = driver.find_element_by_id("username")
Username.send_keys("mintal@rambler.ru")
Password = driver.find_element_by_id("password")
Password.send_keys("Rbhjdcr2015")
Login = driver.find_element_by_xpath("//*[@value='Login']")
Login.click()
Shop = driver.find_element_by_link_text("Shop")
Shop.click()
HTML = driver.find_element_by_link_text("HTML")
HTML.click()
count = driver.find_elements_by_css_selector("[href='http://practice.automationtesting.in/product-category/html/']")
if len(count) == 3:
    print("Отображается 3 товара")
else:
    print("Ошибка. Количество товаров в категории:" + str(len(count)))



