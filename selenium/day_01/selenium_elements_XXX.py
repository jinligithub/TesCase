#导包
from time import sleep

from selenium import webdriver
#创建浏览器对象
driver=webdriver.Firefox
#获取项目的链接
url="E://test//a.html"
driver.get(url)
#定位tag标签，并且操作元素
'''
elements:返回所有符合条件的元素
说明：返回格式为列表，所以访问的时候必须指定下标，下标从0开始
'''
driver.find_elements_by_tag_name("input")[1].send_keys("123456")
sleep(3)
#关闭浏览器d
driver.quit()