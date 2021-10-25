from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get(r"D:\python自动化测试\pc\自动化\day1\练习的html\上传文件和下拉列表")

driver.maximize_window()

driver.find_element_by_xpath("//*[@class = 'icon file' and @draggable = 'true']").click()

time.sleep(2)

# driver.find_element_by_id("accountID") 局限性
driver.find_element_by_xpath("//*[@id='accountID']").send_keys("jason jia")
driver.find_element_by_xpath("//*[@id='passwordID']").send_keys("admin")
driver.find_element_by_xpath("//*[@id='areaID']").send_keys("北京市")

time.sleep(2)
driver.find_element_by_xpath("//*[@id='sexID2']").click()
driver.find_element_by_xpath("//*[@value='spring']").click()
driver.find_element_by_xpath("//*[@value='Auterm']").click()
driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"C:\Users\27283\Pictures\新建文件夹\hutao.jpg")

