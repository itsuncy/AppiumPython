from handle.mine_handle import MineHandle


class Login:
    def __init__(self, driver):
        self.mine_handle = MineHandle(driver)

    def login(self, username, password):
        self.mine_handle.click_mine()
        self.mine_handle.click_go_login()
        self.mine_handle.send_username(username)
        self.mine_handle.send_password(password)
        self.mine_handle.click_login_button()

    def logout(self):
        self.mine_handle.click_mine()
