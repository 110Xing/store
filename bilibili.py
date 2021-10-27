from selenium import  webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.bilibili.com/")
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="internationalHeader"]/div[1]/div/div[3]/div[2]/span[1]/div/span/div').click()

#切换页面
handle = driver.window_handles
driver.switch_to.window(handle[1])

driver.find_element_by_xpath('//*[@id="login-username"]').send_keys("19834025268")
driver.find_element_by_xpath('//*[@id="login-passwd"]').send_keys("a1056900912")
driver.find_element_by_xpath('//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()
time.sleep(5)

driver.find_element_by_xpath('//*[@id="nav_searchform"]/input').send_keys("一人之下")
driver.find_element_by_xpath('//*[@id="nav_searchform"]/div').click()
#切换页面
handle = driver.window_handles
driver.switch_to.window(handle[2])
driver.find_element_by_xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li[1]/a/div/div[1]/img').click()
driver.find_element_by_xpath('//*[@id="bilibiliPlayer"]/div[1]/div[1]/div[9]/video').click()