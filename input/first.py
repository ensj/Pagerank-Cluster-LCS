from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/limjunhyun/Desktop/selenium-drivers/chromedriver')
driver.get("http://www.google.com")
assert "Python" in driver.title

driver.close()