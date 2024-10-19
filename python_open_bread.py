from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://www.checkers.co.za/")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="XS Deals Carousel Home Page"]/div/div[2]/div/div[5]/div/div/figure/section/figcaption/div/h3/a'))
    )
    ActionChains(driver).move_to_element(element).click(element).perform()
    price = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'before'))
    )


    price_text = price.get_attribute('innerHTML').strip()
    price = price_text.replace('<sup>', '.').replace('</sup>', '')

    print("price before: " + price)
finally:
    driver.quit()



