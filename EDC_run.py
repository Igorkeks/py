import create_new_request
from create_new_request import *

# from top_notification import notification_main_phone
number=new_request()
driver.find_element_by_xpath('//span[@class="search ant-input-affix-wrapper"]//input[@id="search"]').send_keys(number)
driver.find_element_by_xpath('//div[@class="enter-icon"]').click()
# notification_main_phone()