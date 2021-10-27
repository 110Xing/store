from selenium import  webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.qichacha.com/")
driver.find_element_by_xpath('/html/body/header/div/ul/li[10]/a/span').click()
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="normalLogin"]').click()
driver.find_element_by_xpath('//*[@id="nameNormal"]').send_keys("19834025268")
driver.find_element_by_xpath('//*[@id="pwdNormal"]').send_keys("a1056900912")
driver.find_element_by_xpath('//*[@id="user_login_normal"]/button/b').click()
time.sleep(5)