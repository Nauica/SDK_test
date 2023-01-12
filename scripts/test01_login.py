# -*- coding:utf-8 -*-
import requests
import unittest
import json
import app
from api.login import LoginApi
from utils import get_Verification_Code

img_src = 'http://192.168.10.134:9090/boss/account/code?deviceId=0.8726684433891518'
header = {"Accept": "application/json, text/javascript, */*; q=0.01",
          "X - Requested - With": "XMLHttpRequest",
          "Authorization": "bearer undefined",
          "Content-Type": "application/json;charset=UTF-8"
          }


class TestLogin(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.login_api = LoginApi()

    # 测试场景1-登录成功
    def test01_case001_success(self):
        sum = get_Verification_Code(img_src)
        print(sum)
        data = {
            "username": "ceshi",
            "password": "53a220bc43e33df3ebab908157f6d0f33024b4c76bf01822163240553180441f",
            "code": sum}
        response = self.login_api.login(headers=header, json=data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("ok", response.json().get("msg"))
        code = "bearer " + response.json().get("data").get("uuid")
        print(code)
        # app.code = code
        with open(r"C:\SDK_test\lib\cookie.txt", 'w+', encoding="utf8") as f:  # 以读写（更新）的方式打开文件
            f.write(code)  # 写数据
        # 获取token进行使用脚本
        # with open("C:\SDK_test\lib\cookie.txt", 'r', encoding="utf8") as f: # 以读的方式打开文件
        #     data = f.read()

    # 测试场景2-用户名错误
    def test02_case002_failusername(self):
        sum = get_Verification_Code(img_src)
        print(sum)
        data = {
            "username": "ceshi1",
            "password": "53a220bc43e33df3ebab908157f6d0f33024b4c76bf01822163240553180441f",
            "code": sum}
        response = self.login_api.login(headers=header, json=data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("用户名或密码错误", response.json().get("msg"))

    # 测试场景3-密码错误
    def test03_case003_failpassword(self):
        sum = get_Verification_Code(img_src)
        print(sum)
        data = {
            "username": "ceshi",
            "password": "53a220bc43e33df3ebab908157f6d0f33024b4c76bf01822163240553180441ff",
            "code": sum}
        response = self.login_api.login(headers=header, json=data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("用户名或密码错误", response.json().get("msg"))

    # 测试场景4-验证码错误
    def test04_case004_failcode(self):
        sum = get_Verification_Code(img_src)
        print(sum)
        data = {
            "username": "ceshi",
            "password": "53a220bc43e33df3ebab908157f6d0f33024b4c76bf01822163240553180441f",
            "code": sum + 1}
        response = self.login_api.login(headers=header, json=data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("验证码错误", response.json().get("msg"))
