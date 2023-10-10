from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.ideal.lv/")
time.sleep(1)
driver.quit()
