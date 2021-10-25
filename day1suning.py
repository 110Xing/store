from selenium import  webdriver

#  当前浏览器
driver = webdriver.Chrome()
driver.maximize_window()


driver.get("http://www.suning.com")
driver.implicitly_wait(2)

driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("联想拯救者y7000")
driver.find_element_by_xpath("//*[@id='searchSubmit']").click()

driver.implicitly_wait(2)
driver.find_element_by_xpath("//*[@id='0070094154-12233144535']/div/div/div[1]/div/a/img").click()

handle = driver.window_handles
driver.switch_to.window(handle[1])

driver.find_element_by_xpath("//*[@id='addCart']").click()