# 导包
import logging.handlers
import os

# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))

# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print("BASE_DIR=", BASE_DIR)

# 被测系统的基本路径
BASE_URL = "http://ihrm-test.itheima.net"

# 存放请求头数据
headers_data = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 9883b125-45aa-4c08-9f8d-80a82dd750ad"
}

# emp_id = None


# 初始化日志配置
def init_log_config():
    # 创建日志器对象
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 创建处理器(控制台处理器、文件处理器)
    sh = logging.StreamHandler()
    file_path = BASE_DIR + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(file_path, when="midnight", interval=1,
                                                   backupCount=15, encoding="UTF-8")

    # 创建格式化器
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)

    # 把格式化器添加到处理器中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 把处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(fh)


if __name__ == '__main__':
    init_log_config()
    logging.info("这是一个普通日志")
    logging.error("这是一个错误日志")
