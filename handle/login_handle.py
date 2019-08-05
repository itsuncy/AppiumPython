from page.login_page import LoginPage


class LoginHandle:
    def __init__(self, driver):
        self.login_page = LoginPage(driver)

    # 操作登录页面的元素
    def click_mine(self):
        self.login_page.get_mine_element().click()

    def click_go_login(self):
        self.login_page.get_go_login_element().click()

    def send_username(self, username):
        self.login_page.get_username_element().send_keys(username)

    def send_password(self, password):
        self.login_page.get_password_element().send_keys(password)

    def click_login(self):
        self.login_page.get_login_button_element().click()
