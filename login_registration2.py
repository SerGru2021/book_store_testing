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
Logout = WebDriverWait(driver, 10).until(
    EC.invisibility_of_element_located((By.CSS_SELECTOR, "Logout")))
