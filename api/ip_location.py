# -*- coding:utf-8 -*-
import requests
import app

class LocationApi:
    #初始化
    def __init__(self):
        self.url =app.api +  ":8036/rest2/client/delegate/voiceCall"

    def escalation(self,headers,data):
        return requests.post(url=self.url,headers=headers,data=data)
