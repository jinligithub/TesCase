#导包
from time import sleep
from selenium import webdriver
#创建浏览器对象
driver=webdriver.Firefox
#获取项目的链接
url="E://test//a.html"
driver.get(url)
#定位link_text标签，并且操作元素
'''
传入要定位的全部元素，全部文本
click（）：单击方法
find_element_by_partial_link_text():模糊匹配必须具有相应的代表性
'''
driver.find_element_by_partial_link_text("访问").click()
sleep(3)
#关闭浏览器d
driver.quit()