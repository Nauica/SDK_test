# 1.导包
import unittest
import time

import app
from lib.HTMLTestRunner import HTMLTestRunner
from scripts.test02_location_Android import TestLocation_Android
from scripts.test03_location_IOS import TestLocation_IOS

# 2.封装测试套件
suite = unittest.TestSuite()

# 登录
suite.addTest(unittest.makeSuite(TestLocation_Android))
suite.addTest(unittest.makeSuite(TestLocation_IOS))


# 3.指定测试报告路径
report ="./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
# report ="./report/report.html"
# 4.文件流形式打开文件
with open(report, "wb") as f:
    # 1.创建 运行器
    runner = HTMLTestRunner(f, title="IP上报接口测试报告")
    # 2.执行测试套件
    runner.run(suite)
