import unittest
import logging
import utils
import app
import json
from api.login import LoginApi
from parameterized import parameterized


# 构建测试数据，读取json文件中的数据
def build_data():
    test_data = []
    with open(app.BASE_DIR + "/data/login.json", encoding="UTF-8") as f:
        json_data = json.load(f)
        for case_data in json_data:
            mobile = case_data.get("mobile")
            password = case_data.get("password")
            status_code = case_data.get("status_code")
            success = case_data.get("success")
            code = case_data.get("code")
            message = case_data.get("message")
            data = (mobile, password, status_code, success,
                    code, message)
            test_data.append(data)
    logging.info("test_data={}".format(test_data))
    return test_data


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 实例化LoginApi对象
        cls.login_api = LoginApi()

    # 登录
    @parameterized.expand(build_data)
    def test_login(self, mobile, password, status_code, success, code, message):
        # 测试数据
        # mobile = "13800000002"
        # password = "123456"

        # 调用登录接口
        response = self.login_api.login(mobile, password)
        json_data = response.json()
        logging.info("json_data={}".format(json_data))

        # 断言
        utils.common_assert(self, response, status_code,
                            success, code, message)

        # 获取token数据，并保存token
        if success:
            token = "Bearer " + json_data.get("data")
            app.headers_data["Authorization"] = token

    # 登录成功
    def atest01_login_success(self):
        # 测试数据
        mobile = "13800000002"
        password = "123456"

        # 调用登录接口
        response = self.login_api.login(mobile, password)
        json_data = response.json()
        logging.info("json_data={}".format(json_data))

        # 断言
        utils.common_assert(self, response, 200, True, 10000, "操作成功")

        # 获取token数据，并保存token
        token = "Bearer " + json_data.get("data")
        app.headers_data["Authorization"] = token

        # self.assertEqual(200, response.status_code)
        # self.assertEqual(True, json_data.get("success"))
        # self.assertTrue(json_data.get("success"))
        # self.assertEqual(10000, json_data.get("code"))
        # self.assertIn("操作成功", json_data.get("message"))

    # 用户名不存在
    def atest02_login_username_is_not_exist(self):
        # 测试数据
        mobile = "13899000012"
        password = "123456"

        # 调用登录接口
        response = self.login_api.login(mobile, password)
        json_data = response.json()
        logging.info("json_data={}".format(json_data))

        # 断言
        utils.common_assert(self, response, 200, False, 20001, "用户名或密码错误")

        # self.assertEqual(200, response.status_code)
        # self.assertEqual(False, json_data.get("success"))
        # self.assertFalse(json_data.get("success"))
        # self.assertEqual(20001, json_data.get("code"))
        # self.assertIn("用户名或密码错误", json_data.get("message"))

    # 密码错误
    def atest03_login_pwd_is_error(self):
        # 测试数据
        mobile = "13800000002"
        password = "error"

        # 调用登录接口
        response = self.login_api.login(mobile, password)
        json_data = response.json()
        logging.info("json_data={}".format(json_data))

        # 断言
        utils.common_assert(self, response, 200, False, 20001, "用户名或密码错误")

    # 用户名为空
    def atest04_login_username_is_empty(self):
        # 测试数据
        mobile = ""
        password = "123456"

        # 调用登录接口
        response = self.login_api.login(mobile, password)
        json_data = response.json()
        logging.info("json_data={}".format(json_data))

        # 断言
        utils.common_assert(self, response, 200, False, 20001, "用户名或密码错误")

    # 密码为空
    def atest05_login_pwd_is_empty(self):
        # 测试数据
        mobile = "13800000002"
        password = ""

        # 调用登录接口
        response = self.login_api.login(mobile, password)
        json_data = response.json()
        logging.info("json_data={}".format(json_data))

        # 断言
        utils.common_assert(self, response, 200, False, 20001, "用户名或密码错误")

    # 缺少用户名参数
    def atest06_login_no_username_param(self):
        # 测试数据
        mobile = None
        password = "123456"

        # 调用登录接口
        response = self.login_api.login(mobile, password)
        json_data = response.json()
        logging.info("json_data={}".format(json_data))

        # 断言
        utils.common_assert(self, response, 200, False, 20001, "用户名或密码错误")

    # 缺少密码参数
    def atest07_login_no_pwd_param(self):
        # 测试数据
        mobile = "13800000002"
        password = None

        # 调用登录接口
        response = self.login_api.login(mobile, password)
        json_data = response.json()
        logging.info("json_data={}".format(json_data))

        # 断言
        utils.common_assert(self, response, 200, False, 20001, "用户名或密码错误")

    # 无参
    def atest08_login_no_param(self):
        # 测试数据
        mobile = None
        password = None

        # 调用登录接口
        response = self.login_api.login(mobile, password)
        json_data = response.json()
        logging.info("json_data={}".format(json_data))

        # 断言
        utils.common_assert(self, response, 200, False, 20001, "用户名或密码错误")

    # 无参2
    def atest09_login_no_param2(self):
        # 测试数据
        # mobile = None
        # password = None

        # 调用登录接口
        response = self.login_api.login2()
        json_data = response.json()
        logging.info("json_data={}".format(json_data))

        # 断言
        utils.common_assert(self, response, 200, False, 99999, "系统繁忙")
