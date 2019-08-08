from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
driver = webdriver.Firefox(capabilities=cap, executable_path="C:\\Users\\ANJUM\\Drop_Down\\Drivers\\geckodriver.exe")


driver.get('https://www.google.com/')
# driver.quit()
