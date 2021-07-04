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
some_element = driver.find_element_by_xpath("//*[@value='menu_order']")
element_check = WebDriverWait(driver, 10).until(
	EC.element_to_be_selected(some_element))
driver.find_element_by_css_selector("[value='price-desc']").click()
some_element2 = driver.find_element_by_xpath("//*[@value='price-desc']")
element_check2 = WebDriverWait(driver, 10).until(
	EC.element_to_be_selected(some_element2))
