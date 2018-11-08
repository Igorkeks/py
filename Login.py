from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login ():
    driver = webdriver.Chrome()
    driver.get("http://213.79.88.85/")
    driver.set_window_size(1200,1200)
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Логин"]'))
    )
    # print(driver.find_element_by_xpath('//input[@placeholder="Логин"]').is_displayed())
    # print(driver.find_element_by_xpath('//input[@placeholder="Логин"]').is_enabled())
    driver.find_element_by_xpath('//input[@placeholder="Логин"]').send_keys('Support')
    driver.find_element_by_xpath('//input[@placeholder="Пароль"]').send_keys('1234')
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(4)

    return driver
