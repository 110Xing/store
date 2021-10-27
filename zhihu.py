from selenium import  webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.zhihu.com/")
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/div[1]/form/div[1]/div[2]').click()
driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/div[1]/form/div[2]/div/label/input').send_keys("19834025268")
driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/div[1]/form/div[3]/div/label/input').send_keys("a1056900912")
driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/div[1]/form/button').click()
time.sleep(5)










