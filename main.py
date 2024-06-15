import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/cookieclicker/')

time.sleep(3)

agreeCookies = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]')
agreeCookies.click()
designatedLang = driver.find_element(By.ID, 'promptContentChangeLanguage').find_elements(By.TAG_NAME, 'div')[1]
designatedLang.click()

time.sleep(3)

btn = driver.find_element(By.ID, 'bigCookie')

while True:
    btn.click()

driver.quit()

