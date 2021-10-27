from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException
import  time
#  当前浏览器
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(1)

driver.get("http://www.jd.com")

driver.find_element_by_xpath('//*[@id="ttbar-login"]/a[1]').click()
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()

driver.find_element_by_xpath('//*[@id="loginname"]').send_keys("19834025268")
driver.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys("a1056900912")
driver.find_element_by_xpath('//*[@id="loginsubmit"]').click()

ac = ActionChains(driver)
ele = driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]')
time.sleep(3)
for i in range(50,250):
    try:
        time.sleep(2)
        ac.click_and_hold(ele).move_by_offset(i,0).perform()

        ac.release()

    except UnexpectedAlertPresentException:
        break
        time.sleep(0.1)
        ac.reset_actions()
ac.release()




