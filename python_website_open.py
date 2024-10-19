from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.news24.com")
driver.implicitly_wait(4)
element = driver.find_element(By.XPATH, '//*[@id="search"]')
driver.implicitly_wait(3)
element.clear()
driver.implicitly_wait(4)
element.send_keys("eskom")
driver.implicitly_wait(10)
element.send_keys(Keys.RETURN)
assert "No results found" not in driver.page_source
print(driver.title)
driver.close()