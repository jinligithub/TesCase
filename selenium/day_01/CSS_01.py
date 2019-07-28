#导包
from time import sleep
from selenium import webdriver
#创建浏览器对象
driver=webdriver.Firefox
#获取项目的链接
url="E://test//a.html"
driver.get(url)
#使用CSS定义id
driver.find_element_by_css_selector("#user").send_keys("admin")
driver.find_element_by_css_selector("password").send_keys("123456")
driver.find_element_by_css_selector(".tel").send_keys("132645646655")

sleep(3)
#关闭浏览器d
driver.quit()