"""
此脚本用于获取www.baidu.com链接中实时热点内容信息与链接地址，存放至C:\SDK_test\lib\search.xlsx中

待优化：获取地址时使用的时字符串拼接的方法，是否可优化为在获取元素时直接抓取元素点击后地址
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import utils
from time import sleep
import xlwt
import pandas as pd

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(r'c:\tools\chromedriver.exe')
# 如果找不到元素， 每隔 半秒钟 再去界面上查看一次， 直到找到该元素， 或者 过了10秒 最大时长。（暂时没用到）
wd.implicitly_wait(10)
# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.baidu.com/')
title = []
title_dict = []

# 通过while循环获取baidu热搜前30
while len(title) < 30:
    title_elements  = wd.find_elements(By.CLASS_NAME, 'title-content-title')
    for i in title_elements:
        title.append(i.text)
    refresh_element = wd.find_element(By.CLASS_NAME, 'hot-refresh-text')
    refresh_element.click()

# 将热搜前三十用字典存储并附带链接
for i in title:
    title_dictionary = {"search_name": "", "search_link": ""}
    title_dictionary['search_name'] = i
    title_dictionary['search_link'] = f"https://www.baidu.com/s?wd={i}"
    title_dict.append(title_dictionary)
print(title_dict)

# 用于将字典导出为excel
utils.export_excel(title_dict)
