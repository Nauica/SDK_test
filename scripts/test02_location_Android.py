# -*- coding:utf-8 -*-
import requests
import unittest
import app
from api.ip_location import LocationApi
from utils import common_assert
from utils import random_Telephone

# Android_Appkey
header = {"Cookie": "SECURITY_CODE=cda722998fb295a807f5a18fd9aed9a6"}


class TestLocation_Android(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.location_api = LocationApi()

    # 测试场景1-Android成功上报
    def test01_Android_success(self):
        data = {'startTime': '2022-07-05 16:20:55.514',
                'callType': 'voiceCall',
                'callPhone': random_Telephone(),
                'calledPhone': random_Telephone(),
                'callDomain': 'ngv.ims.chinaunicom.cn',
                'callDomainPort': '5070',
                'terminalVendor': 'Xiaomi',
                'lat': '0',
                'lon': '0',
                'location': '{"time":"20220705162623","longitude":"104.061913","latitude":"30.57719","altitude":"0"}',
                'callSign': '1'}
        response = self.location_api.escalation(header, data)
        common_assert(self, response)

    # 测试场景2-Android上报失败
    def test02_Android_fail(self):
        data = {'startTime': '2022-07-05 16:20:55.514',
                'callType': 'voiceCall',
                'callPhone': random_Telephone(),
                'calledPhone': random_Telephone(),
                'callDomain': 'ngv.ims.chinaunicom.cn',
                'callDomainPort': '5070',
                'terminalVendor': 'Xiaomi',
                'lat': '0',
                'lon': '0',
                'location': '{"time":"20220705162623","longitude":"104.061913","latitude":"30.57719","altitude":"0"}',
                'callSign': '1'}
        fail_header = {"Cookie": "SECURITY_CODE=cda722998fb295a807f5a18fd9aed9a61"}
        response = self.location_api.escalation(fail_header, data)
        common_assert(self, response, 400, "appkey不存在")

    # 测试场景3-Android成功上报-含无效location信息
    def test03_Android_success_invalidLocation(self):
        data = {'startTime': '2022-07-05 16:20:55.514',
                'callType': 'voiceCall',
                'callPhone': random_Telephone(),
                'calledPhone': random_Telephone(),
                'callDomain': 'ngv.ims.chinaunicom.cn',
                'callDomainPort': '5070',
                'terminalVendor': 'Xiaomi',
                'lat': '0',
                'lon': '0',
                'location': '{"time":"20220705162623","longitude":"104.061913","latitude":"30.57719","altitude":"0","call":"10010"}',
                'callSign': '1'}
        response = self.location_api.escalation(header, data)
        common_assert(self, response)

    # 测试场景4-Android成功上报-longitude的value为空
    def test04_Android_success_emptyLocation(self):
        data = {'startTime': '2022-07-05 16:20:55.514',
                'callType': 'voiceCall',
                'callPhone': random_Telephone(),
                'calledPhone': random_Telephone(),
                'callDomain': 'ngv.ims.chinaunicom.cn',
                'callDomainPort': '5070',
                'terminalVendor': 'Xiaomi',
                'lat': '0',
                'lon': '0',
                'location': '{"time":"20220705162623","longitude":"","latitude":"30.57719","altitude":"0"}',
                'callSign': '1'}
        response = self.location_api.escalation(header, data)
        common_assert(self, response)

    # 测试场景5-Android成功上报-latitude的key和value均为空
    def test05_Android_success_emptyLatitude(self):
        data = {'startTime': '2022-07-05 16:20:55.514',
                'callType': 'voiceCall',
                'callPhone': random_Telephone(),
                'calledPhone': random_Telephone(),
                'callDomain': 'ngv.ims.chinaunicom.cn',
                'callDomainPort': '5070',
                'terminalVendor': 'Xiaomi',
                'lat': '0',
                'lon': '0',
                'location': '{"time":"20220705162623","longitude":"104.061913","altitude":"0"}',
                'callSign': '1'}
        response = self.location_api.escalation(header, data)
        common_assert(self, response)

    # 测试场景6-Android成功上报-altitude的key和value均为空
    def test06_Android_success_emptyAltitude(self):
        data = {'startTime': '2022-07-05 16:20:55.514',
                'callType': 'voiceCall',
                'callPhone': random_Telephone(),
                'calledPhone': random_Telephone(),
                'callDomain': 'ngv.ims.chinaunicom.cn',
                'callDomainPort': '5070',
                'terminalVendor': 'Xiaomi',
                'lat': '0',
                'lon': '0',
                'location': '{"time":"20220705162623","longitude":"104.061913","latitude":"30.57719"}',
                'callSign': '1'}
        response = self.location_api.escalation(header, data)
        common_assert(self, response)

    # 测试场景7-Android成功上报-time的value为空
    def test07_Android_success_emptyTime(self):
        data = {'startTime': '2022-07-05 16:20:55.514',
                'callType': 'voiceCall',
                'callPhone': random_Telephone(),
                'calledPhone': random_Telephone(),
                'callDomain': 'ngv.ims.chinaunicom.cn',
                'callDomainPort': '5070',
                'terminalVendor': 'Xiaomi',
                'lat': '0',
                'lon': '0',
                'location': '{"time":"","longitude":"104.061913","latitude":"30.57719","altitude":"0"}',
                'callSign': '1'}
        response = self.location_api.escalation(header, data)
        common_assert(self, response)

    # 测试场景8-Android成功上报-任意字段格式错误
    def test08_Android_success_errorFormat(self):
        data = {'startTime': '2022-07-05 16:20:55.514',
                'callType': 'voiceCall',
                'callPhone': random_Telephone(),
                'calledPhone': random_Telephone(),
                'callDomain': 'ngv.ims.chinaunicom.cn',
                'callDomainPort': '5070',
                'terminalVendor': 'Xiaomi',
                'lat': '0',
                'lon': '0',
                'location': '{"time":"20220705162623","longitude":"104.061913","latitude":"-30.57719","altitude":"0"}',
                'callSign': '1'}
        response = self.location_api.escalation(header, data)
        common_assert(self, response)

    # 测试场景9-Android成功上报-location所有字段为空
    def test09_Android_success_emptyAll(self):
        data = {'startTime': '2022-07-05 16:20:55.514',
                'callType': 'voiceCall',
                'callPhone': random_Telephone(),
                'calledPhone': random_Telephone(),
                'callDomain': 'ngv.ims.chinaunicom.cn',
                'callDomainPort': '5070',
                'terminalVendor': 'Xiaomi',
                'lat': '0',
                'lon': '0',
                'location': '',
                'callSign': '1'}
        response = self.location_api.escalation(header, data)
        common_assert(self, response)

    # 测试场景10-Android成功上报-任意字段的数据值错误
    def test10_Android_success_errorAnyone(self):
        data = {'startTime': '2022-07-05 16:20:55.514',
                'callType': 'voiceCall',
                'callPhone': random_Telephone(),
                'calledPhone': random_Telephone(),
                'callDomain': 'ngv.ims.chinaunicom.cn',
                'callDomainPort': '5070',
                'terminalVendor': 'Xiaomi',
                'lat': '0',
                'lon': '0',
                'location': '{"time":"20220704162623","longitude":"108.061913","latitude":"31.57719","altitude":"0"}',
                'callSign': '1'}
        response = self.location_api.escalation(header, data)
        common_assert(self, response)

    # 测试场景11-Android成功上报-重复上报
    def test11_Android_success_repeat(self):
        data = {'startTime': '2022-07-05 16:20:55.514',
                'callType': 'voiceCall',
                'callPhone': random_Telephone(),
                'calledPhone': random_Telephone(),
                'callDomain': 'ngv.ims.chinaunicom.cn',
                'callDomainPort': '5070',
                'terminalVendor': 'Xiaomi',
                'lat': '0',
                'lon': '0',
                'location': '{"time":"20220705162623","longitude":"104.061913","latitude":"30.57719","altitude":"0"}',
                'callSign': '1'}
        response1 = self.location_api.escalation(header, data)
        common_assert(self, response1)
        response2 = self.location_api.escalation(header, data)
        common_assert(self, response2, 200, None, "请勿重复请求", "500")
        response3 = self.location_api.escalation(header, data)
        common_assert(self, response3, 200, None, "请勿重复请求", "500")
        response4 = self.location_api.escalation(header, data)
        common_assert(self, response4, 200, None, "请勿重复请求", "500")
