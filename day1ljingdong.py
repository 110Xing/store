from selenium import  webdriver
import  time
#  当前浏览器
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(1)

driver.get("http://www.jd.com")


driver.implicitly_wait(2)
driver.find_element_by_xpath("//*[@id='key']").send_keys("联想拯救者y7000")

driver.find_element_by_xpath("//*[@id='search']/div/div[2]/button/i").click()

driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[1]/div/div[1]/a/img").click()

handle = driver.window_handles

driver.switch_to.window(handle[1])


driver.find_element_by_xpath("//*[@id='area1']/div[1]/b").click()
driver.find_element_by_xpath("//*[@id='area1']/div[2]/div[1]/a[1]").click()
driver.find_element_by_xpath("//*[@id='area1']/div[2]/div[2]/div[1]/ul/li[2]/a").click()
driver.find_element_by_xpath("//*[@id='area1']/div[2]/div[2]/div[2]/ul/li[2]/a").click()
driver.find_element_by_xpath("//*[@id='area1']/div[2]/div[2]/div[3]/ul/li[2]/a").click()
driver.find_element_by_xpath("//*[@id='choose-attr-1']/div[2]/div[1]/a").click()
driver.find_element_by_xpath("//*[@id='choose-attr-2']/div[2]/div[1]/a").click()
driver.find_element_by_xpath("//*[@id='choose-baitiao']/div[2]/div[1]/div[1]/a/strong").click()
driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()





