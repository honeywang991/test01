from page.login_page import LoginPage
class LoginHandle:
    def __init__(self,driver):
        self.login_page = LoginPage(driver)
        #操作登录页面的元素
        #输入用户名
    def send_username(self,user):
        self.login_page.get_user_element().send_keys(user)
        #输入密码
    def send_password(self,password):
        self.login_page.get_password_element().send_keys(password)
        #点击登录按钮
    def click_login(self):
        self.login_page.get_login_button_element().click()
    #忘记密码
    def click_forget_password(self):
        self.login_page.get_forget_password_element().click()
    #点击注册按钮
    def click_register(self):
        self.login_page.get_register_element().click()

    #失败的toast
    def get_fail_toast(self,message):
        toast_element = self.login_page.get_toast_element(message)
        if toast_element:
            return True
        else:
            return False

