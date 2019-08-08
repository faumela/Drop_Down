from selenium import webdriver
import time


driver = webdriver.Chrome("C:\\Users\\ANJUM\\Drop_Down\\Drivers\\chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()


driver.get("https://www.jqueryui.com/checkboxradio")
time.sleep(2)

elem = driver.find_element_by_xpath("//a[contains(text(),'Themes')]")
time.sleep(2)
elem.click()
time.sleep(4)
driver.back()
time.sleep(4)
driver.forward()

