import requests
import hashlib
import time
import json

from tools.read_json import ReadJson


class AuthPost(object):
    def __init__(self):
        pass

    def base_post(self, username, password):
        url = "https://ticketapi.shomes.cn/-/user/login"
        username = username
        # 使用encode 防止密码中含有中文 把密码进行md5加密
        password = hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
        # 浮点取整数
        timestamp = int((str(time.time())).split(".")[0])
        headers = {"content-type": "application/json; charset=utf-8"}
        data1 = {
            "username": username,
            "password": password,
            "timestamp": timestamp
        }
        # 由于指定了headers json 可以不用转换
        r1 = requests.post(url=url, json=data1, headers=headers).json()
        userid = r1["id"]
        key = r1["key"]
        return userid, key, username, password, timestamp  # 这是一个元组

    def auth_post(self, url, data2, username, password):
        userid, key, username, password, timestamp = self.base_post(username, password)

        sign = key + str(timestamp) + "city_web" + str(userid)
        userid = str(userid)  # 需要str
        real_timestamp = str(timestamp)  # 需要str
        shomes_sign = hashlib.md5(sign.encode(encoding='UTF-8')).hexdigest()
        headers = {
            "content-type": "application/json; charset=utf-8",
            "shomes-user": userid,
            "shomes-type": "city_web",
            "shomes-time": real_timestamp,
            "shomes-sign": shomes_sign
        }

        real_r = requests.post(url=url, json=data2, headers=headers).json()
        # print(real_r)
        return real_r




# data = ReadJson("login.json").read_json()
# my_list = []
# for i in data.items():
#     my_list.append(i[1])
# a = my_list
# ap = AuthPost()
# r = ap.base_post(my_list[1], my_list[2])
# print(r)
