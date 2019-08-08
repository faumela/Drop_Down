import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\\Users\\ANJUM\\Drop_Down\\Drivers\\chromedriver.exe")

driver.get("https://jqueryui.com/draggable/#sortable")
driver.maximize_window()
driver.implicitly_wait(10)
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='demo-frame']"))
source = driver.find_element_by_id('draggable')
target = driver.find_element_by_xpath("//li[contains(text(),'Item 5')]")

mouse=ActionChains(driver).drag_and_drop(source,target)
mouse.perform()

time.sleep(2)
