import app
import requests


# 登录模块接口对象封装
class LoginApi:
    def __init__(self):
        # 登录URL
        self.login_url = app.BASE_URL + "/api/sys/login"

    # 登录
    def login(self, mobile, password):
        data = {}
        # 判断mobile参数值是否为空，不为空把数据保存字典对象中
        if mobile is not None:
            data["mobile"] = mobile
        if password is not None:
            data["password"] = password
        print("data===", data)
        return requests.post(self.login_url, headers=app.headers_data, json=data)

    # 登录-无参2
    def login2(self):
        data = None
        return requests.post(self.login_url,
                             headers={"Content-Type": "application/json"}, json=data)