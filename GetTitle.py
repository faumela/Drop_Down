from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\ANJUM\\Drop_Down\\Drivers\\chromedriver.exe")
driver.set_page_load_timeout(20)
driver.maximize_window()

time.sleep(1)
driver.get('https://www.WhatsApp.com')
time.sleep(1)

#Fetching Title
print("Title of page is " + driver.title)

#Fetch URL of page
print("Page URL is" + driver.current_url)

#Fetch Complete page HTML
print("*****************************************************************************************************")
print(driver.page_source)
