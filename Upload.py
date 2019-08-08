import time
import os
from selenium import webdriver


driver = webdriver.Chrome("C:\\Users\\ANJUM\\Drop_Down\\Drivers\\chromedriver.exe")

driver.get("https:the-internet.herokuapp.com/upload")
time.sleep(2)
driver.find_element_by_id("file-upload").send_keys('E:\Pictures\Screenshots\IMG_20190119_202412_406.JPG')
time.sleep(2)
driver.find_element_by_id("file-submit").click()

time.sleep(4)