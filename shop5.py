import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
Shop = driver.find_element_by_link_text("Shop")
Shop.click()
Add = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=181']")
Add.click()
