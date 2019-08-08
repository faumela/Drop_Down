from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\\Users\\ANJUM\\Drop_Down\\Drivers\\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("https://www.theTestingWorld.com/testings")
driver.maximize_window()
driver.implicitly_wait(10)


act = ActionChains(driver)

act.click().perform()
act.click(driver.find_element_by_xpath("//label[contains(text(),'Login')]")).perform()

act.context_click().perform()
act.context_click(driver.find_element_by_xpath("//label[contains(text(),'Login')]")).perform()


act.double_click().perform()
act.double_click(driver.find_element_by_xpath("//label[contains(text(),'Login')]")).perform()

act.move_to_element(driver.find_element_by_xpath("//span[contains(text(),'TUTORIAL')]")).perform()




