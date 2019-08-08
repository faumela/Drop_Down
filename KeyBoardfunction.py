from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome("C:\\Users\\ANJUM\\Drop_Down\\Drivers\\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("https://www.facebook.com")
driver.implicitly_wait(10)
driver.find_element_by_xpath("//input[@id='u_0_l']").send_keys("Misba")

act = ActionChains(driver)
act.send_keys(Keys.TAB).perform()
act.send_keys(Keys.CONTROL).perform()
act.send_keys(Keys.SPACE).perform()
act.send_keys(Keys.ENTER).perform()


