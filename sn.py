from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains

import time
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(1)

driver.get("http://www.suning.com")
driver.find_element_by_xpath('//*[@id="reg-bar-node"]/a[1]').click()#进入登陆页面
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[1]/a[2]/span').click()#选择账号登陆
driver.find_element_by_xpath('//*[@id="showErrorUsernameDiv"]/label').send_keys("19834025268")#输入账号
driver.find_element_by_xpath('//*[@id="showErrorPwdDiv"]/label').send_keys("a1056900912")#输入密码
driver.find_element_by_xpath('//*[@id="iar1_sncaptcha_button"]/span').click()#验证

ac = ActionChains(driver)
ele = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[2]/div[2]/div/div[3]/img[1]')#选择按钮
time.sleep(3)
for i in range(300):
    try:
        ac.click_and_hold(ele).move_by_offset(78,0).perform()

        ac.release()
        driver.implicitly_wait(2)
    except UnexpectedAlertPresentException:
        break
        time.sleep(0.1)
        ac.reset_actions()
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="submit"]').click()

