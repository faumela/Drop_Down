from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\ANJUM\\Drop_Down\\Drivers\\chromedriver.exe")
driver.set_page_load_timeout(10)

driver.get("https://lms.latitudelearning.com")
driver.maximize_window()
driver.set_page_load_timeout(2)

driver.get_screenshot_as_file("E:\\Screenshot\\Latitude.jpeg")
