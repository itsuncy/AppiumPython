from page.mine_page import MinePage


class MineHandle:
    def __init__(self, driver):
        self.mine_page = MinePage(driver)

    # 操作"我的"页面，默认元素
    def click_mine(self):
        self.mine_page.get_mine_element().click()

    def click_go_login(self):
        self.mine_page.get_go_login_element().click()

    def click_setting(self):
        self.mine_page.get_setting_element().click()

    # 操作"登录"子页面，界面元素
    def send_username(self, username):
        self.mine_page.get_username_element().send_keys(username)

    def send_password(self, password):
        self.mine_page.get_password_element().send_keys(password)

    def click_login_button(self):
        self.mine_page.get_login_button_element().click()

    # 操作"设置"子页面，界面元素
    def click_logout_button(self):
        self.mine_page.get_logout_button_element().click()

    def click_accept_alert(self):
        self.mine_page.get_accept_alert_element().click()

    def click_cancel_alert(self):
        self.mine_page.get_cancel_alert_element().click()
