from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Users\\ANJUM\\Drop_Down\\Drivers\\chromedriver.exe")
driver.set_page_load_timeout(20)
driver.maximize_window()
driver.get('https://www.WhatsApp.com')
time.sleep(1)

elm = driver.find_element_by_tag_name("html")
time.sleep(2)
elm.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
elm.send_keys(Keys.HOME)
time.sleep(2)
driver.quit()
