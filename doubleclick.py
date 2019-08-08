from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\\Users\\ANJUM\\Drop_Down\\Drivers\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(2)
driver.get('https://only-testing-blog.blogspot.in/2014/09/selectable.html')
driver.implicitly_wait(2)


element = driver.find_element_by_xpath("//button[contains(text(),'Double-Click Me To See Alert')]").click()

driver.implicitly_wait(10)

act = ActionChains(driver)

act.double_click(element).perform()

driver.switch_to.alert.accept()
