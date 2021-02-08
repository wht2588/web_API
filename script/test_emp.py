import unittest
import utils
import logging
import app
import json

from api.emp import EmpApi
import pymysql
from parameterized import parameterized


# 构建测试数据，读取json文件中的数据
def build_add_emp_data():
    test_data = []
    with open(app.BASE_DIR + "/data/emp.json", encoding="UTF-8") as f:
        json_data = json.load(f)
        case_data = json_data.get("test01_add_emp")
        username = case_data.get("username")
        mobile = case_data.get("mobile")
        work_number = case_data.get("work_number")
        status_code = case_data.get("status_code")
        success = case_data.get("success")
        code = case_data.get("code")
        message = case_data.get("message")
        test_data.append((username, mobile, work_number, status_code,
                          success, code, message))
    logging.info("test_data={}".format(test_data))
    return test_data
class TestEmp(unittest.TestCase):
    emp_id = "1310466651573030912"  # 保存员工id

    @classmethod
    def setUpClass(cls) -> None:
        cls.emp_api = EmpApi()

    # 新增员工
    @parameterized.expand(build_add_emp_data())
    def test01_add_emp(self, username, mobile, work_number, status_code, success, code, message):
        # 测试数据
        # 调用接口
        response = self.emp_api.add_emp(username, mobile, work_number)
        logging.info("add emp resposne data={}".format(response.json()))
        # 断言
        utils.common_assert(self, response, status_code, success, code, message)

        # 获取员工id
        json_data = response.json()
        TestEmp.emp_id = json_data.get("data").get("id")

    # 查询员工
    def test02_query_emp(self):
        # 测试数据
        emp_id = TestEmp.emp_id

        # 发送请求
        response = self.emp_api.query_emp(emp_id)
        json_data = response.json()
        logging.info("query emp response data={}".format(json_data))

        # 断言
        utils.common_assert(self, response, 200, True, 10000, "操作成功")
        self.assertEqual("tom01", json_data.get("data").get("username"))

    # 修改员工
    def test03_update_emp(self):
        # 测试数据
        emp_id = TestEmp.emp_id
        username = "tom01-new"

        # 发送请求
        response = self.emp_api.update_emp(emp_id, username)
        logging.info("update emp response data={}".format(response.json()))

        # 断言
        utils.common_assert(self, response, 200, True, 10000, "操作成功")

        # 读取数据库中的数据，进行断言
        # 获取数据库连接
        # conn = pymysql.connect("localhost", "root", "root", "books", 3306)
        # # 获取游标
        # cursor = conn.cursor()
        # # 执行sql操作
        # sql = "SELECT t.id,t.username FROM `bs_user` t WHERE t.id=1;"
        # cursor.execute(sql)
        # result = cursor.fetchone()
        # db_username = result[1]
        # print("db_username========", db_username)
        # # 关闭游标
        # cursor.close()
        # # 关闭连接
        # conn.close()
        result = utils.DBUtil.get_one("SELECT t.id,t.username FROM `bs_user` t WHERE t.id=1;")
        db_username = result[1]
        self.assertEqual(username, db_username)

    # 删除员工
    def test04_delete_emp(self):
        # 测试数据
        emp_id = TestEmp.emp_id

        # 发送请求
        response = self.emp_api.delete_emp(emp_id)
        logging.info("delete emp response data={}".format(response.json()))

        # 断言
        utils.common_assert(self, response, 200, True, 10000, "操作成功")
