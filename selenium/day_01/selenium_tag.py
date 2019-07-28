#导包
from time import sleep

from selenium import webdriver
#创建浏览器对象
driver=webdriver.Firefox
#获取项目的链接
url="E://test//a.html"
driver.get(url)
#定位tag标签，并且操作元素
driver.find_element_by_tag_name("input").send_keys("admin")
sleep(3)
#关闭浏览器d
driver.quit()