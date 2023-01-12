# -*- coding:utf-8 -*-
import requests
import unittest
import app
from api.ip_location import LocationApi
from utils import common_assert
from utils import random_Telephone

# IOS_Appkey
header = {"Cookie": "SECURITY_CODE=probation_appkey48b0f7a3ac01a7897eb2a5bd5ea40e3e"}

class TestLocation_IOS(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.location_api=LocationApi()

    # 测试场景1-IOS正常上报
    def test01_IOS_success(self):
        data={'startTime':'2022-07-05 16:20:55.514',
                'callType':'voiceCall',
                'callPhone':random_Telephone(),
                'calledPhone':random_Telephone(),
                'callDomain':'ngv.ims.chinaunicom.cn',
                'callDomainPort':'5070',
                'terminalVendor':'Xiaomi',
                'lat':'0',
                'lon':'0',
                'location':'{"speed":"-1.000000","timestamp":"20220704172251","longitude":"104.061617","isSimulatedBySoftware":"0","latitude":"30.577850","verticalAccuracy":"8.802610","speedAccuracy":"-1.000000","course":"-1.000000","ellipsoidalAltitude":"445.879078","altitude":"477.990784","isProducedByAccessory":"0","horizontalAccuracy":"65.114388"}',
                'callSign':'1'}
        response = self.location_api.escalation(headers=header,data=data)
        common_assert(self,response)


    # 测试场景2-IOS上报失败
    def test02_IOS_fail(self):
        data={'startTime':'2022-07-05 16:20:55.514',
                'callType':'voiceCall',
                'callPhone':random_Telephone(),
                'calledPhone':random_Telephone(),
                'callDomain':'ngv.ims.chinaunicom.cn',
                'callDomainPort':'5070',
                'terminalVendor':'Xiaomi',
                'lat':'0',
                'lon':'0',
                'location':'{"speed":"-1.000000","timestamp":"20220704172251","longitude":"104.061617","isSimulatedBySoftware":"0","latitude":"30.577850","verticalAccuracy":"8.802610","speedAccuracy":"-1.000000","course":"-1.000000","ellipsoidalAltitude":"445.879078","altitude":"477.990784","isProducedByAccessory":"0","horizontalAccuracy":"65.114388"}',
                'callSign':'1'}
        fail_header = {"Cookie": "SECURITY_CODE=probation_appkey48b0f7a3ac01a7897eb2a5bd5ea40e3e1"}
        response = self.location_api.escalation(headers=fail_header,data=data)
        common_assert(self,response,400,"appkey不存在")

# 测试场景3-IOS上报成功-含无效location信息
    def test03_IOS_success_invalidLocation(self):
        data={'startTime':'2022-07-05 16:20:55.514',
                'callType':'voiceCall',
                'callPhone':random_Telephone(),
                'calledPhone':random_Telephone(),
                'callDomain':'ngv.ims.chinaunicom.cn',
                'callDomainPort':'5070',
                'terminalVendor':'Xiaomi',
                'lat':'0',
                'lon':'0',
                'location':'{"speed":"-1.000000","timestamp":"20220704172251","longitude":"104.061617","isSimulatedBySoftware":"0","latitude":"30.577850","verticalAccuracy":"8.802610","speedAccuracy":"-1.000000","course":"-1.000000","ellipsoidalAltitude":"445.879078","altitude":"477.990784","isProducedByAccessory":"0","horizontalAccuracy":"65.114388"",call":"10010"}',
                'callSign':'1'}
        response = self.location_api.escalation(headers=header,data=data)
        common_assert(self,response)

# 测试场景4-IOS上报成功-longitude值为空
    def test04_IOS_success_emptyLongitude(self):
        data={'startTime':'2022-07-05 16:20:55.514',
                'callType':'voiceCall',
                'callPhone':random_Telephone(),
                'calledPhone':random_Telephone(),
                'callDomain':'ngv.ims.chinaunicom.cn',
                'callDomainPort':'5070',
                'terminalVendor':'Xiaomi',
                'lat':'0',
                'lon':'0',
                'location':'{"speed":"-1.000000","timestamp":"20220704172251","longitude":"","isSimulatedBySoftware":"0","latitude":"30.577850","verticalAccuracy":"8.802610","speedAccuracy":"-1.000000","course":"-1.000000","ellipsoidalAltitude":"445.879078","altitude":"477.990784","isProducedByAccessory":"0","horizontalAccuracy":"65.114388"}',
                'callSign':'1'}
        response = self.location_api.escalation(headers=header,data=data)
        common_assert(self,response)