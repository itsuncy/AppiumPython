from lib.HTMLTestRunner import HTMLTestRunner
import os
import time


def reports_path():
    return os.path.split(os.path.realpath(__file__))[0]


def get_time():
    return time.strftime('/%Y-%m-%d_%H%M%S')


def file_name():
    return reports_path() + get_time() + '_测试报告.html'


def report_runner(suite, description):
    fp = open(file_name(), 'wb')
    runner = HTMLTestRunner(stream=fp, tester='孙承玉', title='Android自动化测试报告', description=description)
    runner.run(suite)
    fp.close()


# print(reports_path())
# print(get_time())
# print(file_name())
