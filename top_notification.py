from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from Login import login

driver=login()
def notification_main_phone ():
    driver.find_element_by_xpath('//button[@id="createNew"]').click()
    # выбор адреса
    driver.find_element_by_xpath('//div[@class="right"]/descendant::input[@class="ant-input ant-select-search__field"]').send_keys('10-я Парковая улица, дом 15')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//li[contains(@class,"ant-select-dropdown-menu-item-active ant-select-dropdown-menu-item")]'))
        )
    driver.find_element_by_xpath('//li[contains(@class,"ant-select-dropdown-menu-item-active ant-select-dropdown-menu-item")]').click()
    # конец выбора адреса
    time.sleep(2)
    driver.find_element_by_xpath('//span[@class="ant-select-selection__rendered"]').click()
    driver.find_element_by_xpath('//div[@class="tree-content-height-limiter"]//input[@class="ant-select-search__field" and @role="textbox"]').send_keys('Благоустройство Другое')
    driver.find_element_by_xpath('//span[@class="ant-select-tree-node-content-wrapper ant-select-tree-node-content-wrapper-normal"]').click()
    driver.find_element_by_xpath('//button[@title="Сохранить"]').click()
    #проверка доступности элементов на форме
    # print(driver.find_element_by_xpath('//small[text()="Укажите основной телефон"]').is_displayed())
    # print(driver.find_element_by_xpath('//div[contains(@class,"row")]/descendant::input[@id="phone-main" and contains(@style,"margin-bottom: 0px; border-color: red;")]').is_displayed())
    # print(driver.find_element_by_xpath('//div[@id="required"]//div[contains(@class,"closeable-timed-notification")]').is_displayed())
    text=driver.find_element_by_xpath('//div[@id="required"]').text
    text=text[:-2]
    print(text)
    # return notification_main_phone()

