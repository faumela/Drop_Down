from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\\Users\\ANJUM\\Drop_Down\\Drivers\\chromedriver.exe")

driver.get("https://www.amazon.com")
driver.maximize_window()

ele=driver.find_element_by_xpath(".//*[@id='nav-link-accountList']/span[2]").click()
hover = ActionChains(driver).move_to_element(ele)
hover.perform()
driver.implicitly_wait(2)
