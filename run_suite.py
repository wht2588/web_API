# 导包
import unittest
from script.test_emp import TestEmp
from script.test_login import TestLogin
from lib.HTMLTestRunner import HTMLTestRunner
import app

# 创建测试套件对象
suite = unittest.TestSuite()

# 添加测试用例
# suite.addTest(TestLogin("test01_login_success"))
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestEmp))

# 执行测试套件
# unittest.TextTestRunner().run(suite)
# 定义测试报告路径
report_path = app.BASE_DIR + "/report/report.html"
# 打开文件流
with open(report_path, "wb") as f:
    # 实例化HTMLTestRunner对象
    runner = HTMLTestRunner(f, title="人力资源管理系统接口自动化测试报告", description="V1.0。。。")
    # 执行测试套件
    runner.run(suite)
