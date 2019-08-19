import sys

sys.path.append('D:\CoreRepository\Python\AppiumPython')
from time import sleep
from base.start_appium import start
from modules.mine.login import Login
from lib.logger import logger

logger.debug("启动appium服务")
driver = start()
logger.debug("正在登录。。。")
Login(driver).login("13188888888", "12345678")
sleep(3)
logger.debug('点击主页"合约"按钮')
driver.find_element_by_id("com.tbex.trader:id/centerTabView").click()
logger.debug('点击"交割合约"按钮')
driver.find_element_by_id("com.tbex.trader:id/rbRegular").click()
logger.debug('点击"我的"按钮')
driver.find_element_by_id("com.tbex.trader:id/fiveView").click()
logger.debug('点击"设置"按钮')
driver.find_element_by_id("com.tbex.trader:id/img_setting").click()
logger.debug('点击"退出登录"按钮')
driver.find_element_by_id("com.tbex.trader:id/submitView").click()
logger.debug('点击"确认退出"按钮')
driver.find_element_by_id("android:id/button1").click()

driver.quit()
