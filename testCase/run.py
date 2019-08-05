import sys

sys.path.append('D:\CoreRepository\Python\AppiumPython')
from time import sleep
from base.start_appium import start
from modules.mine.login import Login

driver = start()
sleep(1)
Login(driver).login("13154580201", "sunchengyu")
