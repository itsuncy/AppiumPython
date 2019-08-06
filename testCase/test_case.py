import unittest
from report.report_runner import report_runner
from base.start_appium import start
from modules.mine.login import Login


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver = start()
        Login(driver).login("13154580201", "sunchengyu")

    def test_login(self):
        return "登录成功"


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestCase("test_login"))
    report_runner(suite, "58Coin登录模块测试")
