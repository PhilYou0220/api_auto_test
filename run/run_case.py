"""路径一致性 都是../ 父目录"""
import unittest
import time
from my_tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestLoader().discover("../testcase", pattern="test*.py")
with open("../report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S")), mode="wb") as f:  # pycharm时分秒之间别使用冒号
    HTMLTestRunner(stream=f, verbosity=2, title='试运行', description='第一次生成测试报告').run(suite)

if __name__ == '__main__':
    unittest.main()