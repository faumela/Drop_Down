from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\ANJUM\\Drop_Down\\Drivers\\chromedriver.exe")

driver.get("https://demo.guru99.com/test/delete_customer.php")
driver.maximize_window()
driver.set_page_load_timeout(2)

driver.find_element_by_name("cusid").send_keys("55436")
driver.find_element_by_name("submit").click()

driver.switch_to.alert.accept()
time.sleep(2)
driver.switch_to.alert.accept()
driver.close()
