from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

from Login import login
driver=login()
def new_request ():

    driver.find_element_by_xpath('/html//button[@id="createNew"]').click()
    # выбор адреса
    driver.find_element_by_xpath('//div[@class="right"]/descendant::input[@class="ant-input ant-select-search__field"]').send_keys('10-я Парковая улица, дом 15')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//li[contains(@class,"ant-select-dropdown-menu-item-active ant-select-dropdown-menu-item")]'))
        )
    driver.find_element_by_xpath('//li[contains(@class,"ant-select-dropdown-menu-item-active ant-select-dropdown-menu-item")]').click()
    # конец выбора адреса

    driver.find_element_by_xpath('//input[@id="address-comment"]').send_keys('comment')
    driver.find_element_by_xpath('//input[@id="podezd"]').send_keys('1')
    driver.find_element_by_xpath('//input[@id="floor"]').send_keys('3')
    driver.find_element_by_xpath('//input[@id="apartment"]').send_keys('77')
    driver.find_element_by_xpath('//span[contains(text(),"№ квартиры")]').click()
    driver.find_element_by_xpath('//span[contains(text(),"консьерж")]').click()
    driver.find_element_by_xpath('//span[contains(text(),"другой")]').click()
    driver.find_element_by_xpath('//span[@style="margin-bottom: 0px; width: 0px; flex-grow: 1; margin-right: 1px;" and @class="ant-input-affix-wrapper"]/descendant::input[@class="ant-input"]').send_keys('123')
    driver.find_element_by_xpath('//div[contains(@class,"row")]/descendant::input[@id="phone-main"]').send_keys('1111111111')
    driver.find_element_by_xpath('//input[@id="phone-additional"]').send_keys('22222222222')
    driver.find_element_by_xpath('//span[text()="завтра"]').click()
    driver.find_element_by_xpath('//span[text()="сегодня"]').click()
    driver.find_element_by_xpath('//span[text()="первая половина"]').click()
    driver.find_element_by_xpath('//span[text()="вторая половина"]').click()
    driver.find_element_by_xpath('//span[text()="особые условия"]').click()

    #начало выбора времени
    driver.find_element_by_xpath('//input[@class="ant-time-picker-input" and @value="08:00"]').click()
    #выбор времени в первом блоке (часы)
    hours_menu_first = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"ant-time-picker-panel-combobox")]//div[1]//li[text()="10"]')))
    fastrack=driver.find_element_by_xpath('//div[contains(@class,"ant-time-picker-panel-combobox")]//div[1]//li[text()="22"]')
    ActionChains(driver).move_to_element(hours_menu_first).click(fastrack).perform()#фокус на элементе
    # # wait for Fastrack menu item to appear, then click it
    # fastrack = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"ant-time-picker-panel-combobox")]//div[1]//li[text()="22"]')))
    #выбор времени в первом блоке (минуты)
    minutes_menu_first = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"ant-time-picker-panel-combobox")]//div[2]//li[text()="02"]')))
    fastrack2=driver.find_element_by_xpath('//div[contains(@class,"ant-time-picker-panel-combobox")]//div[2]//li[text()="45"]')
    ActionChains(driver).move_to_element(minutes_menu_first).click(fastrack2).perform()

    #выбор времени во втором блоке (часы)
    driver.find_element_by_xpath('//input[@class="ant-time-picker-input" and @value="20:00"]').click()
    time.sleep(1)
    hours_menu_second = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"ant-time-picker-panel-combobox")]//div[1]//li[text()="22"]')))
    fastrack=driver.find_element_by_xpath('//div[contains(@class,"ant-time-picker-panel-combobox")]//div[1]//li[text()="23"]')
    ActionChains(driver).move_to_element(hours_menu_second).click(fastrack).perform()#фокус на элементе
    #выбор времени во втором блоке (минуты)
    minutes_menu_second = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"ant-time-picker-panel-combobox")]//div[2]//li[text()="02"]')))
    fastrack2=driver.find_element_by_xpath('//div[contains(@class,"ant-time-picker-panel-combobox")]//div[2]//li[text()="55"]')
    ActionChains(driver).move_to_element(minutes_menu_second).click(fastrack2).perform()
    #конец выбора времени

    #выбор источника, перебор вариантов
    #телефон
    driver.find_element_by_xpath('//div[text()="телефон"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//div[@class="ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft"]//li[@title="личное обращение (окно)"]').click()
    #личное обращение
    driver.find_element_by_xpath('//div[text()="личное обращение (окно)"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//div[@class="ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft"]//li[@title="переговорное устройство"]').click()
    #переговорное устройство
    driver.find_element_by_xpath('//div[text()="переговорное устройство"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//div[@class="ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft"]//li[@title="телефон"]').click()
    #конц выбора источника

    #выбор типа заявки
    driver.find_element_by_xpath('//span[@class="ant-select-selection__rendered"]').click()
    driver.find_element_by_xpath('//div[@class="tree-content-height-limiter"]//input[@class="ant-select-search__field" and @role="textbox"]').send_keys('Благоустройство Другое')
    driver.find_element_by_xpath('//span[@class="ant-select-tree-node-content-wrapper ant-select-tree-node-content-wrapper-normal"]').click()
    driver.find_element_by_xpath('//div[@class="left"]//textarea[@class="ant-input"]').send_keys('Описание проблемы')
    # driver.find_element_by_xpath('//div[@id="new-request"]//div[@class="close-button"]').click()

    #кнопка СОХРАНИТЬ
    driver.find_element_by_xpath('//button[@title="Сохранить"]').click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[@id="request_created"]'))
    )
    text = driver.find_element_by_xpath('//div[@id="request_created"]').text
    request_number=text[:-2]
    request_number= request_number.replace("Была создана заявка ","")
    driver.find_element_by_xpath('//div[@id="new-request"]//div[@class="close-button"]').click()
    print(request_number)
    return request_number

