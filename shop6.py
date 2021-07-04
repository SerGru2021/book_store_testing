import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
Shop = driver.find_element_by_link_text("Shop")
Shop.click()
driver.execute_script("window.scrollBy(0, 300);")
HTML5Web = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']")
HTML5Web.click()
time.sleep(5)
JSData = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=180']")
JSData.click()
time.sleep(5)
Basket = driver.find_element_by_xpath("//*[@class='cartcontents']")
Basket.click()
time.sleep(5)
Remove = driver.find_element_by_xpath("//*[@title='Remove this item']")
Remove.click()
time.sleep(5)
Undo = driver.find_element_by_link_text("Undo?")
Undo.click()

