from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get(r"D:\python自动化测试\pc\自动化\day1\练习的html\弹框的验证")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath("//*[@class = 'icon file' and @draggable = 'true']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='confirm']").click()

driver.switch_to.alert.accept()  #accept()  确定
driver.switch_to.alert.dismiss() # 取消