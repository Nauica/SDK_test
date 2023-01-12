# 登录接口解析验证码
import requests
import base64
from lxml import etree
import ddddocr
import random
import xlwt
import pandas as pd

# 用于识别登录验证码
def get_Verification_Code(img_src):
    sum = 0
    response = requests.get("http://192.168.10.134:9090/unicom/login.html")
    page_text = response.text
    tree = etree.HTML(page_text)
    # 请求图片链接，获取图片数据并且保存至本地
    img_data = requests.get(url=img_src).content
    with open('C:\SDK_test\lib\code.jpg', 'wb') as fp:
        fp.write(img_data)

    # 修改编码
    png = open('C:\SDK_test\lib\code.jpg', 'rb')
    res = png.read()
    s = base64.b64encode(res)
    png.close()
    # print(s.decode('ascii'))

    # 解析验证码（待优化：解析的验证码精度较差）
    ocr = ddddocr.DdddOcr()
    with open('C:\SDK_test\lib\code.jpg', 'rb') as f:
        img_bytes = f.read()
    result = ocr.classification(img_bytes)
    print("识别的算术式为：" + result)

    # 验证码计算
    if result[1] == "+" or result[2] == "+":
        result = result.split("+")
        # print(result)
        result[1] = result[1].rstrip("=")
        sum = int(result[0]) + int(result[1])
        # print("计算后的结果为：" + str(sum))
    elif result[1] == "-" or result[2] == "-":
        result = result.split("-")
        # print(result)
        result[1] = result[1].rstrip("=")
        sum = int(result[0]) - int(result[1])
        # print("计算后的结果为：" + str(sum))
    return sum

# 用于断言IP地理位置上报
def common_assert(case, response, status_code=200, result="OK",message = None,statusCode = None):
    case.assertEqual(status_code, response.status_code)
    case.assertEqual(result, response.json().get("result"))
    case.assertEqual(message,response.json().get("message"))
    case.assertEqual(statusCode,response.json().get("statusCode"))

# 获取随机8位手机号
def random_Telephone():
    telephone = ""
    ran = random.sample(["0","1","2","3","4","5","6","7","8","9"],8)
    for i in ran:
        telephone = telephone + i
    return telephone

# 用于将字典导出为excel
def export_excel(export):
    # 将字典列表转换为DataFrame
    pf = pd.DataFrame(list(export))
    # 指定字段顺序
    order = ['search_name', 'search_link']
    pf = pf[order]
    # 将列名替换为中文
    columns_map = {
        'search_name': '标题',
        'search_link': '链接'
    }
    pf.rename(columns=columns_map, inplace=True)
    # 指定生成的Excel表格名称
    file_path = pd.ExcelWriter('C:\SDK_test\lib\search.xlsx')
    # 替换空单元格
    pf.fillna(' ', inplace=True)
    # 输出
    pf.to_excel(file_path, encoding='utf-8', index=False)
    # 保存表格
    file_path.save()
