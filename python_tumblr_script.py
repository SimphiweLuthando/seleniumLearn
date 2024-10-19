from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.tumblr.com/register")

try:
    emailElement = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'email'))
    )
    emailElement.clear()
    emailElement.send_keys("put_your_email_here")
    passwordElement = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'password'))
    )
    passwordElement.clear()
    passwordElement.send_keys("put_your_password_here")
    signUpButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="Get started"]/div/div/div[2]/div[1]/section/div[2]/form/button')) # just make sure  this xpath is  still valid because it might not work for you
    )
    signUpButton.click()

except Exception as e:
    print("if you're reading this its too late: " + repr(e))
