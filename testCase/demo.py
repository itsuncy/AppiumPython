import sys

sys.path.append('D:\CoreRepository\Python\AppiumPython')
from time import sleep
from base.start_appium import start
from modules.mine.login import Login
from util.location_route import LocationRoute
from util.read_ini import ReadIni

# driver = start()
# sleep(3)

a = [1, 2, 3, 4, 5]

for i in a:
    if i == 3:
        print("你答对了")
        break
    else:
        print(i)
#
#
#
# for i in b:
#     print(i)
#     print(type(i))

#
#
# for i in b:
#
#
