import sys

sys.path.append('D:\PythonSpace\AppiumPython')
from time import sleep
from case.start_appium import get_driver
from bussiness.login_bussiness import LoginBussiness

driver = get_driver()
sleep(1)
LoginBussiness(driver).login_success()
