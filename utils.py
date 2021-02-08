import pymysql


# 公共的断言方法
def common_assert(test_case, response, status_code, success, code, message):
    test_case.assertEqual(status_code, response.status_code)
    test_case.assertEqual(success, response.json().get("success"))
    test_case.assertEqual(code, response.json().get("code"))
    test_case.assertIn(message, response.json().get("message"))


# 数据操作的工具类
class DBUtil:
    _conn = None

    # 获取数据库连接对象
    @classmethod
    def get_conn(cls):
        if cls._conn is None:
            cls._conn = pymysql.connect("localhost", "root", "root", "books", 3306)
        return cls._conn

    # 关闭数据库连接对象
    @classmethod
    def close_conn(cls):
        if cls._conn:
            cls._conn.close()
            cls._conn = None

    # 获取游标对象
    @classmethod
    def get_cursor(cls):
        return cls.get_conn().cursor()

    # 关闭游标对象
    @classmethod
    def close_cursor(cls, cursor):
        if cursor:
            cursor.close()

    # 查询一条记录
    @classmethod
    def get_one(cls, sql):
        cursor = cls.get_cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        # print("result==", result)
        cls.close_cursor(cursor)
        return result
