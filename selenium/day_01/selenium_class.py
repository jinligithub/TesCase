#导包
from time import sleep
from selenium import webdriver
#创建浏览器对象
driver=webdriver.Firefox
#打开项目的链接
url="E://test//A.html"
driver.get(url)
#定位属性class，
driver.find_element_by_class_name("tel").send_keys("1235465465")
sleep(2)
#退出
driver.quit()