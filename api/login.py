# -*- coding:utf-8 -*-
import requests
import app

class LoginApi:
    #初始化
    def __init__(self):
        self.url =app.api +  ":9090/boss/account/login?deviceId=0.8726684433891518"

    def login(self,headers,json):
        return requests.post(url=self.url,headers=headers,json=json)
