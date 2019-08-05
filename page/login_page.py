from get_by_local import GetByLocal


class LoginPage:
    def __init__(self, driver):
        self.get_by_local = GetByLocal(driver)

    # 获取登录页面所有的页面元素信息
    def get_mine_element(self):
        return self.get_by_local.get_element('mine')

    def get_go_login_element(self):
        return self.get_by_local.get_element('go_login')

    def get_username_element(self):
        return self.get_by_local.get_element('username')

    def get_password_element(self):
        return self.get_by_local.get_element('password')

    def get_login_button_element(self):
        return self.get_by_local.get_element('login_button')
