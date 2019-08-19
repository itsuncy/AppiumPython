from location_route import LocationRoute


class MinePage:
    def __init__(self, driver):
        self.location_route = LocationRoute(driver)

    # 获取"我的"页面，默认元素
    def get_mine_element(self):
        return self.location_route.get_element('MineElement', 'default_element', 'mine')

    def get_go_login_element(self):
        return self.location_route.get_element('MineElement', 'default_element', 'go_login')

    def get_setting_element(self):
        return self.location_route.get_element('MineElement', 'default_element', 'setting')

    # 获取"登录"子页面，界面元素
    def get_username_element(self):
        return self.location_route.get_element('MineElement', 'login_element', 'username')

    def get_password_element(self):
        return self.location_route.get_element('MineElement', 'login_element', 'password')

    def get_login_button_element(self):
        return self.location_route.get_element('MineElement', 'login_element', 'login_button')

    # 获取"设置"子页面，界面元素
    def get_logout_button_element(self):
        return self.location_route.get_element('MineElement', 'setting_element', 'logout_button')

    def get_accept_alert_element(self):
        return self.location_route.get_element('MineElement', 'setting_element', 'accept_alert')

    def get_cancel_alert_element(self):
        return self.location_route.get_element('MineElement', 'setting_element', 'cancel_alert')
