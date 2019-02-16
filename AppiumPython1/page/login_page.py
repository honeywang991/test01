from util.get_by_local import GetByLocal
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

class LoginPage:
    #获取登录页面所有的页面元素信息
    def __init__(self,driver):
        self.get_by_local = GetByLocal(driver)

#获取用户名元素信息
    def get_user_element(self):
        return self.get_by_local.get_element('username')

#获取密码元素信息
    def get_password_element(self):
        return self.get_by_local.get_element('password')

#获取登录按钮元素信息
    def get_login_button_element(self):
        return self.get_by_local.get_element('login1_button')

#忘记密码元素
    def get_forget_password_element(self):
        return self.get_by_local('forget_password')

#注册元素
    def get_register_element(self):
        return self.get_by_local.get_element('register')

  #获取toast_element
    def get_toast_element(self,message,driver):
        time.sleep(3)
        toast_element = ("xpath","//*[contains(@test,"+message+")]")
        return WebDriverWait(driver,10,0.1).until(EC.presence_of_element_located(toast_element))
