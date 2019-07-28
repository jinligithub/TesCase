#导包
from time import sleep
from selenium import webdriver
#实例化对象
driver=webdriver.Firefox
#打开URL
url="E://test//A.html"
driver.get(url)
#定义用户及操作
driver.find_element_by_name("user").send_keys("admin")
#定义用户密码及操作
driver.find_element_by_name("password").send_keys("123456")
sleep(2)
#退出
driver.quit()