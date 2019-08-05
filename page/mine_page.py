from location_route import LocationRoute


class MinePage:
    def __init__(self, driver):
        self.location_route = LocationRoute(driver)

    # 获取登录页面所有的页面元素信息
    def get_mine_element(self):
        return self.location_route.get_element('MineElement', 'default_element', 'mine')

    def get_go_login_element(self):
        return self.location_route.get_element('MineElement', 'default_element', 'go_login')

    def get_username_element(self):
        return self.location_route.get_element('MineElement', 'login_element', 'username')

    def get_password_element(self):
        return self.location_route.get_element('MineElement', 'login_element', 'password')

    def get_login_button_element(self):
        return self.location_route.get_element('MineElement', 'login_element', 'login_button')
