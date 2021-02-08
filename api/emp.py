import app
import requests


# 封装员工管理模块的接口对象
class EmpApi:
    def __init__(self):
        # 新增员工URL
        self.add_emp_url = app.BASE_URL + "/api/sys/user"
        # 查询员工URL
        self.query_emp_url = app.BASE_URL + "/api/sys/user/{}"
        # 修改员工URL
        self.update_emp_url = app.BASE_URL + "/api/sys/user/{}"
        # 删除员工URL
        self.delete_emp_url = app.BASE_URL + "/api/sys/user/{}"

    # 新增员工
    def add_emp(self, username, mobile, work_number):
        data = {"username": username, "mobile": mobile, "workNumber": work_number}
        return requests.post(self.add_emp_url, headers=app.headers_data, json=data)

    # 查询员工
    def query_emp(self, emp_id):
        url = self.query_emp_url.format(emp_id)
        return requests.get(url, headers=app.headers_data)

    # 修改员工
    def update_emp(self, emp_id, username):
        url = self.update_emp_url.format(emp_id)
        data = {"username": username}
        return requests.put(url, headers=app.headers_data, json=data)

    # 删除员工
    def delete_emp(self, emp_id):
        url = self.delete_emp_url.format(emp_id)
        return requests.delete(url, headers=app.headers_data)
