from handle.login_handle import LoginHandle


class LoginBussiness:
    def __init__(self, driver):
        self.login_handle = LoginHandle(driver)

    def login_success(self):
        self.login_handle.click_mine()
        self.login_handle.click_go_login()
        self.login_handle.send_username('13154580201')
        self.login_handle.send_password('sunchengyu')
        self.login_handle.click_login()
