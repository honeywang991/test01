import sys
sys.path.append('D:\wfback\project1\AppiumPython1')
from appium import webdriver
import time
from util.read_init import ReadInni
from util.get_by_local import GetByLocal

def get_driver():
    capabilibies = {
      "platformName": "Android",
      "deviceName": "Nexus 6",
         "app": "C:\\Users\\LXT\\Desktop\\Btest_apk1\\mukewang.apk",
         "noRest":"true"
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilibies)
    return driver

driver = get_driver()

#获取屏幕宽高
def get_size():
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width,height
#向左滑动
def swipe_left():
   x1 = get_size()[0]/10*9
   y1 = get_size()[1]/2
   x = get_size()[0]/10
   driver.swipe(x1,y1,x,y1)
#向右滑动
def swipe_right():
   x1 = get_size()[0]/10
   y1 = get_size()[1]/2
   x = get_size()[0]/10*9
   driver.swipe(x1,y1,x,y1)
#向上滑动
def swipe_up():
   x1 = get_size()[0]/2
   y1 = get_size()[1]/10*9
   y = get_size()[1]/10
   driver.swipe(x1,y1,x1,y)
#向下滑动
def swipe_down():
   x1 = get_size()[0]/2
   y1 = get_size()[1]/10
   y = get_size()[1]/10*9
   driver.swipe(x1,y1,x1,y)
# 方向
def swip_on(direction):
  if direction == "up":
    swipe_up()
  elif direction == "down":
    swipe_down()
  elif direction == "left":
    swipe_left()
  else:
    swipe_right()


def go_login():
    get_by_local = GetByLocal(driver)
    driver.find_element_by_id("cn.com.open.mooc:id/fl_shopping_cart").click()
    driver.find_element_by_id("cn.com.open.mooc:id/tv_go_login").click()
    user_element=get_by_local.get_element("username").send_keys("17718567797")
    get_by_local.get_element("password").send_keys("123456")
    time.sleep(3)
    get_by_local.get_element('login1_button').click()

swip_on("left")
swip_on("left")
swip_on("left")
swip_on("left")

time.sleep(1)
swip_on("up")
time.sleep(1)

time.sleep(4)
go_login()





