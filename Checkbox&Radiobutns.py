import time

from selenium import webdriver
from selenium.webdriver import ActionChains


driver = webdriver.Chrome("C:\\Users\\ANJUM\\Drop_Down\\Drivers\\chromedriver.exe")

driver.get("https://jqueryui.com/checkboxradio/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.switch_to.frame(driver.find_element_by_css_selector(".demo-frame"))

driver.find_element_by_xpath("//label[contains(text(),'New York')]").click()
time.sleep(2)

driver.find_element_by_xpath("//label[contains(text(),'2 Star')]").click()
time.sleep(2)

driver.find_element_by_xpath("//label[contains(text(),'5 Star')]").click()
time.sleep(2)

driver.find_element_by_xpath("//label[contains(text(),'2 Queen')]").click()
time.sleep(2)
driver.close()



