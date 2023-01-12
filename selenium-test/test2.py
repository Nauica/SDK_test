from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import utils
from time import sleep

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(r'c:\tools\chromedriver.exe')
# 如果找不到元素， 每隔 半秒钟 再去界面上查看一次， 直到找到该元素， 或者 过了10秒 最大时长。（暂时没用到）
wd.implicitly_wait(10)
# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.baidu.com/')

# 通过while循环获取baidu热搜前30
title_elements = wd.find_elements(By.CLASS_NAME, 'title-content-title')
print(title_elements[1].get_attribute('outerHTML'))
