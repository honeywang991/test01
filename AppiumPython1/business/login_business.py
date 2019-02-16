#coding=utf-8
from handle.login_handle import LoginHandle
class LoginBusiness:
    def __init__(self,driver):
        self.login_handle = LoginHandle(driver)

    def login_pass(self):
        self.login_handle.send_username("17718567797")
        self.login_handle.send_password('123456')
        self.login_handle.click_login()

    def login_pass_error(self):
        self.login_handle.send_username("17718567790")
        self.login_handle.send_password('123450')
        self.login_handle.click_login()
        user_flag = self.login_handle.get_fail_toast('账号未注册')
        if user_flag:
            return True
        else:
            return False

    def login_password_error(self):
        self.login_handle.send_username("17718567797")
        self.login_handle.send_password('123490')
        self.login_handle.click_login()
        user_flag = self.login_handle.get_fail_toast('登录密码错误')
        if user_flag:
            return True
        else:
            return False
