import sys

sys.path.append('D:\PythonSpace\AppiumPython')
from appium import webdriver


# 启动Appium服务

def start():
    Capabilities = {
        "platformName": "Android",
        "deviceName": "127.0.0.1:62001",
        "app": "D:/CoreRepository/Python/AppiumPython/app/58Coin.apk",
        "noReset": "true"
        # "appwaitActivity":"com.tbex.trader.module.launch.SplashActivity"
    }
    # 启动AppiumServer
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", Capabilities)
    return driver
