"""
此脚本用于SDK管理平台登录功能，登录功能已封装至 LoginSDK()函数中

待优化：图片验证码获取方式较为粗糙，获取的验证码与ui界面上非同一验证码，图片验证码的识别精准度较低
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import utils
from time import sleep
def LoginSDK():
    # 创建 WebDriver 对象，指明使用chrome浏览器驱动
    wd = webdriver.Chrome(r'c:\tools\chromedriver.exe')
    # 如果找不到元素， 每隔 半秒钟 再去界面上查看一次， 直到找到该元素， 或者 过了10秒 最大时长。
    wd.implicitly_wait(10)
    # 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
    wd.get('http://192.168.10.134:9090/')
    # 根据id选择元素，返回的就是该元素对应的WebElement对象
    userName_element = wd.find_element(By.ID, 'userName')

    # 通过该 WebElement对象，就可以对页面元素进行操作了
    # 比如输入字符串到 这个 输入框里
    userName_element.send_keys('ceshi')

    passWord_element = wd.find_element(By.ID, 'passWord')
    passWord_element.send_keys('Juphoon419708!!!')

    # # 手动输入验证码
    # code = input("请输入验证码")
    # code_element = wd.find_element(By.ID,'code')
    # code_element.send_keys(code)

    # 自动获取验证码并识别
    code_element = wd.find_element(By.ID, 'getcode_math')
    code_url = code_element.get_attribute("src")
    code = utils.get_Verification_Code(code_url)
    code_element = wd.find_element(By.ID,'code')
    code_element.send_keys(code)

    # 点击登录
    cancel_element = wd.find_element(By.CLASS_NAME, 'btn-success')
    cancel_element.click()

for i in range(3):
    LoginSDK()