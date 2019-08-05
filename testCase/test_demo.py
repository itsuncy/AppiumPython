import sys

sys.path.append('D:\CoreRepository\Python\AppiumPython')
import unittest
from report.report_runner import file_name
from lib.HTMLTestRunner import HTMLTestRunner


class TestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(4)

    def setUp(self):
        print(1)

    def test_01(self):
        print(2)
        self.assertEqual(1, 1, "数据错误")

    def test_02(self):
        print(6)
        self.assertNotEquals(1, 2)

    @unittest.skip("CaseTest")
    def test_03(self):
        print(7)
        self.assertNotEquals(1, 2)

    def tearDown(self):
        print(3)

    @classmethod
    def tearDownClass(cls):
        print(5)


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestDemo("test_01"))
    suite.addTest(TestDemo("test_02"))
    suite.addTest(TestDemo("test_03"))

    fp = open(file_name(), 'wb')
    runner = HTMLTestRunner(stream=fp, tester='孙承玉', title='Android自动化测试报告', description=description)
    runner.run(suite)
    fp.close()

    # report_runner(suite, "58Coin登录模块测试")
