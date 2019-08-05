from page.mine_page import MinePage


class MineHandle:
    def __init__(self, driver):
        self.mine_page = MinePage(driver)

    # 操作登录页面的元素
    def click_mine(self):
        self.mine_page.get_mine_element().click()

    def click_go_login(self):
        self.mine_page.get_go_login_element().click()

    def send_username(self, username):
        self.mine_page.get_username_element().send_keys(username)

    def send_password(self, password):
        self.mine_page.get_password_element().send_keys(password)

    def click_login_button(self):
        self.mine_page.get_login_button_element().click()
