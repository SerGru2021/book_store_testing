import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
MyAccount = driver.find_element_by_link_text("My Account")
MyAccount.click()
Email = driver.find_element_by_id("reg_email")
Email.send_keys("mintal@rambler.ru")
Password = driver.find_element_by_id("reg_password")
Password.send_keys("Rbhjdcr2015")
time.sleep(10)
Register = driver.find_element_by_xpath("//*[@value='Register']")
Register.click()
