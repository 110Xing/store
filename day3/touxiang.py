from selenium import webdriver


driver = webdriver.Chrome()


driver.get("http://localhost:8080/HKR/")#打开网页
driver.maximize_window()
driver.implicitly_wait(2)

#输入账号密码
driver.find_element_by_xpath('//*[@id="loginname"]').send_keys("a1056900912")#输入账号
driver.find_element_by_xpath('//*[@id="password"]').send_keys("10.22xing")#输入密码
driver.find_element_by_xpath('//*[@id="submit"]').click()#点击登陆
driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="img"]').click()#点击头像
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="ul_pic"]/li[3]/img').click()#更换头像


