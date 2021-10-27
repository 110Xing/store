from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains


import  time
#  当前浏览器
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(1)

driver.get("http://www.taobao.com")

driver.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()
# driver.find_element_by_xpath('//*[@id="login"]/div[2]/div/div[1]/a[1]').click()

driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys("19834025268")
driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys("a1056900912")

ac = ActionChains(driver)
driver.implicitly_wait(2)
ele = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')

ac.click_and_hold(ele).move_by_offset(300,0).perform()
ac.release()
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()