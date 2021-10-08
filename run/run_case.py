"""路径一致性 都是../ 父目录"""
import unittest
import time
from my_tools.HTMLTestRunner import HTMLTestRunner


def run():
    suite = unittest.TestSuite()  # 初始化一个测试套件
    case = unittest.TestLoader().discover("../testcase", pattern="test*.py")  # 加载用例
    suite.addTests(case)  # 添加用例
    with open("../report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S")), mode="wb") as f:  # pycharm时分秒之间别使用冒号
        runner = HTMLTestRunner(stream=f, verbosity=2, title='试运行', description='第一次生成测试报告')
        runner.run(suite)


if __name__ == '__main__':
    run()
