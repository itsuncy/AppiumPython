import sys

sys.path.append('D:\PythonSpace\AppiumPython')
from time import sleep
from appium import webdriver


# 启动APP
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


# 获取屏幕的宽高
def get_size():
    size = driver.get_window_size()
    width = size.get('width')
    height = size.get('height')
    return width, height


# print(type(get_size()[0]))

# 向左滑动
def swipe_left():
    x = get_size()[0] / 10 * 9
    y = get_size()[1] / 2
    x1 = get_size()[0] / 10
    driver.swipe(x, y, x1, y, duration=sleep(1))


# 向右滑动
def swipe_right():
    x = get_size()[0] / 10
    y = get_size()[1] / 2
    x1 = get_size()[0] / 10 * 9
    driver.swipe(x, y, x1, y, duration=sleep(1))


# 向上滑动
def swipe_up():
    x = get_size()[0] / 2
    y = get_size()[1] / 10 * 9
    y1 = get_size()[1] / 10
    driver.swipe(x, y, x, y1, duration=sleep(1))


# 向下滑动
def swipe_down():
    x = get_size()[0] / 2
    y = get_size()[1] / 10
    y1 = get_size()[1] / 10 * 9
    driver.swipe(x, y, x, y1, duration=sleep(1))


# 滑动方向判断
def swipe_on(direction):
    if direction == 'up':
        swipe_up()
    elif direction == 'down':
        swipe_down()
    elif direction == 'left':
        swipe_left()
    else:
        swipe_right()


# ID定位
def go_login_by_id():
    driver.find_element_by_id("com.tbex.trader:id/fiveView").click()


# class定位
def go_login_by_class():
    elements = driver.find_elements_by_class_name("android.widget.RadioButton")
    elements[8].click()


# xPath定位
def go_login_by_xpath():
    # APP自动化尽量不建议用xpath定位元素，效率比较低。UI自动化的xpath速度还是挺快的。
    # // 从当前节点开始递归下降，此路径运算符出现在模式开头时，表示应从根节点递归下降。
    # *  通配符；选择所有元素节点与元素名无关。（不包括文本，注释，指令等节点）
    # [] 应用筛选模式（即谓词，包括"过滤表达式"和"轴（向前/向后）"）。
    # contains() 匹配一个属性值中包含的字符串
    # @  属性名的前缀。
    # 下面xpath内表达示的含意是：匹配根目录下，所有test标签中包含"我的"的元素
    # driver.find_element_by_xpath('//*[contains(@text,"我的")]').click()
    # 下面xpath内表达示的含义是：匹配根目录下，所有android.widget.RadioButton的class标签中
    # name值为"我的"的元素
    driver.find_element_by_xpath('//android.widget.RadioButton[@text="我的"]').click()


# name定位
def go_login_by_name():
    # Appium在1.5版本以后就不再支持ByName的定位，但可以通过uiautomator进行定位
    driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()


# 层级定位
def go_login_by_node():
    # 先通过ID定位到其上级元素
    element = driver.find_element_by_id("com.tbex.trader:id/radioLayout")
    # 再通过其他方定获取无素集合，最后取下标定位元素
    elements = element.find_elements_by_class_name("android.widget.RadioButton")
    elements[4].click()


# 登录
def login():
    get_by_local = GetByLocal(driver)
    get_by_local.get_element('pleas_login').click()
    get_by_local.get_element('username').send_keys("13154580201")
    get_by_local.get_element('password').send_keys("sunchengyu")
    get_by_local.get_element('login_button').click()


# 首页合约跳转到USDT合约
def contract():
    driver.find_element_by_id("com.tbex.trader:id/centerTabView").click()
    driver.find_element_by_id('com.tbex.trader:id/rbUsdt').click()

# driver = get_driver()
# sleep(1)
# swipe_on('left')
# swipe_on('left')
# go_login()
# go_login_by_name()
# go_login_by_xpath()
# sleep(2)
# login()
# contract()
# LoginBussiness(driver).login_success()
