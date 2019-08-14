import sys

sys.path.append('D:\CoreRepository\Python\AppiumPython')
from time import sleep
from base.start_appium import start
from modules.mine.login import Login

driver = start()
Login(driver).login("13188888888", "12345678")
sleep(3)
driver.find_element_by_id("com.tbex.trader:id/centerTabView").click()
driver.find_element_by_id("com.tbex.trader:id/rbRegular").click()

driver.find_element_by_id("com.tbex.trader:id/fiveView").click()
driver.find_element_by_id("com.tbex.trader:id/img_setting").click()
driver.find_element_by_id("com.tbex.trader:id/submitView").click()
driver.find_element_by_id("android:id/button1").click()

driver.quit()
