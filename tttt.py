# -------------------------------
# python3                      
# -*- coding: utf-8 -*-        
# @Author : 刘小渤
# @Email : liuxiaobo@cestc.cn
# -------------------------------
# @File : tttt.py
# @Software : PyCharm
# @Time : 2023/03/25 下午 01:18
# -------------------------------


from requests import get

url = f"https://devapi.qweather.com/v7/weather/3d?location=101290101&key=2b0eac5a4b874cb7b9027fe1039f1ac8"
response = get(url)
response.encoding = "utf-8"
response_data = response.text.split(";")[0].split("=")[-1]
# print(response_data)
response_json = eval(response_data)
# print(response_json)

weatherinfo = response_json["daily"][0]
print(weatherinfo)
# 天气
weather = weatherinfo["textDay"]
# 最高气温
temp = weatherinfo["tempMax"]
# 最低气温
tempn = weatherinfo["tempMin"]
print(tempn)
