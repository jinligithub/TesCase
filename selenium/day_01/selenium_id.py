#导包(ctrl+alt+enter)
from time import sleep
from selenium import webdriver
#实例化浏览器
driver=webdriver.Firefox
#打开项目的URL
'''
第一种写法：url="E:\\test\\a.html"
第二种写法：url=r"E:\\test\\a.html"
r作用：被r修饰的字符串，字符串中的转义中文字符不能做转义使用
\: 作为转义字符，必须要用两个\\
第三种写法：直接从浏览器复制URL链接

'''
url="E:\\test\\a.html"
driver.get(url)
#操作
driver.find_element_by_id("user").send_keys("admin")
sleep(2)
#退出
driver.quit();



