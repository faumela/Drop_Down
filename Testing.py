from selenium .webdriver.support.select import Select
from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\ANJUM\\Drop_Down\\Drivers\\chromedriver.exe")
driver.set_page_load_timeout(20)
driver.maximize_window()
time.sleep(1)
driver.get("http://www.theTestingWorld.com/testings")
time.sleep(1)

driver.find_element_by_xpath("//input[@placeholder='myusername']").send_keys("Misba")
driver.find_element_by_xpath("//input[@placeholder='myusername@gmail.com']").send_keys("sabatahseen442@gmail.com")
driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("abc123")
driver.find_element_by_xpath("//input[@placeholder='Confirm password']").send_keys("abc123")
driver.find_element_by_xpath("//input[@id='datepicker']").send_keys("29/07/1999")
driver.find_element_by_xpath("//input[@placeholder='Phone']").send_keys("9988776655")
driver.find_element_by_xpath("//input[@placeholder='Address']").send_keys("KCT college")
driver.find_element_by_xpath("/html[1]/body[1]/div[4]/section[1]/ul[1]/li[1]/div[1]/form[1]/input[9]").click()
time.sleep(1)

#Select by index
obj = Select(driver.find_element_by_name("sex"))
obj.select_by_index(2)


obj = Select(driver.find_element_by_name("country"))
obj.select_by_visible_text("India")
time.sleep(10)
obj = Select(driver.find_element_by_name("state"))
obj.select_by_visible_text("Karnataka")
time.sleep(6)
obj = Select(driver.find_element_by_name("city"))
obj.select_by_visible_text("Alur")

time.sleep(1)
driver.find_element_by_css_selector("div.container:nth-child(7) section.tabblue.center ul.tabs.blue li:nth-child(1) div.tab-content:nth-child(3) form:nth-child(3) div.btn:nth-child(24) > input:nth-child(3)").click()
driver.close()
