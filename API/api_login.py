import requests
import hashlib
import time
import json

class Login(object):
    def pre_login(self, username, password):
        url = "https://ticketapi.shomes.cn/-/user/login"
        username = username
        # 使用encode 防止密码中含有中文 把密码进行md5加密
        password = hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
        timestamp = time.time()
        data = {}
        r = requests.post(url, password)
        return r.json()
