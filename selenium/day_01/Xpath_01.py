#导包
from time import sleep
from selenium import webdriver
#创建浏览器对象
driver=webdriver.Firefox
#获取项目的链接
url="E://test//a.html"
driver.get(url)
#定位link_text标签，
driver.find_element_by_xpath("/html/body/div/p[1]").send_keys("admin")
driver.find_element_by_xpath("/html/body/div/p[1]").send_keys("123456")
sleep(3)
#关闭浏览器d
driver.quit()