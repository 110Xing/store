from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get(r"D:\python自动化测试\pc\自动化\day1\练习的html\跳转页面")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath("//*[@class = 'icon file' and @draggable = 'true']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id = 'goo']").click()